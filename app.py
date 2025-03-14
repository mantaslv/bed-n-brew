from unittest.mock import Mock
import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from flask import redirect
from forms.space_form import *
from lib.spaces.space_repo import SpaceRepo
from lib.spaces.space import Space
from flask_bcrypt import Bcrypt
from lib.users.user import *
from lib.users.user_repo import *
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import calendar
from datetime import datetime
from flask import render_template


# Load environment variables from .env file
load_dotenv()

# Create a new Flask app
app = Flask(__name__)

# Get secret key from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

# Session Tracking
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    user = user_repo.find_by_id(int(user_id))
    if user:
        return UserSession(user.id, user.email, user.password)
    return None


# == Your Routes Here ==
@app.route("/spaces", methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection(app)
    spaces_repo = SpaceRepo(connection)
    spaces = spaces_repo.all()
    return render_template("spaces/list_of_spaces.html", spaces=spaces)


@app.route("/", methods=["GET"])
def index():
    # This just redirects to the spaces page
    return redirect("/spaces")

def get_month_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return cal, month_name

@app.route("/spaces/<id>", methods=["GET", "POST"])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepo(connection)
    space, host = space_repo.find_by_id(id)

    now = datetime.now()

    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        if start_date and end_date:
            session['start_date'] = start_date
            session['end_date'] = end_date
        elif 'direction' in request.form:
            direction = request.form.get('direction')
            if direction == 'previous':
                if now.month == 1:
                    now = now.replace(year=now.year - 1, month=12)
                else:
                    now = now.replace(month=now.month - 1)
            elif direction == 'next':
                if now.month == 12:
                    now = now.replace(year=now.year + 1, month=1)
                else:
                    now = now.replace(month=now.month + 1)
    
    # Set the current and next month based on the session or default to current month
    current_year = now.year
    current_month = now.month

    cal_current, month_name_current = get_month_calendar(current_year, current_month)
    cal_next, month_name_next = get_month_calendar(current_year, current_month + 1 if current_month < 12 else 1)

    # Get selected start and end dates from the session if they exist
    start_date = int(request.form.get('start_date')) if request.form.get('start_date') else None
    end_date = int(request.form.get('end_date')) if request.form.get('end_date') else None


    return render_template(
        "spaces/single_space.html", 
        space=space, 
        host=host,
        cal_current=cal_current,
        month_name_current=month_name_current,
        cal_next=cal_next,
        month_name_next=month_name_next,
        current_year=current_year,
        current_month=current_month,
        start_date=start_date,
        end_date=end_date
    )

@app.route("/spaces/new", methods=["GET", "POST"])
@login_required
def create_space():
    connection = get_flask_database_connection(app)
    spaces_repo = SpaceRepo(connection)
    spaces = spaces_repo.all()
    form = SpaceForm()
    if form.validate_on_submit():
        new_space = Space(
            None,
            form.property_name.data,
            form.location.data,
            form.beds.data,
            form.property_type.data,
            float(form.price_per_night.data),
            form.description.data,
            form.image_url.data,
            form.rating.data,
            form.availability.data,
            None,
            current_user.id,
        )
        spaces_repo.create(new_space)
        return redirect("/spaces")
    return render_template("spaces/new_space.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("users/register.html")

    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    # Get form data
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    contact_number = request.form["contact_number"]
    password = request.form["password"]

    # Check if any field is empty
    if not all([first_name, last_name, email, contact_number, password]):
        errors = "All fields are required. Please fill in all fields."
        return render_template("users/register.html", errors=errors)

    # Hash the password before passing to DB
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # Create a new user
    new_user = User(None, first_name, last_name, email, contact_number, hashed_password)

    # Saving user to our users_table database
    user_repo.create(new_user)

    # Redirecting to /spaces page
    return redirect("/spaces")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("users/login.html")

    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    # Get form data
    email = request.form["email"]
    password = request.form["password"]

    # Find user (if they exist)
    user = user_repo.find_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password):
        # Create a UserSession object from the User data
        user_session = UserSession(user.id, user.email, user.password)
        login_user(user_session)
        return redirect("/spaces")

    return render_template("users/login.html", errors="Incorrect email or password.")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/spaces")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

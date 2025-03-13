from unittest.mock import Mock
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from flask import redirect
from forms.space_form import *
from lib.spaces.space_repo import SpaceRepo
from lib.spaces.space import Space
from flask_bcrypt import Bcrypt
from lib.users.user import *
from lib.users.user_repo import *
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a new Flask app
app = Flask(__name__)

# Get secret key from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)


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


@app.route("/spaces/<id>", methods=["GET"])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepo(connection)
    space = space_repo.find_by_id(id)
    return render_template("spaces/single_space.html", space=space)


@app.route("/spaces/new", methods=["GET", "POST"])
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
            1,
        )
        spaces_repo.create(new_space)
        return redirect("/spaces")
    return render_template("spaces/new_space.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("Users/register.html")

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
        return render_template("Users/register.html", errors=errors)

    # Hash the password before passing to DB
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # Create a new user
    new_user = User(None, first_name, last_name, email, contact_number, hashed_password)

    # Saving user to our users_table database
    user_repo.create(new_user)

    # Redirecting to /spaces page
    return redirect("/spaces")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

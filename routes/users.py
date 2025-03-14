from flask import request, render_template, redirect, Blueprint
from lib.database_connection import get_flask_database_connection
from lib.users.user import *
from lib.users.user_repo import *
from flask_login import login_user, logout_user
from flask_bcrypt import Bcrypt

users = Blueprint('users', __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("users/register.html")

    connection = get_flask_database_connection()
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
    hashed_password = Bcrypt().generate_password_hash(password).decode("utf-8")

    # Create a new user
    new_user = User(None, first_name, last_name, email, contact_number, hashed_password)

    # Saving user to our users_table database
    user_repo.create(new_user)

    # Redirecting to /spaces page
    return redirect("/spaces")


@users.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("users/login.html")

    connection = get_flask_database_connection()
    user_repo = UserRepository(connection)

    # Get form data
    email = request.form["email"]
    password = request.form["password"]

    # Find user (if they exist)
    user = user_repo.find_by_email(email)

    if user and Bcrypt().check_password_hash(user.password, password):
        # Create a UserSession object from the User data
        user_session = UserSession(user.id, user.email, user.password)
        login_user(user_session)
        return redirect("/spaces")

    return render_template("users/login.html", errors="Incorrect email or password.")


@users.route("/logout")
def logout():
    logout_user()
    return redirect("/spaces")
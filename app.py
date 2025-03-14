import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from flask import redirect
from forms.space_form import *
from forms.booking_form import *
from lib.spaces.space_repo import SpaceRepo
from lib.spaces.space import Space
from flask_bcrypt import Bcrypt
from lib.users.user import *
from lib.users.user_repo import *
from dotenv import load_dotenv
from routes.spaces import spaces
from routes.users import users
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from lib.database_connection import get_flask_database_connection
from flask import flash

load_dotenv()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "/login"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(spaces, url_prefix='/spaces')
    app.register_blueprint(users)

    @app.route("/", methods=["GET"])
    def index():
        return redirect("/spaces")

    return app

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection()
    user_repo = UserRepository(connection)
    user = user_repo.find_by_id(int(user_id))
    if user:
        return UserSession(user.id, user.email, user.password)
    return None


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

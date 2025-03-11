from unittest.mock import Mock
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from flask import redirect
from lib.spaces.spaces_repo import SpaceRepo

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==



@app.route("/spaces", methods=["GET"])
def get_spaces():
    space_repo = SpaceRepo()
    spaces = space_repo.all()
    return render_template("spaces/list_of_spaces.html", spaces=spaces)


@app.route("/", methods=["GET"])
def index():
    # This just redirects to the spaces page
    return redirect("/spaces")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

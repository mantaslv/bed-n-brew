from unittest.mock import Mock
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from flask import redirect
from forms.space_form import *
from lib.spaces.space_repo import SpaceRepo
from tests.mock_spaces_data import spaces

# Create a new Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "This is a secret key"

# == Your Routes Here ==
@app.route("/spaces", methods=["GET"])
def get_spaces():
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
    form = SpaceForm()
    if form.validate_on_submit():
        new_space = {
            "property_name": form.property_name.data,
            "price_per_night": form.price_per_night.data,
            "beds": form.beds.data,
            "location": form.location.data,
            "rating": form.rating.data,
            "image_url": form.image_url.data,
            "property_type": form.property_type.data,
            "description": form.description.data,
            "availability": form.availability.data,
            "host_name": form.host_name.data}
        spaces.append(new_space)
        return redirect("/spaces")
    return render_template("spaces/new_space.html", form=form)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

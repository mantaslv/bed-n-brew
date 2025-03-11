from unittest.mock import Mock
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from flask import redirect
from forms.space_form import *

# Create a new Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "This is a secret key"

# Mock objects (until we have the DB built out)
spaces_repository = Mock()
spaces_repository.all.return_value = [
    {
        "property_name": "Cozy London Loft",
        "price_per_night": 120.50,
        "beds": 2,
        "location": "London, UK",
        "rating": 4,
        "image_url": "https://i.ytimg.com/vi/lIiMDDdKXZ8/maxresdefault.jpg",
        "property_type": "flat",
        "description": "A bright and airy loft in central London",
        "availability": True,
        "host_details": {"name": "Sarah Smith", "phone": "07700 900123"},
        "booked_dates": ["2025-04-10", "2025-04-11", "2025-04-12"],
        "host_id": 1001,
    },
    {
        "property_name": "Beach House Retreat",
        "price_per_night": 200.00,
        "beds": 4,
        "location": "Brighton, UK",
        "rating": 5,
        "image_url": "https://t4.ftcdn.net/jpg/09/81/81/31/360_F_981813162_GW3xJ8ZK3wYZ6Lx6kdDTm7Jdwtnhe3go.jpg",
        "property_type": "house",
        "description": "Beautiful beachfront property with stunning sea views",
        "availability": True,
        "host_details": {"name": "John Davies", "phone": "07700 900456"},
        "booked_dates": [],
        "host_id": 1002,
    },
    {
        "property_name": "City Centre Studio",
        "price_per_night": 85.75,
        "beds": 1,
        "location": "Manchester, UK",
        "rating": 3,
        "image_url": "https://i.pinimg.com/736x/d0/c0/4b/d0c04be7f982a0753cb6dc0c565ea661.jpg",
        "property_type": "flat",
        "description": "Compact studio apartment in the heart of Manchester",
        "availability": False,
        "host_details": {"name": "Emma Wilson", "phone": "07700 900789"},
        "booked_dates": ["2025-03-15", "2025-03-16", "2025-03-17", "2025-03-18"],
        "host_id": 1003,
    },
    {
        "property_name": "Countryside Cottage",
        "price_per_night": 150.00,
        "beds": 3,
        "location": "Cotswolds, UK",
        "rating": 5,
        "image_url": "https://i.guim.co.uk/img/media/1dea2a0c222a28facdab89fdb2ecb3e0bc0edde0/0_214_4500_2700/master/4500.jpg?width=1200&quality=85&auto=format&fit=max&s=ef38dd3b6df7952d675dfeb60a7921af",
        "property_type": "house",
        "description": "Charming stone cottage with garden in idyllic countryside setting",
        "availability": True,
        "host_details": {"name": "Robert Taylor", "phone": "07700 900234"},
        "booked_dates": ["2025-05-25", "2025-05-26"],
        "host_id": 1004,
    },
    {
        "property_name": "Modern Apartment",
        "price_per_night": 110.25,
        "beds": 2,
        "location": "Edinburgh, UK",
        "rating": 4,
        "image_url": "https://i.ytimg.com/vi/lIiMDDdKXZ8/maxresdefault.jpg",
        "property_type": "flat",
        "description": "Contemporary apartment with views of Edinburgh Castle",
        "availability": True,
        "host_details": {"name": "Alice Johnson", "phone": "07700 900567"},
        "booked_dates": ["2025-04-01", "2025-04-02"],
        "host_id": 1005,
    },
]

# == Your Routes Here ==


@app.route("/spaces", methods=["GET"])
def get_spaces():
    spaces = spaces_repository.all()
    return render_template("spaces/list_of_spaces.html", spaces=spaces)


@app.route("/", methods=["GET"])
def index():
    # This just redirects to the spaces page
    return redirect("/spaces")

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
        spaces_repository.all.return_value.append(new_space)
        return redirect("/spaces")
    return render_template("spaces/new_space.html", form=form)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

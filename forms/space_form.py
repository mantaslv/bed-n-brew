from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    IntegerField,
    BooleanField,
    SelectField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import DataRequired, NumberRange, URL, Optional


class SpaceForm(FlaskForm):
    property_name = StringField("Property Name", validators=[DataRequired()])
    price_per_night = FloatField(
        "Price per Night", validators=[DataRequired(), NumberRange(min=0)]
    )
    beds = IntegerField(
        "Number of Beds", validators=[DataRequired(), NumberRange(min=1)]
    )
    location = StringField("Location", validators=[DataRequired()])
    rating = IntegerField("Rating (1 - 5)", validators=[NumberRange(min=1, max=5)])
    image_url = StringField("Image URL", validators=[URL()])
    property_type = SelectField(
        "Property Type",
        choices=[
            ("house", "House"),
            ("apartment", "Apartment"),
            ("villa", "Villa"),
            ("other", "Other"),
        ])
    description = TextAreaField("Description", validators=[DataRequired()])
    availability = BooleanField("Available?")
    host_name = StringField("Host Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
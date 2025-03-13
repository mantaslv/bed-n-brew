from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    IntegerField,
    BooleanField,
    SelectField,
    TextAreaField,
    SubmitField,
    HiddenField
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
            ("House", "House"),
            ("Flat", "Flat"),
            ("Hotel", "Hotel"),
            ("Guest House", "Guest House"),
        ])
    description = TextAreaField("Description", validators=[DataRequired()])
    availability = StringField("Availability Date Range", validators=[DataRequired()])
    host_id = HiddenField("Host ID")
    submit = SubmitField("Submit")
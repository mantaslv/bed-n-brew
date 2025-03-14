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


class BookingForm(FlaskForm):
    user_id = HiddenField("User ID")
    customer_name = StringField("Name", validators=[DataRequired()])
    number_of_guests = IntegerField(
        "Number of Guests", validators=[DataRequired(), NumberRange(min=0)]
    )
    preferred_dates = StringField("Preferred Dates", validators=[DataRequired()])
    message_to_host = TextAreaField("Message to Host", validators=[DataRequired()])
    submit = SubmitField("Submit")
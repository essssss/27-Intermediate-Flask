from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
)
from wtforms.validators import InputRequired, Email

states = [
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
]


class AddSnackForm(FlaskForm):
    """A form for a snack"""

    email = StringField(
        "Your email address, please",
        validators=[Email(message="Not an email")],
    )
    name = StringField("Snack Name", validators=[InputRequired()])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a healthy snack")

    category = RadioField(
        "Category",
        choices=[
            ("ic", "Ice Cream"),
            ("chips", "Potato Chips"),
            ("candy", "Candy/Sweets"),
        ],
    )


class EmployeeForm(FlaskForm):
    """A form for a new Employee"""

    name = StringField(
        "Employee Name", validators=[InputRequired(message="name cannot be blank")]
    )
    state = SelectField("State", choices=[(st, st) for st in states])
    dept_code = SelectField("Department Code")

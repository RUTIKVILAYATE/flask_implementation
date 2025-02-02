# making forms using flask_wtf 

from flask_wtf import FlaskForm
# to store string typed -> text and so on 
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
# to check conditions for accuracy 
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)


class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        # check that user has given value or not and in username and check about length of that user_name
        # validate the data 
        validators=[DataRequired(), Length(2, 30)]
    )
    
    
    email = StringField(
        "Email",
        # make it required field and check if the format is email or not 
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        "Gender",
        # allow to choose from choices
        choices=["Male", "Female", "Other"],
        # make it optional so that user can choose from one of the options 
        validators=[Optional()]
    )
    dob = DateField(
        "Date of Birth",
        # make it optional if want to give or not 
        validators=[Optional()]
    )
    password = PasswordField(
        "Password",
        # password must ge required and lenght in between 5 to 25 
        validators=[DataRequired(), Length(5, 25)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        # must match with previously given password -> use EqualTo()
        validators=[DataRequired(), Length(5, 25), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        # email is required and must be in format of email
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        # requires value and length must be between 5 to 25
        validators=[DataRequired(), Length(5, 25)]
    )
    # true or false -> remember or not remember 
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

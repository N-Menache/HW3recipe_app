# This file is used to define web forms. These forms are used to collect login, recipe, and user inputs

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit =  SubmitField("Sign in")
    remember_me = BooleanField("Remember Me")

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(message="This field is required."),Length(max=80)])
    description = TextAreaField('Description', validators=[InputRequired(message="This field is required.")])
    ingredients = TextAreaField('Ingredients', validators=[InputRequired(message="This field is required.")])
    instructions = TextAreaField('Instructions', validators=[InputRequired(message="This field is required.")])
    submit =  SubmitField("Submit")

class UserForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])

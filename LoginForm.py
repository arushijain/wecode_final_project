from flask_wtf import Form, validators
from wtforms import Form, validators, StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Required


class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    aboutme = StringField('About me', [validators.Length(min=0, max=200)])
    website = StringField('Website', [validators.Length(min=6, max=35)])
    feedback = StringField('What do you like about WeCode', [validators.Length(min=6, max=300)])

from flask_wtf import Form, validators
from wtforms import Form, validators, StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Required
import time

class PostForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    content = StringField('Content', [validators.Length(min=1, max=200)])
    
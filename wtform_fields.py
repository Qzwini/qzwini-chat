from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import User

def invalid_credentials(form, field):
    """ Username and password checker """
    username = form.username.data
    password = field.data

    # Check username & Password is valid 
    user_object = User.query.filter_by(username=username).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect")
    elif password != user_object.password:
        raise ValidationError("Username or password is incorrect")


 


class RegistrationForm(FlaskForm):
    """ Registration Form """

    username = StringField('username',validators=[InputRequired(message="Username required"),Length(min=4, max=25, message="Username must be between 4 and 25 cahracters")])
    password = PasswordField('password',validators=[InputRequired(message="password required"),Length(min=4, max=25, message="password must be between 4 and 25 cahracters")])
    confirm_pswd = PasswordField('confirm_psw',validators=[InputRequired(message="password required"), EqualTo('password',message="Password must match")])
    submit_button = SubmitField('Create')


    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username alrady exists. Select a difrent username.")

class LoginForm(FlaskForm):
    """ Login form """

    username = StringField('username', validators=[InputRequired(message="Username required")])
    password = PasswordField('password',validators=[InputRequired(message="Password required"),invalid_credentials])
    submit_button = SubmitField('Login')


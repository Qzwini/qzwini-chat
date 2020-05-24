from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration Form """

    username = StringField('username',validators=[InputRequired(message="Username required"),Length(min=4, max=25, message="Username must be between 4 and 25 cahracters")])
    password = PasswordField('password',validators=[InputRequired(message="password required"),Length(min=4, max=25, message="password must be between 4 and 25 cahracters")])
    confirm_pswd = PasswordField('confirm_psw',validators=[InputRequired(message="password required"), EqualTo('password',message="Password must match")])


    submit_button = SubmitField('Create')


    
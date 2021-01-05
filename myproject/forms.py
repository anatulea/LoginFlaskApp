from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField("LogIn!")

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm =PasswordField('Confirm Password', validators=[DataRequired()])
    submit=SubmitField("Register!")

    # def check_email(self,field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been registered already!')
 
    # def check_username(self,field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Your username has been registered already!')

    # Due to some changes to flask_login library you need to make 2 changes to the naming of the methods used in the subsequent lectures.
    
    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')

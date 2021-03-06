from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from ManishWeb.models import User


class RegisterForm(FlaskForm):
    '''To get a validation FlaskForm class searches for function starting with validate followed by underscore and the parameter we want to validate'''

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()  # returns an object of User
        if user:
            raise ValidationError("Username already Exists! Try different username")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()  # returns an object of User
        if email:
            raise ValidationError("Email already Exists! Try different one")

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')

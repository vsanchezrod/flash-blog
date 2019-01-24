# Para el uso de formularios
from flask_wtf import FlaskForm

# Para crear un campo de tipo texto y tipo password
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# Para validaciones de campos
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Se crea una clase para los formulario de registro
class RegistrationForm(FlaskForm):
    # Campo 1
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    # Campo 2
    email = StringField('Email',
                        validators=[DataRequired(), Length(min=2, max=20), Email()])

    # Campo 3
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # Botón REGISTRO
    submit = SubmitField('Sign Up')


# Se crea una clase para los formulario de login
class LoginForm(FlaskForm):
    # Campo 1
    email = StringField('Email',
                        validators=[DataRequired(), Length(min=2, max=20), Email()])

    # Campo 2
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember me')

    # Botón REGISTRO
    submit = SubmitField('Login')

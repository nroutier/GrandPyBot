from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    query = StringField('Indiquer un lieu :', validators=[DataRequired()])
    submit = SubmitField('Entrer')
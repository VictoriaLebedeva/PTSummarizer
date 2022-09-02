from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class URLForm(FlaskForm):
    """URL submit form."""
    name = StringField('Name')
    submit = SubmitField('Submit')

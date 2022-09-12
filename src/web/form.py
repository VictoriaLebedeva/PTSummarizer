from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ArticleURLSubmit(FlaskForm):
  url =  StringField("URL: ", validators=[InputRequired()])
  submit = SubmitField("GO")
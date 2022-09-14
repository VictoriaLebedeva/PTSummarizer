from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ArticleURLSubmit(FlaskForm):
  url =  StringField("url", validators=[InputRequired()])
  submit = SubmitField("go")
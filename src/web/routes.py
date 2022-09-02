from flask import Flask, url_for, render_template, redirect
from .forms import URLForm

app = Flask(
  __name__, 
  template_folder="templates",
  static_folder="static",
)

@app.route('/getarticle', methods=['GET', 'POST'])
def get_article():
  """Gets article content by given url."""
  form = URLForm()
  if form.validate_on_submit():
    return redirect(url_for('success'))
  return render_template(
    "index.html",
    title="PTSummarizer", 
    form=form,
    template="form-template"
)
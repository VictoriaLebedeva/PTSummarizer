import requests

from flask import Flask, render_template, request
from form import ArticleURLSubmit
from get_data import parse_article

app = Flask(__name__)
# app.debug = True
app.config['SECRET_KEY'] = 'QWERTYUIOP!@#$%^&*('

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = ArticleURLSubmit()
    if request.method == 'POST':
      url = request.form.get('url')  

      title, text = parse_article(url)
      return render_template('summary.html', title = title, text=text)

    return render_template('home_page.html', form=form)

  
if __name__ == '__main__':
    app.run()

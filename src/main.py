from parse_article import parse_article
from flask import Flask, render_template, request
from form import ArticleURLSubmit

app = Flask(__name__)
# app.debug = True
app.config['SECRET_KEY'] = 'QWERTYUIOP!@#$%^&*('

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = ArticleURLSubmit()
    if request.method == 'POST':
      url = request.form.get('url')  

      title, original = parse_article(url)
      return render_template('summary.html', title=title, original=original, summary=original)

    return render_template('home_page.html', form=form)

  
if __name__ == '__main__':
    app.run()
    
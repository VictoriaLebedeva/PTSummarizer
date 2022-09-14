from parser.parse_article import parse_article
from flask import Flask, render_template, request
from web.form import ArticleURLSubmit

from ml.models.train_model import preprocess_data, text_rank

app = Flask(__name__, 
           template_folder='web/templates', 
           static_folder='web/static')
app.config['SECRET_KEY'] = 'QWERTYUIOP!@#$%^&*('

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = ArticleURLSubmit()
    if request.method == 'POST':
      url = request.form.get('url')  

      title, original = parse_article(url)
      tfidf, tokens = preprocess_data(original)
      summary = text_rank(tfidf, tokens)

      return render_template('summary.html', title=title, original=original, summary=summary)

    return render_template('home_page.html', form=form)

  
if __name__ == '__main__':
    app.run()
    
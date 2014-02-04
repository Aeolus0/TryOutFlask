from app import app


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
             {
              'author': {'nickname': 'John'},
              'body'
import sqlite3, random, string
from flask import Flask, request, session, g, redirect, \
    abort, render_template, flash
from contextlib import closing

# config
DATABASE = '/tmp/surl.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'defult'

DEV_URL = 'http://127.0.0.1:5000'

# creating the app
app = Flask(__name__)
app.config.from_object(__name__)


# database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def gen_url(length):
    while True:
        url = ''.join(random.choice(string.ascii_lowercase + string.digits) \
                      for _ in range(length))
        db_url = g.db.execute('select * from entries where url = ?', [url])
        entries = [dict(url=row[0], links=row[1], text=row[2]) for row in db_url.fetchall()]
        print entries
        if not entries:
            return url


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    url = gen_url(4)
    g.db.execute('insert into entries (url, links, text) values (?, ?, ?)',
                 [url, request.form['links'], request.form['text']])
    g.db.commit()
    return '{}/{}'.format(DEV_URL, url)


@app.route('/<url>')
def urls(url=None):
    result = g.db.execute('select * from entries where url = ?', [url])
    entries = [dict(url=row[0], links=row[1], text=row[2]) for row in result.fetchall()]
    return render_template('urls.html', entries=entries)


if __name__ == '__main__':
    app.run()

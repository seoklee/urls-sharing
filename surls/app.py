from flask import Flask, request, session, g, redirect, \
    abort, render_template, flash
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine import DoesNotExist
from urlparse import urlparse
# need to fix this to import only one model
from models import *
import random
import string

DEV_URL = 'http://127.0.0.1:5000'

# creating the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)

db = MongoEngine(app)


def gen_url(length):
    while True:
        url = ''.join(random.choice(string.ascii_lowercase + string.digits) \
                      for _ in range(length))
        try:
            LinkEntry.objects.get(token=url)
        except DoesNotExist:
            return url


def check_and_fix_http(url):
    o = urlparse(url)
    print o
    if not o.scheme:
        url = "http://" + url
    print url
    return url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    url = gen_url(4)
    links = [x.strip() for x in request.form['links'].split(',')]
    for i, link in enumerate(links):
        links[i] = check_and_fix_http(link)
    link_entry = LinkEntry(
            token=url,
            links=links,
            description=request.form['text']
    )
    link_entry.save()
    url_link = '{}/u/{}'.format(DEV_URL, url)
    return render_template('create.html', url_link=url_link)


@app.route('/u/<url>')
def urls(url=None):
    entry = LinkEntry.objects.get(token=url)
    return render_template('urls.html', entry=entry)


if __name__ == '__main__':
    app.run()

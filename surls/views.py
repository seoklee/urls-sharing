from flask import request, render_template
from urlparse import urlparse
from surls import app
from surls.models import *
from surls import database
from requests import HTTPError
import random
import string

# change this later
# DEV_URL = 'http://localhost:8080'
PROD_URL = 'http://shareurls.appspot.com'


def gen_url(length):
    while True:
        url = ''.join(random.choice(string.ascii_lowercase + string.digits) \
                      for _ in range(length))
        try:
            database.get(url)
        except HTTPError:
            return url


def check_and_fix_http(url):
    o = urlparse(url)
    if not o.scheme:
        url = "http://" + url
    return url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    url = gen_url(4)
    links = request.form.getlist('links')
    links = filter(None, links)
    for i, link in enumerate(links):
        links[i] = check_and_fix_http(link)
    link_entry = LinkEntry(
            _id=url,
            links=links,
            description=request.form['text']
    )
    database.add(link_entry)
    url_link = '{}/u/{}'.format(PROD_URL, url)
    return render_template('create.html', url_link=url_link)


@app.route('/u/<url>')
def urls(url=None):
    entry = database.get(url)
    url_link = '{}/u/{}'.format(PROD_URL, url)
    return render_template('urls.html', url_link=url_link, entry=entry)

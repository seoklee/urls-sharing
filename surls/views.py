from flask import request, render_template, flash, redirect, session
from urlparse import urlparse
from surls import app
from surls.models import *
from surls.forms import *
from surls import database
from requests import HTTPError
import random
import string
import json

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


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"%s\n" % error)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = link_form()

    if request.method == 'POST':
        url = gen_url(4)
        # attempting to fix each entry
        for index, item in enumerate(form.link.raw_data):
            form.link.raw_data[index] = check_and_fix_http(str(item))

        if not form.validate():
            flash_errors(form)
            session['links'] = form.link.raw_data
            print json.dumps(form.failed_links)
            return render_template('index.html', form=form, links=session.get("links"),
                                   failed_links=map(json.dumps, form.failed_links))
        else:
            link_entry = LinkEntry(
                _id=url,
                links=form.link.raw_data,
                description=request.form['text']
            )
            database.add(link_entry)
            url_link = '{}/u/{}'.format(PROD_URL, url)
            return redirect(url_link)

    return render_template('index.html', form=form)


@app.route('/u/<url>')
def urls(url=None):
    entry = database.get(url)
    url_link = '{}/u/{}'.format(PROD_URL, url)
    return render_template('urls.html', url_link=url_link, entry=entry)

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import ShortenerForm, ApiForm
from app.models import Links, Api, clear
import re
from datetime import date, timedelta


@app.route('/', methods=['GET', 'POST'])
@app.route('/short', methods=['GET', 'POST'])
def short():
    form = ShortenerForm()
    if form.is_submitted():
        if not 1 <= int(form.expired.data) <= 365:
            return { "error": "wrong_expired" }
        if not re.match( r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[-a-z0-9]{2,63}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", form.link.data):
            return { "error": "wrong_link" }
        link = Links(link=form.link.data, expired = form.expired.data)
        db.session.add(link)
        db.session.commit()
        flash('Requested shortened link: {}\n Active for {} days'.format(
            link.short, form.expired.data))
        form.shortened = link.short
        return render_template('short.html', form=form)
    return render_template('short.html', form=form)

@app.route('/api', methods=['GET', 'POST'])
def get_api():
    form = ApiForm()
    if form.is_submitted():
        api = Api()
        db.session.add(api)
        db.session.commit()
        flash('Your generated API key is: {}'.format(api.key))
        form.api = api.key
        return render_template('api.html', form=form)
    return render_template('api.html', form=form)

@app.route('/<redir>', methods=['GET'])
def redir(redir):
    if app.last_cleared < date.today():
        clear()
        app.last_cleared = date.today()
    link = Links.query.filter_by(short=redir).first_or_404()
    return redirect(link.link)
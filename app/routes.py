from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ShortenerForm, ApiForm
from app.models import Links, Api

@app.route('/', methods=['GET', 'POST'])
@app.route('/short', methods=['GET', 'POST'])
def short():
    form = ShortenerForm()
    if form.validate_on_submit():
        link = Links(link=form.link.data, expired = form.expired.data)
        db.session.add(link)
        db.session.commit()
        flash('Requested shortened link: {}\n Active for {} days'.format(
            link.short, form.expired.data))
        form.shortened = link.short
        return redirect(url_for('short'))
    return render_template('short.html', form=form)

@app.route('/api', methods=['GET', 'POST'])
def get_api():
    form = ApiForm()
    if form.is_submitted():
        api = Api()
        db.session.add(api)
        db.session.commit()
        flash('Your generated API key is: {}'.format(api.key))
        return redirect(url_for('get_api'))
    return render_template('api.html', form=form)

@app.route('/<redir>', methods=['GET'])
def redir(redir):
    link = Links.query.filter_by(short=redir).first_or_404()

    return redirect(link.link)
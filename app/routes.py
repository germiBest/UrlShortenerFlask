from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ShortenerForm, ApiForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/short', methods=['GET', 'POST'])
def short():
    form = ShortenerForm()
    if form.validate_on_submit():
        flash('Requested shortened link:{}\n Active for {} days'.format(
            form.link.data, form.expired.data))
        return redirect(url_for('short'))
    return render_template('short.html', form=form)

@app.route('/api', methods=['GET', 'POST'])
def get_api():
    form = ApiForm()
    if form.is_submitted():
        flash('Your generated API is: 1234')
        return redirect(url_for('get_api'))
    return render_template('api.html', form=form)
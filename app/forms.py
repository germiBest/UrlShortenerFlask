from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import IntegerRangeField


class ShortenerForm(FlaskForm):
    link = StringField('Link', validators=[DataRequired()])
    expired = IntegerRangeField('Link Expiration', default=90, validators=[DataRequired()])
    submit = SubmitField('Short URL')

class ApiForm(FlaskForm):
    submit = SubmitField('Get API key')
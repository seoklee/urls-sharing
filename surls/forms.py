from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, FieldList
from wtforms.validators import DataRequired, URL


class link_form(Form):
    link = StringField('Add some URLS', validators=[DataRequired()])
    text = TextAreaField('Give a description (optional)')
    submit = SubmitField('submit')

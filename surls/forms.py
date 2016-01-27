from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired
import re


class link_form(Form):
    link = StringField('Add some URLS', validators=[DataRequired()])
    text = TextAreaField('Give a description (optional)')
    submit = SubmitField('submit')
    failed_links = []

    def validate_link(form, field):
        # django regex for url matching
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        form.failed_links = []
        raise_exception = False

        for index, val in enumerate(field.raw_data):
            if not regex.match(val):
                form.failed_links.append(index)
                raise_exception = True

        if raise_exception:
            raise ValidationError("Please enter a valid URL.")

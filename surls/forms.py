from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Regexp
import re


class link_form(Form):
    link = StringField('Add some URLS', validators=[DataRequired()])
    text = TextAreaField('Give a description (optional)')
    submit = SubmitField('submit')

    def validate_link(form, field):
        print "Validating links"
        #django regex for url matching
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        failed_link = []
        raise_exception = False;

        for index, val in enumerate(field.raw_data):
            if not regex.match(val):
                failed_link.append(index)
                raise_exception = True;

        if raise_exception:
            raise ValidationError("These links, " + failed_link.__str__() + " are not proper URLs. Try Again.")

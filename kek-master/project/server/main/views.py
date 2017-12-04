# project/server/main/views.py

from mayan_api_client import API

from flask import render_template, Blueprint

from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField
from wtforms.validators import DataRequired


main_blueprint = Blueprint('main', __name__,)

api = API(host='http://192.168.22.188:81', username='Dave', password='dbvjdu123')

'''for result in api.metadata.metadata_types.get()['results']:
    print(result['name'])
'''
'''for result in api.documents.document_types.get()['results']:
    print(result['label'])
'''
class SomeForm(FlaskForm):
    label = SelectField('label', choices=[(result['label'], result['label']) for result in api.documents.document_types.get()['results']])

    '''invoice_number = StringField('Invoice number (Required)', [DataRequired()])
    test = SelectField('test', choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004)], \
                       validators=[DataRequired()])
    status = SelectField('status', choices=[('nova', 'nova'), ('zauctovano', 'zauctovano')])
'''

class metadataForm(FlaskForm):
    for result in api.metadata.metadata_types.get()['results']:
        name=StringField(result['name'])







@main_blueprint.route('/')
def home():
    form = SomeForm()
    return render_template('main/home.html', form=form)


@main_blueprint.route('/metadata')
def red():
    form=metadataForm()
    return render_template('main/metadata.html',form=form)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")

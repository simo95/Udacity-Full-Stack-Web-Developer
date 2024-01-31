from datetime import datetime
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, Regexp


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = SelectField('state', validators=[DataRequired()], choices=[])
    address = StringField('address', validators=[DataRequired()])
    phone = StringField('phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$', message='Invalid phone number format. Please use XXX-XXX-XXXX.')])
    image_link = StringField('image_link')
    genres = SelectMultipleField('genres', validators=[DataRequired()], choices=[])
    facebook_link = StringField('facebook_link', validators=[URL()])
    website_link = StringField('website_link')
    seeking_talent = BooleanField('seeking_talent')
    seeking_description = StringField('seeking_description')



from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, URL

class ArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = SelectField('state', validators=[DataRequired()], choices=[])
    phone = StringField('phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$', message='Invalid phone number format. Please use XXX-XXX-XXXX.')])
    image_link = StringField('image_link')
    genres = SelectMultipleField('genres', validators=[DataRequired()], choices=[])
    facebook_link = StringField('facebook_link', validators=[URL()])
    website_link = StringField('website_link')
    seeking_venue = BooleanField('seeking_venue')
    seeking_description = StringField('seeking_description')

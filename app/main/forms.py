from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[Optional(), EqualTo('password')])
    submit = SubmitField('Update Profile')

class TicketForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    attachment = FileField('Attach File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'pdf', 'zip'], 'Invalid file type')])
    submit = SubmitField('Submit Ticket')

class TicketReplyForm(FlaskForm):
    message = StringField('Reply', validators=[DataRequired()])
    attachment = FileField('Attach File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'pdf', 'zip'])])
    submit = SubmitField('Post Reply')
    
class PrivateMessageForm(FlaskForm):
    recipient = SelectField('To', coerce=int)
    message = TextAreaField('Message', validators=[DataRequired()])
    attachment = FileField('Attach File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'pdf', 'zip'])])
    submit = SubmitField('Send')

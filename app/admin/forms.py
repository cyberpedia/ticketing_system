class AdminTicketForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    description = StringField('Description')
    status = SelectField('Status', choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')])
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')])
    assigned_to = SelectField('Assign To', coerce=int)
    submit = SubmitField('Update')

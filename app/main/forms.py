
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField, TimeField
from wtforms.validators import ValidationError, DataRequired, Length


class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

class AppointmentForm(FlaskForm):
    appointment_desc = StringField('appointment_desc', validators=[DataRequired()])
    appointment_status_completed = SelectField('Status', choices=[('upcoming', 'Upcoming'), ('in progress', 'In Progress'),('completed', 'Completed')])
    appointment_title = StringField('Title',validators=[DataRequired()])
    appointment_date = DateField('Date', validators=[DataRequired()])
    appointment_time = TimeField('Time', validators=[DataRequired()])
    appointment_address = StringField('Address',validators=[DataRequired()])
    appointment_name = StringField('Name',validators=[DataRequired()])
    appointment_notes = StringField('Notes',validators=[DataRequired()])
    submit = SubmitField('Submit')

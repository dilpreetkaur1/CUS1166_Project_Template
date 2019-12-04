
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length



class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

class createAEntry(FlaskForm):
    EntryTitle = StringField('Appointment Title', validators=[DataRequired()])
    EntryDate= StringField('Appointment Date', validators=[DataRequired()])
    EntryAddress = StringField('Appointment Address', validators=[DataRequired()])
    EntryName= StringField('Appointment Name', validators=[DataRequired()])
    EntryNote= StringField('Appointment Note', validators=[DataRequired()])
    submit = SubmitField('Create')
""" 
class UpdateAppointmentInfo(FlaskForm):
    title = StringField('new title', validators=[DataRequired()])
    date = StringField('new date', validators=[DataRequired()])
    address = StringField('new address', validators=[DataRequired()])
    name = StringField('new name', validators=[DataRequired()])
    note = StringField('new note', validators=[DataRequired()])
    submit = SubmitField('Update')
"""
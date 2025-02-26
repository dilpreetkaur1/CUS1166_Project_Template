from flask import render_template,  redirect, url_for, request
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Task
from app.models import Appointment
from .forms import AppointmentForm
from flask import flash
import datetime
from datetime import timedelta

# Main route of the applicaitons.
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)

@bp.route('/appointment', methods=['GET','POST'])
def appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        new_appointment = Appointment()
        new_appointment.appointment_desc =  form.appointment_desc.data
        new_appointment.appointment_status = form.appointment_status_completed.data
        new_appointment.appointment_date_time=form.appointment_date_time.data
        new_appointment.appointment_title = form.appointment_title.data
        new_appointment.appointment_address = form.appointment_address.data
        new_appointment.appointment_name = form.appointment_name.data
        new_appointment.appointment_notes = form.appointment_notes.data
        db.session.add(new_appointment)
        db.session.commit()

        return redirect(url_for('main.appointment'))


    new_appointment = db.session.query(Appointment).all()

    return render_template("main/appointment.html",new_appointment = new_appointment,form= form)

#
# Route for removing a appointment
@bp.route('/appointment/remove/<int:appointment_id>', methods=['GET','POST'])
def remove_appointment(appointment_id):

    # Query database, remove items
    Appointment.query.filter(Appointment.appointment_id == appointment_id).delete()
    db.session.commit()

    return redirect(url_for('main.appointment'))

# Route for editing a appointment

@bp.route('/appointment/edit/<int:appointment_id>', methods=['GET','POST'])
def edit_appointment(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        current_appointment = Appointment()

        current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.appointment_desc =  form.appointment_desc.data
        current_appointment.appointment_status = form.appointment_status_completed.data
        current_appointment.appointment_title =  form.appointment_title.data
        current_appointment.appointment_date_time = form.appointment_date_time.data
        current_appointment.appointment_address = form.appointment_address.data
        current_appointment.appointment_name =  form.appointment_name.data
        current_appointment.appointment_notes = form.appointment_notes.data

        db.session.add(current_appointment)
        db.session.commit()
        return redirect(url_for('main.appointment'))

    current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()


    form.appointment_desc.data = current_appointment.appointment_desc
    form.appointment_status_completed.data = current_appointment.appointment_status
    form.appointment_title.data = current_appointment.appointment_title
    form.appointment_date_time.data = current_appointment.appointment_date_time
    form.appointment_address.data = current_appointment.appointment_address
    form.appointment_name.data = current_appointment.appointment_name
    form.appointment_notes.data = current_appointment.appointment_notes

    return render_template("main/appointment_edit_view.html",form=form, appointment_id = appointment_id)



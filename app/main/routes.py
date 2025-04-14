import os
from werkzeug.utils import secure_filename
from ..config import UPLOAD_FOLDER
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .. import db
from ..models import User
from .forms import ProfileForm

main = Blueprint('main', __name__, template_folder='../templates/main')

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data.lower()
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('main.profile'))
    return render_template('main/profile.html', form=form)

@main.route('/tickets/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = TicketForm()
    if form.validate_on_submit():
        filename = None
        if form.attachment.data:
            filename = secure_filename(form.attachment.data.filename)
            form.attachment.data.save(os.path.join(UPLOAD_FOLDER, filename))

        ticket = Ticket(
            subject=form.subject.data,
            description=form.description.data,
            user=current_user,
            attachment=filename
        )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket submitted successfully.')
        return redirect(url_for('main.ticket_list'))
    return render_template('main/ticket_create.html', form=form)


@main.route('/tickets')
@login_required
def ticket_list():
    status = request.args.get('status')
    if status:
        tickets = Ticket.query.filter_by(user=current_user, status=status).order_by(Ticket.created_at.desc()).all()
    else:
        tickets = Ticket.query.filter_by(user=current_user).order_by(Ticket.created_at.desc()).all()
    return render_template('main/ticket_list.html', tickets=tickets)

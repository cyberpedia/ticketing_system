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

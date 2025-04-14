from ..models import User

@admin.route('/tickets')
@login_required
@admin_required
def manage_tickets():
    tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
    return render_template('admin/ticket_list.html', tickets=tickets)

@admin.route('/tickets/<int:ticket_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    form = AdminTicketForm(obj=ticket)
    form.assigned_to.choices = [(u.id, u.username) for u in User.query.filter_by(role='support').all()]

    if form.validate_on_submit():
        ticket.subject = form.subject.data
        ticket.description = form.description.data
        ticket.status = form.status.data
        ticket.priority = form.priority.data
        ticket.assigned_to_id = form.assigned_to.data
        db.session.commit()
        flash('Ticket updated.')
        return redirect(url_for('admin.manage_tickets'))

    return render_template('admin/ticket_edit.html', form=form, ticket=ticket)

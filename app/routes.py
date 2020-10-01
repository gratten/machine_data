from app import app
from app import db
from flask import render_template, flash, redirect, url_for
from app.forms import AddMachineForm
from app.models import Machine

@app.route('/')
@app.route('/index')
def index():
    machines = Machine.query.all()
    return render_template('index.html', title='Home', machines=machines)

@app.route('/add_machine', methods=['GET', 'POST'])
def add_machine():
    form = AddMachineForm()
    if form.validate_on_submit():
        machine = Machine(project=form.project.data,
                          serialnum=form.serialnum.data,
                          customer=form.customer.data,
                          description=form.description.data)
        db.session.add(machine)
        db.session.commit()
        flash('Machine added')
        return redirect(url_for('index'))
    return render_template('add_machine.html', form=form)

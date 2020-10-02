from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,IntegerField, DecimalField
from wtforms.validators import DataRequired
from app.models import Machine

class AddMachineForm(FlaskForm):
    project = StringField('Project', validators=[DataRequired()])
    serialnum = StringField('Serial Number', validators=[DataRequired()])
    customer = StringField('Customer', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddKitForm(FlaskForm):
    project = StringField('Project', validators=[DataRequired()])
    # serialnum = StringField('Serial Number', validators=[DataRequired()])

    # create list of serial numbers that will populate the dropdown box
    machines = Machine.query.all()
    serialnums = []
    for m in machines:
        serialnums.append(m.serialnum)

    # serial number dropdown box
    serialnum = SelectField('Serial Number', choices=serialnums, validators=[DataRequired()])

    customer = StringField('Customer', validators=[DataRequired()])
    speed = IntegerField('Speed', validators=[DataRequired()])
    length = DecimalField('Length', validators=[DataRequired()])
    width = DecimalField('Width', validators=[DataRequired()])
    depth = DecimalField('Depth', validators=[DataRequired()])
    submit = SubmitField('Submit')
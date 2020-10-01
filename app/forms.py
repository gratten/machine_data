from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddMachineForm(FlaskForm):
    project = StringField('Project', validators=[DataRequired()])
    serialnum = StringField('Serial Number', validators=[DataRequired()])
    customer = StringField('Customer', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
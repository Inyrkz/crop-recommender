from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired


class SoilParameters(FlaskForm):
    '''Form to input the soil parameters'''
    nitrogen = IntegerField('Nitrogen', validators=[DataRequired()])
    phosphorous = IntegerField('Phosphorous', validators=[DataRequired()])
    potassium = IntegerField('Potassium', validators=[DataRequired()])
    temperature = FloatField('Temperature', validators=[DataRequired()])
    humidity = FloatField('Humidity', validators=[DataRequired()])
    pH = FloatField('pH', validators=[DataRequired()])
    rainfall = FloatField('Rainfall', validators=[DataRequired()])
    send = SubmitField('Check')

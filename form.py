from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired


class SoilParameters(FlaskForm):
    '''Form to input the soil parameters'''
    nitrogen = IntegerField('nitrogen', validators=[DataRequired()])
    phosphorous = IntegerField('phosphorous', validators=[DataRequired()])
    potassium = IntegerField('potassium', validators=[DataRequired()])
    temperature = FloatField('temperature', validators=[DataRequired()])
    humidity = FloatField('humidity', validators=[DataRequired()])
    pH = FloatField('pH', validators=[DataRequired()])
    rainfall = FloatField('rainfall', validators=[DataRequired()])
    send = SubmitField('send')

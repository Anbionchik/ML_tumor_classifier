from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TumorForm(FlaskForm):
    tumor_number = StringField('№ Опухоли')
    submit = SubmitField('Подтвердить')

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class TumorForm(FlaskForm):
    tumor_number = IntegerField('№ Опухоли',
                               validators=[InputRequired(message='Вы не ввели значение.'),
                                           NumberRange(min=1, max=171)])
    submit = SubmitField('Подтвердить')

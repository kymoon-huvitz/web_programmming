from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length

class GuestbookForm(FlaskForm):
    name = StringField("이름", validators=[DataRequired(), Length(max=50)])
    message = TextAreaField("내용", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField("등록")
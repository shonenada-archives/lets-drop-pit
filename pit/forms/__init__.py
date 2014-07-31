from wtforms import StringField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from wtforms.validators import ValidationError
from wtforms_tornado import Form

from pit.services.user import check_email_exist


class SignUpForm(Form):
    email = StringField('Email', [Email(), InputRequired()])
    password = StringField('Password', [Length(min=6, max=16)])
    confirm_password = StringField('Comfirm Password',
                                   [EqualTo('password')])
    nickname = StringField('Nickname', [Length(min=4, max=20)])

    def validate_email(form, field):
        if check_email_exist(field.data):
            raise ValidationError('Email is existed')


class SignInForm(Form):
    email = StringField('Email', [Email(), InputRequired()])
    password = StringField('Password', [Length(min=6, max=16)])

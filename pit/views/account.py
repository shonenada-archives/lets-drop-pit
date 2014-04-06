import json

from tornado.web import RequestHandler

from pit.app import db
from pit.models import User
from pit.services.user import check_email_exist


class SignUpView(RequestHandler):

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        nickname = self.get_argument('nickname')
        if check_email_exist(email):
            return self.write('exist')
        new_user = User(email=email, nickname=nickname)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return self.write('finished')


class SignInView(RequestHandler):

    def post(self):
        email = self.get_argument('email')
        print email

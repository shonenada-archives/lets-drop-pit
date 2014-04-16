from tornado.web import RequestHandler

from pit.app import db
from pit.models import User
from pit.forms import SignUpForm


class SignUpView(RequestHandler):

    def post(self):
        form = SignUpForm(self.request.arguments)
        if not form.validate():
            return self.finish({'success': False, 'messages': form.errors})
        new_user = User(email=email, nickname=nickname)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return self.finish({'success': True,
                           'message': 'Register Successfully.'})


class SignInView(RequestHandler):

    def post(self):
        email = self.get_argument('email')
        print email

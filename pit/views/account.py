from pit.views.base import View
from pit.app import db
from pit.models import User
from pit.forms import SignUpForm, SignInForm
from pit.services.user import authenticate
from pit.extensions import rbac


@rbac.allow(None, 'POST')
class SignUpView(View):

    def post(self):
        form = SignUpForm(self.request.arguments)

        if not form.validate():
            return self.finish({'success': False, 'messages': form.errors})

        new_user = User(email=form.data['email'],
                        nickname=form.data['nickname'])
        new_user.set_password(form.data['password'])
        db.session.add(new_user)
        db.session.commit()
        return self.finish({'success': True,
                           'message': 'Register Successfully.'})


@rbac.allow(None, 'POST')
class SignInView(View):

    def post(self):
        form = SignInForm(self.request.arguments)

        if not form.validate():
            return self.finish({'success': False, 'messages': form.errors})

        user = authenticate(form.data['email'], form.data['raw_passwd'])

        if not user:
            return self.finish({'success': False,
                                'messages': 'Wrong username or password.'})
        else:
            # login user
            self.set_secure_cookie('user_id', user.id)

import functools

from pit.views.base import View
from pit.forms import SignUpForm
from pit.extensions import rbac


class IndexView(View):

    @rbac.allow(None)
    def get(self):
        sign_up_form = SignUpForm()
        return self.render('index.html',
                           sign_up_form=sign_up_form)

from pit.views.base import View
from pit.forms import SignUpForm
from pit.extensions import rbac


@rbac.allow(None, 'GET')
class IndexView(View):

    def get(self):
        sign_up_form = SignUpForm()
        return self.render('index.html',
                           sign_up_form=sign_up_form)

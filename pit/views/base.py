from tornado.web import RequestHandler

from pit.models import User
from pit.extensions import rbac


class View(RequestHandler):

    def prepare(self):
        rbac.auth(self)
    
    @property
    def current_user(self):
        user_id = self.get_secure_cookie('user_id')
        if not user_id:
            return None
        current_user = User.query.find(user_id).first()
        return current_user

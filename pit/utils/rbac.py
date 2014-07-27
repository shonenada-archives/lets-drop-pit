from tornado.web import HTTPError


class RBAC(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

        self.allowed = set()
        self.denied = set()

    def record(self, operation, role_name):
        assert operation in ('allow', 'deny')

        def decorator(method_func):
            def wrapper(cls, *arg, **kwargs):
                view = cls.__class__
                method = method_func.__name__.upper()
                if operation == 'allow':
                    self.allowed.add((role_name, method, view))
                elif operation == 'deny':
                    self.denied.add((role_name, method, view))
                return method_func(cls, *arg, **kwargs)
            return wrapper
        return decorator

    def allow(self, role_name):
        return self.record('allow', derole_name)

    def deny(self, role_name):
        return self.record('deny', role_name)

    def init_app(self, app):
        self.app = app

    def has_permission(self, user, method, resource):
        if user:
            role_name = user.role.name
        else:
            role_name = None
        is_allowed = (role_name, method, resource) in self.allowed
        is_denied = (role_name, method, resource) in self.denied
        return is_allowed and not is_denied

    def auth(self, view):
        user = view.current_user
        method = view.request.method
        resource = type(view)
        permit = self.has_permission(user, method, resource)
        if not permit:
            raise HTTPError(403)

    def load_permission(self, permissions):
        allowed = permissions['allowed']
        denied = permissions['denied']

        for a in allowed:
            self.allowed.add(a)

        for d in denied:
            self.denied.add(d)

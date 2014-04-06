from pit.models import User


def check_email_exist(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False

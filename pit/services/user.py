from pit.models import User


def check_email_exist(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False


def authenticate(email, raw_passwd):
    if not check_email_exist(email):
        return None

    hashed_passwd = User.hash_password(raw_passwd)
    user = (User.query.filter_by(email=email).filter_by(password=hashed_passwd)
            .first())
    if user:
        return user
    else:
        return None

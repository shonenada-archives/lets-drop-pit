import os


app_root = os.path.dirname(os.path.realpath(__name__))


app_settings = {
    'title': 'Lets drop into pits',
    'template_path': os.path.join(app_root, 'pit', 'templates'),
    'static_path': os.path.join(app_root, 'pit', 'static'),
    'autoscape': True,
    'xsrf_cookies': True,
    'gzip': True,
}

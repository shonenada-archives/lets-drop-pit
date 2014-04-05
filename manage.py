import sys

from pit.app import create_app, db

from development import config


application = create_app(config)

if sys.argv[1] == 'db':
    db.create_all()
    print 'Create database.'

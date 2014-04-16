import sys

from pit.app import create_app, db

from development import config


application = create_app(config)

if sys.argv[1] == 'db':
    if len(sys.argv) > 2 and sys.argv[2] == '-d':
        db.drop_all()
        print 'Droped database.'
    db.create_all()
    print 'Create database.'

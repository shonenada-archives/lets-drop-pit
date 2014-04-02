from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from pit.app import create_app

from development import config


WEB_PORT = 8888


application = create_app(config)

http_server = HTTPServer(application, xheaders=True)
http_server.listen(WEB_PORT)
IOLoop.instance().start()


import sys
import os

dirname = os.path.dirname(__file__)
if dirname not in sys.path:
    sys.path.append(dirname)
    sys.path.append(dirname+'/../')


import tornado.web
import tornado.httpserver
from storage.models_manager import ModelManager
from settings import TEMPLATE_PATH, STATIC_PATH, MYSQL_USER, MYSQL_PASS, MYSQL_DB_NAME, MYSQL_HOST, MYSQL_PORT
from views import MainHandler



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
        ]
        settings = {
            "template_path": TEMPLATE_PATH,
            "static_path": STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)




def main():
    MainHandler.DB_MANAGER = ModelManager(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB_NAME)
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()



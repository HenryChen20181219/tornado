import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado
import tornado.options
from tornado.options import options,parse_command_line,define
from tornado.web import RequestHandler,url

define('port',default=8000,type=int,help='run server on the given port')
# tornado.options.define('itcast',default=[],type=str,multiple=True,help='itcast subject.')

class IndexHandler(RequestHandler):
    def get(self):
        python_url = self.reverse_url('python_url')
        self.write('<a href="%s">itcast</a>'%python_url)

class ItcastHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)

if __name__ == '__main__':
    # tornado.options.parse_command_line()
    # tornado.options.parse_config_file('./config')
    # options.logging = None
    parse_command_line()
    # print(tornado.options.options.itcast)

    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/cpp',ItcastHandler,{"subject":"c++"}),
                                   url(r'/python',ItcastHandler,{'subject':'python'},name='python_url'),
                                   ],
                                  debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


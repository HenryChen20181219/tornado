import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    '''主路由处理类'''
    def get(self):
        self.write('Hello itcast!')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler),])
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8000)
    http_server.bind(8000)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()

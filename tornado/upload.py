import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options,define
from tornado.web import RequestHandler
import json

define('port',default=8000,type=int,help='run server on the given port')

class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello itcast')

class UploadHandler(RequestHandler):
    def post(self):
        files = self.request.files
        img_files = files.get('img')
        if img_files:

            img_file = img_files[0]['body']#列表 格式如下：[{'filename':filename},{'body',body},],故取img_file[0]['body']
            file = open('./itcast','wb')
            file.write(img_file)
            file.close()
        d = dict(
            a=str(img_files),
            # b=str(img_files[0]),
            # c=str(img_files[0]['body'])
          )
        e = json.dumps(d)
        self.write(e)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/upload',UploadHandler)],
                                  debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
#coding=utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os

# 设置配置
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__),"static")
)

# 渲染首页的模板
class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("home.html");

# 渲染登录的模板
class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html");

# app 的编写
app = tornado.web.Application(handlers=[(r"/home",HomeHandler),

                                        (r"/login",LoginHandler)
                                        ], **settings);


# main 函数
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();

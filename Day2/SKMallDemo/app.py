#coding=utf-8;

import os

import tornado.ioloop
import tornado.httpserver
import tornado.web


# 关系数据库管理类
from SKMallDemo.py import orm

user_orm = orm.UserManagerORM();

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

# 注册页面渲染
class  RegistHandler(tornado.web.RequestHandler):
    # 访问进行渲染
    def get(self, *args, **kwargs):
        self.render("regist.html");
    # 提交数据 进行访问数据库
    def post(self, *args, **kwargs):
        username = self.get_argument("username",default=None);
        password = self.get_argument("password",default=None);
        self.write(username + "--" + password);

        user_info = {
            'user_name':username,
            'user_password':password
        };

        user_orm.CreateNewUser(user_info)






# app 的编写
app = tornado.web.Application(handlers=[(r"/home",HomeHandler),
                                        (r"/login",LoginHandler),
                                        (r"/regist",RegistHandler),
                                        ], **settings);


# main 函数
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8666);
    tornado.ioloop.IOLoop.instance().start();

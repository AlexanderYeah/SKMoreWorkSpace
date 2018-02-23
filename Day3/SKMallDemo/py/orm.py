#coding=utf-8;

from sqlalchemy import  *
from sqlalchemy.orm import  *
from pymysql import *
# 设置去连接数据库
db_setting = {
    'database_type':'pymysql',
    'connector':'mysqlconnector',
    'user_name':'root',
    'password':'123456',
    'host_name':'localhost',
    'database_name':'MallDatabase',
};

# 下面这个类 就是实体的类 对应数据库中的User的表
class User(object):
    def __init__(self,user_name,user_password):
        self.user_name = user_name;
        self.user_password  = user_password;

# 这个类就是直接操作数据库的类
class UserManagerORM():
    def __init__(self):
        """
            类的构造函数 对象创建的时候 自动运行
            初始化数据库连接
            mysql+mysqlconnector://root:password@localhost:3306/test 格式固定的
        """

        self.engine = create_engine(
            "mysql+mysqlconnector://root:123456@localhost:3306/MallDatabase"
        );

        #获取所有的表
        self.metadata = MetaData(self.engine);
        # 获取user 表
        self.user_table = Table('user_table',self.metadata,autoload = True);
        # 将实体类 映射到 user 的类
        # 在数据库建立表格的时候 要增加主键 否则映射会出现问题的
        # 还有一点就是主键设置为自增 否则存入信息到数据库的时候 还是会出现问题
        mapper(User,self.user_table);
        # 生成一个会话层 与上面建立的数据库引擎进行绑定
        self.Session = sessionmaker();
        self.Session.configure(bind = self.engine);
        # 创建一个会话
        self.session = self.Session();



    # 创建一个新的用户
    def CreateNewUser(self,user_info):
        """
            根据传入的信息创建一张表格
        """
        new_user = User(
            user_info['user_name'],
            user_info['user_password']
        );
        # 添加一个新的用户 并且进行提交
        self.session.add(new_user);
        self.session.commit();


    # 查询用户名和密码
    def GetPwdByUsername(self,username):
        """
        根据用户名返回密码
        :param 用户名:
        :return:
        """
        # 使用query 方法去调用
        return self.session.query(User).filter_by(user_name = username).all()[0];

    # 获取所有的用户列表
    def GetAllUser(self):
        return  self.session.query(User);

    # 删除指定的用户
    def DeleteUserByName(self,username):
        target_delete_user = self.session.query(User).filter_by(user_name = username).all()[0];
        self.session.delete(target_delete_user);









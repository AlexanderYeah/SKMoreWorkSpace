# Day2  注册的简单逻辑实现 

逻辑:前端把用户名和密码 post 过来,后台存储到mysql数据库。


##  orm.py 的编写 此文件主要是数据库管理类

使用的SQLAlchemy 
使用pip 安装
> pip install sqlalchemy  

Object-Relational Mapping，把关系数据库的表结构映射到对象上面去,以便于数据的操作。


# Tips

1. 映射表的时候第一点就要 数据库建立表的时候要设置主键并且要设置为自增的类型，否则会报错。
 

# 实例化sqlalchemy对象
# 配置连接数据库的参数
# 注册SQLALchemy

import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# 实例化迁移对象
migrate = Migrate()


def init_ext(app):
    config_db(app)
    # 初始化SQLALchemy
    db.init_app(app)
    # 注册迁移命令
    migrate.init_app(app=app, db=db)




# 配置数据库连接的参数
def config_db(app):
    # 配置数据库
    # 地址格式： mysql+驱动(pymysql)://root:root@127.0.0.1:3306/(数据库名称)?+参数
    app.config['SECRET_KEY'] = '13131231321'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask?charset=utf8'



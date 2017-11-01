# coding=utf-8
from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course


def create_app(config):
    """可以根据传入的config 名称，加在不同的配置
    """
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLAlchemy的初始化方式改为使用 init_app
    db.init_app(app)

    #路由函数暂时写在这里，后面会介绍使用Flask 的Blueprint实现路由的模块化
    
    @app.route('/')
    def index():
        courses = Course.query.all()
        return render_template('index.html', courses=courses)

    @app.route('/admin')
    def admin_index():
        return 'admin'
    """
    """ APP 工厂
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprint(app)
    return app


def register_blueprint(app):
    from .handlers import front, course, admin

    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

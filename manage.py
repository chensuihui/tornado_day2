import tornado.web
import os
import tornado.ioloop
from tornado.options import define, options, parse_command_line
from app.views import IndexHandler, XindexHandler, DbHandler, DropDbHandler, AddStuHandler, StusHandler

# 设置默认端口
define('port', default=8080, type=int)


def make_app():
    # handlers参数中定义路由匹配地址
    return tornado.web.Application(handlers=[
        (r'/', IndexHandler),
        (r'/xindex/', XindexHandler),
        (r'/init_db/', DbHandler),
        (r'/drop_db/', DropDbHandler),
        (r'/add_stu/', AddStuHandler),
        (r'/stus/', StusHandler),
    ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    )


if __name__ == '__main__':
    # 解析启动命令，python xxx.py --port=端口号
    parse_command_line()
    # 生成Application对象
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 启动
    tornado.ioloop.IOLoop.current().start()

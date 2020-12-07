import tornado.web
from .models import create_db, drop_db, Student
from utils.conn import session


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello day2 tornado')


class XindexHandler(tornado.web.RequestHandler):

    def get(self):
        items = ['Python', 'Php', 'C++', '从入门到放弃']
        self.render('index.html', items=items, items2=items)


class DbHandler(tornado.web.RequestHandler):
    def get(self):
        create_db()
        self.write('创建表成功')


class DropDbHandler(tornado.web.RequestHandler):
    def get(self):
        drop_db()
        self.write('删除表成功')


class AddStuHandler(tornado.web.RequestHandler):

    def post(self):
        # 创建单条数据
        # stu = Student()
        # stu.s_name = '小明'
        # session.add(stu)
        # session.commit()
        # self.write('新增数据成功')
        # 创建多条数据
        stus = []
        for i in range(10):
            stu = Student()
            stu.s_name = '小明_%s' % i
            stus.append(stu)

        session.add_all(stus)
        session.commit()
        self.write('新增数据成功')


class StusHandler(tornado.web.RequestHandler):

    def get(self):
        # stus = session.query(Student).filter(Student.s_name == '小明_0').all()
        stus = session.query(Student).filter_by(s_name='小明_0').all()
        print(stus)
        self.write('查询数据成功')

    def delete(self):
        # 实现删除,session.delete()
        stu = session.query(Student).filter(Student.s_name == '小明_0').first()
        if stu:
            session.delete(stu)
            session.commit()
        # 第二种方法，delete()方法
        session.query(Student).filter(Student.s_name == '小明_1').delete()
        session.commit()
        self.write('删除成功')

    def patch(self):
        # 实现修改部分属性，第一种方式
        # stu = session.query(Student).filter(Student.s_name == '小明_2').first()
        # stu.s_name = '小花'
        # session.add(stu)
        # session.commit()
        # 第二种方式，update
        session.query(Student).filter(Student.s_name == '小花').update({'s_name': '小狗'})
        session.commit()
        self.write('修改成功')

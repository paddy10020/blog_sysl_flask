# -*- coding=utf-8 -*-
from flask.ext.script import Manager
from apps import app

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
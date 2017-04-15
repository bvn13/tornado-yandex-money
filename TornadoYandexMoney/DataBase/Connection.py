# -*- encoding: utf-8 -*-

'''
Created on Apr 14, 2017
@author: bvn13
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker

from TornadoYandexMoney.DataBase.Settings import settings


engine = create_engine('%s://%s:%s@%s:%s/%s' % (
    settings['protocol'],
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['database']))
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

#Session = sessionmaker(bind=engine)


class Connection(object):

    @staticmethod
    def getSession():
        return Session()

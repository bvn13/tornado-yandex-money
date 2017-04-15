# -*- encoding: utf-8 -*-

'''
Created on Apr 14, 2017
@author: bvn13
'''
from abc import ABCMeta, abstractstaticmethod


class Manager(metaclass=ABCMeta):
    '''
    Database table manager
    '''
    pass

    @abstractstaticmethod
    def _find_by_id(id : int):
        pass


Manager.register(tuple)
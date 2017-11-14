#! /usr/bin/python
# -*- coding: utf-8 -*-

class Setting(object):
    '''定义设置类'''
    def __init__(self):
        # 自动回复
        self.auto_replay = False
        self.person_auto = {}  # 每个用户的自动回复状态

        # 防撤销
        self.revocation = True

        #用户信息储存
        self.msg_information = {}

    def login_info(self):
        '''登陆成功时，打印反馈'''
        print u'您已成功登陆网页版微信！'

    def exit_info(self):
        '''退出时，打印反馈'''
        print u'您已退出网页版微信！'

#! /usr/bin/python
# -*- coding: utf-8 -*-
import itchat
import function_library as fun
from setting import Setting
from itchat.content import *


if __name__ == '__main__':
    '''程序主代码'''
    setting = Setting()
    itchat.auto_login(hotReload=True, loginCallback=setting.login_info, exitCallback=setting.exit_info)

    #注册一般消息事件
    @itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True, isGroupChat=True)
    def getmsginfo(msg):
        fun.get_msg_info(msg,setting)


    #注册通知事件
    @itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
    def getrevocation(msg):
        '''如果为撤回操作'''
        if setting.revocation == True and u'撤回了一条消息' in msg['Content']:
            fun.send_revocation(msg,setting)






    itchat.run()
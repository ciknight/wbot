#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import  unicode_literals

import itchat
from itchat.content import *


# auto accept friends request
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('你好!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    text = itchat.send(msg['Text'], msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
    itchat.dump_login_status()

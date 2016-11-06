#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import  unicode_literals

import itchat
from itchat.content import *
from bot import tuling


# auto accept friends request
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('你好!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    text = itchat.send(msg['Text'], msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def groupchat_reply(msg):
    if msg['isAt']:
        replay_text = tuling.replay_text(msg['Content'],
                msg['ActualNickName']) or '系统错误'
        itchat.send(replay_text, msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
    itchat.dump_login_status()

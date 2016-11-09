#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import  unicode_literals

import itchat
from itchat.content import *
from bot import faq, tuling

REPLAY_ERROR_TEXT = '系统错误'


# auto accept friends request
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(faq.replay_welcome(), msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    if faq.invite_key in msg['Text'].upper():
        # TODO Modify add_member_into_chatroom
        invite_friend = [{'UserName': msg['FromUserName']}]
        grouproom = itchat.search_chatrooms(name=faq.group_name)
        grouproom = grouproom and grouproom[0] or None
        result = itchat.add_member_into_chatroom(grouproom.get('UserName'),
                invite_friend, useInvitation=True)
        # invite success
        if result['BaseResponse']['Ret'] == 0:
            # TODO can not return Bool
            return
        else:
            itchat.send(REPLAY_ERROR_TEXT, msg['FromUserName'])
            return

    # else TuLing replay
    replay_text = tuling.replay_text(msg['Text'],
            msg['FromUserName']) or REPLAY_ERROR_TEXT
    itchat.send(replay_text, msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def groupchat_reply(msg):
    if msg['isAt']:
        replay_text = tuling.replay_text(msg['Text'],
                msg['ActualNickName']) or '系统错误'
        itchat.send(replay_text, msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
    itchat.dump_login_status()

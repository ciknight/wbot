#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from itchat.content import *


@itchat.msg_register(TEXT)
def text_reply(msg):
    text = itchat.send(msg['Text'], msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
    itchat.dump_login_status()

# -*- coding: utf-8 -*-
import logging

from tornado import log

import itchat
from itchat.content import *
from bot import faq, interpreter, tuling

log.enable_pretty_logging()
# logging.basicConfig(format='[%(levelname)s] %(asctime)s %(name)s:%(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

REPLAY_ERROR_TEXT = '系统错误'


# auto accept friends request
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    logging.info('add friend {}, message {}'.format(msg['RecommendInfo']['UserName'], msg['Text']))
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(faq.replay_welcome(), msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT)
def text_reply(msg):
    if  msg['FromUserName'] == '@046be09334d1b7580027e688768e9010':
            itchat.send('你已被拉黑', msg['FromUserName'])
            return

    nickName = itchat.search_friends(userName=msg['FromUserName']).get('NickName', 'Unknown')
    logging.info('{}-{} send: {}'.format(nickName, msg['FromUserName'], msg['Content']))
    if msg["FromUserName"] == itchat.get_friends()[0]["UserName"]:
        # dont replay self
        return

    # if invite
    if faq.invite_key in msg['Text'].upper():
        # TODO Modify add_member_into_chatroom
        invite_friend = [{'UserName': msg['FromUserName']}]
        grouproom = itchat.search_chatrooms(name=faq.group_name)
        grouproom = grouproom and grouproom[0] or None
        result = itchat.add_member_into_chatroom(grouproom.get('UserName'),
                invite_friend, useInvitation=True)

        # invite success
        if result['BaseResponse']['Ret'] == 0:
            logging.info('invite user {}-{} successful'.format(nickName, msg['FromUserName']))
        else:
            logging.error('invite user {}-{} failed'.format(nickName, msg['FromUserName']))
            itchat.send(REPLAY_ERROR_TEXT, msg['FromUserName'])
    else:
        # else TuLing replay
        replay_text = tuling.replay_text(msg['Text'],
                msg['FromUserName']) or REPLAY_ERROR_TEXT
        logging.info('tuling replay user {}-{}: {}'.format(nickName, msg['FromUserName'], replay_text))
        itchat.send(replay_text, msg['FromUserName'])

    # TODO can not return Bool
    return


@itchat.msg_register(TEXT, isGroupChat=True)
def groupchat_reply(msg):
    # TODO
    #nickName = itchat.search_friends(userName=msg['FromUserName']).get('NickName', 'Unknown')
    #logging.info('group xxx: {}-{} send: {}'.format(nickName, msg['FromUserName'], msg))
    if msg['Text'][0] == interpreter.PY_SYMBLOE:
        replay_text = interpreter.run_py_cmd(msg['Text'][1:])
        itchat.send(replay_text, msg['FromUserName'])
    elif msg['isAt']:
        replay_text = tuling.replay_text(msg['Text'],
                msg['ActualNickName']) or REPLAY_ERROR_TEXT
        itchat.send(replay_text, msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
    itchat.dump_login_status()

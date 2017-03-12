# -*- coding: utf-8 -*-

from .meta_singleton import MetaSingleton


class FAQ(object):
    __metaclass__ = MetaSingleton

    def __init__(self, *args, **kwargs):
        super(FAQ, self).__init__()
        self._friend_welcome = kwargs.get('friend_welcome', '' )
        self._group_info = kwargs.get('group_info', {})

    @property
    def group_name(self):
        return self._group_info.get('name', 'PY Learning')

    @property
    def invite_key(self):
        return self._group_info.get('invite_key', 'PYTHON')

    def replay_welcome(self, is_group=False):
        if is_group: return None # TODO group replay
        return self._friend_welcome

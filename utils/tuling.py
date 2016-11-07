# -*- coding: utf-8 -*-

import requests

from .meta_singleton import MetaSingleton


class TuLing(object):
    """
    Tuling robot http://www.tuling123.com
    Doc http://www.tuling123.com/help/h_cent_webapi.jhtml
    """
    __metaclass__ = MetaSingleton
    API_URL = 'http://www.tuling123.com/openapi/api'

    SUB_TYPE_TEXT = 100000

    def __init__(self, *args, **kwargs):
        super(TuLing, self).__init__()
        self._api_key = kwargs.get('api_key')
        self._api_secret = kwargs.get('api_secret')
        self._api_url = kwargs.get('api_url', TuLing.API_URL)
        assert self._api_key and self._api_secret, \
            'tuling key or secret is None'

    def _post(self, data):
        response = requests.post(url=self._api_url, data=data)
        if response.status_code is not 200:
            return None
        return response.json()

    def replay_text(self, info, userid=None):
        data = {
            'key': self._api_key,
            'info': info
        }
        if userid: data['userid'] = userid
        return_dict = self._post(data)
        # TODO news and urls type
        if return_dict['code'] == TuLing.SUB_TYPE_TEXT:
            return return_dict['text']

        return None

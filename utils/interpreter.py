# -*- coding: utf-8 -*-

import subprocess

from .meta_singleton import MetaSingleton


class Interpreter(object):
    __metaclass__ = MetaSingleton

    PY_SYMBLOE = '#'

    def __init___(self, *args, **kwargs):
        super(Interpreter, self).__init__()

    def run_py_cmd(self, cmd):
        cmd = cmd.strip()
        if not cmd: return u'脚本不能为空'

        command = [u"python", u"-c", cmd]
        result = subprocess.check_output(command) or u'执行成功'
        return isinstance(result, str) and result.decode('utf-8') or result

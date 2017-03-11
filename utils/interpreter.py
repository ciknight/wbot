# -*- coding: utf-8 -*-
import sys


class TextArea(object):

    def __init__(self):
        self.buffer = []

    def write(self, *args, **kwargs):
        self.buffer.append(args)


class Interpreter(object):
    PY_SYMBLOE = '#'

    def __init___(self, *args, **kwargs):
        super(Interpreter, self).__init__()

    @staticmethod
    def run_py_cmd(cmd):
        cmd = cmd.strip()
        if not cmd: return 'NULL'

        try:
            # eval("eval('__import__(\"os\")')", {'__builtins__':__builtins__, "__import__": None})))"
            stdout = sys.stdout
            sys.stdout = TextArea()
            eval(cmd, {'__builtins__':__builtins__, '__import__': None})
            text_area, sys.stdout = sys.stdout, stdout
            return ''.join([''.join(text) for text in text_area.buffer])
        except:
            return '执行错误'

# -*- coding: utf-8 -*-


class Interpreter(object):
    PY_SYMBLOE = '#'

    def __init___(self, *args, **kwargs):
        super(Interpreter, self).__init__()

    @staticmethod
    def run_py_cmd(cmd):
        cmd = cmd.strip()
        if not cmd: return u'空指令'

        try:
            # eval("eval('__import__(\"os\")')", {'__builtins__':__builtins__, "__import__": None})))"
            result = eval(cmd, {'__builtins__':__builtins__, '__import__': None})
        except:
            return u'执行错误'
        return isinstance(result, str) and result.decode('utf-8') or result

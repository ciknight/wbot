# -*- coding: utf8 -*-


class MetaSingleton(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.instance

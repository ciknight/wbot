# -*- coding: utf-8 -*-

from config import *
from utils import FAQ, Interpreter, TuLing

__all__ = ['tuling', 'faq']


faq = FAQ(**faq_config)
interpreter = Interpreter()
tuling = TuLing(**tuling_config)

# -*- coding: utf-8 -*-

from config import *
from utils import TuLing, FAQ

__all__ = ['tuling', 'faq']


tuling = TuLing(**tuling_config)
faq = FAQ(**faq_config)

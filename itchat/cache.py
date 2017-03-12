# -*- coding: utf-8 -*-
from .expire_dict import ExpireDict


_cache = ExpireDict(max_len=300)

def set_cache(key, value, seconds=180):
    _cache[key] = value
    _cache.set_ttl(key, seconds)

def get_cache(key):
    return _cache[key]

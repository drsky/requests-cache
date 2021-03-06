#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path hack
import os, sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

from tests.test_custom_dict import BaseCustomDictTestCase
try:
    from requests_cache.backends.storage.redisdict import RedisDict
except ImportError:
    print("Redis not installed")
else:

    class RedisDictTestCase(BaseCustomDictTestCase, unittest.TestCase):
        dict_class = RedisDict
        pickled_dict_class = RedisDict

    if __name__ == '__main__':
        unittest.main()

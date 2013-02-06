#!/usr/bin/env python
try:
  # a hack to see if the app engine sdk is loaded..
  import yaml
except ImportError:
  import dev_appserver
  dev_appserver.fix_sys_path()

import unittest
from flask.ext import gae_tests
from flask.ext import gae_shorturl


class TestCase(gae_tests.TestCase):
  def setUp(self):
    gae_tests.TestCase.setUp(self)


if __name__ == '__main__':
  unittest.main()

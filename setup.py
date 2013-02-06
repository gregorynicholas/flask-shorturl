#!/usr/bin/env python
"""
Flask App Engine ShortURLs
-----------------------

Flask extension for working with short url generation and routing on App Engine.

Links
`````

* `documentation <http://packages.python.org/flask-gae_shorturl>`_
* `development version
  <http://github.com/gregorynicholas/flask-gae_shorturl/zipball/master#egg=Flask%20App%20Engine%20Messages-dev>`_

"""
from setuptools import setup

setup(
  name='flask-gae_shorturl',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-gae_shorturl',
  license='MIT',
  author='gregorynicholas',
  description='Flask extension for working with short url generation and \
routing on App Engine.',
  long_description=__doc__,
  py_modules=['flask_gae_shorturl'],
  # packages=['flaskext'],
  # namespace_packages=['flaskext'],
  include_package_data=True,
  data_files=[],
  zip_safe=False,
  platforms='any',
  install_requires=[
    'flask',
    'blinker',
  ],
  tests_require=[
    'nose',
    'blinker',
    'flask_gae_tests',
  ],
  dependency_links = [
    'https://github.com/gregorynicholas/flask-gae_tests/tarball/master',
  ],
  test_suite='nose.collector',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)

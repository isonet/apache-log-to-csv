#! /usr/bin/env python

from setuptools import setup

setup(name="apache-log-to-csv",
      version="1.0.0",
      author="Paul Biester",
      author_email="p.biester@isonet.fr",
      packages=['apache_log_to_csv'],
      install_requires = [
        'apache-log-parser',
        'argparse',
        'csv',
      ],
      license = 'GPLv3+',
      description = "Convert apache log files to csv files. Supports different formats. Excel compatible.",
      test_suite='apache_log_to_csv.tests',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
)

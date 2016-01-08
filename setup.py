#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from setuptools.command.test import test

import os, sys, subprocess

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise SystemExit(
            subprocess.call([sys.executable,
                             'app_test_runner.py',
                             'test']))

install_requires = ['']
base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = "djangomi",
    version = "0.2",
    description = "Django Mi(ni) for Django projects",
    url = "http://github.com/futurice/djangomi",
    author = "Jussi Vaihia",
    author_email = "jussi.vaihia@futurice.com",
    packages = ["djangomi"],
    include_package_data = True,
    keywords = 'django as flask',
    license = 'BSD',
    install_requires = install_requires,
    cmdclass = {
        'test': TestCommand,
    },
)

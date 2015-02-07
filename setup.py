# coding=utf-8

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTestCommand(TestCommand):
    """Command to run py.test unit tests"""
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    tests_require=['pytest'],
    cmdclass={'test': PyTestCommand},
)

"""
In this file, Keep
- all variables
- all functions
- all classes
which we are planning to use it in other programs.

This file is also called as "PYTHON-MODULE" or "PYTHON-LIBRARY"
"""

course = "Python"


def add(a, b):
    return a + b


class Employee:
    def store_name(self, n):
        self.name = n
    def get_name(self):
        return self.name
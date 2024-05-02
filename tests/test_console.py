#!/usr/bin/python3
"""
Test for class BaseModel
"""

import console
import json
from datetime import datetime
import unittest
HBNBCommand = console.HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_class(self):
        """Documentation for class"""
        this = '\n        Command interpreter class\n    '
        that = HBNBCommand.__doc__
        self.assertEqual(this, that)

    def test_doc_file(self):
        """Documentation for file"""
        this = '\nCommand interpreter for Holberton AirBnB project\n'
        that = console.__doc__
        self.assertEqual(this, that)


if __name__ == "__main__":
    unittest.main

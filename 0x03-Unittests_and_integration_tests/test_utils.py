#!/usr/bin/env python3
"""
This module contains a python unit test for utils
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    this class is for testing access_nested_map method/function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        this method test the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

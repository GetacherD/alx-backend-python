#!/usr/bin/env python3
"""
Test nested_map
"""
from unittest.mock import patch, MagicMock
from unittest import TestCase
from parameterized import parameterized
import utils


class TestAccessNestedMap(TestCase):
    """ Class to test for nested_map"""
    nested_map1 = {"a": 1}
    nested_map2 = {"a": {"b": 2}}
    nested_map3 = {"a": {"b": 2}}
    path3 = ("a", "b")
    path2 = ("a",)
    path1 = ("a",)
    nested_map4: dict = {}
    nested_map5 = {"a": 1}
    path4 = ("a",)
    path5 = ("a", "b")

    @parameterized.expand([
        ([nested_map1, path1], 1),
        ([nested_map2, path2], {"b": 2}),
        ([nested_map3, path3], 2)
    ])
    def test_access_nested_map(self, nmap, out):
        """ test for access_nested_map """
        self.assertEqual(utils.access_nested_map(*nmap), out)

    @parameterized.expand([
        (nested_map4, path4, KeyError('a')),
        (nested_map5, path5, KeyError('b'))
    ])
    def test_access_nested_map_exception(self, nmap, path, out):
        """ test exception"""
        with self.assertRaises(KeyError) as exc:
            utils.access_nested_map(nmap, path)
        self.assertIsInstance(exc.exception, KeyError)
        self.assertEqual(str(exc.exception), str(out))


class TestGetJson(TestCase):
    """ Test for get json """

    test_url_1 = "http://example.com"
    test_payload_1 = {"payload": True}
    test_url_2 = "http://holberton.io"
    test_payload_2 = {"payload": False}

    @parameterized.expand([
        (test_url_1, test_payload_1),
        (test_url_2, test_payload_2)
    ])
    def test_get_json(self, url, out):
        """ test get json method"""
        with patch("utils.requests.get") as resp_mock:
            resp = MagicMock()
            resp.json.return_value = out
            resp_mock.return_value = resp
            self.assertEqual(utils.get_json(url), out)
            resp_mock.assert_called_once_with(url)


class TestMemoize(TestCase):
    """ test momoization"""

    def test_memoize(self):
        """ test memoize"""
        class TestClass:
            """ test class """

            def a_method(self):
                """ dummy method"""
                return 42

            @utils.memoize
            def a_property(self):
                """ dummy property"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mk:
            mk.return_value = 42
            tst = TestClass()
            res2 = tst.a_property
            res2 = tst.a_property
            mk.assert_called_once()
            self.assertEqual(42, res2)

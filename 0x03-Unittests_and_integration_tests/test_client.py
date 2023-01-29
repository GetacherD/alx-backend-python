#!/usr/bin/env python3
"""
Test For Client Module
"""
import unittest
from unittest.mock import patch
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing client module """

    @parameterized.expand([
        ("google", {"google": "google"}),
        ("abc", {"abc": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org, output, mk_get_json):
        """ Test Org property"""

        gcl = client.GithubOrgClient(org)
        url = gcl.ORG_URL.format(org=org)
        mk_get_json.return_value = output
        self.assertEqual(output, gcl.org)
        mk_get_json.assert_called_once_with(url)

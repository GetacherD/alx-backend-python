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
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mk_get_json):
        """ Test Org property"""

        gcl = client.GithubOrgClient(org)
        url = gcl.ORG_URL.format(org=org)
        gcl.org()
        mk_get_json.assert_called_once_with(url)

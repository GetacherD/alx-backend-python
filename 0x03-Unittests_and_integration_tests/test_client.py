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

    @parameterized.expand(
        [("google", {"google": "google.github"}), (
            "abc", {"abc": "abc.github"})])
    def test_org(self, org, output):
        """ Test Org property"""
        with patch("client.get_json") as mk_get_json:
            mk_get_json.return_value = output
            gcl = client.GithubOrgClient(org)
            url = gcl.ORG_URL.format(org=org)
            self.assertEqual(gcl.org, output)
            self.assertEqual(gcl.org, output)
            mk_get_json.assert_called_once_with(url)

#!/usr/bin/env python3
"""
Test For Client Module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing client module """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org, mk_get_json):
        """ Test Org property"""

        gc = client.GithubOrgClient(org)
        url = gc.ORG_URL.format(org=org)
        gc.org()
        mk_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """ test property"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as my_org:
            my_org.return_value = {"repos_url": "www.google.com"}
            gc = client.GithubOrgClient("google")
            self.assertEqual(gc._public_repos_url, "www.google.com")

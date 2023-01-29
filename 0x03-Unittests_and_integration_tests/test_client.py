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

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """ Test public_repos """
        mock_json.return_value = [{'license': {'key': 'apache-2.0',
                                               'name': 'Apache License 2.0',
                                               'node_id': 'MDc6TGljZW5zZTI=',
                                               'spdx_id': 'Apache-2.0'},
                                   'name': 'truth'
                                   },
                                  {
            'license': None,
            'name': 'ruby-openid-apps-discovery'
        },
            {
                'license': {'key': 'apache-2.0',
                            'name': 'Apache License 2.0',
                            'node_id': 'MDc6TGljZW5zZTI=',
                            'spdx_id': 'Apache-2.0',
                            },
                'name': 'autoparse'
        },
            {
                                      'license': {'key': 'other',
                                                  'name': 'Other',
                                                  'node_id': 'MDc6TG=',
                                                  'spdx_id': 'NOASSERTION',
                                                  'url': None},

                                      'name': 'anvil-build'}
        ]
        with patch("client.GithubOrgClient._public_repos_url"
                   ) as mock_repo_url:
            mock_repo_url.return_value = "https://api.google.com/repos"
            gc = client.GithubOrgClient("google")
            gc._public_repos_url()
            self.assertEqual(gc.public_repos(), [
                             'truth',
                             'ruby-openid-apps-discovery',
                             'autoparse', 'anvil-build'])
            self.assertEqual(gc.public_repos("other"), ['anvil-build'])
            mock_json.assert_called_once()
            mock_repo_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, lic, out):
        """ test has license """
        self.assertEqual(client.GithubOrgClient.has_license(repo, lic), out)

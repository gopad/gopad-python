# coding: utf-8

"""
    Gopad OpenAPI

    API definition for Gopad  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import gopad
from gopad.api.team_api import TeamApi  # noqa: E501
from gopad.rest import ApiException


class TestTeamApi(unittest.TestCase):
    """TeamApi unit test stubs"""

    def setUp(self):
        self.api = gopad.api.team_api.TeamApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_append_team_to_user(self):
        """Test case for append_team_to_user

        Assign a user to team  # noqa: E501
        """
        pass

    def test_create_team(self):
        """Test case for create_team

        Create a new team  # noqa: E501
        """
        pass

    def test_delete_team(self):
        """Test case for delete_team

        Delete a specific team  # noqa: E501
        """
        pass

    def test_delete_team_from_user(self):
        """Test case for delete_team_from_user

        Remove a user from team  # noqa: E501
        """
        pass

    def test_list_team_users(self):
        """Test case for list_team_users

        Fetch all users assigned to team  # noqa: E501
        """
        pass

    def test_list_teams(self):
        """Test case for list_teams

        Fetch all available teams  # noqa: E501
        """
        pass

    def test_permit_team_user(self):
        """Test case for permit_team_user

        Update user perms for team  # noqa: E501
        """
        pass

    def test_show_team(self):
        """Test case for show_team

        Fetch a specific team  # noqa: E501
        """
        pass

    def test_update_team(self):
        """Test case for update_team

        Update a specific team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

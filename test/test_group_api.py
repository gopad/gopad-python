# coding: utf-8

"""
    Gopad OpenAPI

    API definition for Gopad, Etherpad for markdown with Go

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: gopad@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gopad.api.group_api import GroupApi


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GroupApi()

    def tearDown(self) -> None:
        pass

    def test_attach_group_to_user(self) -> None:
        """Test case for attach_group_to_user

        Attach a user to group
        """
        pass

    def test_create_group(self) -> None:
        """Test case for create_group

        Create a new group
        """
        pass

    def test_delete_group(self) -> None:
        """Test case for delete_group

        Delete a specific group
        """
        pass

    def test_delete_group_from_user(self) -> None:
        """Test case for delete_group_from_user

        Unlink a user from group
        """
        pass

    def test_list_group_users(self) -> None:
        """Test case for list_group_users

        Fetch all users attached to group
        """
        pass

    def test_list_groups(self) -> None:
        """Test case for list_groups

        Fetch all available groups
        """
        pass

    def test_permit_group_user(self) -> None:
        """Test case for permit_group_user

        Update user perms for group
        """
        pass

    def test_show_group(self) -> None:
        """Test case for show_group

        Fetch a specific group
        """
        pass

    def test_update_group(self) -> None:
        """Test case for update_group

        Update a specific group
        """
        pass


if __name__ == '__main__':
    unittest.main()

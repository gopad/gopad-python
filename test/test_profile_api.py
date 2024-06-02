# coding: utf-8

"""
    Gopad OpenAPI

    API definition for Gopad, Etherpad for markdown with go

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: gopad@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gopad.api.profile_api import ProfileApi


class TestProfileApi(unittest.TestCase):
    """ProfileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProfileApi()

    def tearDown(self) -> None:
        pass

    def test_show_profile(self) -> None:
        """Test case for show_profile

        Fetch profile details of the personal account
        """
        pass

    def test_token_profile(self) -> None:
        """Test case for token_profile

        Retrieve an unlimited auth token
        """
        pass

    def test_update_profile(self) -> None:
        """Test case for update_profile

        Update your own profile information
        """
        pass


if __name__ == '__main__':
    unittest.main()

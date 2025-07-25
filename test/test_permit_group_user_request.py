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

from gopad.models.permit_group_user_request import PermitGroupUserRequest

class TestPermitGroupUserRequest(unittest.TestCase):
    """PermitGroupUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermitGroupUserRequest:
        """Test PermitGroupUserRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermitGroupUserRequest`
        """
        model = PermitGroupUserRequest()
        if include_optional:
            return PermitGroupUserRequest(
                user = '',
                perm = ''
            )
        else:
            return PermitGroupUserRequest(
                user = '',
                perm = '',
        )
        """

    def testPermitGroupUserRequest(self):
        """Test PermitGroupUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from gopad.models.notification import Notification

class TestNotification(unittest.TestCase):
    """Notification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Notification:
        """Test Notification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Notification`
        """
        model = Notification()
        if include_optional:
            return Notification(
                status = 56,
                message = '',
                errors = [
                    gopad.models.validation.Validation(
                        field = '', 
                        message = '', )
                    ]
            )
        else:
            return Notification(
        )
        """

    def testNotification(self):
        """Test Notification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

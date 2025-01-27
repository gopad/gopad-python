# coding: utf-8

# flake8: noqa

"""
    Gopad OpenAPI

    API definition for Gopad, Etherpad for markdown with go

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: gopad@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.5.2"

# import apis into sdk package
from gopad.api.auth_api import AuthApi
from gopad.api.profile_api import ProfileApi
from gopad.api.team_api import TeamApi
from gopad.api.user_api import UserApi

# import ApiClient
from gopad.api_response import ApiResponse
from gopad.api_client import ApiClient
from gopad.configuration import Configuration
from gopad.exceptions import OpenApiException
from gopad.exceptions import ApiTypeError
from gopad.exceptions import ApiValueError
from gopad.exceptions import ApiKeyError
from gopad.exceptions import ApiAttributeError
from gopad.exceptions import ApiException

# import models into sdk package
from gopad.models.auth_login import AuthLogin
from gopad.models.auth_token import AuthToken
from gopad.models.auth_verify import AuthVerify
from gopad.models.notification import Notification
from gopad.models.profile import Profile
from gopad.models.team import Team
from gopad.models.team_user_params import TeamUserParams
from gopad.models.team_users import TeamUsers
from gopad.models.teams import Teams
from gopad.models.user import User
from gopad.models.user_auth import UserAuth
from gopad.models.user_team import UserTeam
from gopad.models.user_team_params import UserTeamParams
from gopad.models.user_teams import UserTeams
from gopad.models.users import Users
from gopad.models.validation import Validation

# coding: utf-8

"""
    Gopad OpenAPI

    API definition for Gopad  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gopad.api_client import ApiClient
from gopad.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TeamApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def append_team_to_user(self, team_id, team_user, **kwargs):  # noqa: E501
        """Assign a user to team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.append_team_to_user(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.append_team_to_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
        else:
            (data) = self.append_team_to_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
            return data

    def append_team_to_user_with_http_info(self, team_id, team_user, **kwargs):  # noqa: E501
        """Assign a user to team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.append_team_to_user_with_http_info(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'team_user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method append_team_to_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `append_team_to_user`")  # noqa: E501
        # verify the required parameter 'team_user' is set
        if ('team_user' not in local_var_params or
                local_var_params['team_user'] is None):
            raise ApiValueError("Missing the required parameter `team_user` when calling `append_team_to_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'team_user' in local_var_params:
            body_params = local_var_params['team_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_team(self, team, **kwargs):  # noqa: E501
        """Create a new team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_team(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Team team: The team data to create (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_team_with_http_info(team, **kwargs)  # noqa: E501
        else:
            (data) = self.create_team_with_http_info(team, **kwargs)  # noqa: E501
            return data

    def create_team_with_http_info(self, team, **kwargs):  # noqa: E501
        """Create a new team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_team_with_http_info(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Team team: The team data to create (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_team" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team' is set
        if ('team' not in local_var_params or
                local_var_params['team'] is None):
            raise ApiValueError("Missing the required parameter `team` when calling `create_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'team' in local_var_params:
            body_params = local_var_params['team']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Team',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_team(self, team_id, **kwargs):  # noqa: E501
        """Delete a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_team(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_team_with_http_info(team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_team_with_http_info(team_id, **kwargs)  # noqa: E501
            return data

    def delete_team_with_http_info(self, team_id, **kwargs):  # noqa: E501
        """Delete a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_team_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_team" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `delete_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delte_team_from_user(self, team_id, team_user, **kwargs):  # noqa: E501
        """Remove a user from team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delte_team_from_user(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to delete (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delte_team_from_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
        else:
            (data) = self.delte_team_from_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
            return data

    def delte_team_from_user_with_http_info(self, team_id, team_user, **kwargs):  # noqa: E501
        """Remove a user from team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delte_team_from_user_with_http_info(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to delete (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'team_user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delte_team_from_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `delte_team_from_user`")  # noqa: E501
        # verify the required parameter 'team_user' is set
        if ('team_user' not in local_var_params or
                local_var_params['team_user'] is None):
            raise ApiValueError("Missing the required parameter `team_user` when calling `delte_team_from_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'team_user' in local_var_params:
            body_params = local_var_params['team_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}/users', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_team_users(self, team_id, **kwargs):  # noqa: E501
        """Fetch all users assigned to team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_team_users(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: list[TeamUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_team_users_with_http_info(team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_team_users_with_http_info(team_id, **kwargs)  # noqa: E501
            return data

    def list_team_users_with_http_info(self, team_id, **kwargs):  # noqa: E501
        """Fetch all users assigned to team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_team_users_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: list[TeamUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_team_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `list_team_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamUser]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_teams(self, **kwargs):  # noqa: E501
        """Fetch all available teams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_teams_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch all available teams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_teams" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Team]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def permit_team_user(self, team_id, team_user, **kwargs):  # noqa: E501
        """Update user perms for team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permit_team_user(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to update (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.permit_team_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
        else:
            (data) = self.permit_team_user_with_http_info(team_id, team_user, **kwargs)  # noqa: E501
            return data

    def permit_team_user_with_http_info(self, team_id, team_user, **kwargs):  # noqa: E501
        """Update user perms for team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permit_team_user_with_http_info(team_id, team_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param TeamUserParams team_user: The team user data to update (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'team_user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permit_team_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `permit_team_user`")  # noqa: E501
        # verify the required parameter 'team_user' is set
        if ('team_user' not in local_var_params or
                local_var_params['team_user'] is None):
            raise ApiValueError("Missing the required parameter `team_user` when calling `permit_team_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'team_user' in local_var_params:
            body_params = local_var_params['team_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}/users', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_team(self, team_id, **kwargs):  # noqa: E501
        """Fetch a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_team(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_team_with_http_info(team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.show_team_with_http_info(team_id, **kwargs)  # noqa: E501
            return data

    def show_team_with_http_info(self, team_id, **kwargs):  # noqa: E501
        """Fetch a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_team_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_team" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `show_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Team',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_team(self, team_id, team, **kwargs):  # noqa: E501
        """Update a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_team(team_id, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param Team team: The team data to update (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_team_with_http_info(team_id, team, **kwargs)  # noqa: E501
        else:
            (data) = self.update_team_with_http_info(team_id, team, **kwargs)  # noqa: E501
            return data

    def update_team_with_http_info(self, team_id, team, **kwargs):  # noqa: E501
        """Update a specific team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_team_with_http_info(team_id, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: A team UUID or slug (required)
        :param Team team: The team data to update (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_team" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ApiValueError("Missing the required parameter `team_id` when calling `update_team`")  # noqa: E501
        # verify the required parameter 'team' is set
        if ('team' not in local_var_params or
                local_var_params['team'] is None):
            raise ApiValueError("Missing the required parameter `team` when calling `update_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['team_id'] = local_var_params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'team' in local_var_params:
            body_params = local_var_params['team']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Team',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

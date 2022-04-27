# Kleister: SDK for Python

[![General Workflow](https://github.com/gopad/gopad-python/actions/workflows/general.yml/badge.svg)](https://github.com/gopad/gopad-python/actions/workflows/general.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/0581d0652d4d4dddb3fc353f74cd9bed)](https://www.codacy.com/gh/gopad/gopad-python/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gopad/gopad-python&amp;utm_campaign=Badge_Grade) [![Join the Matrix chat at https://matrix.to/#/#gopad:matrix.org](https://img.shields.io/badge/matrix-%23gopad%3Amatrix.org-7bc9a4.svg)](https://matrix.to/#/#gopad:matrix.org) [![PyPI Version](https://badge.fury.io/py/gopad.svg)](https://badge.fury.io/py/gopad)

This repository provides a client SDK for Python. This SDK is automatically
generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

-   API version: 1.0.0-alpha1
-   Package version: 1.0.0-alpha1
-   Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements

Python >=3.6

## Installation

### Install with `pip`

If you want to install a published version, you just need to execute this
command to get the SDK installed via `pip`:

```console
pip install gopad
```

After the installation you can simply start to import the SDK:

```python
import gopad
```

### Install with `setuptools`

If you want to install a unpublished version you can simply clone this
repository and use `setuptools` to install the SDK:

```console
python setup.py install --user
```

After the installation you can simply start to import the SDK:

```python
import gopad
```

## Getting Started

Please follow the [installation](#installation) instructions and then run the
following code:

```python

import time
import gopad
from pprint import pprint
from gopad.api import auth_api
from gopad.model.auth_login import AuthLogin
from gopad.model.auth_token import AuthToken
from gopad.model.auth_verify import AuthVerify
from gopad.model.general_error import GeneralError

# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)



with gopad.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    auth_login = AuthLogin(
        username="username_example",
        password="password_example",
    ) # AuthLogin | The credentials to authenticate

    try:
        # Authenticate an user by credentials
        api_response = api_instance.login_user(auth_login)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling AuthApi->login_user: %s\n" % e)
```

## Documentation for endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**login_user**](docs/AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
*AuthApi* | [**refresh_auth**](docs/AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
*AuthApi* | [**verify_auth**](docs/AuthApi.md#verify_auth) | **GET** /auth/verify/{token} | Verify validity for an authentication token
*ProfileApi* | [**show_profile**](docs/ProfileApi.md#show_profile) | **GET** /profile/self | Retrieve an unlimited auth token
*ProfileApi* | [**token_profile**](docs/ProfileApi.md#token_profile) | **GET** /profile/token | Retrieve an unlimited auth token
*ProfileApi* | [**update_profile**](docs/ProfileApi.md#update_profile) | **PUT** /profile/self | Retrieve an unlimited auth token
*TeamApi* | [**append_team_to_user**](docs/TeamApi.md#append_team_to_user) | **POST** /teams/{team_id}/users | Assign a user to team
*TeamApi* | [**create_team**](docs/TeamApi.md#create_team) | **POST** /teams | Create a new team
*TeamApi* | [**delete_team**](docs/TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
*TeamApi* | [**delete_team_from_user**](docs/TeamApi.md#delete_team_from_user) | **DELETE** /teams/{team_id}/users | Remove a user from team
*TeamApi* | [**list_team_users**](docs/TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users assigned to team
*TeamApi* | [**list_teams**](docs/TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
*TeamApi* | [**permit_team_user**](docs/TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
*TeamApi* | [**show_team**](docs/TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
*TeamApi* | [**update_team**](docs/TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team
*UserApi* | [**append_user_to_team**](docs/UserApi.md#append_user_to_team) | **POST** /users/{user_id}/teams | Assign a team to user
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /users | Create a new user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
*UserApi* | [**delete_user_from_team**](docs/UserApi.md#delete_user_from_team) | **DELETE** /users/{user_id}/teams | Remove a team from user
*UserApi* | [**list_user_teams**](docs/UserApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all teams assigned to user
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /users | Fetch all available users
*UserApi* | [**permit_user_team**](docs/UserApi.md#permit_user_team) | **PUT** /users/{user_id}/teams | Update team perms for user
*UserApi* | [**show_user**](docs/UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user

## Documentation for models

-   [AuthLogin](docs/AuthLogin.md)
-   [AuthToken](docs/AuthToken.md)
-   [AuthVerify](docs/AuthVerify.md)
-   [GeneralError](docs/GeneralError.md)
-   [Profile](docs/Profile.md)
-   [Team](docs/Team.md)
-   [TeamUser](docs/TeamUser.md)
-   [TeamUserParams](docs/TeamUserParams.md)
-   [User](docs/User.md)
-   [UserTeamParams](docs/UserTeamParams.md)
-   [ValidationError](docs/ValidationError.md)
-   [ValidationErrorErrors](docs/ValidationErrorErrors.md)

## Documentation for authorization

### BasicAuth

-   **Type**: HTTP basic authentication

### HeaderAuth

-   **Type**: API key
-   **API key parameter name**: X-API-Key
-   **Location**: HTTP header

## Security

If you find a security issue please contact gopad@webhippie.de first.

## Contributing

Fork -> Patch -> Push -> Pull Request

## Authors

-   [Thomas Boerger](https://github.com/tboerger)

## License

Apache-2.0

## Copyright

```console
Copyright (c) 2018 Thomas Boerger <thomas@webhippie.de>
```


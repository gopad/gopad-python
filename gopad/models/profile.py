# coding: utf-8

"""
    Gopad OpenAPI

    API definition for Gopad, Etherpad for markdown with go

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: gopad@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, SecretStr, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gopad.models.user_auth import UserAuth
from gopad.models.user_group import UserGroup
from typing import Optional, Set
from typing_extensions import Self

class Profile(BaseModel):
    """
    Model to represent profile
    """ # noqa: E501
    id: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    password: Optional[SecretStr] = None
    email: Optional[StrictStr] = None
    fullname: Optional[StrictStr] = None
    profile: Optional[StrictStr] = None
    admin: Optional[StrictBool] = None
    active: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    auths: Optional[List[UserAuth]] = None
    groups: Optional[List[UserGroup]] = None
    __properties: ClassVar[List[str]] = ["id", "username", "password", "email", "fullname", "profile", "admin", "active", "created_at", "updated_at", "auths", "groups"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Profile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "admin",
            "active",
            "created_at",
            "updated_at",
            "auths",
            "groups",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in auths (list)
        _items = []
        if self.auths:
            for _item_auths in self.auths:
                if _item_auths:
                    _items.append(_item_auths.to_dict())
            _dict['auths'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if fullname (nullable) is None
        # and model_fields_set contains the field
        if self.fullname is None and "fullname" in self.model_fields_set:
            _dict['fullname'] = None

        # set to None if profile (nullable) is None
        # and model_fields_set contains the field
        if self.profile is None and "profile" in self.model_fields_set:
            _dict['profile'] = None

        # set to None if auths (nullable) is None
        # and model_fields_set contains the field
        if self.auths is None and "auths" in self.model_fields_set:
            _dict['auths'] = None

        # set to None if groups (nullable) is None
        # and model_fields_set contains the field
        if self.groups is None and "groups" in self.model_fields_set:
            _dict['groups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Profile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "email": obj.get("email"),
            "fullname": obj.get("fullname"),
            "profile": obj.get("profile"),
            "admin": obj.get("admin"),
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "auths": [UserAuth.from_dict(_item) for _item in obj["auths"]] if obj.get("auths") is not None else None,
            "groups": [UserGroup.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None
        })
        return _obj



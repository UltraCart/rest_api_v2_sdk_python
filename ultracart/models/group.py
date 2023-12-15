# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Group(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_oid': 'int',
        'name': 'str',
        'notifications': 'list[Notification]',
        'permissions': 'list[Permission]',
        'users': 'list[GroupUserMembership]'
    }

    attribute_map = {
        'group_oid': 'group_oid',
        'name': 'name',
        'notifications': 'notifications',
        'permissions': 'permissions',
        'users': 'users'
    }

    def __init__(self, group_oid=None, name=None, notifications=None, permissions=None, users=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._group_oid = None
        self._name = None
        self._notifications = None
        self._permissions = None
        self._users = None
        self.discriminator = None

        if group_oid is not None:
            self.group_oid = group_oid
        if name is not None:
            self.name = name
        if notifications is not None:
            self.notifications = notifications
        if permissions is not None:
            self.permissions = permissions
        if users is not None:
            self.users = users

    @property
    def group_oid(self):
        """Gets the group_oid of this Group.  # noqa: E501

        The unique object identifier (oid for short) for this group  # noqa: E501

        :return: The group_oid of this Group.  # noqa: E501
        :rtype: int
        """
        return self._group_oid

    @group_oid.setter
    def group_oid(self, group_oid):
        """Sets the group_oid of this Group.

        The unique object identifier (oid for short) for this group  # noqa: E501

        :param group_oid: The group_oid of this Group.  # noqa: E501
        :type: int
        """

        self._group_oid = group_oid

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        The name of this group.  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        The name of this group.  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notifications(self):
        """Gets the notifications of this Group.  # noqa: E501

        A list of notifications the user receives.  # noqa: E501

        :return: The notifications of this Group.  # noqa: E501
        :rtype: list[Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Group.

        A list of notifications the user receives.  # noqa: E501

        :param notifications: The notifications of this Group.  # noqa: E501
        :type: list[Notification]
        """

        self._notifications = notifications

    @property
    def permissions(self):
        """Gets the permissions of this Group.  # noqa: E501

        A list of permissions the user enjoys for accessing the backend of UltraCart.  # noqa: E501

        :return: The permissions of this Group.  # noqa: E501
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Group.

        A list of permissions the user enjoys for accessing the backend of UltraCart.  # noqa: E501

        :param permissions: The permissions of this Group.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions

    @property
    def users(self):
        """Gets the users of this Group.  # noqa: E501

        A list of users that belong to this group.  # noqa: E501

        :return: The users of this Group.  # noqa: E501
        :rtype: list[GroupUserMembership]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Group.

        A list of users that belong to this group.  # noqa: E501

        :param users: The users of this Group.  # noqa: E501
        :type: list[GroupUserMembership]
        """

        self._users = users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Group, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

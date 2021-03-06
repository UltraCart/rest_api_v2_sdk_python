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


class GroupUserMembership(object):
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
        'email': 'str',
        'full_name': 'str',
        'login': 'str',
        'member': 'bool',
        'user_id': 'int'
    }

    attribute_map = {
        'email': 'email',
        'full_name': 'fullName',
        'login': 'login',
        'member': 'member',
        'user_id': 'user_id'
    }

    def __init__(self, email=None, full_name=None, login=None, member=None, user_id=None):  # noqa: E501
        """GroupUserMembership - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._full_name = None
        self._login = None
        self._member = None
        self._user_id = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if login is not None:
            self.login = login
        if member is not None:
            self.member = member
        if user_id is not None:
            self.user_id = user_id

    @property
    def email(self):
        """Gets the email of this GroupUserMembership.  # noqa: E501

        The email for this user.  # noqa: E501

        :return: The email of this GroupUserMembership.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GroupUserMembership.

        The email for this user.  # noqa: E501

        :param email: The email of this GroupUserMembership.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this GroupUserMembership.  # noqa: E501

        The full name for this user.  # noqa: E501

        :return: The full_name of this GroupUserMembership.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GroupUserMembership.

        The full name for this user.  # noqa: E501

        :param full_name: The full_name of this GroupUserMembership.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def login(self):
        """Gets the login of this GroupUserMembership.  # noqa: E501

        The login for this user.  # noqa: E501

        :return: The login of this GroupUserMembership.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this GroupUserMembership.

        The login for this user.  # noqa: E501

        :param login: The login of this GroupUserMembership.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def member(self):
        """Gets the member of this GroupUserMembership.  # noqa: E501

        True if this user belongs to the parent group, false otherwise.  # noqa: E501

        :return: The member of this GroupUserMembership.  # noqa: E501
        :rtype: bool
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this GroupUserMembership.

        True if this user belongs to the parent group, false otherwise.  # noqa: E501

        :param member: The member of this GroupUserMembership.  # noqa: E501
        :type: bool
        """

        self._member = member

    @property
    def user_id(self):
        """Gets the user_id of this GroupUserMembership.  # noqa: E501

        The user id for this user.  # noqa: E501

        :return: The user_id of this GroupUserMembership.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupUserMembership.

        The user id for this user.  # noqa: E501

        :param user_id: The user_id of this GroupUserMembership.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(GroupUserMembership, dict):
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
        if not isinstance(other, GroupUserMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

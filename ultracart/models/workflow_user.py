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


class WorkflowUser(object):
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
        'user': 'str',
        'user_icon_url': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'user': 'user',
        'user_icon_url': 'user_icon_url',
        'user_id': 'user_id'
    }

    def __init__(self, user=None, user_icon_url=None, user_id=None):  # noqa: E501
        """WorkflowUser - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._user_icon_url = None
        self._user_id = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if user_icon_url is not None:
            self.user_icon_url = user_icon_url
        if user_id is not None:
            self.user_id = user_id

    @property
    def user(self):
        """Gets the user of this WorkflowUser.  # noqa: E501

        The user  # noqa: E501

        :return: The user of this WorkflowUser.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkflowUser.

        The user  # noqa: E501

        :param user: The user of this WorkflowUser.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def user_icon_url(self):
        """Gets the user_icon_url of this WorkflowUser.  # noqa: E501

        The user icon URL if available  # noqa: E501

        :return: The user_icon_url of this WorkflowUser.  # noqa: E501
        :rtype: str
        """
        return self._user_icon_url

    @user_icon_url.setter
    def user_icon_url(self, user_icon_url):
        """Sets the user_icon_url of this WorkflowUser.

        The user icon URL if available  # noqa: E501

        :param user_icon_url: The user_icon_url of this WorkflowUser.  # noqa: E501
        :type: str
        """

        self._user_icon_url = user_icon_url

    @property
    def user_id(self):
        """Gets the user_id of this WorkflowUser.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this WorkflowUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WorkflowUser.

        User ID  # noqa: E501

        :param user_id: The user_id of this WorkflowUser.  # noqa: E501
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
        if issubclass(WorkflowUser, dict):
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
        if not isinstance(other, WorkflowUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

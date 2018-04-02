# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Error(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'developer_message': 'str',
        'error_code': 'str',
        'more_info': 'str',
        'user_message': 'str'
    }

    attribute_map = {
        'developer_message': 'developer_message',
        'error_code': 'error_code',
        'more_info': 'more_info',
        'user_message': 'user_message'
    }

    def __init__(self, developer_message=None, error_code=None, more_info=None, user_message=None):
        """
        Error - a model defined in Swagger
        """

        self._developer_message = None
        self._error_code = None
        self._more_info = None
        self._user_message = None
        self.discriminator = None

        if developer_message is not None:
          self.developer_message = developer_message
        if error_code is not None:
          self.error_code = error_code
        if more_info is not None:
          self.more_info = more_info
        if user_message is not None:
          self.user_message = user_message

    @property
    def developer_message(self):
        """
        Gets the developer_message of this Error.
        A technical message meant to be read by a developer

        :return: The developer_message of this Error.
        :rtype: str
        """
        return self._developer_message

    @developer_message.setter
    def developer_message(self, developer_message):
        """
        Sets the developer_message of this Error.
        A technical message meant to be read by a developer

        :param developer_message: The developer_message of this Error.
        :type: str
        """

        self._developer_message = developer_message

    @property
    def error_code(self):
        """
        Gets the error_code of this Error.
        HTTP status code

        :return: The error_code of this Error.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this Error.
        HTTP status code

        :param error_code: The error_code of this Error.
        :type: str
        """

        self._error_code = error_code

    @property
    def more_info(self):
        """
        Gets the more_info of this Error.
        Additional information often a link to additional documentation

        :return: The more_info of this Error.
        :rtype: str
        """
        return self._more_info

    @more_info.setter
    def more_info(self, more_info):
        """
        Sets the more_info of this Error.
        Additional information often a link to additional documentation

        :param more_info: The more_info of this Error.
        :type: str
        """

        self._more_info = more_info

    @property
    def user_message(self):
        """
        Gets the user_message of this Error.
        An end-user friendly message suitable for display to the customer

        :return: The user_message of this Error.
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """
        Sets the user_message of this Error.
        An end-user friendly message suitable for display to the customer

        :param user_message: The user_message of this Error.
        :type: str
        """

        self._user_message = user_message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

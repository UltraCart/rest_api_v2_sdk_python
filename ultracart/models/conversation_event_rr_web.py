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


class ConversationEventRRWeb(object):
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
        'data': 'str',
        'data_part': 'int',
        'data_sha256': 'str',
        'data_total_parts': 'int',
        'data_total_sha256': 'str',
        'event_index': 'int',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'data_part': 'data_part',
        'data_sha256': 'data_sha256',
        'data_total_parts': 'data_total_parts',
        'data_total_sha256': 'data_total_sha256',
        'event_index': 'event_index',
        'type': 'type'
    }

    def __init__(self, data=None, data_part=None, data_sha256=None, data_total_parts=None, data_total_sha256=None, event_index=None, type=None):  # noqa: E501
        """ConversationEventRRWeb - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._data_part = None
        self._data_sha256 = None
        self._data_total_parts = None
        self._data_total_sha256 = None
        self._event_index = None
        self._type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if data_part is not None:
            self.data_part = data_part
        if data_sha256 is not None:
            self.data_sha256 = data_sha256
        if data_total_parts is not None:
            self.data_total_parts = data_total_parts
        if data_total_sha256 is not None:
            self.data_total_sha256 = data_total_sha256
        if event_index is not None:
            self.event_index = event_index
        if type is not None:
            self.type = type

    @property
    def data(self):
        """Gets the data of this ConversationEventRRWeb.  # noqa: E501


        :return: The data of this ConversationEventRRWeb.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConversationEventRRWeb.


        :param data: The data of this ConversationEventRRWeb.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def data_part(self):
        """Gets the data_part of this ConversationEventRRWeb.  # noqa: E501


        :return: The data_part of this ConversationEventRRWeb.  # noqa: E501
        :rtype: int
        """
        return self._data_part

    @data_part.setter
    def data_part(self, data_part):
        """Sets the data_part of this ConversationEventRRWeb.


        :param data_part: The data_part of this ConversationEventRRWeb.  # noqa: E501
        :type: int
        """

        self._data_part = data_part

    @property
    def data_sha256(self):
        """Gets the data_sha256 of this ConversationEventRRWeb.  # noqa: E501


        :return: The data_sha256 of this ConversationEventRRWeb.  # noqa: E501
        :rtype: str
        """
        return self._data_sha256

    @data_sha256.setter
    def data_sha256(self, data_sha256):
        """Sets the data_sha256 of this ConversationEventRRWeb.


        :param data_sha256: The data_sha256 of this ConversationEventRRWeb.  # noqa: E501
        :type: str
        """

        self._data_sha256 = data_sha256

    @property
    def data_total_parts(self):
        """Gets the data_total_parts of this ConversationEventRRWeb.  # noqa: E501


        :return: The data_total_parts of this ConversationEventRRWeb.  # noqa: E501
        :rtype: int
        """
        return self._data_total_parts

    @data_total_parts.setter
    def data_total_parts(self, data_total_parts):
        """Sets the data_total_parts of this ConversationEventRRWeb.


        :param data_total_parts: The data_total_parts of this ConversationEventRRWeb.  # noqa: E501
        :type: int
        """

        self._data_total_parts = data_total_parts

    @property
    def data_total_sha256(self):
        """Gets the data_total_sha256 of this ConversationEventRRWeb.  # noqa: E501


        :return: The data_total_sha256 of this ConversationEventRRWeb.  # noqa: E501
        :rtype: str
        """
        return self._data_total_sha256

    @data_total_sha256.setter
    def data_total_sha256(self, data_total_sha256):
        """Sets the data_total_sha256 of this ConversationEventRRWeb.


        :param data_total_sha256: The data_total_sha256 of this ConversationEventRRWeb.  # noqa: E501
        :type: str
        """

        self._data_total_sha256 = data_total_sha256

    @property
    def event_index(self):
        """Gets the event_index of this ConversationEventRRWeb.  # noqa: E501


        :return: The event_index of this ConversationEventRRWeb.  # noqa: E501
        :rtype: int
        """
        return self._event_index

    @event_index.setter
    def event_index(self, event_index):
        """Sets the event_index of this ConversationEventRRWeb.


        :param event_index: The event_index of this ConversationEventRRWeb.  # noqa: E501
        :type: int
        """

        self._event_index = event_index

    @property
    def type(self):
        """Gets the type of this ConversationEventRRWeb.  # noqa: E501

        Type of event  # noqa: E501

        :return: The type of this ConversationEventRRWeb.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationEventRRWeb.

        Type of event  # noqa: E501

        :param type: The type of this ConversationEventRRWeb.  # noqa: E501
        :type: str
        """
        allowed_values = ["init", "events"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ConversationEventRRWeb, dict):
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
        if not isinstance(other, ConversationEventRRWeb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
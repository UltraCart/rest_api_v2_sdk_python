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


class ConversationLocationCountry(object):
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
        'iso2': 'str',
        'name': 'str',
        'state_provinces': 'list[ConversationLocationStateProvince]'
    }

    attribute_map = {
        'iso2': 'iso2',
        'name': 'name',
        'state_provinces': 'state_provinces'
    }

    def __init__(self, iso2=None, name=None, state_provinces=None):  # noqa: E501
        """ConversationLocationCountry - a model defined in Swagger"""  # noqa: E501

        self._iso2 = None
        self._name = None
        self._state_provinces = None
        self.discriminator = None

        if iso2 is not None:
            self.iso2 = iso2
        if name is not None:
            self.name = name
        if state_provinces is not None:
            self.state_provinces = state_provinces

    @property
    def iso2(self):
        """Gets the iso2 of this ConversationLocationCountry.  # noqa: E501


        :return: The iso2 of this ConversationLocationCountry.  # noqa: E501
        :rtype: str
        """
        return self._iso2

    @iso2.setter
    def iso2(self, iso2):
        """Sets the iso2 of this ConversationLocationCountry.


        :param iso2: The iso2 of this ConversationLocationCountry.  # noqa: E501
        :type: str
        """

        self._iso2 = iso2

    @property
    def name(self):
        """Gets the name of this ConversationLocationCountry.  # noqa: E501


        :return: The name of this ConversationLocationCountry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConversationLocationCountry.


        :param name: The name of this ConversationLocationCountry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state_provinces(self):
        """Gets the state_provinces of this ConversationLocationCountry.  # noqa: E501


        :return: The state_provinces of this ConversationLocationCountry.  # noqa: E501
        :rtype: list[ConversationLocationStateProvince]
        """
        return self._state_provinces

    @state_provinces.setter
    def state_provinces(self, state_provinces):
        """Sets the state_provinces of this ConversationLocationCountry.


        :param state_provinces: The state_provinces of this ConversationLocationCountry.  # noqa: E501
        :type: list[ConversationLocationStateProvince]
        """

        self._state_provinces = state_provinces

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
        if issubclass(ConversationLocationCountry, dict):
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
        if not isinstance(other, ConversationLocationCountry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class ConversationPbxTimeBasedMappingConfig(object):
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
        'default_mapping': 'ConversationPbxTimeBasedMapping',
        'mappings': 'list[ConversationPbxTimeBasedMapping]'
    }

    attribute_map = {
        'default_mapping': 'default_mapping',
        'mappings': 'mappings'
    }

    def __init__(self, default_mapping=None, mappings=None):  # noqa: E501
        """ConversationPbxTimeBasedMappingConfig - a model defined in Swagger"""  # noqa: E501

        self._default_mapping = None
        self._mappings = None
        self.discriminator = None

        if default_mapping is not None:
            self.default_mapping = default_mapping
        if mappings is not None:
            self.mappings = mappings

    @property
    def default_mapping(self):
        """Gets the default_mapping of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501


        :return: The default_mapping of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501
        :rtype: ConversationPbxTimeBasedMapping
        """
        return self._default_mapping

    @default_mapping.setter
    def default_mapping(self, default_mapping):
        """Sets the default_mapping of this ConversationPbxTimeBasedMappingConfig.


        :param default_mapping: The default_mapping of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501
        :type: ConversationPbxTimeBasedMapping
        """

        self._default_mapping = default_mapping

    @property
    def mappings(self):
        """Gets the mappings of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501

        Mappings  # noqa: E501

        :return: The mappings of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501
        :rtype: list[ConversationPbxTimeBasedMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this ConversationPbxTimeBasedMappingConfig.

        Mappings  # noqa: E501

        :param mappings: The mappings of this ConversationPbxTimeBasedMappingConfig.  # noqa: E501
        :type: list[ConversationPbxTimeBasedMapping]
        """

        self._mappings = mappings

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
        if issubclass(ConversationPbxTimeBasedMappingConfig, dict):
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
        if not isinstance(other, ConversationPbxTimeBasedMappingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
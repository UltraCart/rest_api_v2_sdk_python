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


class ConversationPbxMenuMapping(object):
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
        'action': 'str',
        'action_target': 'str',
        'digits': 'int',
        'speech': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_target': 'action_target',
        'digits': 'digits',
        'speech': 'speech'
    }

    def __init__(self, action=None, action_target=None, digits=None, speech=None):  # noqa: E501
        """ConversationPbxMenuMapping - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._action_target = None
        self._digits = None
        self._speech = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_target is not None:
            self.action_target = action_target
        if digits is not None:
            self.digits = digits
        if speech is not None:
            self.speech = speech

    @property
    def action(self):
        """Gets the action of this ConversationPbxMenuMapping.  # noqa: E501

        Action  # noqa: E501

        :return: The action of this ConversationPbxMenuMapping.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ConversationPbxMenuMapping.

        Action  # noqa: E501

        :param action: The action of this ConversationPbxMenuMapping.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def action_target(self):
        """Gets the action_target of this ConversationPbxMenuMapping.  # noqa: E501

        Action target  # noqa: E501

        :return: The action_target of this ConversationPbxMenuMapping.  # noqa: E501
        :rtype: str
        """
        return self._action_target

    @action_target.setter
    def action_target(self, action_target):
        """Sets the action_target of this ConversationPbxMenuMapping.

        Action target  # noqa: E501

        :param action_target: The action_target of this ConversationPbxMenuMapping.  # noqa: E501
        :type: str
        """

        self._action_target = action_target

    @property
    def digits(self):
        """Gets the digits of this ConversationPbxMenuMapping.  # noqa: E501

        Digits  # noqa: E501

        :return: The digits of this ConversationPbxMenuMapping.  # noqa: E501
        :rtype: int
        """
        return self._digits

    @digits.setter
    def digits(self, digits):
        """Sets the digits of this ConversationPbxMenuMapping.

        Digits  # noqa: E501

        :param digits: The digits of this ConversationPbxMenuMapping.  # noqa: E501
        :type: int
        """

        self._digits = digits

    @property
    def speech(self):
        """Gets the speech of this ConversationPbxMenuMapping.  # noqa: E501

        Speech  # noqa: E501

        :return: The speech of this ConversationPbxMenuMapping.  # noqa: E501
        :rtype: str
        """
        return self._speech

    @speech.setter
    def speech(self, speech):
        """Sets the speech of this ConversationPbxMenuMapping.

        Speech  # noqa: E501

        :param speech: The speech of this ConversationPbxMenuMapping.  # noqa: E501
        :type: str
        """

        self._speech = speech

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
        if issubclass(ConversationPbxMenuMapping, dict):
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
        if not isinstance(other, ConversationPbxMenuMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

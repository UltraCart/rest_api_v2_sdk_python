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


class ConversationStartRequest(object):
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
        'add_conversation_participant_arns': 'list[str]',
        'conversation_arn': 'str',
        'conversation_webchat_queue_uuid': 'str'
    }

    attribute_map = {
        'add_conversation_participant_arns': 'add_conversation_participant_arns',
        'conversation_arn': 'conversation_arn',
        'conversation_webchat_queue_uuid': 'conversation_webchat_queue_uuid'
    }

    def __init__(self, add_conversation_participant_arns=None, conversation_arn=None, conversation_webchat_queue_uuid=None):  # noqa: E501
        """ConversationStartRequest - a model defined in Swagger"""  # noqa: E501

        self._add_conversation_participant_arns = None
        self._conversation_arn = None
        self._conversation_webchat_queue_uuid = None
        self.discriminator = None

        if add_conversation_participant_arns is not None:
            self.add_conversation_participant_arns = add_conversation_participant_arns
        if conversation_arn is not None:
            self.conversation_arn = conversation_arn
        if conversation_webchat_queue_uuid is not None:
            self.conversation_webchat_queue_uuid = conversation_webchat_queue_uuid

    @property
    def add_conversation_participant_arns(self):
        """Gets the add_conversation_participant_arns of this ConversationStartRequest.  # noqa: E501


        :return: The add_conversation_participant_arns of this ConversationStartRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_conversation_participant_arns

    @add_conversation_participant_arns.setter
    def add_conversation_participant_arns(self, add_conversation_participant_arns):
        """Sets the add_conversation_participant_arns of this ConversationStartRequest.


        :param add_conversation_participant_arns: The add_conversation_participant_arns of this ConversationStartRequest.  # noqa: E501
        :type: list[str]
        """

        self._add_conversation_participant_arns = add_conversation_participant_arns

    @property
    def conversation_arn(self):
        """Gets the conversation_arn of this ConversationStartRequest.  # noqa: E501


        :return: The conversation_arn of this ConversationStartRequest.  # noqa: E501
        :rtype: str
        """
        return self._conversation_arn

    @conversation_arn.setter
    def conversation_arn(self, conversation_arn):
        """Sets the conversation_arn of this ConversationStartRequest.


        :param conversation_arn: The conversation_arn of this ConversationStartRequest.  # noqa: E501
        :type: str
        """

        self._conversation_arn = conversation_arn

    @property
    def conversation_webchat_queue_uuid(self):
        """Gets the conversation_webchat_queue_uuid of this ConversationStartRequest.  # noqa: E501


        :return: The conversation_webchat_queue_uuid of this ConversationStartRequest.  # noqa: E501
        :rtype: str
        """
        return self._conversation_webchat_queue_uuid

    @conversation_webchat_queue_uuid.setter
    def conversation_webchat_queue_uuid(self, conversation_webchat_queue_uuid):
        """Sets the conversation_webchat_queue_uuid of this ConversationStartRequest.


        :param conversation_webchat_queue_uuid: The conversation_webchat_queue_uuid of this ConversationStartRequest.  # noqa: E501
        :type: str
        """

        self._conversation_webchat_queue_uuid = conversation_webchat_queue_uuid

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
        if issubclass(ConversationStartRequest, dict):
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
        if not isinstance(other, ConversationStartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

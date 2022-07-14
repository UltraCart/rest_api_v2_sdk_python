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


class ConversationParticipant(object):
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
        'conversation_participant_arn': 'str',
        'conversation_participant_name': 'str',
        'conversation_participant_uuid': 'str',
        'joined_dts': 'str',
        'last_message_dts': 'str',
        'left_dts': 'str',
        'status': 'str'
    }

    attribute_map = {
        'conversation_participant_arn': 'conversation_participant_arn',
        'conversation_participant_name': 'conversation_participant_name',
        'conversation_participant_uuid': 'conversation_participant_uuid',
        'joined_dts': 'joined_dts',
        'last_message_dts': 'last_message_dts',
        'left_dts': 'left_dts',
        'status': 'status'
    }

    def __init__(self, conversation_participant_arn=None, conversation_participant_name=None, conversation_participant_uuid=None, joined_dts=None, last_message_dts=None, left_dts=None, status=None):  # noqa: E501
        """ConversationParticipant - a model defined in Swagger"""  # noqa: E501

        self._conversation_participant_arn = None
        self._conversation_participant_name = None
        self._conversation_participant_uuid = None
        self._joined_dts = None
        self._last_message_dts = None
        self._left_dts = None
        self._status = None
        self.discriminator = None

        if conversation_participant_arn is not None:
            self.conversation_participant_arn = conversation_participant_arn
        if conversation_participant_name is not None:
            self.conversation_participant_name = conversation_participant_name
        if conversation_participant_uuid is not None:
            self.conversation_participant_uuid = conversation_participant_uuid
        if joined_dts is not None:
            self.joined_dts = joined_dts
        if last_message_dts is not None:
            self.last_message_dts = last_message_dts
        if left_dts is not None:
            self.left_dts = left_dts
        if status is not None:
            self.status = status

    @property
    def conversation_participant_arn(self):
        """Gets the conversation_participant_arn of this ConversationParticipant.  # noqa: E501


        :return: The conversation_participant_arn of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._conversation_participant_arn

    @conversation_participant_arn.setter
    def conversation_participant_arn(self, conversation_participant_arn):
        """Sets the conversation_participant_arn of this ConversationParticipant.


        :param conversation_participant_arn: The conversation_participant_arn of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._conversation_participant_arn = conversation_participant_arn

    @property
    def conversation_participant_name(self):
        """Gets the conversation_participant_name of this ConversationParticipant.  # noqa: E501


        :return: The conversation_participant_name of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._conversation_participant_name

    @conversation_participant_name.setter
    def conversation_participant_name(self, conversation_participant_name):
        """Sets the conversation_participant_name of this ConversationParticipant.


        :param conversation_participant_name: The conversation_participant_name of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._conversation_participant_name = conversation_participant_name

    @property
    def conversation_participant_uuid(self):
        """Gets the conversation_participant_uuid of this ConversationParticipant.  # noqa: E501


        :return: The conversation_participant_uuid of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._conversation_participant_uuid

    @conversation_participant_uuid.setter
    def conversation_participant_uuid(self, conversation_participant_uuid):
        """Sets the conversation_participant_uuid of this ConversationParticipant.


        :param conversation_participant_uuid: The conversation_participant_uuid of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._conversation_participant_uuid = conversation_participant_uuid

    @property
    def joined_dts(self):
        """Gets the joined_dts of this ConversationParticipant.  # noqa: E501

        Joined conversation date/time  # noqa: E501

        :return: The joined_dts of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._joined_dts

    @joined_dts.setter
    def joined_dts(self, joined_dts):
        """Sets the joined_dts of this ConversationParticipant.

        Joined conversation date/time  # noqa: E501

        :param joined_dts: The joined_dts of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._joined_dts = joined_dts

    @property
    def last_message_dts(self):
        """Gets the last_message_dts of this ConversationParticipant.  # noqa: E501

        Last message date/time  # noqa: E501

        :return: The last_message_dts of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._last_message_dts

    @last_message_dts.setter
    def last_message_dts(self, last_message_dts):
        """Sets the last_message_dts of this ConversationParticipant.

        Last message date/time  # noqa: E501

        :param last_message_dts: The last_message_dts of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._last_message_dts = last_message_dts

    @property
    def left_dts(self):
        """Gets the left_dts of this ConversationParticipant.  # noqa: E501

        Left conversation date/time  # noqa: E501

        :return: The left_dts of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._left_dts

    @left_dts.setter
    def left_dts(self, left_dts):
        """Sets the left_dts of this ConversationParticipant.

        Left conversation date/time  # noqa: E501

        :param left_dts: The left_dts of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._left_dts = left_dts

    @property
    def status(self):
        """Gets the status of this ConversationParticipant.  # noqa: E501


        :return: The status of this ConversationParticipant.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConversationParticipant.


        :param status: The status of this ConversationParticipant.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ConversationParticipant, dict):
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
        if not isinstance(other, ConversationParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

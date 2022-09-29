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


class ConversationSummary(object):
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
        'closed': 'bool',
        'conversation_arn': 'str',
        'conversation_uuid': 'str',
        'last_conversation_message_body': 'str',
        'last_conversation_participant_arn': 'str',
        'last_conversation_participant_name': 'str',
        'last_message_dts': 'str',
        'medium': 'str',
        'merchant_id': 'str',
        'message_count': 'int',
        'participants': 'list[ConversationParticipant]',
        'start_dts': 'str',
        'unread_messages': 'bool',
        'visible': 'bool'
    }

    attribute_map = {
        'closed': 'closed',
        'conversation_arn': 'conversation_arn',
        'conversation_uuid': 'conversation_uuid',
        'last_conversation_message_body': 'last_conversation_message_body',
        'last_conversation_participant_arn': 'last_conversation_participant_arn',
        'last_conversation_participant_name': 'last_conversation_participant_name',
        'last_message_dts': 'last_message_dts',
        'medium': 'medium',
        'merchant_id': 'merchant_id',
        'message_count': 'message_count',
        'participants': 'participants',
        'start_dts': 'start_dts',
        'unread_messages': 'unread_messages',
        'visible': 'visible'
    }

    def __init__(self, closed=None, conversation_arn=None, conversation_uuid=None, last_conversation_message_body=None, last_conversation_participant_arn=None, last_conversation_participant_name=None, last_message_dts=None, medium=None, merchant_id=None, message_count=None, participants=None, start_dts=None, unread_messages=None, visible=None):  # noqa: E501
        """ConversationSummary - a model defined in Swagger"""  # noqa: E501

        self._closed = None
        self._conversation_arn = None
        self._conversation_uuid = None
        self._last_conversation_message_body = None
        self._last_conversation_participant_arn = None
        self._last_conversation_participant_name = None
        self._last_message_dts = None
        self._medium = None
        self._merchant_id = None
        self._message_count = None
        self._participants = None
        self._start_dts = None
        self._unread_messages = None
        self._visible = None
        self.discriminator = None

        if closed is not None:
            self.closed = closed
        if conversation_arn is not None:
            self.conversation_arn = conversation_arn
        if conversation_uuid is not None:
            self.conversation_uuid = conversation_uuid
        if last_conversation_message_body is not None:
            self.last_conversation_message_body = last_conversation_message_body
        if last_conversation_participant_arn is not None:
            self.last_conversation_participant_arn = last_conversation_participant_arn
        if last_conversation_participant_name is not None:
            self.last_conversation_participant_name = last_conversation_participant_name
        if last_message_dts is not None:
            self.last_message_dts = last_message_dts
        if medium is not None:
            self.medium = medium
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if message_count is not None:
            self.message_count = message_count
        if participants is not None:
            self.participants = participants
        if start_dts is not None:
            self.start_dts = start_dts
        if unread_messages is not None:
            self.unread_messages = unread_messages
        if visible is not None:
            self.visible = visible

    @property
    def closed(self):
        """Gets the closed of this ConversationSummary.  # noqa: E501


        :return: The closed of this ConversationSummary.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this ConversationSummary.


        :param closed: The closed of this ConversationSummary.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def conversation_arn(self):
        """Gets the conversation_arn of this ConversationSummary.  # noqa: E501


        :return: The conversation_arn of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._conversation_arn

    @conversation_arn.setter
    def conversation_arn(self, conversation_arn):
        """Sets the conversation_arn of this ConversationSummary.


        :param conversation_arn: The conversation_arn of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._conversation_arn = conversation_arn

    @property
    def conversation_uuid(self):
        """Gets the conversation_uuid of this ConversationSummary.  # noqa: E501


        :return: The conversation_uuid of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._conversation_uuid

    @conversation_uuid.setter
    def conversation_uuid(self, conversation_uuid):
        """Sets the conversation_uuid of this ConversationSummary.


        :param conversation_uuid: The conversation_uuid of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._conversation_uuid = conversation_uuid

    @property
    def last_conversation_message_body(self):
        """Gets the last_conversation_message_body of this ConversationSummary.  # noqa: E501


        :return: The last_conversation_message_body of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_conversation_message_body

    @last_conversation_message_body.setter
    def last_conversation_message_body(self, last_conversation_message_body):
        """Sets the last_conversation_message_body of this ConversationSummary.


        :param last_conversation_message_body: The last_conversation_message_body of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._last_conversation_message_body = last_conversation_message_body

    @property
    def last_conversation_participant_arn(self):
        """Gets the last_conversation_participant_arn of this ConversationSummary.  # noqa: E501


        :return: The last_conversation_participant_arn of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_conversation_participant_arn

    @last_conversation_participant_arn.setter
    def last_conversation_participant_arn(self, last_conversation_participant_arn):
        """Sets the last_conversation_participant_arn of this ConversationSummary.


        :param last_conversation_participant_arn: The last_conversation_participant_arn of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._last_conversation_participant_arn = last_conversation_participant_arn

    @property
    def last_conversation_participant_name(self):
        """Gets the last_conversation_participant_name of this ConversationSummary.  # noqa: E501


        :return: The last_conversation_participant_name of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_conversation_participant_name

    @last_conversation_participant_name.setter
    def last_conversation_participant_name(self, last_conversation_participant_name):
        """Sets the last_conversation_participant_name of this ConversationSummary.


        :param last_conversation_participant_name: The last_conversation_participant_name of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._last_conversation_participant_name = last_conversation_participant_name

    @property
    def last_message_dts(self):
        """Gets the last_message_dts of this ConversationSummary.  # noqa: E501

        Last message date/time  # noqa: E501

        :return: The last_message_dts of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_message_dts

    @last_message_dts.setter
    def last_message_dts(self, last_message_dts):
        """Sets the last_message_dts of this ConversationSummary.

        Last message date/time  # noqa: E501

        :param last_message_dts: The last_message_dts of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._last_message_dts = last_message_dts

    @property
    def medium(self):
        """Gets the medium of this ConversationSummary.  # noqa: E501

        The communication medium of the customer.  # noqa: E501

        :return: The medium of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this ConversationSummary.

        The communication medium of the customer.  # noqa: E501

        :param medium: The medium of this ConversationSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["sms", "websocket"]  # noqa: E501
        if medium not in allowed_values:
            raise ValueError(
                "Invalid value for `medium` ({0}), must be one of {1}"  # noqa: E501
                .format(medium, allowed_values)
            )

        self._medium = medium

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationSummary.  # noqa: E501


        :return: The merchant_id of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationSummary.


        :param merchant_id: The merchant_id of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def message_count(self):
        """Gets the message_count of this ConversationSummary.  # noqa: E501


        :return: The message_count of this ConversationSummary.  # noqa: E501
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count):
        """Sets the message_count of this ConversationSummary.


        :param message_count: The message_count of this ConversationSummary.  # noqa: E501
        :type: int
        """

        self._message_count = message_count

    @property
    def participants(self):
        """Gets the participants of this ConversationSummary.  # noqa: E501


        :return: The participants of this ConversationSummary.  # noqa: E501
        :rtype: list[ConversationParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this ConversationSummary.


        :param participants: The participants of this ConversationSummary.  # noqa: E501
        :type: list[ConversationParticipant]
        """

        self._participants = participants

    @property
    def start_dts(self):
        """Gets the start_dts of this ConversationSummary.  # noqa: E501

        Start of the conversation date/time  # noqa: E501

        :return: The start_dts of this ConversationSummary.  # noqa: E501
        :rtype: str
        """
        return self._start_dts

    @start_dts.setter
    def start_dts(self, start_dts):
        """Sets the start_dts of this ConversationSummary.

        Start of the conversation date/time  # noqa: E501

        :param start_dts: The start_dts of this ConversationSummary.  # noqa: E501
        :type: str
        """

        self._start_dts = start_dts

    @property
    def unread_messages(self):
        """Gets the unread_messages of this ConversationSummary.  # noqa: E501


        :return: The unread_messages of this ConversationSummary.  # noqa: E501
        :rtype: bool
        """
        return self._unread_messages

    @unread_messages.setter
    def unread_messages(self, unread_messages):
        """Sets the unread_messages of this ConversationSummary.


        :param unread_messages: The unread_messages of this ConversationSummary.  # noqa: E501
        :type: bool
        """

        self._unread_messages = unread_messages

    @property
    def visible(self):
        """Gets the visible of this ConversationSummary.  # noqa: E501


        :return: The visible of this ConversationSummary.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ConversationSummary.


        :param visible: The visible of this ConversationSummary.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if issubclass(ConversationSummary, dict):
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
        if not isinstance(other, ConversationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
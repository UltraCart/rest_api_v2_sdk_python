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


class ConversationWebsocketMessage(object):
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
        'conversation_arn': 'str',
        'conversation_uuid': 'str',
        'event_add_coupon': 'ConversationEventAddCoupon',
        'event_add_item': 'ConversationEventAddItem',
        'event_conversation_closed': 'ConversationSummary',
        'event_engage_customer': 'ConversationWebchatQueueStatusQueueEntry',
        'event_new_conversation': 'ConversationSummary',
        'event_new_message': 'ConversationSummary',
        'event_participant_join': 'ConversationSummary',
        'event_participant_join_participant': 'ConversationParticipant',
        'event_participant_left': 'ConversationSummary',
        'event_participant_left_participant': 'ConversationParticipant',
        'event_participant_update': 'ConversationSummary',
        'event_queue_new_member': 'ConversationWebchatQueueStatusQueueEntry',
        'event_queue_position': 'ConversationEventQueuePosition',
        'event_queue_status_update': 'ConversationWebchatQueueStatus',
        'event_read_message': 'ConversationEventReadMessage',
        'event_rrweb': 'ConversationEventRRWeb',
        'event_type': 'str',
        'event_typing': 'ConversationEventTyping',
        'event_updated_message': 'ConversationMessage',
        'event_webchat_context': 'ConversationEventWebchatContext',
        'message': 'ConversationMessage',
        'type': 'str'
    }

    attribute_map = {
        'conversation_arn': 'conversation_arn',
        'conversation_uuid': 'conversation_uuid',
        'event_add_coupon': 'event_add_coupon',
        'event_add_item': 'event_add_item',
        'event_conversation_closed': 'event_conversation_closed',
        'event_engage_customer': 'event_engage_customer',
        'event_new_conversation': 'event_new_conversation',
        'event_new_message': 'event_new_message',
        'event_participant_join': 'event_participant_join',
        'event_participant_join_participant': 'event_participant_join_participant',
        'event_participant_left': 'event_participant_left',
        'event_participant_left_participant': 'event_participant_left_participant',
        'event_participant_update': 'event_participant_update',
        'event_queue_new_member': 'event_queue_new_member',
        'event_queue_position': 'event_queue_position',
        'event_queue_status_update': 'event_queue_status_update',
        'event_read_message': 'event_read_message',
        'event_rrweb': 'event_rrweb',
        'event_type': 'event_type',
        'event_typing': 'event_typing',
        'event_updated_message': 'event_updated_message',
        'event_webchat_context': 'event_webchat_context',
        'message': 'message',
        'type': 'type'
    }

    def __init__(self, conversation_arn=None, conversation_uuid=None, event_add_coupon=None, event_add_item=None, event_conversation_closed=None, event_engage_customer=None, event_new_conversation=None, event_new_message=None, event_participant_join=None, event_participant_join_participant=None, event_participant_left=None, event_participant_left_participant=None, event_participant_update=None, event_queue_new_member=None, event_queue_position=None, event_queue_status_update=None, event_read_message=None, event_rrweb=None, event_type=None, event_typing=None, event_updated_message=None, event_webchat_context=None, message=None, type=None):  # noqa: E501
        """ConversationWebsocketMessage - a model defined in Swagger"""  # noqa: E501

        self._conversation_arn = None
        self._conversation_uuid = None
        self._event_add_coupon = None
        self._event_add_item = None
        self._event_conversation_closed = None
        self._event_engage_customer = None
        self._event_new_conversation = None
        self._event_new_message = None
        self._event_participant_join = None
        self._event_participant_join_participant = None
        self._event_participant_left = None
        self._event_participant_left_participant = None
        self._event_participant_update = None
        self._event_queue_new_member = None
        self._event_queue_position = None
        self._event_queue_status_update = None
        self._event_read_message = None
        self._event_rrweb = None
        self._event_type = None
        self._event_typing = None
        self._event_updated_message = None
        self._event_webchat_context = None
        self._message = None
        self._type = None
        self.discriminator = None

        if conversation_arn is not None:
            self.conversation_arn = conversation_arn
        if conversation_uuid is not None:
            self.conversation_uuid = conversation_uuid
        if event_add_coupon is not None:
            self.event_add_coupon = event_add_coupon
        if event_add_item is not None:
            self.event_add_item = event_add_item
        if event_conversation_closed is not None:
            self.event_conversation_closed = event_conversation_closed
        if event_engage_customer is not None:
            self.event_engage_customer = event_engage_customer
        if event_new_conversation is not None:
            self.event_new_conversation = event_new_conversation
        if event_new_message is not None:
            self.event_new_message = event_new_message
        if event_participant_join is not None:
            self.event_participant_join = event_participant_join
        if event_participant_join_participant is not None:
            self.event_participant_join_participant = event_participant_join_participant
        if event_participant_left is not None:
            self.event_participant_left = event_participant_left
        if event_participant_left_participant is not None:
            self.event_participant_left_participant = event_participant_left_participant
        if event_participant_update is not None:
            self.event_participant_update = event_participant_update
        if event_queue_new_member is not None:
            self.event_queue_new_member = event_queue_new_member
        if event_queue_position is not None:
            self.event_queue_position = event_queue_position
        if event_queue_status_update is not None:
            self.event_queue_status_update = event_queue_status_update
        if event_read_message is not None:
            self.event_read_message = event_read_message
        if event_rrweb is not None:
            self.event_rrweb = event_rrweb
        if event_type is not None:
            self.event_type = event_type
        if event_typing is not None:
            self.event_typing = event_typing
        if event_updated_message is not None:
            self.event_updated_message = event_updated_message
        if event_webchat_context is not None:
            self.event_webchat_context = event_webchat_context
        if message is not None:
            self.message = message
        if type is not None:
            self.type = type

    @property
    def conversation_arn(self):
        """Gets the conversation_arn of this ConversationWebsocketMessage.  # noqa: E501

        Conversation ARN  # noqa: E501

        :return: The conversation_arn of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: str
        """
        return self._conversation_arn

    @conversation_arn.setter
    def conversation_arn(self, conversation_arn):
        """Sets the conversation_arn of this ConversationWebsocketMessage.

        Conversation ARN  # noqa: E501

        :param conversation_arn: The conversation_arn of this ConversationWebsocketMessage.  # noqa: E501
        :type: str
        """

        self._conversation_arn = conversation_arn

    @property
    def conversation_uuid(self):
        """Gets the conversation_uuid of this ConversationWebsocketMessage.  # noqa: E501

        Conversation UUID if the websocket message is tied to a specific conversation  # noqa: E501

        :return: The conversation_uuid of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: str
        """
        return self._conversation_uuid

    @conversation_uuid.setter
    def conversation_uuid(self, conversation_uuid):
        """Sets the conversation_uuid of this ConversationWebsocketMessage.

        Conversation UUID if the websocket message is tied to a specific conversation  # noqa: E501

        :param conversation_uuid: The conversation_uuid of this ConversationWebsocketMessage.  # noqa: E501
        :type: str
        """

        self._conversation_uuid = conversation_uuid

    @property
    def event_add_coupon(self):
        """Gets the event_add_coupon of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_add_coupon of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventAddCoupon
        """
        return self._event_add_coupon

    @event_add_coupon.setter
    def event_add_coupon(self, event_add_coupon):
        """Sets the event_add_coupon of this ConversationWebsocketMessage.


        :param event_add_coupon: The event_add_coupon of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventAddCoupon
        """

        self._event_add_coupon = event_add_coupon

    @property
    def event_add_item(self):
        """Gets the event_add_item of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_add_item of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventAddItem
        """
        return self._event_add_item

    @event_add_item.setter
    def event_add_item(self, event_add_item):
        """Sets the event_add_item of this ConversationWebsocketMessage.


        :param event_add_item: The event_add_item of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventAddItem
        """

        self._event_add_item = event_add_item

    @property
    def event_conversation_closed(self):
        """Gets the event_conversation_closed of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_conversation_closed of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_conversation_closed

    @event_conversation_closed.setter
    def event_conversation_closed(self, event_conversation_closed):
        """Sets the event_conversation_closed of this ConversationWebsocketMessage.


        :param event_conversation_closed: The event_conversation_closed of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_conversation_closed = event_conversation_closed

    @property
    def event_engage_customer(self):
        """Gets the event_engage_customer of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_engage_customer of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationWebchatQueueStatusQueueEntry
        """
        return self._event_engage_customer

    @event_engage_customer.setter
    def event_engage_customer(self, event_engage_customer):
        """Sets the event_engage_customer of this ConversationWebsocketMessage.


        :param event_engage_customer: The event_engage_customer of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationWebchatQueueStatusQueueEntry
        """

        self._event_engage_customer = event_engage_customer

    @property
    def event_new_conversation(self):
        """Gets the event_new_conversation of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_new_conversation of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_new_conversation

    @event_new_conversation.setter
    def event_new_conversation(self, event_new_conversation):
        """Sets the event_new_conversation of this ConversationWebsocketMessage.


        :param event_new_conversation: The event_new_conversation of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_new_conversation = event_new_conversation

    @property
    def event_new_message(self):
        """Gets the event_new_message of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_new_message of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_new_message

    @event_new_message.setter
    def event_new_message(self, event_new_message):
        """Sets the event_new_message of this ConversationWebsocketMessage.


        :param event_new_message: The event_new_message of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_new_message = event_new_message

    @property
    def event_participant_join(self):
        """Gets the event_participant_join of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_participant_join of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_participant_join

    @event_participant_join.setter
    def event_participant_join(self, event_participant_join):
        """Sets the event_participant_join of this ConversationWebsocketMessage.


        :param event_participant_join: The event_participant_join of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_participant_join = event_participant_join

    @property
    def event_participant_join_participant(self):
        """Gets the event_participant_join_participant of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_participant_join_participant of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationParticipant
        """
        return self._event_participant_join_participant

    @event_participant_join_participant.setter
    def event_participant_join_participant(self, event_participant_join_participant):
        """Sets the event_participant_join_participant of this ConversationWebsocketMessage.


        :param event_participant_join_participant: The event_participant_join_participant of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationParticipant
        """

        self._event_participant_join_participant = event_participant_join_participant

    @property
    def event_participant_left(self):
        """Gets the event_participant_left of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_participant_left of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_participant_left

    @event_participant_left.setter
    def event_participant_left(self, event_participant_left):
        """Sets the event_participant_left of this ConversationWebsocketMessage.


        :param event_participant_left: The event_participant_left of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_participant_left = event_participant_left

    @property
    def event_participant_left_participant(self):
        """Gets the event_participant_left_participant of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_participant_left_participant of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationParticipant
        """
        return self._event_participant_left_participant

    @event_participant_left_participant.setter
    def event_participant_left_participant(self, event_participant_left_participant):
        """Sets the event_participant_left_participant of this ConversationWebsocketMessage.


        :param event_participant_left_participant: The event_participant_left_participant of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationParticipant
        """

        self._event_participant_left_participant = event_participant_left_participant

    @property
    def event_participant_update(self):
        """Gets the event_participant_update of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_participant_update of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationSummary
        """
        return self._event_participant_update

    @event_participant_update.setter
    def event_participant_update(self, event_participant_update):
        """Sets the event_participant_update of this ConversationWebsocketMessage.


        :param event_participant_update: The event_participant_update of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationSummary
        """

        self._event_participant_update = event_participant_update

    @property
    def event_queue_new_member(self):
        """Gets the event_queue_new_member of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_queue_new_member of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationWebchatQueueStatusQueueEntry
        """
        return self._event_queue_new_member

    @event_queue_new_member.setter
    def event_queue_new_member(self, event_queue_new_member):
        """Sets the event_queue_new_member of this ConversationWebsocketMessage.


        :param event_queue_new_member: The event_queue_new_member of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationWebchatQueueStatusQueueEntry
        """

        self._event_queue_new_member = event_queue_new_member

    @property
    def event_queue_position(self):
        """Gets the event_queue_position of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_queue_position of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventQueuePosition
        """
        return self._event_queue_position

    @event_queue_position.setter
    def event_queue_position(self, event_queue_position):
        """Sets the event_queue_position of this ConversationWebsocketMessage.


        :param event_queue_position: The event_queue_position of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventQueuePosition
        """

        self._event_queue_position = event_queue_position

    @property
    def event_queue_status_update(self):
        """Gets the event_queue_status_update of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_queue_status_update of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationWebchatQueueStatus
        """
        return self._event_queue_status_update

    @event_queue_status_update.setter
    def event_queue_status_update(self, event_queue_status_update):
        """Sets the event_queue_status_update of this ConversationWebsocketMessage.


        :param event_queue_status_update: The event_queue_status_update of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationWebchatQueueStatus
        """

        self._event_queue_status_update = event_queue_status_update

    @property
    def event_read_message(self):
        """Gets the event_read_message of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_read_message of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventReadMessage
        """
        return self._event_read_message

    @event_read_message.setter
    def event_read_message(self, event_read_message):
        """Sets the event_read_message of this ConversationWebsocketMessage.


        :param event_read_message: The event_read_message of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventReadMessage
        """

        self._event_read_message = event_read_message

    @property
    def event_rrweb(self):
        """Gets the event_rrweb of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_rrweb of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventRRWeb
        """
        return self._event_rrweb

    @event_rrweb.setter
    def event_rrweb(self, event_rrweb):
        """Sets the event_rrweb of this ConversationWebsocketMessage.


        :param event_rrweb: The event_rrweb of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventRRWeb
        """

        self._event_rrweb = event_rrweb

    @property
    def event_type(self):
        """Gets the event_type of this ConversationWebsocketMessage.  # noqa: E501

        Type of event  # noqa: E501

        :return: The event_type of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ConversationWebsocketMessage.

        Type of event  # noqa: E501

        :param event_type: The event_type of this ConversationWebsocketMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["queue position", "webchat start conversation", "conversation closed", "new conversation", "new message", "updated message", "queue status update", "rrweb", "participant update", "participant join", "participant left", "read message", "typing", "add coupon", "add item", "webchat context", "engage customer", "queue new member"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def event_typing(self):
        """Gets the event_typing of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_typing of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventTyping
        """
        return self._event_typing

    @event_typing.setter
    def event_typing(self, event_typing):
        """Sets the event_typing of this ConversationWebsocketMessage.


        :param event_typing: The event_typing of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventTyping
        """

        self._event_typing = event_typing

    @property
    def event_updated_message(self):
        """Gets the event_updated_message of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_updated_message of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationMessage
        """
        return self._event_updated_message

    @event_updated_message.setter
    def event_updated_message(self, event_updated_message):
        """Sets the event_updated_message of this ConversationWebsocketMessage.


        :param event_updated_message: The event_updated_message of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationMessage
        """

        self._event_updated_message = event_updated_message

    @property
    def event_webchat_context(self):
        """Gets the event_webchat_context of this ConversationWebsocketMessage.  # noqa: E501


        :return: The event_webchat_context of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationEventWebchatContext
        """
        return self._event_webchat_context

    @event_webchat_context.setter
    def event_webchat_context(self, event_webchat_context):
        """Sets the event_webchat_context of this ConversationWebsocketMessage.


        :param event_webchat_context: The event_webchat_context of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationEventWebchatContext
        """

        self._event_webchat_context = event_webchat_context

    @property
    def message(self):
        """Gets the message of this ConversationWebsocketMessage.  # noqa: E501


        :return: The message of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: ConversationMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConversationWebsocketMessage.


        :param message: The message of this ConversationWebsocketMessage.  # noqa: E501
        :type: ConversationMessage
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this ConversationWebsocketMessage.  # noqa: E501

        Type of message  # noqa: E501

        :return: The type of this ConversationWebsocketMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationWebsocketMessage.

        Type of message  # noqa: E501

        :param type: The type of this ConversationWebsocketMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["message", "event", "ping", "check queue position"]  # noqa: E501
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
        if issubclass(ConversationWebsocketMessage, dict):
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
        if not isinstance(other, ConversationWebsocketMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

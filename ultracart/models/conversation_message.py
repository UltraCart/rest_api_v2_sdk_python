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


class ConversationMessage(object):
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
        'author_conversation_participant_arn': 'str',
        'author_conversation_participant_name': 'str',
        'body': 'str',
        'client_message_id': 'str',
        'conversation_message_uuid': 'str',
        'delay_until_dts': 'str',
        'language_iso_code': 'str',
        'media_urls': 'list[str]',
        'merchant_id': 'str',
        'message_dts': 'str',
        'message_epoch': 'int',
        'translations': 'list[ConversationMessageTranslation]',
        'transport_statuses': 'list[ConversationMessageTransportStatus]',
        'type': 'str',
        'upload_keys': 'list[str]'
    }

    attribute_map = {
        'author_conversation_participant_arn': 'author_conversation_participant_arn',
        'author_conversation_participant_name': 'author_conversation_participant_name',
        'body': 'body',
        'client_message_id': 'client_message_id',
        'conversation_message_uuid': 'conversation_message_uuid',
        'delay_until_dts': 'delay_until_dts',
        'language_iso_code': 'language_iso_code',
        'media_urls': 'media_urls',
        'merchant_id': 'merchant_id',
        'message_dts': 'message_dts',
        'message_epoch': 'message_epoch',
        'translations': 'translations',
        'transport_statuses': 'transport_statuses',
        'type': 'type',
        'upload_keys': 'upload_keys'
    }

    def __init__(self, author_conversation_participant_arn=None, author_conversation_participant_name=None, body=None, client_message_id=None, conversation_message_uuid=None, delay_until_dts=None, language_iso_code=None, media_urls=None, merchant_id=None, message_dts=None, message_epoch=None, translations=None, transport_statuses=None, type=None, upload_keys=None):  # noqa: E501
        """ConversationMessage - a model defined in Swagger"""  # noqa: E501

        self._author_conversation_participant_arn = None
        self._author_conversation_participant_name = None
        self._body = None
        self._client_message_id = None
        self._conversation_message_uuid = None
        self._delay_until_dts = None
        self._language_iso_code = None
        self._media_urls = None
        self._merchant_id = None
        self._message_dts = None
        self._message_epoch = None
        self._translations = None
        self._transport_statuses = None
        self._type = None
        self._upload_keys = None
        self.discriminator = None

        if author_conversation_participant_arn is not None:
            self.author_conversation_participant_arn = author_conversation_participant_arn
        if author_conversation_participant_name is not None:
            self.author_conversation_participant_name = author_conversation_participant_name
        if body is not None:
            self.body = body
        if client_message_id is not None:
            self.client_message_id = client_message_id
        if conversation_message_uuid is not None:
            self.conversation_message_uuid = conversation_message_uuid
        if delay_until_dts is not None:
            self.delay_until_dts = delay_until_dts
        if language_iso_code is not None:
            self.language_iso_code = language_iso_code
        if media_urls is not None:
            self.media_urls = media_urls
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if message_dts is not None:
            self.message_dts = message_dts
        if message_epoch is not None:
            self.message_epoch = message_epoch
        if translations is not None:
            self.translations = translations
        if transport_statuses is not None:
            self.transport_statuses = transport_statuses
        if type is not None:
            self.type = type
        if upload_keys is not None:
            self.upload_keys = upload_keys

    @property
    def author_conversation_participant_arn(self):
        """Gets the author_conversation_participant_arn of this ConversationMessage.  # noqa: E501


        :return: The author_conversation_participant_arn of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._author_conversation_participant_arn

    @author_conversation_participant_arn.setter
    def author_conversation_participant_arn(self, author_conversation_participant_arn):
        """Sets the author_conversation_participant_arn of this ConversationMessage.


        :param author_conversation_participant_arn: The author_conversation_participant_arn of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._author_conversation_participant_arn = author_conversation_participant_arn

    @property
    def author_conversation_participant_name(self):
        """Gets the author_conversation_participant_name of this ConversationMessage.  # noqa: E501


        :return: The author_conversation_participant_name of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._author_conversation_participant_name

    @author_conversation_participant_name.setter
    def author_conversation_participant_name(self, author_conversation_participant_name):
        """Sets the author_conversation_participant_name of this ConversationMessage.


        :param author_conversation_participant_name: The author_conversation_participant_name of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._author_conversation_participant_name = author_conversation_participant_name

    @property
    def body(self):
        """Gets the body of this ConversationMessage.  # noqa: E501


        :return: The body of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ConversationMessage.


        :param body: The body of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def client_message_id(self):
        """Gets the client_message_id of this ConversationMessage.  # noqa: E501


        :return: The client_message_id of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._client_message_id

    @client_message_id.setter
    def client_message_id(self, client_message_id):
        """Sets the client_message_id of this ConversationMessage.


        :param client_message_id: The client_message_id of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._client_message_id = client_message_id

    @property
    def conversation_message_uuid(self):
        """Gets the conversation_message_uuid of this ConversationMessage.  # noqa: E501


        :return: The conversation_message_uuid of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._conversation_message_uuid

    @conversation_message_uuid.setter
    def conversation_message_uuid(self, conversation_message_uuid):
        """Sets the conversation_message_uuid of this ConversationMessage.


        :param conversation_message_uuid: The conversation_message_uuid of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._conversation_message_uuid = conversation_message_uuid

    @property
    def delay_until_dts(self):
        """Gets the delay_until_dts of this ConversationMessage.  # noqa: E501

        Delay message transmission until date/time  # noqa: E501

        :return: The delay_until_dts of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._delay_until_dts

    @delay_until_dts.setter
    def delay_until_dts(self, delay_until_dts):
        """Sets the delay_until_dts of this ConversationMessage.

        Delay message transmission until date/time  # noqa: E501

        :param delay_until_dts: The delay_until_dts of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._delay_until_dts = delay_until_dts

    @property
    def language_iso_code(self):
        """Gets the language_iso_code of this ConversationMessage.  # noqa: E501


        :return: The language_iso_code of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._language_iso_code

    @language_iso_code.setter
    def language_iso_code(self, language_iso_code):
        """Sets the language_iso_code of this ConversationMessage.


        :param language_iso_code: The language_iso_code of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._language_iso_code = language_iso_code

    @property
    def media_urls(self):
        """Gets the media_urls of this ConversationMessage.  # noqa: E501


        :return: The media_urls of this ConversationMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._media_urls

    @media_urls.setter
    def media_urls(self, media_urls):
        """Sets the media_urls of this ConversationMessage.


        :param media_urls: The media_urls of this ConversationMessage.  # noqa: E501
        :type: list[str]
        """

        self._media_urls = media_urls

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationMessage.  # noqa: E501


        :return: The merchant_id of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationMessage.


        :param merchant_id: The merchant_id of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def message_dts(self):
        """Gets the message_dts of this ConversationMessage.  # noqa: E501

        Message date/time  # noqa: E501

        :return: The message_dts of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._message_dts

    @message_dts.setter
    def message_dts(self, message_dts):
        """Sets the message_dts of this ConversationMessage.

        Message date/time  # noqa: E501

        :param message_dts: The message_dts of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._message_dts = message_dts

    @property
    def message_epoch(self):
        """Gets the message_epoch of this ConversationMessage.  # noqa: E501

        Message epoch milliseconds  # noqa: E501

        :return: The message_epoch of this ConversationMessage.  # noqa: E501
        :rtype: int
        """
        return self._message_epoch

    @message_epoch.setter
    def message_epoch(self, message_epoch):
        """Sets the message_epoch of this ConversationMessage.

        Message epoch milliseconds  # noqa: E501

        :param message_epoch: The message_epoch of this ConversationMessage.  # noqa: E501
        :type: int
        """

        self._message_epoch = message_epoch

    @property
    def translations(self):
        """Gets the translations of this ConversationMessage.  # noqa: E501


        :return: The translations of this ConversationMessage.  # noqa: E501
        :rtype: list[ConversationMessageTranslation]
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this ConversationMessage.


        :param translations: The translations of this ConversationMessage.  # noqa: E501
        :type: list[ConversationMessageTranslation]
        """

        self._translations = translations

    @property
    def transport_statuses(self):
        """Gets the transport_statuses of this ConversationMessage.  # noqa: E501


        :return: The transport_statuses of this ConversationMessage.  # noqa: E501
        :rtype: list[ConversationMessageTransportStatus]
        """
        return self._transport_statuses

    @transport_statuses.setter
    def transport_statuses(self, transport_statuses):
        """Sets the transport_statuses of this ConversationMessage.


        :param transport_statuses: The transport_statuses of this ConversationMessage.  # noqa: E501
        :type: list[ConversationMessageTransportStatus]
        """

        self._transport_statuses = transport_statuses

    @property
    def type(self):
        """Gets the type of this ConversationMessage.  # noqa: E501

        Message type  # noqa: E501

        :return: The type of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationMessage.

        Message type  # noqa: E501

        :param type: The type of this ConversationMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["message", "notice"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def upload_keys(self):
        """Gets the upload_keys of this ConversationMessage.  # noqa: E501


        :return: The upload_keys of this ConversationMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._upload_keys

    @upload_keys.setter
    def upload_keys(self, upload_keys):
        """Sets the upload_keys of this ConversationMessage.


        :param upload_keys: The upload_keys of this ConversationMessage.  # noqa: E501
        :type: list[str]
        """

        self._upload_keys = upload_keys

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
        if issubclass(ConversationMessage, dict):
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
        if not isinstance(other, ConversationMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
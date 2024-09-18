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


class ConversationPbxAgent(object):
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
        'cellphone': 'str',
        'conversation_pbx_agent_uuid': 'str',
        'extension': 'int',
        'forward_calls_to_cellphone': 'bool',
        'full_name': 'str',
        'login': 'str',
        'merchant_id': 'str',
        'personal_conversation_pbx_voicemail_mailbox_uuid': 'str',
        'record_outgoing_automatically': 'bool',
        'shared_conversation_pbx_voicemail_mailbox_uuid': 'str',
        'twilio_taskrouter_worker_id': 'str',
        'unavailable_play_audio_uuid': 'str',
        'unavailable_say': 'str',
        'unavailable_say_voice': 'str',
        'user_id': 'int',
        'voicemail': 'bool'
    }

    attribute_map = {
        'cellphone': 'cellphone',
        'conversation_pbx_agent_uuid': 'conversation_pbx_agent_uuid',
        'extension': 'extension',
        'forward_calls_to_cellphone': 'forward_calls_to_cellphone',
        'full_name': 'full_name',
        'login': 'login',
        'merchant_id': 'merchant_id',
        'personal_conversation_pbx_voicemail_mailbox_uuid': 'personal_conversation_pbx_voicemail_mailbox_uuid',
        'record_outgoing_automatically': 'record_outgoing_automatically',
        'shared_conversation_pbx_voicemail_mailbox_uuid': 'shared_conversation_pbx_voicemail_mailbox_uuid',
        'twilio_taskrouter_worker_id': 'twilio_taskrouter_worker_id',
        'unavailable_play_audio_uuid': 'unavailable_play_audio_uuid',
        'unavailable_say': 'unavailable_say',
        'unavailable_say_voice': 'unavailable_say_voice',
        'user_id': 'user_id',
        'voicemail': 'voicemail'
    }

    def __init__(self, cellphone=None, conversation_pbx_agent_uuid=None, extension=None, forward_calls_to_cellphone=None, full_name=None, login=None, merchant_id=None, personal_conversation_pbx_voicemail_mailbox_uuid=None, record_outgoing_automatically=None, shared_conversation_pbx_voicemail_mailbox_uuid=None, twilio_taskrouter_worker_id=None, unavailable_play_audio_uuid=None, unavailable_say=None, unavailable_say_voice=None, user_id=None, voicemail=None):  # noqa: E501
        """ConversationPbxAgent - a model defined in Swagger"""  # noqa: E501

        self._cellphone = None
        self._conversation_pbx_agent_uuid = None
        self._extension = None
        self._forward_calls_to_cellphone = None
        self._full_name = None
        self._login = None
        self._merchant_id = None
        self._personal_conversation_pbx_voicemail_mailbox_uuid = None
        self._record_outgoing_automatically = None
        self._shared_conversation_pbx_voicemail_mailbox_uuid = None
        self._twilio_taskrouter_worker_id = None
        self._unavailable_play_audio_uuid = None
        self._unavailable_say = None
        self._unavailable_say_voice = None
        self._user_id = None
        self._voicemail = None
        self.discriminator = None

        if cellphone is not None:
            self.cellphone = cellphone
        if conversation_pbx_agent_uuid is not None:
            self.conversation_pbx_agent_uuid = conversation_pbx_agent_uuid
        if extension is not None:
            self.extension = extension
        if forward_calls_to_cellphone is not None:
            self.forward_calls_to_cellphone = forward_calls_to_cellphone
        if full_name is not None:
            self.full_name = full_name
        if login is not None:
            self.login = login
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if personal_conversation_pbx_voicemail_mailbox_uuid is not None:
            self.personal_conversation_pbx_voicemail_mailbox_uuid = personal_conversation_pbx_voicemail_mailbox_uuid
        if record_outgoing_automatically is not None:
            self.record_outgoing_automatically = record_outgoing_automatically
        if shared_conversation_pbx_voicemail_mailbox_uuid is not None:
            self.shared_conversation_pbx_voicemail_mailbox_uuid = shared_conversation_pbx_voicemail_mailbox_uuid
        if twilio_taskrouter_worker_id is not None:
            self.twilio_taskrouter_worker_id = twilio_taskrouter_worker_id
        if unavailable_play_audio_uuid is not None:
            self.unavailable_play_audio_uuid = unavailable_play_audio_uuid
        if unavailable_say is not None:
            self.unavailable_say = unavailable_say
        if unavailable_say_voice is not None:
            self.unavailable_say_voice = unavailable_say_voice
        if user_id is not None:
            self.user_id = user_id
        if voicemail is not None:
            self.voicemail = voicemail

    @property
    def cellphone(self):
        """Gets the cellphone of this ConversationPbxAgent.  # noqa: E501

        Cellphone number of agent in E.164 format  # noqa: E501

        :return: The cellphone of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._cellphone

    @cellphone.setter
    def cellphone(self, cellphone):
        """Sets the cellphone of this ConversationPbxAgent.

        Cellphone number of agent in E.164 format  # noqa: E501

        :param cellphone: The cellphone of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if cellphone is not None and len(cellphone) > 50:
            raise ValueError("Invalid value for `cellphone`, length must be less than or equal to `50`")  # noqa: E501

        self._cellphone = cellphone

    @property
    def conversation_pbx_agent_uuid(self):
        """Gets the conversation_pbx_agent_uuid of this ConversationPbxAgent.  # noqa: E501

        Conversation Pbx Agent unique identifier  # noqa: E501

        :return: The conversation_pbx_agent_uuid of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._conversation_pbx_agent_uuid

    @conversation_pbx_agent_uuid.setter
    def conversation_pbx_agent_uuid(self, conversation_pbx_agent_uuid):
        """Sets the conversation_pbx_agent_uuid of this ConversationPbxAgent.

        Conversation Pbx Agent unique identifier  # noqa: E501

        :param conversation_pbx_agent_uuid: The conversation_pbx_agent_uuid of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """

        self._conversation_pbx_agent_uuid = conversation_pbx_agent_uuid

    @property
    def extension(self):
        """Gets the extension of this ConversationPbxAgent.  # noqa: E501

        Extension  # noqa: E501

        :return: The extension of this ConversationPbxAgent.  # noqa: E501
        :rtype: int
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this ConversationPbxAgent.

        Extension  # noqa: E501

        :param extension: The extension of this ConversationPbxAgent.  # noqa: E501
        :type: int
        """

        self._extension = extension

    @property
    def forward_calls_to_cellphone(self):
        """Gets the forward_calls_to_cellphone of this ConversationPbxAgent.  # noqa: E501

        True if calls to this agent should be forwarded to their cellphone  # noqa: E501

        :return: The forward_calls_to_cellphone of this ConversationPbxAgent.  # noqa: E501
        :rtype: bool
        """
        return self._forward_calls_to_cellphone

    @forward_calls_to_cellphone.setter
    def forward_calls_to_cellphone(self, forward_calls_to_cellphone):
        """Sets the forward_calls_to_cellphone of this ConversationPbxAgent.

        True if calls to this agent should be forwarded to their cellphone  # noqa: E501

        :param forward_calls_to_cellphone: The forward_calls_to_cellphone of this ConversationPbxAgent.  # noqa: E501
        :type: bool
        """

        self._forward_calls_to_cellphone = forward_calls_to_cellphone

    @property
    def full_name(self):
        """Gets the full_name of this ConversationPbxAgent.  # noqa: E501

        Full name  # noqa: E501

        :return: The full_name of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ConversationPbxAgent.

        Full name  # noqa: E501

        :param full_name: The full_name of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def login(self):
        """Gets the login of this ConversationPbxAgent.  # noqa: E501

        Agent login  # noqa: E501

        :return: The login of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ConversationPbxAgent.

        Agent login  # noqa: E501

        :param login: The login of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationPbxAgent.  # noqa: E501

        Merchant Id  # noqa: E501

        :return: The merchant_id of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationPbxAgent.

        Merchant Id  # noqa: E501

        :param merchant_id: The merchant_id of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if merchant_id is not None and len(merchant_id) > 5:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `5`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def personal_conversation_pbx_voicemail_mailbox_uuid(self):
        """Gets the personal_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501

        Personal Conversation Pbx Voicemail Mailbox UUID  # noqa: E501

        :return: The personal_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._personal_conversation_pbx_voicemail_mailbox_uuid

    @personal_conversation_pbx_voicemail_mailbox_uuid.setter
    def personal_conversation_pbx_voicemail_mailbox_uuid(self, personal_conversation_pbx_voicemail_mailbox_uuid):
        """Sets the personal_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.

        Personal Conversation Pbx Voicemail Mailbox UUID  # noqa: E501

        :param personal_conversation_pbx_voicemail_mailbox_uuid: The personal_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if personal_conversation_pbx_voicemail_mailbox_uuid is not None and len(personal_conversation_pbx_voicemail_mailbox_uuid) > 50:
            raise ValueError("Invalid value for `personal_conversation_pbx_voicemail_mailbox_uuid`, length must be less than or equal to `50`")  # noqa: E501

        self._personal_conversation_pbx_voicemail_mailbox_uuid = personal_conversation_pbx_voicemail_mailbox_uuid

    @property
    def record_outgoing_automatically(self):
        """Gets the record_outgoing_automatically of this ConversationPbxAgent.  # noqa: E501

        True if outgoing calls should be automatically recorded  # noqa: E501

        :return: The record_outgoing_automatically of this ConversationPbxAgent.  # noqa: E501
        :rtype: bool
        """
        return self._record_outgoing_automatically

    @record_outgoing_automatically.setter
    def record_outgoing_automatically(self, record_outgoing_automatically):
        """Sets the record_outgoing_automatically of this ConversationPbxAgent.

        True if outgoing calls should be automatically recorded  # noqa: E501

        :param record_outgoing_automatically: The record_outgoing_automatically of this ConversationPbxAgent.  # noqa: E501
        :type: bool
        """

        self._record_outgoing_automatically = record_outgoing_automatically

    @property
    def shared_conversation_pbx_voicemail_mailbox_uuid(self):
        """Gets the shared_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501

        Shared Conversation Pbx Voicemail Mailbox UUID  # noqa: E501

        :return: The shared_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._shared_conversation_pbx_voicemail_mailbox_uuid

    @shared_conversation_pbx_voicemail_mailbox_uuid.setter
    def shared_conversation_pbx_voicemail_mailbox_uuid(self, shared_conversation_pbx_voicemail_mailbox_uuid):
        """Sets the shared_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.

        Shared Conversation Pbx Voicemail Mailbox UUID  # noqa: E501

        :param shared_conversation_pbx_voicemail_mailbox_uuid: The shared_conversation_pbx_voicemail_mailbox_uuid of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if shared_conversation_pbx_voicemail_mailbox_uuid is not None and len(shared_conversation_pbx_voicemail_mailbox_uuid) > 50:
            raise ValueError("Invalid value for `shared_conversation_pbx_voicemail_mailbox_uuid`, length must be less than or equal to `50`")  # noqa: E501

        self._shared_conversation_pbx_voicemail_mailbox_uuid = shared_conversation_pbx_voicemail_mailbox_uuid

    @property
    def twilio_taskrouter_worker_id(self):
        """Gets the twilio_taskrouter_worker_id of this ConversationPbxAgent.  # noqa: E501

        Twilio taskrouter worker Id  # noqa: E501

        :return: The twilio_taskrouter_worker_id of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._twilio_taskrouter_worker_id

    @twilio_taskrouter_worker_id.setter
    def twilio_taskrouter_worker_id(self, twilio_taskrouter_worker_id):
        """Sets the twilio_taskrouter_worker_id of this ConversationPbxAgent.

        Twilio taskrouter worker Id  # noqa: E501

        :param twilio_taskrouter_worker_id: The twilio_taskrouter_worker_id of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if twilio_taskrouter_worker_id is not None and len(twilio_taskrouter_worker_id) > 100:
            raise ValueError("Invalid value for `twilio_taskrouter_worker_id`, length must be less than or equal to `100`")  # noqa: E501

        self._twilio_taskrouter_worker_id = twilio_taskrouter_worker_id

    @property
    def unavailable_play_audio_uuid(self):
        """Gets the unavailable_play_audio_uuid of this ConversationPbxAgent.  # noqa: E501

        Unavailable play audio UUID  # noqa: E501

        :return: The unavailable_play_audio_uuid of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._unavailable_play_audio_uuid

    @unavailable_play_audio_uuid.setter
    def unavailable_play_audio_uuid(self, unavailable_play_audio_uuid):
        """Sets the unavailable_play_audio_uuid of this ConversationPbxAgent.

        Unavailable play audio UUID  # noqa: E501

        :param unavailable_play_audio_uuid: The unavailable_play_audio_uuid of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if unavailable_play_audio_uuid is not None and len(unavailable_play_audio_uuid) > 50:
            raise ValueError("Invalid value for `unavailable_play_audio_uuid`, length must be less than or equal to `50`")  # noqa: E501

        self._unavailable_play_audio_uuid = unavailable_play_audio_uuid

    @property
    def unavailable_say(self):
        """Gets the unavailable_say of this ConversationPbxAgent.  # noqa: E501

        Unavailable say  # noqa: E501

        :return: The unavailable_say of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._unavailable_say

    @unavailable_say.setter
    def unavailable_say(self, unavailable_say):
        """Sets the unavailable_say of this ConversationPbxAgent.

        Unavailable say  # noqa: E501

        :param unavailable_say: The unavailable_say of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """

        self._unavailable_say = unavailable_say

    @property
    def unavailable_say_voice(self):
        """Gets the unavailable_say_voice of this ConversationPbxAgent.  # noqa: E501

        Unavailable say voice  # noqa: E501

        :return: The unavailable_say_voice of this ConversationPbxAgent.  # noqa: E501
        :rtype: str
        """
        return self._unavailable_say_voice

    @unavailable_say_voice.setter
    def unavailable_say_voice(self, unavailable_say_voice):
        """Sets the unavailable_say_voice of this ConversationPbxAgent.

        Unavailable say voice  # noqa: E501

        :param unavailable_say_voice: The unavailable_say_voice of this ConversationPbxAgent.  # noqa: E501
        :type: str
        """
        if unavailable_say_voice is not None and len(unavailable_say_voice) > 50:
            raise ValueError("Invalid value for `unavailable_say_voice`, length must be less than or equal to `50`")  # noqa: E501

        self._unavailable_say_voice = unavailable_say_voice

    @property
    def user_id(self):
        """Gets the user_id of this ConversationPbxAgent.  # noqa: E501

        User Id  # noqa: E501

        :return: The user_id of this ConversationPbxAgent.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConversationPbxAgent.

        User Id  # noqa: E501

        :param user_id: The user_id of this ConversationPbxAgent.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def voicemail(self):
        """Gets the voicemail of this ConversationPbxAgent.  # noqa: E501

        True if this agent has voicemail configured  # noqa: E501

        :return: The voicemail of this ConversationPbxAgent.  # noqa: E501
        :rtype: bool
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """Sets the voicemail of this ConversationPbxAgent.

        True if this agent has voicemail configured  # noqa: E501

        :param voicemail: The voicemail of this ConversationPbxAgent.  # noqa: E501
        :type: bool
        """

        self._voicemail = voicemail

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
        if issubclass(ConversationPbxAgent, dict):
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
        if not isinstance(other, ConversationPbxAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
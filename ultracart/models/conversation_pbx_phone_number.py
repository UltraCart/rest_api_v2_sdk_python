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


class ConversationPbxPhoneNumber(object):
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
        'conversation_pbx_time_range_uuid': 'str',
        'merchant_id': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_target': 'action_target',
        'conversation_pbx_time_range_uuid': 'conversation_pbx_time_range_uuid',
        'merchant_id': 'merchant_id',
        'phone_number': 'phone_number'
    }

    def __init__(self, action=None, action_target=None, conversation_pbx_time_range_uuid=None, merchant_id=None, phone_number=None):  # noqa: E501
        """ConversationPbxPhoneNumber - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._action_target = None
        self._conversation_pbx_time_range_uuid = None
        self._merchant_id = None
        self._phone_number = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_target is not None:
            self.action_target = action_target
        if conversation_pbx_time_range_uuid is not None:
            self.conversation_pbx_time_range_uuid = conversation_pbx_time_range_uuid
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def action(self):
        """Gets the action of this ConversationPbxPhoneNumber.  # noqa: E501

        Action  # noqa: E501

        :return: The action of this ConversationPbxPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ConversationPbxPhoneNumber.

        Action  # noqa: E501

        :param action: The action of this ConversationPbxPhoneNumber.  # noqa: E501
        :type: str
        """
        if action is not None and len(action) > 30:
            raise ValueError("Invalid value for `action`, length must be less than or equal to `30`")  # noqa: E501

        self._action = action

    @property
    def action_target(self):
        """Gets the action_target of this ConversationPbxPhoneNumber.  # noqa: E501

        Action target  # noqa: E501

        :return: The action_target of this ConversationPbxPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._action_target

    @action_target.setter
    def action_target(self, action_target):
        """Sets the action_target of this ConversationPbxPhoneNumber.

        Action target  # noqa: E501

        :param action_target: The action_target of this ConversationPbxPhoneNumber.  # noqa: E501
        :type: str
        """
        if action_target is not None and len(action_target) > 50:
            raise ValueError("Invalid value for `action_target`, length must be less than or equal to `50`")  # noqa: E501

        self._action_target = action_target

    @property
    def conversation_pbx_time_range_uuid(self):
        """Gets the conversation_pbx_time_range_uuid of this ConversationPbxPhoneNumber.  # noqa: E501

        Conversation Pbx Phone Number UUID  # noqa: E501

        :return: The conversation_pbx_time_range_uuid of this ConversationPbxPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._conversation_pbx_time_range_uuid

    @conversation_pbx_time_range_uuid.setter
    def conversation_pbx_time_range_uuid(self, conversation_pbx_time_range_uuid):
        """Sets the conversation_pbx_time_range_uuid of this ConversationPbxPhoneNumber.

        Conversation Pbx Phone Number UUID  # noqa: E501

        :param conversation_pbx_time_range_uuid: The conversation_pbx_time_range_uuid of this ConversationPbxPhoneNumber.  # noqa: E501
        :type: str
        """
        if conversation_pbx_time_range_uuid is not None and len(conversation_pbx_time_range_uuid) > 50:
            raise ValueError("Invalid value for `conversation_pbx_time_range_uuid`, length must be less than or equal to `50`")  # noqa: E501

        self._conversation_pbx_time_range_uuid = conversation_pbx_time_range_uuid

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationPbxPhoneNumber.  # noqa: E501

        Merchant Id  # noqa: E501

        :return: The merchant_id of this ConversationPbxPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationPbxPhoneNumber.

        Merchant Id  # noqa: E501

        :param merchant_id: The merchant_id of this ConversationPbxPhoneNumber.  # noqa: E501
        :type: str
        """
        if merchant_id is not None and len(merchant_id) > 5:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `5`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def phone_number(self):
        """Gets the phone_number of this ConversationPbxPhoneNumber.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone_number of this ConversationPbxPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ConversationPbxPhoneNumber.

        Phone number  # noqa: E501

        :param phone_number: The phone_number of this ConversationPbxPhoneNumber.  # noqa: E501
        :type: str
        """
        if phone_number is not None and len(phone_number) > 50:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `50`")  # noqa: E501

        self._phone_number = phone_number

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
        if issubclass(ConversationPbxPhoneNumber, dict):
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
        if not isinstance(other, ConversationPbxPhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

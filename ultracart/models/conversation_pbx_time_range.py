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


class ConversationPbxTimeRange(object):
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
        'configs': 'list[ConversationPbxTimeRangeConfig]',
        'conversation_pbx_time_range_uuid': 'str',
        'merchant_id': 'str',
        'time_range_name': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'configs': 'configs',
        'conversation_pbx_time_range_uuid': 'conversation_pbx_time_range_uuid',
        'merchant_id': 'merchant_id',
        'time_range_name': 'time_range_name',
        'timezone': 'timezone'
    }

    def __init__(self, configs=None, conversation_pbx_time_range_uuid=None, merchant_id=None, time_range_name=None, timezone=None):  # noqa: E501
        """ConversationPbxTimeRange - a model defined in Swagger"""  # noqa: E501

        self._configs = None
        self._conversation_pbx_time_range_uuid = None
        self._merchant_id = None
        self._time_range_name = None
        self._timezone = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        if conversation_pbx_time_range_uuid is not None:
            self.conversation_pbx_time_range_uuid = conversation_pbx_time_range_uuid
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if time_range_name is not None:
            self.time_range_name = time_range_name
        if timezone is not None:
            self.timezone = timezone

    @property
    def configs(self):
        """Gets the configs of this ConversationPbxTimeRange.  # noqa: E501

        Configurations for all ranges in this time range  # noqa: E501

        :return: The configs of this ConversationPbxTimeRange.  # noqa: E501
        :rtype: list[ConversationPbxTimeRangeConfig]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ConversationPbxTimeRange.

        Configurations for all ranges in this time range  # noqa: E501

        :param configs: The configs of this ConversationPbxTimeRange.  # noqa: E501
        :type: list[ConversationPbxTimeRangeConfig]
        """

        self._configs = configs

    @property
    def conversation_pbx_time_range_uuid(self):
        """Gets the conversation_pbx_time_range_uuid of this ConversationPbxTimeRange.  # noqa: E501

        Conversation Pbx Time Range UUID  # noqa: E501

        :return: The conversation_pbx_time_range_uuid of this ConversationPbxTimeRange.  # noqa: E501
        :rtype: str
        """
        return self._conversation_pbx_time_range_uuid

    @conversation_pbx_time_range_uuid.setter
    def conversation_pbx_time_range_uuid(self, conversation_pbx_time_range_uuid):
        """Sets the conversation_pbx_time_range_uuid of this ConversationPbxTimeRange.

        Conversation Pbx Time Range UUID  # noqa: E501

        :param conversation_pbx_time_range_uuid: The conversation_pbx_time_range_uuid of this ConversationPbxTimeRange.  # noqa: E501
        :type: str
        """
        if conversation_pbx_time_range_uuid is not None and len(conversation_pbx_time_range_uuid) > 50:
            raise ValueError("Invalid value for `conversation_pbx_time_range_uuid`, length must be less than or equal to `50`")  # noqa: E501

        self._conversation_pbx_time_range_uuid = conversation_pbx_time_range_uuid

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationPbxTimeRange.  # noqa: E501

        Merchant Id  # noqa: E501

        :return: The merchant_id of this ConversationPbxTimeRange.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationPbxTimeRange.

        Merchant Id  # noqa: E501

        :param merchant_id: The merchant_id of this ConversationPbxTimeRange.  # noqa: E501
        :type: str
        """
        if merchant_id is not None and len(merchant_id) > 5:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `5`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def time_range_name(self):
        """Gets the time_range_name of this ConversationPbxTimeRange.  # noqa: E501

        Time range name  # noqa: E501

        :return: The time_range_name of this ConversationPbxTimeRange.  # noqa: E501
        :rtype: str
        """
        return self._time_range_name

    @time_range_name.setter
    def time_range_name(self, time_range_name):
        """Sets the time_range_name of this ConversationPbxTimeRange.

        Time range name  # noqa: E501

        :param time_range_name: The time_range_name of this ConversationPbxTimeRange.  # noqa: E501
        :type: str
        """
        if time_range_name is not None and len(time_range_name) > 50:
            raise ValueError("Invalid value for `time_range_name`, length must be less than or equal to `50`")  # noqa: E501

        self._time_range_name = time_range_name

    @property
    def timezone(self):
        """Gets the timezone of this ConversationPbxTimeRange.  # noqa: E501

        Timezone  # noqa: E501

        :return: The timezone of this ConversationPbxTimeRange.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ConversationPbxTimeRange.

        Timezone  # noqa: E501

        :param timezone: The timezone of this ConversationPbxTimeRange.  # noqa: E501
        :type: str
        """
        if timezone is not None and len(timezone) > 100:
            raise ValueError("Invalid value for `timezone`, length must be less than or equal to `100`")  # noqa: E501

        self._timezone = timezone

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
        if issubclass(ConversationPbxTimeRange, dict):
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
        if not isinstance(other, ConversationPbxTimeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

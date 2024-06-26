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


class ConversationPbxTimeBased(object):
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
        'conversation_pbx_time_based_uuid': 'str',
        'mapping_config': 'ConversationPbxTimeBasedMappingConfig',
        'merchant_id': 'str',
        'time_based_name': 'str'
    }

    attribute_map = {
        'conversation_pbx_time_based_uuid': 'conversation_pbx_time_based_uuid',
        'mapping_config': 'mapping_config',
        'merchant_id': 'merchant_id',
        'time_based_name': 'time_based_name'
    }

    def __init__(self, conversation_pbx_time_based_uuid=None, mapping_config=None, merchant_id=None, time_based_name=None):  # noqa: E501
        """ConversationPbxTimeBased - a model defined in Swagger"""  # noqa: E501

        self._conversation_pbx_time_based_uuid = None
        self._mapping_config = None
        self._merchant_id = None
        self._time_based_name = None
        self.discriminator = None

        if conversation_pbx_time_based_uuid is not None:
            self.conversation_pbx_time_based_uuid = conversation_pbx_time_based_uuid
        if mapping_config is not None:
            self.mapping_config = mapping_config
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if time_based_name is not None:
            self.time_based_name = time_based_name

    @property
    def conversation_pbx_time_based_uuid(self):
        """Gets the conversation_pbx_time_based_uuid of this ConversationPbxTimeBased.  # noqa: E501


        :return: The conversation_pbx_time_based_uuid of this ConversationPbxTimeBased.  # noqa: E501
        :rtype: str
        """
        return self._conversation_pbx_time_based_uuid

    @conversation_pbx_time_based_uuid.setter
    def conversation_pbx_time_based_uuid(self, conversation_pbx_time_based_uuid):
        """Sets the conversation_pbx_time_based_uuid of this ConversationPbxTimeBased.


        :param conversation_pbx_time_based_uuid: The conversation_pbx_time_based_uuid of this ConversationPbxTimeBased.  # noqa: E501
        :type: str
        """

        self._conversation_pbx_time_based_uuid = conversation_pbx_time_based_uuid

    @property
    def mapping_config(self):
        """Gets the mapping_config of this ConversationPbxTimeBased.  # noqa: E501


        :return: The mapping_config of this ConversationPbxTimeBased.  # noqa: E501
        :rtype: ConversationPbxTimeBasedMappingConfig
        """
        return self._mapping_config

    @mapping_config.setter
    def mapping_config(self, mapping_config):
        """Sets the mapping_config of this ConversationPbxTimeBased.


        :param mapping_config: The mapping_config of this ConversationPbxTimeBased.  # noqa: E501
        :type: ConversationPbxTimeBasedMappingConfig
        """

        self._mapping_config = mapping_config

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ConversationPbxTimeBased.  # noqa: E501


        :return: The merchant_id of this ConversationPbxTimeBased.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ConversationPbxTimeBased.


        :param merchant_id: The merchant_id of this ConversationPbxTimeBased.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def time_based_name(self):
        """Gets the time_based_name of this ConversationPbxTimeBased.  # noqa: E501


        :return: The time_based_name of this ConversationPbxTimeBased.  # noqa: E501
        :rtype: str
        """
        return self._time_based_name

    @time_based_name.setter
    def time_based_name(self, time_based_name):
        """Sets the time_based_name of this ConversationPbxTimeBased.


        :param time_based_name: The time_based_name of this ConversationPbxTimeBased.  # noqa: E501
        :type: str
        """

        self._time_based_name = time_based_name

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
        if issubclass(ConversationPbxTimeBased, dict):
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
        if not isinstance(other, ConversationPbxTimeBased):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

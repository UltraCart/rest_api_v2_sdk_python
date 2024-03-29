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


class EmailCommseqSmsSendTestRequest(object):
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
        'esp_commseq_step_uuid': 'str',
        'esp_commseq_uuid': 'str',
        'send_to_cellphone_e164': 'str'
    }

    attribute_map = {
        'esp_commseq_step_uuid': 'esp_commseq_step_uuid',
        'esp_commseq_uuid': 'esp_commseq_uuid',
        'send_to_cellphone_e164': 'send_to_cellphone_e164'
    }

    def __init__(self, esp_commseq_step_uuid=None, esp_commseq_uuid=None, send_to_cellphone_e164=None):  # noqa: E501
        """EmailCommseqSmsSendTestRequest - a model defined in Swagger"""  # noqa: E501

        self._esp_commseq_step_uuid = None
        self._esp_commseq_uuid = None
        self._send_to_cellphone_e164 = None
        self.discriminator = None

        if esp_commseq_step_uuid is not None:
            self.esp_commseq_step_uuid = esp_commseq_step_uuid
        if esp_commseq_uuid is not None:
            self.esp_commseq_uuid = esp_commseq_uuid
        if send_to_cellphone_e164 is not None:
            self.send_to_cellphone_e164 = send_to_cellphone_e164

    @property
    def esp_commseq_step_uuid(self):
        """Gets the esp_commseq_step_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501


        :return: The esp_commseq_step_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_step_uuid

    @esp_commseq_step_uuid.setter
    def esp_commseq_step_uuid(self, esp_commseq_step_uuid):
        """Sets the esp_commseq_step_uuid of this EmailCommseqSmsSendTestRequest.


        :param esp_commseq_step_uuid: The esp_commseq_step_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_step_uuid = esp_commseq_step_uuid

    @property
    def esp_commseq_uuid(self):
        """Gets the esp_commseq_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501


        :return: The esp_commseq_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_uuid

    @esp_commseq_uuid.setter
    def esp_commseq_uuid(self, esp_commseq_uuid):
        """Sets the esp_commseq_uuid of this EmailCommseqSmsSendTestRequest.


        :param esp_commseq_uuid: The esp_commseq_uuid of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_uuid = esp_commseq_uuid

    @property
    def send_to_cellphone_e164(self):
        """Gets the send_to_cellphone_e164 of this EmailCommseqSmsSendTestRequest.  # noqa: E501


        :return: The send_to_cellphone_e164 of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_to_cellphone_e164

    @send_to_cellphone_e164.setter
    def send_to_cellphone_e164(self, send_to_cellphone_e164):
        """Sets the send_to_cellphone_e164 of this EmailCommseqSmsSendTestRequest.


        :param send_to_cellphone_e164: The send_to_cellphone_e164 of this EmailCommseqSmsSendTestRequest.  # noqa: E501
        :type: str
        """

        self._send_to_cellphone_e164 = send_to_cellphone_e164

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
        if issubclass(EmailCommseqSmsSendTestRequest, dict):
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
        if not isinstance(other, EmailCommseqSmsSendTestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

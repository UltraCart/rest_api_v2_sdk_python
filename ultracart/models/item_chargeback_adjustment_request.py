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


class ItemChargebackAdjustmentRequest(object):
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
        'chargeback_adjustment_request_oid': 'int',
        'description': 'str',
        'reason_code': 'str'
    }

    attribute_map = {
        'chargeback_adjustment_request_oid': 'chargeback_adjustment_request_oid',
        'description': 'description',
        'reason_code': 'reason_code'
    }

    def __init__(self, chargeback_adjustment_request_oid=None, description=None, reason_code=None):  # noqa: E501
        """ItemChargebackAdjustmentRequest - a model defined in Swagger"""  # noqa: E501

        self._chargeback_adjustment_request_oid = None
        self._description = None
        self._reason_code = None
        self.discriminator = None

        if chargeback_adjustment_request_oid is not None:
            self.chargeback_adjustment_request_oid = chargeback_adjustment_request_oid
        if description is not None:
            self.description = description
        if reason_code is not None:
            self.reason_code = reason_code

    @property
    def chargeback_adjustment_request_oid(self):
        """Gets the chargeback_adjustment_request_oid of this ItemChargebackAdjustmentRequest.  # noqa: E501

        Chargeback adjustment request object identifier  # noqa: E501

        :return: The chargeback_adjustment_request_oid of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._chargeback_adjustment_request_oid

    @chargeback_adjustment_request_oid.setter
    def chargeback_adjustment_request_oid(self, chargeback_adjustment_request_oid):
        """Sets the chargeback_adjustment_request_oid of this ItemChargebackAdjustmentRequest.

        Chargeback adjustment request object identifier  # noqa: E501

        :param chargeback_adjustment_request_oid: The chargeback_adjustment_request_oid of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :type: int
        """

        self._chargeback_adjustment_request_oid = chargeback_adjustment_request_oid

    @property
    def description(self):
        """Gets the description of this ItemChargebackAdjustmentRequest.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemChargebackAdjustmentRequest.

        Description  # noqa: E501

        :param description: The description of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def reason_code(self):
        """Gets the reason_code of this ItemChargebackAdjustmentRequest.  # noqa: E501

        Reason code  # noqa: E501

        :return: The reason_code of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this ItemChargebackAdjustmentRequest.

        Reason code  # noqa: E501

        :param reason_code: The reason_code of this ItemChargebackAdjustmentRequest.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

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
        if issubclass(ItemChargebackAdjustmentRequest, dict):
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
        if not isinstance(other, ItemChargebackAdjustmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

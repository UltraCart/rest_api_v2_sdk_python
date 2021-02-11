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


class CouponPercentOffSubtotalWithSubtotal(object):
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
        'currency_code': 'str',
        'discount_percent': 'float',
        'subtotal_amount': 'float'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'discount_percent': 'discount_percent',
        'subtotal_amount': 'subtotal_amount'
    }

    def __init__(self, currency_code=None, discount_percent=None, subtotal_amount=None):  # noqa: E501
        """CouponPercentOffSubtotalWithSubtotal - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._discount_percent = None
        self._subtotal_amount = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if discount_percent is not None:
            self.discount_percent = discount_percent
        if subtotal_amount is not None:
            self.subtotal_amount = subtotal_amount

    @property
    def currency_code(self):
        """Gets the currency_code of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :return: The currency_code of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CouponPercentOffSubtotalWithSubtotal.

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :param currency_code: The currency_code of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def discount_percent(self):
        """Gets the discount_percent of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501

        The percentage of subtotal discount  # noqa: E501

        :return: The discount_percent of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """Sets the discount_percent of this CouponPercentOffSubtotalWithSubtotal.

        The percentage of subtotal discount  # noqa: E501

        :param discount_percent: The discount_percent of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def subtotal_amount(self):
        """Gets the subtotal_amount of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501

        The amount of subtotal required to receive the discount percent  # noqa: E501

        :return: The subtotal_amount of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :rtype: float
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        """Sets the subtotal_amount of this CouponPercentOffSubtotalWithSubtotal.

        The amount of subtotal required to receive the discount percent  # noqa: E501

        :param subtotal_amount: The subtotal_amount of this CouponPercentOffSubtotalWithSubtotal.  # noqa: E501
        :type: float
        """

        self._subtotal_amount = subtotal_amount

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
        if issubclass(CouponPercentOffSubtotalWithSubtotal, dict):
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
        if not isinstance(other, CouponPercentOffSubtotalWithSubtotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
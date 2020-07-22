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


class OrderGiftCertificate(object):
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
        'gift_certificate_amount': 'Currency',
        'gift_certificate_code': 'str',
        'gift_certificate_oid': 'int'
    }

    attribute_map = {
        'gift_certificate_amount': 'gift_certificate_amount',
        'gift_certificate_code': 'gift_certificate_code',
        'gift_certificate_oid': 'gift_certificate_oid'
    }

    def __init__(self, gift_certificate_amount=None, gift_certificate_code=None, gift_certificate_oid=None):  # noqa: E501
        """OrderGiftCertificate - a model defined in Swagger"""  # noqa: E501

        self._gift_certificate_amount = None
        self._gift_certificate_code = None
        self._gift_certificate_oid = None
        self.discriminator = None

        if gift_certificate_amount is not None:
            self.gift_certificate_amount = gift_certificate_amount
        if gift_certificate_code is not None:
            self.gift_certificate_code = gift_certificate_code
        if gift_certificate_oid is not None:
            self.gift_certificate_oid = gift_certificate_oid

    @property
    def gift_certificate_amount(self):
        """Gets the gift_certificate_amount of this OrderGiftCertificate.  # noqa: E501


        :return: The gift_certificate_amount of this OrderGiftCertificate.  # noqa: E501
        :rtype: Currency
        """
        return self._gift_certificate_amount

    @gift_certificate_amount.setter
    def gift_certificate_amount(self, gift_certificate_amount):
        """Sets the gift_certificate_amount of this OrderGiftCertificate.


        :param gift_certificate_amount: The gift_certificate_amount of this OrderGiftCertificate.  # noqa: E501
        :type: Currency
        """

        self._gift_certificate_amount = gift_certificate_amount

    @property
    def gift_certificate_code(self):
        """Gets the gift_certificate_code of this OrderGiftCertificate.  # noqa: E501

        Gift certificate code used on the order  # noqa: E501

        :return: The gift_certificate_code of this OrderGiftCertificate.  # noqa: E501
        :rtype: str
        """
        return self._gift_certificate_code

    @gift_certificate_code.setter
    def gift_certificate_code(self, gift_certificate_code):
        """Sets the gift_certificate_code of this OrderGiftCertificate.

        Gift certificate code used on the order  # noqa: E501

        :param gift_certificate_code: The gift_certificate_code of this OrderGiftCertificate.  # noqa: E501
        :type: str
        """

        self._gift_certificate_code = gift_certificate_code

    @property
    def gift_certificate_oid(self):
        """Gets the gift_certificate_oid of this OrderGiftCertificate.  # noqa: E501

        Gift certificate object identifier  # noqa: E501

        :return: The gift_certificate_oid of this OrderGiftCertificate.  # noqa: E501
        :rtype: int
        """
        return self._gift_certificate_oid

    @gift_certificate_oid.setter
    def gift_certificate_oid(self, gift_certificate_oid):
        """Sets the gift_certificate_oid of this OrderGiftCertificate.

        Gift certificate object identifier  # noqa: E501

        :param gift_certificate_oid: The gift_certificate_oid of this OrderGiftCertificate.  # noqa: E501
        :type: int
        """

        self._gift_certificate_oid = gift_certificate_oid

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
        if issubclass(OrderGiftCertificate, dict):
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
        if not isinstance(other, OrderGiftCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

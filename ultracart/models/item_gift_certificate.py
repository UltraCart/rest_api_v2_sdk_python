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


class ItemGiftCertificate(object):
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
        'gift_certificate': 'bool',
        'gift_certificate_expiration_days': 'int'
    }

    attribute_map = {
        'gift_certificate': 'gift_certificate',
        'gift_certificate_expiration_days': 'gift_certificate_expiration_days'
    }

    def __init__(self, gift_certificate=None, gift_certificate_expiration_days=None):  # noqa: E501
        """ItemGiftCertificate - a model defined in Swagger"""  # noqa: E501

        self._gift_certificate = None
        self._gift_certificate_expiration_days = None
        self.discriminator = None

        if gift_certificate is not None:
            self.gift_certificate = gift_certificate
        if gift_certificate_expiration_days is not None:
            self.gift_certificate_expiration_days = gift_certificate_expiration_days

    @property
    def gift_certificate(self):
        """Gets the gift_certificate of this ItemGiftCertificate.  # noqa: E501

        True if the purchase of this item generates a gift certificate  # noqa: E501

        :return: The gift_certificate of this ItemGiftCertificate.  # noqa: E501
        :rtype: bool
        """
        return self._gift_certificate

    @gift_certificate.setter
    def gift_certificate(self, gift_certificate):
        """Sets the gift_certificate of this ItemGiftCertificate.

        True if the purchase of this item generates a gift certificate  # noqa: E501

        :param gift_certificate: The gift_certificate of this ItemGiftCertificate.  # noqa: E501
        :type: bool
        """

        self._gift_certificate = gift_certificate

    @property
    def gift_certificate_expiration_days(self):
        """Gets the gift_certificate_expiration_days of this ItemGiftCertificate.  # noqa: E501

        The number of days that the gift certificate is good for (optional)  # noqa: E501

        :return: The gift_certificate_expiration_days of this ItemGiftCertificate.  # noqa: E501
        :rtype: int
        """
        return self._gift_certificate_expiration_days

    @gift_certificate_expiration_days.setter
    def gift_certificate_expiration_days(self, gift_certificate_expiration_days):
        """Sets the gift_certificate_expiration_days of this ItemGiftCertificate.

        The number of days that the gift certificate is good for (optional)  # noqa: E501

        :param gift_certificate_expiration_days: The gift_certificate_expiration_days of this ItemGiftCertificate.  # noqa: E501
        :type: int
        """

        self._gift_certificate_expiration_days = gift_certificate_expiration_days

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
        if issubclass(ItemGiftCertificate, dict):
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
        if not isinstance(other, ItemGiftCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

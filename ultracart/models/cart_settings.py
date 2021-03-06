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


class CartSettings(object):
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
        'billing': 'CartSettingsBilling',
        'gift': 'CartSettingsGift',
        'payment': 'CartSettingsPayment',
        'shipping': 'CartSettingsShipping',
        'taxes': 'CartSettingsTaxes',
        'terms': 'CartSettingsTerms'
    }

    attribute_map = {
        'billing': 'billing',
        'gift': 'gift',
        'payment': 'payment',
        'shipping': 'shipping',
        'taxes': 'taxes',
        'terms': 'terms'
    }

    def __init__(self, billing=None, gift=None, payment=None, shipping=None, taxes=None, terms=None):  # noqa: E501
        """CartSettings - a model defined in Swagger"""  # noqa: E501

        self._billing = None
        self._gift = None
        self._payment = None
        self._shipping = None
        self._taxes = None
        self._terms = None
        self.discriminator = None

        if billing is not None:
            self.billing = billing
        if gift is not None:
            self.gift = gift
        if payment is not None:
            self.payment = payment
        if shipping is not None:
            self.shipping = shipping
        if taxes is not None:
            self.taxes = taxes
        if terms is not None:
            self.terms = terms

    @property
    def billing(self):
        """Gets the billing of this CartSettings.  # noqa: E501


        :return: The billing of this CartSettings.  # noqa: E501
        :rtype: CartSettingsBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this CartSettings.


        :param billing: The billing of this CartSettings.  # noqa: E501
        :type: CartSettingsBilling
        """

        self._billing = billing

    @property
    def gift(self):
        """Gets the gift of this CartSettings.  # noqa: E501


        :return: The gift of this CartSettings.  # noqa: E501
        :rtype: CartSettingsGift
        """
        return self._gift

    @gift.setter
    def gift(self, gift):
        """Sets the gift of this CartSettings.


        :param gift: The gift of this CartSettings.  # noqa: E501
        :type: CartSettingsGift
        """

        self._gift = gift

    @property
    def payment(self):
        """Gets the payment of this CartSettings.  # noqa: E501


        :return: The payment of this CartSettings.  # noqa: E501
        :rtype: CartSettingsPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this CartSettings.


        :param payment: The payment of this CartSettings.  # noqa: E501
        :type: CartSettingsPayment
        """

        self._payment = payment

    @property
    def shipping(self):
        """Gets the shipping of this CartSettings.  # noqa: E501


        :return: The shipping of this CartSettings.  # noqa: E501
        :rtype: CartSettingsShipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this CartSettings.


        :param shipping: The shipping of this CartSettings.  # noqa: E501
        :type: CartSettingsShipping
        """

        self._shipping = shipping

    @property
    def taxes(self):
        """Gets the taxes of this CartSettings.  # noqa: E501


        :return: The taxes of this CartSettings.  # noqa: E501
        :rtype: CartSettingsTaxes
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this CartSettings.


        :param taxes: The taxes of this CartSettings.  # noqa: E501
        :type: CartSettingsTaxes
        """

        self._taxes = taxes

    @property
    def terms(self):
        """Gets the terms of this CartSettings.  # noqa: E501


        :return: The terms of this CartSettings.  # noqa: E501
        :rtype: CartSettingsTerms
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this CartSettings.


        :param terms: The terms of this CartSettings.  # noqa: E501
        :type: CartSettingsTerms
        """

        self._terms = terms

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
        if issubclass(CartSettings, dict):
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
        if not isinstance(other, CartSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ItemPricingTier(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'default_tier': 'bool',
        'discounts': 'list[ItemPricingTierDiscount]',
        'limit': 'ItemPricingTierLimit',
        'name': 'str',
        'pricing_tier_oid': 'int'
    }

    attribute_map = {
        'default_tier': 'default_tier',
        'discounts': 'discounts',
        'limit': 'limit',
        'name': 'name',
        'pricing_tier_oid': 'pricing_tier_oid'
    }

    def __init__(self, default_tier=None, discounts=None, limit=None, name=None, pricing_tier_oid=None):
        """
        ItemPricingTier - a model defined in Swagger
        """

        self._default_tier = None
        self._discounts = None
        self._limit = None
        self._name = None
        self._pricing_tier_oid = None
        self.discriminator = None

        if default_tier is not None:
          self.default_tier = default_tier
        if discounts is not None:
          self.discounts = discounts
        if limit is not None:
          self.limit = limit
        if name is not None:
          self.name = name
        if pricing_tier_oid is not None:
          self.pricing_tier_oid = pricing_tier_oid

    @property
    def default_tier(self):
        """
        Gets the default_tier of this ItemPricingTier.
        True if this is the default tier

        :return: The default_tier of this ItemPricingTier.
        :rtype: bool
        """
        return self._default_tier

    @default_tier.setter
    def default_tier(self, default_tier):
        """
        Sets the default_tier of this ItemPricingTier.
        True if this is the default tier

        :param default_tier: The default_tier of this ItemPricingTier.
        :type: bool
        """

        self._default_tier = default_tier

    @property
    def discounts(self):
        """
        Gets the discounts of this ItemPricingTier.
        Discounts

        :return: The discounts of this ItemPricingTier.
        :rtype: list[ItemPricingTierDiscount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """
        Sets the discounts of this ItemPricingTier.
        Discounts

        :param discounts: The discounts of this ItemPricingTier.
        :type: list[ItemPricingTierDiscount]
        """

        self._discounts = discounts

    @property
    def limit(self):
        """
        Gets the limit of this ItemPricingTier.

        :return: The limit of this ItemPricingTier.
        :rtype: ItemPricingTierLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ItemPricingTier.

        :param limit: The limit of this ItemPricingTier.
        :type: ItemPricingTierLimit
        """

        self._limit = limit

    @property
    def name(self):
        """
        Gets the name of this ItemPricingTier.
        Pricing tier name

        :return: The name of this ItemPricingTier.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ItemPricingTier.
        Pricing tier name

        :param name: The name of this ItemPricingTier.
        :type: str
        """

        self._name = name

    @property
    def pricing_tier_oid(self):
        """
        Gets the pricing_tier_oid of this ItemPricingTier.
        Pricing tier object identifier

        :return: The pricing_tier_oid of this ItemPricingTier.
        :rtype: int
        """
        return self._pricing_tier_oid

    @pricing_tier_oid.setter
    def pricing_tier_oid(self, pricing_tier_oid):
        """
        Sets the pricing_tier_oid of this ItemPricingTier.
        Pricing tier object identifier

        :param pricing_tier_oid: The pricing_tier_oid of this ItemPricingTier.
        :type: int
        """

        self._pricing_tier_oid = pricing_tier_oid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ItemPricingTier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

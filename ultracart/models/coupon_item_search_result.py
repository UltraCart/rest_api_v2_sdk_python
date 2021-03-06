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


class CouponItemSearchResult(object):
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
        'cost': 'str',
        'description': 'str',
        'manufacturer_name': 'str',
        'manufacturer_sku': 'str',
        'merchant_item_id': 'str',
        'merchant_item_oid': 'int',
        'score': 'str',
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'description': 'description',
        'manufacturer_name': 'manufacturer_name',
        'manufacturer_sku': 'manufacturer_sku',
        'merchant_item_id': 'merchant_item_id',
        'merchant_item_oid': 'merchant_item_oid',
        'score': 'score',
        'thumbnail_url': 'thumbnail_url'
    }

    def __init__(self, cost=None, description=None, manufacturer_name=None, manufacturer_sku=None, merchant_item_id=None, merchant_item_oid=None, score=None, thumbnail_url=None):  # noqa: E501
        """CouponItemSearchResult - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._description = None
        self._manufacturer_name = None
        self._manufacturer_sku = None
        self._merchant_item_id = None
        self._merchant_item_oid = None
        self._score = None
        self._thumbnail_url = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if description is not None:
            self.description = description
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if manufacturer_sku is not None:
            self.manufacturer_sku = manufacturer_sku
        if merchant_item_id is not None:
            self.merchant_item_id = merchant_item_id
        if merchant_item_oid is not None:
            self.merchant_item_oid = merchant_item_oid
        if score is not None:
            self.score = score
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url

    @property
    def cost(self):
        """Gets the cost of this CouponItemSearchResult.  # noqa: E501

        The cost of this item.  # noqa: E501

        :return: The cost of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CouponItemSearchResult.

        The cost of this item.  # noqa: E501

        :param cost: The cost of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._cost = cost

    @property
    def description(self):
        """Gets the description of this CouponItemSearchResult.  # noqa: E501

        A human readable description of this item.  # noqa: E501

        :return: The description of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CouponItemSearchResult.

        A human readable description of this item.  # noqa: E501

        :param description: The description of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this CouponItemSearchResult.  # noqa: E501

        The manufacturer of this item.  # noqa: E501

        :return: The manufacturer_name of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this CouponItemSearchResult.

        The manufacturer of this item.  # noqa: E501

        :param manufacturer_name: The manufacturer_name of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._manufacturer_name = manufacturer_name

    @property
    def manufacturer_sku(self):
        """Gets the manufacturer_sku of this CouponItemSearchResult.  # noqa: E501

        The manufacturer sku of this item.  # noqa: E501

        :return: The manufacturer_sku of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_sku

    @manufacturer_sku.setter
    def manufacturer_sku(self, manufacturer_sku):
        """Sets the manufacturer_sku of this CouponItemSearchResult.

        The manufacturer sku of this item.  # noqa: E501

        :param manufacturer_sku: The manufacturer_sku of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._manufacturer_sku = manufacturer_sku

    @property
    def merchant_item_id(self):
        """Gets the merchant_item_id of this CouponItemSearchResult.  # noqa: E501

        The merchant item identifier, which is unique for this merchant, but not across all of UltraCart.  # noqa: E501

        :return: The merchant_item_id of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._merchant_item_id

    @merchant_item_id.setter
    def merchant_item_id(self, merchant_item_id):
        """Sets the merchant_item_id of this CouponItemSearchResult.

        The merchant item identifier, which is unique for this merchant, but not across all of UltraCart.  # noqa: E501

        :param merchant_item_id: The merchant_item_id of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._merchant_item_id = merchant_item_id

    @property
    def merchant_item_oid(self):
        """Gets the merchant_item_oid of this CouponItemSearchResult.  # noqa: E501

        The unique internal identifier used by UltraCart to manage this item.  # noqa: E501

        :return: The merchant_item_oid of this CouponItemSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._merchant_item_oid

    @merchant_item_oid.setter
    def merchant_item_oid(self, merchant_item_oid):
        """Sets the merchant_item_oid of this CouponItemSearchResult.

        The unique internal identifier used by UltraCart to manage this item.  # noqa: E501

        :param merchant_item_oid: The merchant_item_oid of this CouponItemSearchResult.  # noqa: E501
        :type: int
        """

        self._merchant_item_oid = merchant_item_oid

    @property
    def score(self):
        """Gets the score of this CouponItemSearchResult.  # noqa: E501

        The search score of this item.  Larger scores mean more accurate matches against the search term.  # noqa: E501

        :return: The score of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this CouponItemSearchResult.

        The search score of this item.  Larger scores mean more accurate matches against the search term.  # noqa: E501

        :param score: The score of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._score = score

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this CouponItemSearchResult.  # noqa: E501

        A url for displaying a thumbnail of this item  # noqa: E501

        :return: The thumbnail_url of this CouponItemSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this CouponItemSearchResult.

        A url for displaying a thumbnail of this item  # noqa: E501

        :param thumbnail_url: The thumbnail_url of this CouponItemSearchResult.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

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
        if issubclass(CouponItemSearchResult, dict):
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
        if not isinstance(other, CouponItemSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

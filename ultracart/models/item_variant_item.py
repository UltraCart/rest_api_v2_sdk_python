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


class ItemVariantItem(object):
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
        'description': 'str',
        'merchant_item_multimedia_oid': 'int',
        'variant_merchant_item_id': 'str',
        'variant_merchant_item_oid': 'int',
        'variation_options': 'list[str]',
        'variations': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'merchant_item_multimedia_oid': 'merchant_item_multimedia_oid',
        'variant_merchant_item_id': 'variant_merchant_item_id',
        'variant_merchant_item_oid': 'variant_merchant_item_oid',
        'variation_options': 'variation_options',
        'variations': 'variations'
    }

    def __init__(self, description=None, merchant_item_multimedia_oid=None, variant_merchant_item_id=None, variant_merchant_item_oid=None, variation_options=None, variations=None):  # noqa: E501
        """ItemVariantItem - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._merchant_item_multimedia_oid = None
        self._variant_merchant_item_id = None
        self._variant_merchant_item_oid = None
        self._variation_options = None
        self._variations = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if merchant_item_multimedia_oid is not None:
            self.merchant_item_multimedia_oid = merchant_item_multimedia_oid
        if variant_merchant_item_id is not None:
            self.variant_merchant_item_id = variant_merchant_item_id
        if variant_merchant_item_oid is not None:
            self.variant_merchant_item_oid = variant_merchant_item_oid
        if variation_options is not None:
            self.variation_options = variation_options
        if variations is not None:
            self.variations = variations

    @property
    def description(self):
        """Gets the description of this ItemVariantItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ItemVariantItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemVariantItem.

        Description  # noqa: E501

        :param description: The description of this ItemVariantItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 512:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501

        self._description = description

    @property
    def merchant_item_multimedia_oid(self):
        """Gets the merchant_item_multimedia_oid of this ItemVariantItem.  # noqa: E501

        Multimedia object identifier  # noqa: E501

        :return: The merchant_item_multimedia_oid of this ItemVariantItem.  # noqa: E501
        :rtype: int
        """
        return self._merchant_item_multimedia_oid

    @merchant_item_multimedia_oid.setter
    def merchant_item_multimedia_oid(self, merchant_item_multimedia_oid):
        """Sets the merchant_item_multimedia_oid of this ItemVariantItem.

        Multimedia object identifier  # noqa: E501

        :param merchant_item_multimedia_oid: The merchant_item_multimedia_oid of this ItemVariantItem.  # noqa: E501
        :type: int
        """

        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid

    @property
    def variant_merchant_item_id(self):
        """Gets the variant_merchant_item_id of this ItemVariantItem.  # noqa: E501

        Variant item id  # noqa: E501

        :return: The variant_merchant_item_id of this ItemVariantItem.  # noqa: E501
        :rtype: str
        """
        return self._variant_merchant_item_id

    @variant_merchant_item_id.setter
    def variant_merchant_item_id(self, variant_merchant_item_id):
        """Sets the variant_merchant_item_id of this ItemVariantItem.

        Variant item id  # noqa: E501

        :param variant_merchant_item_id: The variant_merchant_item_id of this ItemVariantItem.  # noqa: E501
        :type: str
        """

        self._variant_merchant_item_id = variant_merchant_item_id

    @property
    def variant_merchant_item_oid(self):
        """Gets the variant_merchant_item_oid of this ItemVariantItem.  # noqa: E501

        Variant item object identifier  # noqa: E501

        :return: The variant_merchant_item_oid of this ItemVariantItem.  # noqa: E501
        :rtype: int
        """
        return self._variant_merchant_item_oid

    @variant_merchant_item_oid.setter
    def variant_merchant_item_oid(self, variant_merchant_item_oid):
        """Sets the variant_merchant_item_oid of this ItemVariantItem.

        Variant item object identifier  # noqa: E501

        :param variant_merchant_item_oid: The variant_merchant_item_oid of this ItemVariantItem.  # noqa: E501
        :type: int
        """

        self._variant_merchant_item_oid = variant_merchant_item_oid

    @property
    def variation_options(self):
        """Gets the variation_options of this ItemVariantItem.  # noqa: E501

        Variation options  # noqa: E501

        :return: The variation_options of this ItemVariantItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._variation_options

    @variation_options.setter
    def variation_options(self, variation_options):
        """Sets the variation_options of this ItemVariantItem.

        Variation options  # noqa: E501

        :param variation_options: The variation_options of this ItemVariantItem.  # noqa: E501
        :type: list[str]
        """

        self._variation_options = variation_options

    @property
    def variations(self):
        """Gets the variations of this ItemVariantItem.  # noqa: E501

        Variations  # noqa: E501

        :return: The variations of this ItemVariantItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this ItemVariantItem.

        Variations  # noqa: E501

        :param variations: The variations of this ItemVariantItem.  # noqa: E501
        :type: list[str]
        """

        self._variations = variations

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
        if issubclass(ItemVariantItem, dict):
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
        if not isinstance(other, ItemVariantItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

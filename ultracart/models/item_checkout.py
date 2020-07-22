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


class ItemCheckout(object):
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
        'suppress_buysafe': 'bool',
        'terms': 'str',
        'terms_translated_text_instance_oid': 'int'
    }

    attribute_map = {
        'suppress_buysafe': 'suppress_buysafe',
        'terms': 'terms',
        'terms_translated_text_instance_oid': 'terms_translated_text_instance_oid'
    }

    def __init__(self, suppress_buysafe=None, terms=None, terms_translated_text_instance_oid=None):  # noqa: E501
        """ItemCheckout - a model defined in Swagger"""  # noqa: E501

        self._suppress_buysafe = None
        self._terms = None
        self._terms_translated_text_instance_oid = None
        self.discriminator = None

        if suppress_buysafe is not None:
            self.suppress_buysafe = suppress_buysafe
        if terms is not None:
            self.terms = terms
        if terms_translated_text_instance_oid is not None:
            self.terms_translated_text_instance_oid = terms_translated_text_instance_oid

    @property
    def suppress_buysafe(self):
        """Gets the suppress_buysafe of this ItemCheckout.  # noqa: E501

        True to suppress buySAFE  # noqa: E501

        :return: The suppress_buysafe of this ItemCheckout.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_buysafe

    @suppress_buysafe.setter
    def suppress_buysafe(self, suppress_buysafe):
        """Sets the suppress_buysafe of this ItemCheckout.

        True to suppress buySAFE  # noqa: E501

        :param suppress_buysafe: The suppress_buysafe of this ItemCheckout.  # noqa: E501
        :type: bool
        """

        self._suppress_buysafe = suppress_buysafe

    @property
    def terms(self):
        """Gets the terms of this ItemCheckout.  # noqa: E501

        Terms for purchasing this item  # noqa: E501

        :return: The terms of this ItemCheckout.  # noqa: E501
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this ItemCheckout.

        Terms for purchasing this item  # noqa: E501

        :param terms: The terms of this ItemCheckout.  # noqa: E501
        :type: str
        """
        if terms is not None and len(terms) > 10000:
            raise ValueError("Invalid value for `terms`, length must be less than or equal to `10000`")  # noqa: E501

        self._terms = terms

    @property
    def terms_translated_text_instance_oid(self):
        """Gets the terms_translated_text_instance_oid of this ItemCheckout.  # noqa: E501

        Terms translated text instance identifier  # noqa: E501

        :return: The terms_translated_text_instance_oid of this ItemCheckout.  # noqa: E501
        :rtype: int
        """
        return self._terms_translated_text_instance_oid

    @terms_translated_text_instance_oid.setter
    def terms_translated_text_instance_oid(self, terms_translated_text_instance_oid):
        """Sets the terms_translated_text_instance_oid of this ItemCheckout.

        Terms translated text instance identifier  # noqa: E501

        :param terms_translated_text_instance_oid: The terms_translated_text_instance_oid of this ItemCheckout.  # noqa: E501
        :type: int
        """

        self._terms_translated_text_instance_oid = terms_translated_text_instance_oid

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
        if issubclass(ItemCheckout, dict):
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
        if not isinstance(other, ItemCheckout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

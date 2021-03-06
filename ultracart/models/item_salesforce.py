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


class ItemSalesforce(object):
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
        'sfdc_pricebook_id': 'str',
        'sfdc_product_id': 'str'
    }

    attribute_map = {
        'sfdc_pricebook_id': 'sfdc_pricebook_id',
        'sfdc_product_id': 'sfdc_product_id'
    }

    def __init__(self, sfdc_pricebook_id=None, sfdc_product_id=None):  # noqa: E501
        """ItemSalesforce - a model defined in Swagger"""  # noqa: E501

        self._sfdc_pricebook_id = None
        self._sfdc_product_id = None
        self.discriminator = None

        if sfdc_pricebook_id is not None:
            self.sfdc_pricebook_id = sfdc_pricebook_id
        if sfdc_product_id is not None:
            self.sfdc_product_id = sfdc_product_id

    @property
    def sfdc_pricebook_id(self):
        """Gets the sfdc_pricebook_id of this ItemSalesforce.  # noqa: E501

        Salesforce.com pricebook id  # noqa: E501

        :return: The sfdc_pricebook_id of this ItemSalesforce.  # noqa: E501
        :rtype: str
        """
        return self._sfdc_pricebook_id

    @sfdc_pricebook_id.setter
    def sfdc_pricebook_id(self, sfdc_pricebook_id):
        """Sets the sfdc_pricebook_id of this ItemSalesforce.

        Salesforce.com pricebook id  # noqa: E501

        :param sfdc_pricebook_id: The sfdc_pricebook_id of this ItemSalesforce.  # noqa: E501
        :type: str
        """

        self._sfdc_pricebook_id = sfdc_pricebook_id

    @property
    def sfdc_product_id(self):
        """Gets the sfdc_product_id of this ItemSalesforce.  # noqa: E501

        Salesforce.com product id  # noqa: E501

        :return: The sfdc_product_id of this ItemSalesforce.  # noqa: E501
        :rtype: str
        """
        return self._sfdc_product_id

    @sfdc_product_id.setter
    def sfdc_product_id(self, sfdc_product_id):
        """Sets the sfdc_product_id of this ItemSalesforce.

        Salesforce.com product id  # noqa: E501

        :param sfdc_product_id: The sfdc_product_id of this ItemSalesforce.  # noqa: E501
        :type: str
        """

        self._sfdc_product_id = sfdc_product_id

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
        if issubclass(ItemSalesforce, dict):
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
        if not isinstance(other, ItemSalesforce):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

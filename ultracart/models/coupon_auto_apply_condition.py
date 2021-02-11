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


class CouponAutoApplyCondition(object):
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
        'coupon_code': 'str',
        'minimum_subtotal': 'float',
        'required_item_id': 'str'
    }

    attribute_map = {
        'coupon_code': 'coupon_code',
        'minimum_subtotal': 'minimum_subtotal',
        'required_item_id': 'required_item_id'
    }

    def __init__(self, coupon_code=None, minimum_subtotal=None, required_item_id=None):  # noqa: E501
        """CouponAutoApplyCondition - a model defined in Swagger"""  # noqa: E501

        self._coupon_code = None
        self._minimum_subtotal = None
        self._required_item_id = None
        self.discriminator = None

        if coupon_code is not None:
            self.coupon_code = coupon_code
        if minimum_subtotal is not None:
            self.minimum_subtotal = minimum_subtotal
        if required_item_id is not None:
            self.required_item_id = required_item_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this CouponAutoApplyCondition.  # noqa: E501


        :return: The coupon_code of this CouponAutoApplyCondition.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this CouponAutoApplyCondition.


        :param coupon_code: The coupon_code of this CouponAutoApplyCondition.  # noqa: E501
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def minimum_subtotal(self):
        """Gets the minimum_subtotal of this CouponAutoApplyCondition.  # noqa: E501

        The minimum subtotal that must be purchased to receive this coupon. Item and subtotal are exclusive.  Only one can be populated.  # noqa: E501

        :return: The minimum_subtotal of this CouponAutoApplyCondition.  # noqa: E501
        :rtype: float
        """
        return self._minimum_subtotal

    @minimum_subtotal.setter
    def minimum_subtotal(self, minimum_subtotal):
        """Sets the minimum_subtotal of this CouponAutoApplyCondition.

        The minimum subtotal that must be purchased to receive this coupon. Item and subtotal are exclusive.  Only one can be populated.  # noqa: E501

        :param minimum_subtotal: The minimum_subtotal of this CouponAutoApplyCondition.  # noqa: E501
        :type: float
        """

        self._minimum_subtotal = minimum_subtotal

    @property
    def required_item_id(self):
        """Gets the required_item_id of this CouponAutoApplyCondition.  # noqa: E501

        The item that must be purchased to receive this coupon. Item and subtotal are exclusive.  Only one can be populated.  # noqa: E501

        :return: The required_item_id of this CouponAutoApplyCondition.  # noqa: E501
        :rtype: str
        """
        return self._required_item_id

    @required_item_id.setter
    def required_item_id(self, required_item_id):
        """Sets the required_item_id of this CouponAutoApplyCondition.

        The item that must be purchased to receive this coupon. Item and subtotal are exclusive.  Only one can be populated.  # noqa: E501

        :param required_item_id: The required_item_id of this CouponAutoApplyCondition.  # noqa: E501
        :type: str
        """

        self._required_item_id = required_item_id

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
        if issubclass(CouponAutoApplyCondition, dict):
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
        if not isinstance(other, CouponAutoApplyCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
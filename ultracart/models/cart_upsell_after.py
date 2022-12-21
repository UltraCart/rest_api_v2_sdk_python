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


class CartUpsellAfter(object):
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
        'finalize_after_dts': 'str',
        'finalize_after_minutes': 'int',
        'upsell_path_code': 'str'
    }

    attribute_map = {
        'finalize_after_dts': 'finalize_after_dts',
        'finalize_after_minutes': 'finalize_after_minutes',
        'upsell_path_code': 'upsell_path_code'
    }

    def __init__(self, finalize_after_dts=None, finalize_after_minutes=None, upsell_path_code=None):  # noqa: E501
        """CartUpsellAfter - a model defined in Swagger"""  # noqa: E501

        self._finalize_after_dts = None
        self._finalize_after_minutes = None
        self._upsell_path_code = None
        self.discriminator = None

        if finalize_after_dts is not None:
            self.finalize_after_dts = finalize_after_dts
        if finalize_after_minutes is not None:
            self.finalize_after_minutes = finalize_after_minutes
        if upsell_path_code is not None:
            self.upsell_path_code = upsell_path_code

    @property
    def finalize_after_dts(self):
        """Gets the finalize_after_dts of this CartUpsellAfter.  # noqa: E501

        The date/time after which the cart will finalize into an order.  # noqa: E501

        :return: The finalize_after_dts of this CartUpsellAfter.  # noqa: E501
        :rtype: str
        """
        return self._finalize_after_dts

    @finalize_after_dts.setter
    def finalize_after_dts(self, finalize_after_dts):
        """Sets the finalize_after_dts of this CartUpsellAfter.

        The date/time after which the cart will finalize into an order.  # noqa: E501

        :param finalize_after_dts: The finalize_after_dts of this CartUpsellAfter.  # noqa: E501
        :type: str
        """

        self._finalize_after_dts = finalize_after_dts

    @property
    def finalize_after_minutes(self):
        """Gets the finalize_after_minutes of this CartUpsellAfter.  # noqa: E501

        The amount of inactivity in minutes after which the cart should be finalized into an order.  This will calculate the finalize_after_dts field.  # noqa: E501

        :return: The finalize_after_minutes of this CartUpsellAfter.  # noqa: E501
        :rtype: int
        """
        return self._finalize_after_minutes

    @finalize_after_minutes.setter
    def finalize_after_minutes(self, finalize_after_minutes):
        """Sets the finalize_after_minutes of this CartUpsellAfter.

        The amount of inactivity in minutes after which the cart should be finalized into an order.  This will calculate the finalize_after_dts field.  # noqa: E501

        :param finalize_after_minutes: The finalize_after_minutes of this CartUpsellAfter.  # noqa: E501
        :type: int
        """

        self._finalize_after_minutes = finalize_after_minutes

    @property
    def upsell_path_code(self):
        """Gets the upsell_path_code of this CartUpsellAfter.  # noqa: E501

        Upsell path code  # noqa: E501

        :return: The upsell_path_code of this CartUpsellAfter.  # noqa: E501
        :rtype: str
        """
        return self._upsell_path_code

    @upsell_path_code.setter
    def upsell_path_code(self, upsell_path_code):
        """Sets the upsell_path_code of this CartUpsellAfter.

        Upsell path code  # noqa: E501

        :param upsell_path_code: The upsell_path_code of this CartUpsellAfter.  # noqa: E501
        :type: str
        """
        if upsell_path_code is not None and len(upsell_path_code) > 5:
            raise ValueError("Invalid value for `upsell_path_code`, length must be less than or equal to `5`")  # noqa: E501

        self._upsell_path_code = upsell_path_code

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
        if issubclass(CartUpsellAfter, dict):
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
        if not isinstance(other, CartUpsellAfter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
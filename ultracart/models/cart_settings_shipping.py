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


class CartSettingsShipping(object):
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
        'deliver_on_date': 'CartSettingsShippingCalendar',
        'estimates': 'list[CartSettingsShippingEstimate]',
        'need_shipping': 'bool',
        'provinces': 'list[CartSettingsProvince]',
        'ship_on_date': 'CartSettingsShippingCalendar'
    }

    attribute_map = {
        'deliver_on_date': 'deliver_on_date',
        'estimates': 'estimates',
        'need_shipping': 'need_shipping',
        'provinces': 'provinces',
        'ship_on_date': 'ship_on_date'
    }

    def __init__(self, deliver_on_date=None, estimates=None, need_shipping=None, provinces=None, ship_on_date=None):  # noqa: E501
        """CartSettingsShipping - a model defined in Swagger"""  # noqa: E501

        self._deliver_on_date = None
        self._estimates = None
        self._need_shipping = None
        self._provinces = None
        self._ship_on_date = None
        self.discriminator = None

        if deliver_on_date is not None:
            self.deliver_on_date = deliver_on_date
        if estimates is not None:
            self.estimates = estimates
        if need_shipping is not None:
            self.need_shipping = need_shipping
        if provinces is not None:
            self.provinces = provinces
        if ship_on_date is not None:
            self.ship_on_date = ship_on_date

    @property
    def deliver_on_date(self):
        """Gets the deliver_on_date of this CartSettingsShipping.  # noqa: E501


        :return: The deliver_on_date of this CartSettingsShipping.  # noqa: E501
        :rtype: CartSettingsShippingCalendar
        """
        return self._deliver_on_date

    @deliver_on_date.setter
    def deliver_on_date(self, deliver_on_date):
        """Sets the deliver_on_date of this CartSettingsShipping.


        :param deliver_on_date: The deliver_on_date of this CartSettingsShipping.  # noqa: E501
        :type: CartSettingsShippingCalendar
        """

        self._deliver_on_date = deliver_on_date

    @property
    def estimates(self):
        """Gets the estimates of this CartSettingsShipping.  # noqa: E501

        Estimates for this cart  # noqa: E501

        :return: The estimates of this CartSettingsShipping.  # noqa: E501
        :rtype: list[CartSettingsShippingEstimate]
        """
        return self._estimates

    @estimates.setter
    def estimates(self, estimates):
        """Sets the estimates of this CartSettingsShipping.

        Estimates for this cart  # noqa: E501

        :param estimates: The estimates of this CartSettingsShipping.  # noqa: E501
        :type: list[CartSettingsShippingEstimate]
        """

        self._estimates = estimates

    @property
    def need_shipping(self):
        """Gets the need_shipping of this CartSettingsShipping.  # noqa: E501

        True if this order needs shipping  # noqa: E501

        :return: The need_shipping of this CartSettingsShipping.  # noqa: E501
        :rtype: bool
        """
        return self._need_shipping

    @need_shipping.setter
    def need_shipping(self, need_shipping):
        """Sets the need_shipping of this CartSettingsShipping.

        True if this order needs shipping  # noqa: E501

        :param need_shipping: The need_shipping of this CartSettingsShipping.  # noqa: E501
        :type: bool
        """

        self._need_shipping = need_shipping

    @property
    def provinces(self):
        """Gets the provinces of this CartSettingsShipping.  # noqa: E501

        Provinces  # noqa: E501

        :return: The provinces of this CartSettingsShipping.  # noqa: E501
        :rtype: list[CartSettingsProvince]
        """
        return self._provinces

    @provinces.setter
    def provinces(self, provinces):
        """Sets the provinces of this CartSettingsShipping.

        Provinces  # noqa: E501

        :param provinces: The provinces of this CartSettingsShipping.  # noqa: E501
        :type: list[CartSettingsProvince]
        """

        self._provinces = provinces

    @property
    def ship_on_date(self):
        """Gets the ship_on_date of this CartSettingsShipping.  # noqa: E501


        :return: The ship_on_date of this CartSettingsShipping.  # noqa: E501
        :rtype: CartSettingsShippingCalendar
        """
        return self._ship_on_date

    @ship_on_date.setter
    def ship_on_date(self, ship_on_date):
        """Sets the ship_on_date of this CartSettingsShipping.


        :param ship_on_date: The ship_on_date of this CartSettingsShipping.  # noqa: E501
        :type: CartSettingsShippingCalendar
        """

        self._ship_on_date = ship_on_date

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
        if issubclass(CartSettingsShipping, dict):
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
        if not isinstance(other, CartSettingsShipping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
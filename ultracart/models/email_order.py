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


class EmailOrder(object):
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
        'email': 'str',
        'order_dts': 'str',
        'order_id': 'str',
        'total': 'Currency'
    }

    attribute_map = {
        'email': 'email',
        'order_dts': 'order_dts',
        'order_id': 'order_id',
        'total': 'total'
    }

    def __init__(self, email=None, order_dts=None, order_id=None, total=None):  # noqa: E501
        """EmailOrder - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._order_dts = None
        self._order_id = None
        self._total = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if order_dts is not None:
            self.order_dts = order_dts
        if order_id is not None:
            self.order_id = order_id
        if total is not None:
            self.total = total

    @property
    def email(self):
        """Gets the email of this EmailOrder.  # noqa: E501

        email  # noqa: E501

        :return: The email of this EmailOrder.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmailOrder.

        email  # noqa: E501

        :param email: The email of this EmailOrder.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def order_dts(self):
        """Gets the order_dts of this EmailOrder.  # noqa: E501

        order_dts  # noqa: E501

        :return: The order_dts of this EmailOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_dts

    @order_dts.setter
    def order_dts(self, order_dts):
        """Sets the order_dts of this EmailOrder.

        order_dts  # noqa: E501

        :param order_dts: The order_dts of this EmailOrder.  # noqa: E501
        :type: str
        """

        self._order_dts = order_dts

    @property
    def order_id(self):
        """Gets the order_id of this EmailOrder.  # noqa: E501

        order_id  # noqa: E501

        :return: The order_id of this EmailOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this EmailOrder.

        order_id  # noqa: E501

        :param order_id: The order_id of this EmailOrder.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def total(self):
        """Gets the total of this EmailOrder.  # noqa: E501


        :return: The total of this EmailOrder.  # noqa: E501
        :rtype: Currency
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EmailOrder.


        :param total: The total of this EmailOrder.  # noqa: E501
        :type: Currency
        """

        self._total = total

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
        if issubclass(EmailOrder, dict):
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
        if not isinstance(other, EmailOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

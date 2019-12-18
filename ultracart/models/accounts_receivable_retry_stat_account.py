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


class AccountsReceivableRetryStatAccount(object):
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
        'days': 'list[AccountsReceivableRetryStatMetrics]',
        'merchant_id': 'str',
        'overall': 'AccountsReceivableRetryStatMetrics',
        'revenue_for_period': 'list[AccountsReceivableRetryStatRevenue]'
    }

    attribute_map = {
        'days': 'days',
        'merchant_id': 'merchant_id',
        'overall': 'overall',
        'revenue_for_period': 'revenue_for_period'
    }

    def __init__(self, days=None, merchant_id=None, overall=None, revenue_for_period=None):
        """
        AccountsReceivableRetryStatAccount - a model defined in Swagger
        """

        self._days = None
        self._merchant_id = None
        self._overall = None
        self._revenue_for_period = None
        self.discriminator = None

        if days is not None:
          self.days = days
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if overall is not None:
          self.overall = overall
        if revenue_for_period is not None:
          self.revenue_for_period = revenue_for_period

    @property
    def days(self):
        """
        Gets the days of this AccountsReceivableRetryStatAccount.

        :return: The days of this AccountsReceivableRetryStatAccount.
        :rtype: list[AccountsReceivableRetryStatMetrics]
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this AccountsReceivableRetryStatAccount.

        :param days: The days of this AccountsReceivableRetryStatAccount.
        :type: list[AccountsReceivableRetryStatMetrics]
        """

        self._days = days

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this AccountsReceivableRetryStatAccount.

        :return: The merchant_id of this AccountsReceivableRetryStatAccount.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this AccountsReceivableRetryStatAccount.

        :param merchant_id: The merchant_id of this AccountsReceivableRetryStatAccount.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def overall(self):
        """
        Gets the overall of this AccountsReceivableRetryStatAccount.

        :return: The overall of this AccountsReceivableRetryStatAccount.
        :rtype: AccountsReceivableRetryStatMetrics
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """
        Sets the overall of this AccountsReceivableRetryStatAccount.

        :param overall: The overall of this AccountsReceivableRetryStatAccount.
        :type: AccountsReceivableRetryStatMetrics
        """

        self._overall = overall

    @property
    def revenue_for_period(self):
        """
        Gets the revenue_for_period of this AccountsReceivableRetryStatAccount.

        :return: The revenue_for_period of this AccountsReceivableRetryStatAccount.
        :rtype: list[AccountsReceivableRetryStatRevenue]
        """
        return self._revenue_for_period

    @revenue_for_period.setter
    def revenue_for_period(self, revenue_for_period):
        """
        Sets the revenue_for_period of this AccountsReceivableRetryStatAccount.

        :param revenue_for_period: The revenue_for_period of this AccountsReceivableRetryStatAccount.
        :type: list[AccountsReceivableRetryStatRevenue]
        """

        self._revenue_for_period = revenue_for_period

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
        if not isinstance(other, AccountsReceivableRetryStatAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

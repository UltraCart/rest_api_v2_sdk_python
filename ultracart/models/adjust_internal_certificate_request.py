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


class AdjustInternalCertificateRequest(object):
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
        'adjustment_amount': 'float',
        'description': 'str',
        'entry_dts': 'str',
        'expiration_days': 'int',
        'order_id': 'str',
        'vesting_days': 'int'
    }

    attribute_map = {
        'adjustment_amount': 'adjustment_amount',
        'description': 'description',
        'entry_dts': 'entry_dts',
        'expiration_days': 'expiration_days',
        'order_id': 'order_id',
        'vesting_days': 'vesting_days'
    }

    def __init__(self, adjustment_amount=None, description=None, entry_dts=None, expiration_days=None, order_id=None, vesting_days=None):  # noqa: E501
        """AdjustInternalCertificateRequest - a model defined in Swagger"""  # noqa: E501

        self._adjustment_amount = None
        self._description = None
        self._entry_dts = None
        self._expiration_days = None
        self._order_id = None
        self._vesting_days = None
        self.discriminator = None

        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if description is not None:
            self.description = description
        if entry_dts is not None:
            self.entry_dts = entry_dts
        if expiration_days is not None:
            self.expiration_days = expiration_days
        if order_id is not None:
            self.order_id = order_id
        if vesting_days is not None:
            self.vesting_days = vesting_days

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this AdjustInternalCertificateRequest.  # noqa: E501

        The adjustment amount  # noqa: E501

        :return: The adjustment_amount of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this AdjustInternalCertificateRequest.

        The adjustment amount  # noqa: E501

        :param adjustment_amount: The adjustment_amount of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: float
        """

        self._adjustment_amount = adjustment_amount

    @property
    def description(self):
        """Gets the description of this AdjustInternalCertificateRequest.  # noqa: E501

        Description of this adjustment, 50 characters max  # noqa: E501

        :return: The description of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdjustInternalCertificateRequest.

        Description of this adjustment, 50 characters max  # noqa: E501

        :param description: The description of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entry_dts(self):
        """Gets the entry_dts of this AdjustInternalCertificateRequest.  # noqa: E501

        Optional timestamp for the adjustment, defaults to current time  # noqa: E501

        :return: The entry_dts of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._entry_dts

    @entry_dts.setter
    def entry_dts(self, entry_dts):
        """Sets the entry_dts of this AdjustInternalCertificateRequest.

        Optional timestamp for the adjustment, defaults to current time  # noqa: E501

        :param entry_dts: The entry_dts of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: str
        """

        self._entry_dts = entry_dts

    @property
    def expiration_days(self):
        """Gets the expiration_days of this AdjustInternalCertificateRequest.  # noqa: E501

        Optional expiration days from the entry_dts when these adjustment becomes worthless  # noqa: E501

        :return: The expiration_days of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_days

    @expiration_days.setter
    def expiration_days(self, expiration_days):
        """Sets the expiration_days of this AdjustInternalCertificateRequest.

        Optional expiration days from the entry_dts when these adjustment becomes worthless  # noqa: E501

        :param expiration_days: The expiration_days of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: int
        """

        self._expiration_days = expiration_days

    @property
    def order_id(self):
        """Gets the order_id of this AdjustInternalCertificateRequest.  # noqa: E501

        Optional order id if this adjustment is related to a particular order  # noqa: E501

        :return: The order_id of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this AdjustInternalCertificateRequest.

        Optional order id if this adjustment is related to a particular order  # noqa: E501

        :param order_id: The order_id of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def vesting_days(self):
        """Gets the vesting_days of this AdjustInternalCertificateRequest.  # noqa: E501

        Optional days required for this adjustment to vest  # noqa: E501

        :return: The vesting_days of this AdjustInternalCertificateRequest.  # noqa: E501
        :rtype: int
        """
        return self._vesting_days

    @vesting_days.setter
    def vesting_days(self, vesting_days):
        """Sets the vesting_days of this AdjustInternalCertificateRequest.

        Optional days required for this adjustment to vest  # noqa: E501

        :param vesting_days: The vesting_days of this AdjustInternalCertificateRequest.  # noqa: E501
        :type: int
        """

        self._vesting_days = vesting_days

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
        if issubclass(AdjustInternalCertificateRequest, dict):
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
        if not isinstance(other, AdjustInternalCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

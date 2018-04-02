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


class ItemAccounting(object):
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
        'accounting_code': 'str',
        'qb_class': 'str'
    }

    attribute_map = {
        'accounting_code': 'accounting_code',
        'qb_class': 'qb_class'
    }

    def __init__(self, accounting_code=None, qb_class=None):
        """
        ItemAccounting - a model defined in Swagger
        """

        self._accounting_code = None
        self._qb_class = None
        self.discriminator = None

        if accounting_code is not None:
          self.accounting_code = accounting_code
        if qb_class is not None:
          self.qb_class = qb_class

    @property
    def accounting_code(self):
        """
        Gets the accounting_code of this ItemAccounting.
        QuickBooks item name if different than the item id

        :return: The accounting_code of this ItemAccounting.
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """
        Sets the accounting_code of this ItemAccounting.
        QuickBooks item name if different than the item id

        :param accounting_code: The accounting_code of this ItemAccounting.
        :type: str
        """
        if accounting_code is not None and len(accounting_code) > 50:
            raise ValueError("Invalid value for `accounting_code`, length must be less than or equal to `50`")

        self._accounting_code = accounting_code

    @property
    def qb_class(self):
        """
        Gets the qb_class of this ItemAccounting.
        QuickBooks class if you are classifying items on your invoices/receipts

        :return: The qb_class of this ItemAccounting.
        :rtype: str
        """
        return self._qb_class

    @qb_class.setter
    def qb_class(self, qb_class):
        """
        Sets the qb_class of this ItemAccounting.
        QuickBooks class if you are classifying items on your invoices/receipts

        :param qb_class: The qb_class of this ItemAccounting.
        :type: str
        """
        if qb_class is not None and len(qb_class) > 31:
            raise ValueError("Invalid value for `qb_class`, length must be less than or equal to `31`")

        self._qb_class = qb_class

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
        if not isinstance(other, ItemAccounting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

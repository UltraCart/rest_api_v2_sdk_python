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


class OrderInternal(object):
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
        'exported_to_accounting': 'bool',
        'merchant_notes': 'str',
        'placed_by_user': 'str',
        'refund_by_user': 'str',
        'sales_rep_code': 'str',
        'transactional_merchant_notes': 'list[OrderTransactionalMerchantNote]'
    }

    attribute_map = {
        'exported_to_accounting': 'exported_to_accounting',
        'merchant_notes': 'merchant_notes',
        'placed_by_user': 'placed_by_user',
        'refund_by_user': 'refund_by_user',
        'sales_rep_code': 'sales_rep_code',
        'transactional_merchant_notes': 'transactional_merchant_notes'
    }

    def __init__(self, exported_to_accounting=None, merchant_notes=None, placed_by_user=None, refund_by_user=None, sales_rep_code=None, transactional_merchant_notes=None):  # noqa: E501
        """OrderInternal - a model defined in Swagger"""  # noqa: E501

        self._exported_to_accounting = None
        self._merchant_notes = None
        self._placed_by_user = None
        self._refund_by_user = None
        self._sales_rep_code = None
        self._transactional_merchant_notes = None
        self.discriminator = None

        if exported_to_accounting is not None:
            self.exported_to_accounting = exported_to_accounting
        if merchant_notes is not None:
            self.merchant_notes = merchant_notes
        if placed_by_user is not None:
            self.placed_by_user = placed_by_user
        if refund_by_user is not None:
            self.refund_by_user = refund_by_user
        if sales_rep_code is not None:
            self.sales_rep_code = sales_rep_code
        if transactional_merchant_notes is not None:
            self.transactional_merchant_notes = transactional_merchant_notes

    @property
    def exported_to_accounting(self):
        """Gets the exported_to_accounting of this OrderInternal.  # noqa: E501

        True if the order has been exported to QuickBooks. If QuickBooks is not configured, then this will already be true  # noqa: E501

        :return: The exported_to_accounting of this OrderInternal.  # noqa: E501
        :rtype: bool
        """
        return self._exported_to_accounting

    @exported_to_accounting.setter
    def exported_to_accounting(self, exported_to_accounting):
        """Sets the exported_to_accounting of this OrderInternal.

        True if the order has been exported to QuickBooks. If QuickBooks is not configured, then this will already be true  # noqa: E501

        :param exported_to_accounting: The exported_to_accounting of this OrderInternal.  # noqa: E501
        :type: bool
        """

        self._exported_to_accounting = exported_to_accounting

    @property
    def merchant_notes(self):
        """Gets the merchant_notes of this OrderInternal.  # noqa: E501

        Merchant notes.  Full notes in non-transactional mode.  Just used to write a new merchant note when transaction merchant notes enabled.  # noqa: E501

        :return: The merchant_notes of this OrderInternal.  # noqa: E501
        :rtype: str
        """
        return self._merchant_notes

    @merchant_notes.setter
    def merchant_notes(self, merchant_notes):
        """Sets the merchant_notes of this OrderInternal.

        Merchant notes.  Full notes in non-transactional mode.  Just used to write a new merchant note when transaction merchant notes enabled.  # noqa: E501

        :param merchant_notes: The merchant_notes of this OrderInternal.  # noqa: E501
        :type: str
        """

        self._merchant_notes = merchant_notes

    @property
    def placed_by_user(self):
        """Gets the placed_by_user of this OrderInternal.  # noqa: E501

        If placed via the BEOE, this is the user that placed the order  # noqa: E501

        :return: The placed_by_user of this OrderInternal.  # noqa: E501
        :rtype: str
        """
        return self._placed_by_user

    @placed_by_user.setter
    def placed_by_user(self, placed_by_user):
        """Sets the placed_by_user of this OrderInternal.

        If placed via the BEOE, this is the user that placed the order  # noqa: E501

        :param placed_by_user: The placed_by_user of this OrderInternal.  # noqa: E501
        :type: str
        """

        self._placed_by_user = placed_by_user

    @property
    def refund_by_user(self):
        """Gets the refund_by_user of this OrderInternal.  # noqa: E501

        User that issued the refund  # noqa: E501

        :return: The refund_by_user of this OrderInternal.  # noqa: E501
        :rtype: str
        """
        return self._refund_by_user

    @refund_by_user.setter
    def refund_by_user(self, refund_by_user):
        """Sets the refund_by_user of this OrderInternal.

        User that issued the refund  # noqa: E501

        :param refund_by_user: The refund_by_user of this OrderInternal.  # noqa: E501
        :type: str
        """

        self._refund_by_user = refund_by_user

    @property
    def sales_rep_code(self):
        """Gets the sales_rep_code of this OrderInternal.  # noqa: E501

        Sales rep code associated with the order  # noqa: E501

        :return: The sales_rep_code of this OrderInternal.  # noqa: E501
        :rtype: str
        """
        return self._sales_rep_code

    @sales_rep_code.setter
    def sales_rep_code(self, sales_rep_code):
        """Sets the sales_rep_code of this OrderInternal.

        Sales rep code associated with the order  # noqa: E501

        :param sales_rep_code: The sales_rep_code of this OrderInternal.  # noqa: E501
        :type: str
        """
        if sales_rep_code is not None and len(sales_rep_code) > 10:
            raise ValueError("Invalid value for `sales_rep_code`, length must be less than or equal to `10`")  # noqa: E501

        self._sales_rep_code = sales_rep_code

    @property
    def transactional_merchant_notes(self):
        """Gets the transactional_merchant_notes of this OrderInternal.  # noqa: E501

        Transactional merchant notes  # noqa: E501

        :return: The transactional_merchant_notes of this OrderInternal.  # noqa: E501
        :rtype: list[OrderTransactionalMerchantNote]
        """
        return self._transactional_merchant_notes

    @transactional_merchant_notes.setter
    def transactional_merchant_notes(self, transactional_merchant_notes):
        """Sets the transactional_merchant_notes of this OrderInternal.

        Transactional merchant notes  # noqa: E501

        :param transactional_merchant_notes: The transactional_merchant_notes of this OrderInternal.  # noqa: E501
        :type: list[OrderTransactionalMerchantNote]
        """

        self._transactional_merchant_notes = transactional_merchant_notes

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
        if issubclass(OrderInternal, dict):
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
        if not isinstance(other, OrderInternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class ItemPaymentProcessing(object):
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
        'block_prepaid': 'bool',
        'credit_card_transaction_type': 'str',
        'no_realtime_charge': 'bool',
        'payment_method_validity': 'list[str]',
        'rotating_transaction_gateway_codes': 'list[str]'
    }

    attribute_map = {
        'block_prepaid': 'block_prepaid',
        'credit_card_transaction_type': 'credit_card_transaction_type',
        'no_realtime_charge': 'no_realtime_charge',
        'payment_method_validity': 'payment_method_validity',
        'rotating_transaction_gateway_codes': 'rotating_transaction_gateway_codes'
    }

    def __init__(self, block_prepaid=None, credit_card_transaction_type=None, no_realtime_charge=None, payment_method_validity=None, rotating_transaction_gateway_codes=None):  # noqa: E501
        """ItemPaymentProcessing - a model defined in Swagger"""  # noqa: E501

        self._block_prepaid = None
        self._credit_card_transaction_type = None
        self._no_realtime_charge = None
        self._payment_method_validity = None
        self._rotating_transaction_gateway_codes = None
        self.discriminator = None

        if block_prepaid is not None:
            self.block_prepaid = block_prepaid
        if credit_card_transaction_type is not None:
            self.credit_card_transaction_type = credit_card_transaction_type
        if no_realtime_charge is not None:
            self.no_realtime_charge = no_realtime_charge
        if payment_method_validity is not None:
            self.payment_method_validity = payment_method_validity
        if rotating_transaction_gateway_codes is not None:
            self.rotating_transaction_gateway_codes = rotating_transaction_gateway_codes

    @property
    def block_prepaid(self):
        """Gets the block_prepaid of this ItemPaymentProcessing.  # noqa: E501

        True if prepaid cards should be blocked from buying this item  # noqa: E501

        :return: The block_prepaid of this ItemPaymentProcessing.  # noqa: E501
        :rtype: bool
        """
        return self._block_prepaid

    @block_prepaid.setter
    def block_prepaid(self, block_prepaid):
        """Sets the block_prepaid of this ItemPaymentProcessing.

        True if prepaid cards should be blocked from buying this item  # noqa: E501

        :param block_prepaid: The block_prepaid of this ItemPaymentProcessing.  # noqa: E501
        :type: bool
        """

        self._block_prepaid = block_prepaid

    @property
    def credit_card_transaction_type(self):
        """Gets the credit_card_transaction_type of this ItemPaymentProcessing.  # noqa: E501

        Credit card transaction type  # noqa: E501

        :return: The credit_card_transaction_type of this ItemPaymentProcessing.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_transaction_type

    @credit_card_transaction_type.setter
    def credit_card_transaction_type(self, credit_card_transaction_type):
        """Sets the credit_card_transaction_type of this ItemPaymentProcessing.

        Credit card transaction type  # noqa: E501

        :param credit_card_transaction_type: The credit_card_transaction_type of this ItemPaymentProcessing.  # noqa: E501
        :type: str
        """

        self._credit_card_transaction_type = credit_card_transaction_type

    @property
    def no_realtime_charge(self):
        """Gets the no_realtime_charge of this ItemPaymentProcessing.  # noqa: E501

        True if no real-time charge should be performed on this item.  # noqa: E501

        :return: The no_realtime_charge of this ItemPaymentProcessing.  # noqa: E501
        :rtype: bool
        """
        return self._no_realtime_charge

    @no_realtime_charge.setter
    def no_realtime_charge(self, no_realtime_charge):
        """Sets the no_realtime_charge of this ItemPaymentProcessing.

        True if no real-time charge should be performed on this item.  # noqa: E501

        :param no_realtime_charge: The no_realtime_charge of this ItemPaymentProcessing.  # noqa: E501
        :type: bool
        """

        self._no_realtime_charge = no_realtime_charge

    @property
    def payment_method_validity(self):
        """Gets the payment_method_validity of this ItemPaymentProcessing.  # noqa: E501

        Payment method validity  # noqa: E501

        :return: The payment_method_validity of this ItemPaymentProcessing.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_method_validity

    @payment_method_validity.setter
    def payment_method_validity(self, payment_method_validity):
        """Sets the payment_method_validity of this ItemPaymentProcessing.

        Payment method validity  # noqa: E501

        :param payment_method_validity: The payment_method_validity of this ItemPaymentProcessing.  # noqa: E501
        :type: list[str]
        """

        self._payment_method_validity = payment_method_validity

    @property
    def rotating_transaction_gateway_codes(self):
        """Gets the rotating_transaction_gateway_codes of this ItemPaymentProcessing.  # noqa: E501

        Rotating transaction gateway codes  # noqa: E501

        :return: The rotating_transaction_gateway_codes of this ItemPaymentProcessing.  # noqa: E501
        :rtype: list[str]
        """
        return self._rotating_transaction_gateway_codes

    @rotating_transaction_gateway_codes.setter
    def rotating_transaction_gateway_codes(self, rotating_transaction_gateway_codes):
        """Sets the rotating_transaction_gateway_codes of this ItemPaymentProcessing.

        Rotating transaction gateway codes  # noqa: E501

        :param rotating_transaction_gateway_codes: The rotating_transaction_gateway_codes of this ItemPaymentProcessing.  # noqa: E501
        :type: list[str]
        """

        self._rotating_transaction_gateway_codes = rotating_transaction_gateway_codes

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
        if issubclass(ItemPaymentProcessing, dict):
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
        if not isinstance(other, ItemPaymentProcessing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
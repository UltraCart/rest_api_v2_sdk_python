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


class OrderPaymentCreditCard(object):
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
        'card_auth_ticket': 'str',
        'card_authorization_amount': 'float',
        'card_authorization_dts': 'str',
        'card_authorization_reference_number': 'str',
        'card_expiration_month': 'int',
        'card_expiration_year': 'int',
        'card_number': 'str',
        'card_number_token': 'str',
        'card_number_truncated': 'bool',
        'card_type': 'str',
        'card_verification_number_token': 'str',
        'dual_vaulted': 'OrderPaymentCreditCardDualVaulted'
    }

    attribute_map = {
        'card_auth_ticket': 'card_auth_ticket',
        'card_authorization_amount': 'card_authorization_amount',
        'card_authorization_dts': 'card_authorization_dts',
        'card_authorization_reference_number': 'card_authorization_reference_number',
        'card_expiration_month': 'card_expiration_month',
        'card_expiration_year': 'card_expiration_year',
        'card_number': 'card_number',
        'card_number_token': 'card_number_token',
        'card_number_truncated': 'card_number_truncated',
        'card_type': 'card_type',
        'card_verification_number_token': 'card_verification_number_token',
        'dual_vaulted': 'dual_vaulted'
    }

    def __init__(self, card_auth_ticket=None, card_authorization_amount=None, card_authorization_dts=None, card_authorization_reference_number=None, card_expiration_month=None, card_expiration_year=None, card_number=None, card_number_token=None, card_number_truncated=None, card_type=None, card_verification_number_token=None, dual_vaulted=None):  # noqa: E501
        """OrderPaymentCreditCard - a model defined in Swagger"""  # noqa: E501

        self._card_auth_ticket = None
        self._card_authorization_amount = None
        self._card_authorization_dts = None
        self._card_authorization_reference_number = None
        self._card_expiration_month = None
        self._card_expiration_year = None
        self._card_number = None
        self._card_number_token = None
        self._card_number_truncated = None
        self._card_type = None
        self._card_verification_number_token = None
        self._dual_vaulted = None
        self.discriminator = None

        if card_auth_ticket is not None:
            self.card_auth_ticket = card_auth_ticket
        if card_authorization_amount is not None:
            self.card_authorization_amount = card_authorization_amount
        if card_authorization_dts is not None:
            self.card_authorization_dts = card_authorization_dts
        if card_authorization_reference_number is not None:
            self.card_authorization_reference_number = card_authorization_reference_number
        if card_expiration_month is not None:
            self.card_expiration_month = card_expiration_month
        if card_expiration_year is not None:
            self.card_expiration_year = card_expiration_year
        if card_number is not None:
            self.card_number = card_number
        if card_number_token is not None:
            self.card_number_token = card_number_token
        if card_number_truncated is not None:
            self.card_number_truncated = card_number_truncated
        if card_type is not None:
            self.card_type = card_type
        if card_verification_number_token is not None:
            self.card_verification_number_token = card_verification_number_token
        if dual_vaulted is not None:
            self.dual_vaulted = dual_vaulted

    @property
    def card_auth_ticket(self):
        """Gets the card_auth_ticket of this OrderPaymentCreditCard.  # noqa: E501

        Card authorization ticket  # noqa: E501

        :return: The card_auth_ticket of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_auth_ticket

    @card_auth_ticket.setter
    def card_auth_ticket(self, card_auth_ticket):
        """Sets the card_auth_ticket of this OrderPaymentCreditCard.

        Card authorization ticket  # noqa: E501

        :param card_auth_ticket: The card_auth_ticket of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_auth_ticket = card_auth_ticket

    @property
    def card_authorization_amount(self):
        """Gets the card_authorization_amount of this OrderPaymentCreditCard.  # noqa: E501

        Card authorization amount  # noqa: E501

        :return: The card_authorization_amount of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: float
        """
        return self._card_authorization_amount

    @card_authorization_amount.setter
    def card_authorization_amount(self, card_authorization_amount):
        """Sets the card_authorization_amount of this OrderPaymentCreditCard.

        Card authorization amount  # noqa: E501

        :param card_authorization_amount: The card_authorization_amount of this OrderPaymentCreditCard.  # noqa: E501
        :type: float
        """

        self._card_authorization_amount = card_authorization_amount

    @property
    def card_authorization_dts(self):
        """Gets the card_authorization_dts of this OrderPaymentCreditCard.  # noqa: E501

        Card authorization date/time  # noqa: E501

        :return: The card_authorization_dts of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_authorization_dts

    @card_authorization_dts.setter
    def card_authorization_dts(self, card_authorization_dts):
        """Sets the card_authorization_dts of this OrderPaymentCreditCard.

        Card authorization date/time  # noqa: E501

        :param card_authorization_dts: The card_authorization_dts of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_authorization_dts = card_authorization_dts

    @property
    def card_authorization_reference_number(self):
        """Gets the card_authorization_reference_number of this OrderPaymentCreditCard.  # noqa: E501

        Card authorization reference number  # noqa: E501

        :return: The card_authorization_reference_number of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_authorization_reference_number

    @card_authorization_reference_number.setter
    def card_authorization_reference_number(self, card_authorization_reference_number):
        """Sets the card_authorization_reference_number of this OrderPaymentCreditCard.

        Card authorization reference number  # noqa: E501

        :param card_authorization_reference_number: The card_authorization_reference_number of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_authorization_reference_number = card_authorization_reference_number

    @property
    def card_expiration_month(self):
        """Gets the card_expiration_month of this OrderPaymentCreditCard.  # noqa: E501

        Card expiration month (1-12)  # noqa: E501

        :return: The card_expiration_month of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._card_expiration_month

    @card_expiration_month.setter
    def card_expiration_month(self, card_expiration_month):
        """Sets the card_expiration_month of this OrderPaymentCreditCard.

        Card expiration month (1-12)  # noqa: E501

        :param card_expiration_month: The card_expiration_month of this OrderPaymentCreditCard.  # noqa: E501
        :type: int
        """

        self._card_expiration_month = card_expiration_month

    @property
    def card_expiration_year(self):
        """Gets the card_expiration_year of this OrderPaymentCreditCard.  # noqa: E501

        Card expiration year (Four digit year)  # noqa: E501

        :return: The card_expiration_year of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._card_expiration_year

    @card_expiration_year.setter
    def card_expiration_year(self, card_expiration_year):
        """Sets the card_expiration_year of this OrderPaymentCreditCard.

        Card expiration year (Four digit year)  # noqa: E501

        :param card_expiration_year: The card_expiration_year of this OrderPaymentCreditCard.  # noqa: E501
        :type: int
        """

        self._card_expiration_year = card_expiration_year

    @property
    def card_number(self):
        """Gets the card_number of this OrderPaymentCreditCard.  # noqa: E501

        Card number (masked to last 4)  # noqa: E501

        :return: The card_number of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this OrderPaymentCreditCard.

        Card number (masked to last 4)  # noqa: E501

        :param card_number: The card_number of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def card_number_token(self):
        """Gets the card_number_token of this OrderPaymentCreditCard.  # noqa: E501

        Card number token from hosted fields used to update the card number  # noqa: E501

        :return: The card_number_token of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number_token

    @card_number_token.setter
    def card_number_token(self, card_number_token):
        """Sets the card_number_token of this OrderPaymentCreditCard.

        Card number token from hosted fields used to update the card number  # noqa: E501

        :param card_number_token: The card_number_token of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_number_token = card_number_token

    @property
    def card_number_truncated(self):
        """Gets the card_number_truncated of this OrderPaymentCreditCard.  # noqa: E501

        True if the card has been truncated  # noqa: E501

        :return: The card_number_truncated of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._card_number_truncated

    @card_number_truncated.setter
    def card_number_truncated(self, card_number_truncated):
        """Sets the card_number_truncated of this OrderPaymentCreditCard.

        True if the card has been truncated  # noqa: E501

        :param card_number_truncated: The card_number_truncated of this OrderPaymentCreditCard.  # noqa: E501
        :type: bool
        """

        self._card_number_truncated = card_number_truncated

    @property
    def card_type(self):
        """Gets the card_type of this OrderPaymentCreditCard.  # noqa: E501

        Card type  # noqa: E501

        :return: The card_type of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this OrderPaymentCreditCard.

        Card type  # noqa: E501

        :param card_type: The card_type of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMEX", "Diners Club", "Discover", "JCB", "MasterCard", "VISA"]  # noqa: E501
        if card_type not in allowed_values:
            raise ValueError(
                "Invalid value for `card_type` ({0}), must be one of {1}"  # noqa: E501
                .format(card_type, allowed_values)
            )

        self._card_type = card_type

    @property
    def card_verification_number_token(self):
        """Gets the card_verification_number_token of this OrderPaymentCreditCard.  # noqa: E501

        Card verification number token from hosted fields, only for import/insert of new orders, completely ignored for updates, and always null/empty for queries  # noqa: E501

        :return: The card_verification_number_token of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_verification_number_token

    @card_verification_number_token.setter
    def card_verification_number_token(self, card_verification_number_token):
        """Sets the card_verification_number_token of this OrderPaymentCreditCard.

        Card verification number token from hosted fields, only for import/insert of new orders, completely ignored for updates, and always null/empty for queries  # noqa: E501

        :param card_verification_number_token: The card_verification_number_token of this OrderPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_verification_number_token = card_verification_number_token

    @property
    def dual_vaulted(self):
        """Gets the dual_vaulted of this OrderPaymentCreditCard.  # noqa: E501


        :return: The dual_vaulted of this OrderPaymentCreditCard.  # noqa: E501
        :rtype: OrderPaymentCreditCardDualVaulted
        """
        return self._dual_vaulted

    @dual_vaulted.setter
    def dual_vaulted(self, dual_vaulted):
        """Sets the dual_vaulted of this OrderPaymentCreditCard.


        :param dual_vaulted: The dual_vaulted of this OrderPaymentCreditCard.  # noqa: E501
        :type: OrderPaymentCreditCardDualVaulted
        """

        self._dual_vaulted = dual_vaulted

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
        if issubclass(OrderPaymentCreditCard, dict):
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
        if not isinstance(other, OrderPaymentCreditCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

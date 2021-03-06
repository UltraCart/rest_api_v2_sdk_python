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


class CartPaymentCreditCard(object):
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
        'card_expiration_month': 'int',
        'card_expiration_year': 'int',
        'card_number': 'str',
        'card_number_token': 'str',
        'card_type': 'str',
        'card_verification_number': 'str',
        'card_verification_number_token': 'str',
        'customer_profile_credit_card_id': 'int',
        'store_credit_card': 'bool'
    }

    attribute_map = {
        'card_expiration_month': 'card_expiration_month',
        'card_expiration_year': 'card_expiration_year',
        'card_number': 'card_number',
        'card_number_token': 'card_number_token',
        'card_type': 'card_type',
        'card_verification_number': 'card_verification_number',
        'card_verification_number_token': 'card_verification_number_token',
        'customer_profile_credit_card_id': 'customer_profile_credit_card_id',
        'store_credit_card': 'store_credit_card'
    }

    def __init__(self, card_expiration_month=None, card_expiration_year=None, card_number=None, card_number_token=None, card_type=None, card_verification_number=None, card_verification_number_token=None, customer_profile_credit_card_id=None, store_credit_card=None):  # noqa: E501
        """CartPaymentCreditCard - a model defined in Swagger"""  # noqa: E501

        self._card_expiration_month = None
        self._card_expiration_year = None
        self._card_number = None
        self._card_number_token = None
        self._card_type = None
        self._card_verification_number = None
        self._card_verification_number_token = None
        self._customer_profile_credit_card_id = None
        self._store_credit_card = None
        self.discriminator = None

        if card_expiration_month is not None:
            self.card_expiration_month = card_expiration_month
        if card_expiration_year is not None:
            self.card_expiration_year = card_expiration_year
        if card_number is not None:
            self.card_number = card_number
        if card_number_token is not None:
            self.card_number_token = card_number_token
        if card_type is not None:
            self.card_type = card_type
        if card_verification_number is not None:
            self.card_verification_number = card_verification_number
        if card_verification_number_token is not None:
            self.card_verification_number_token = card_verification_number_token
        if customer_profile_credit_card_id is not None:
            self.customer_profile_credit_card_id = customer_profile_credit_card_id
        if store_credit_card is not None:
            self.store_credit_card = store_credit_card

    @property
    def card_expiration_month(self):
        """Gets the card_expiration_month of this CartPaymentCreditCard.  # noqa: E501

        Card expiration month (1-12)  # noqa: E501

        :return: The card_expiration_month of this CartPaymentCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._card_expiration_month

    @card_expiration_month.setter
    def card_expiration_month(self, card_expiration_month):
        """Sets the card_expiration_month of this CartPaymentCreditCard.

        Card expiration month (1-12)  # noqa: E501

        :param card_expiration_month: The card_expiration_month of this CartPaymentCreditCard.  # noqa: E501
        :type: int
        """

        self._card_expiration_month = card_expiration_month

    @property
    def card_expiration_year(self):
        """Gets the card_expiration_year of this CartPaymentCreditCard.  # noqa: E501

        Card expiration year (four digit year)  # noqa: E501

        :return: The card_expiration_year of this CartPaymentCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._card_expiration_year

    @card_expiration_year.setter
    def card_expiration_year(self, card_expiration_year):
        """Sets the card_expiration_year of this CartPaymentCreditCard.

        Card expiration year (four digit year)  # noqa: E501

        :param card_expiration_year: The card_expiration_year of this CartPaymentCreditCard.  # noqa: E501
        :type: int
        """

        self._card_expiration_year = card_expiration_year

    @property
    def card_number(self):
        """Gets the card_number of this CartPaymentCreditCard.  # noqa: E501

        Card number (masked to the last 4)  # noqa: E501

        :return: The card_number of this CartPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this CartPaymentCreditCard.

        Card number (masked to the last 4)  # noqa: E501

        :param card_number: The card_number of this CartPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def card_number_token(self):
        """Gets the card_number_token of this CartPaymentCreditCard.  # noqa: E501

        Hosted field token for the card number  # noqa: E501

        :return: The card_number_token of this CartPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number_token

    @card_number_token.setter
    def card_number_token(self, card_number_token):
        """Sets the card_number_token of this CartPaymentCreditCard.

        Hosted field token for the card number  # noqa: E501

        :param card_number_token: The card_number_token of this CartPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_number_token = card_number_token

    @property
    def card_type(self):
        """Gets the card_type of this CartPaymentCreditCard.  # noqa: E501

        Card type  # noqa: E501

        :return: The card_type of this CartPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CartPaymentCreditCard.

        Card type  # noqa: E501

        :param card_type: The card_type of this CartPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def card_verification_number(self):
        """Gets the card_verification_number of this CartPaymentCreditCard.  # noqa: E501

        Card verification number (masked)  # noqa: E501

        :return: The card_verification_number of this CartPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_verification_number

    @card_verification_number.setter
    def card_verification_number(self, card_verification_number):
        """Sets the card_verification_number of this CartPaymentCreditCard.

        Card verification number (masked)  # noqa: E501

        :param card_verification_number: The card_verification_number of this CartPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_verification_number = card_verification_number

    @property
    def card_verification_number_token(self):
        """Gets the card_verification_number_token of this CartPaymentCreditCard.  # noqa: E501

        Hosted field token for the card verification number  # noqa: E501

        :return: The card_verification_number_token of this CartPaymentCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._card_verification_number_token

    @card_verification_number_token.setter
    def card_verification_number_token(self, card_verification_number_token):
        """Sets the card_verification_number_token of this CartPaymentCreditCard.

        Hosted field token for the card verification number  # noqa: E501

        :param card_verification_number_token: The card_verification_number_token of this CartPaymentCreditCard.  # noqa: E501
        :type: str
        """

        self._card_verification_number_token = card_verification_number_token

    @property
    def customer_profile_credit_card_id(self):
        """Gets the customer_profile_credit_card_id of this CartPaymentCreditCard.  # noqa: E501

        ID of the stored credit card to use  # noqa: E501

        :return: The customer_profile_credit_card_id of this CartPaymentCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_credit_card_id

    @customer_profile_credit_card_id.setter
    def customer_profile_credit_card_id(self, customer_profile_credit_card_id):
        """Sets the customer_profile_credit_card_id of this CartPaymentCreditCard.

        ID of the stored credit card to use  # noqa: E501

        :param customer_profile_credit_card_id: The customer_profile_credit_card_id of this CartPaymentCreditCard.  # noqa: E501
        :type: int
        """

        self._customer_profile_credit_card_id = customer_profile_credit_card_id

    @property
    def store_credit_card(self):
        """Gets the store_credit_card of this CartPaymentCreditCard.  # noqa: E501

        True if the customer wants to store the card on their profile for future re-use  # noqa: E501

        :return: The store_credit_card of this CartPaymentCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._store_credit_card

    @store_credit_card.setter
    def store_credit_card(self, store_credit_card):
        """Sets the store_credit_card of this CartPaymentCreditCard.

        True if the customer wants to store the card on their profile for future re-use  # noqa: E501

        :param store_credit_card: The store_credit_card of this CartPaymentCreditCard.  # noqa: E501
        :type: bool
        """

        self._store_credit_card = store_credit_card

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
        if issubclass(CartPaymentCreditCard, dict):
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
        if not isinstance(other, CartPaymentCreditCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

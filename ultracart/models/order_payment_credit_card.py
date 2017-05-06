# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class OrderPaymentCreditCard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, card_auth_ticket=None, card_authorization_amount=None, card_authorization_dts=None, card_authorization_reference_number=None, card_expiration_month=None, card_expiration_year=None, card_number=None, card_number_token=None, card_number_truncated=None, card_type=None):
        """
        OrderPaymentCreditCard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'card_auth_ticket': 'str',
            'card_authorization_amount': 'float',
            'card_authorization_dts': 'str',
            'card_authorization_reference_number': 'str',
            'card_expiration_month': 'int',
            'card_expiration_year': 'int',
            'card_number': 'str',
            'card_number_token': 'str',
            'card_number_truncated': 'bool',
            'card_type': 'str'
        }

        self.attribute_map = {
            'card_auth_ticket': 'card_auth_ticket',
            'card_authorization_amount': 'card_authorization_amount',
            'card_authorization_dts': 'card_authorization_dts',
            'card_authorization_reference_number': 'card_authorization_reference_number',
            'card_expiration_month': 'card_expiration_month',
            'card_expiration_year': 'card_expiration_year',
            'card_number': 'card_number',
            'card_number_token': 'card_number_token',
            'card_number_truncated': 'card_number_truncated',
            'card_type': 'card_type'
        }

        self._card_auth_ticket = card_auth_ticket
        self._card_authorization_amount = card_authorization_amount
        self._card_authorization_dts = card_authorization_dts
        self._card_authorization_reference_number = card_authorization_reference_number
        self._card_expiration_month = card_expiration_month
        self._card_expiration_year = card_expiration_year
        self._card_number = card_number
        self._card_number_token = card_number_token
        self._card_number_truncated = card_number_truncated
        self._card_type = card_type

    @property
    def card_auth_ticket(self):
        """
        Gets the card_auth_ticket of this OrderPaymentCreditCard.
        Card authorization ticket

        :return: The card_auth_ticket of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_auth_ticket

    @card_auth_ticket.setter
    def card_auth_ticket(self, card_auth_ticket):
        """
        Sets the card_auth_ticket of this OrderPaymentCreditCard.
        Card authorization ticket

        :param card_auth_ticket: The card_auth_ticket of this OrderPaymentCreditCard.
        :type: str
        """

        self._card_auth_ticket = card_auth_ticket

    @property
    def card_authorization_amount(self):
        """
        Gets the card_authorization_amount of this OrderPaymentCreditCard.
        Card authorization amount

        :return: The card_authorization_amount of this OrderPaymentCreditCard.
        :rtype: float
        """
        return self._card_authorization_amount

    @card_authorization_amount.setter
    def card_authorization_amount(self, card_authorization_amount):
        """
        Sets the card_authorization_amount of this OrderPaymentCreditCard.
        Card authorization amount

        :param card_authorization_amount: The card_authorization_amount of this OrderPaymentCreditCard.
        :type: float
        """

        self._card_authorization_amount = card_authorization_amount

    @property
    def card_authorization_dts(self):
        """
        Gets the card_authorization_dts of this OrderPaymentCreditCard.
        Card authorization date/time

        :return: The card_authorization_dts of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_authorization_dts

    @card_authorization_dts.setter
    def card_authorization_dts(self, card_authorization_dts):
        """
        Sets the card_authorization_dts of this OrderPaymentCreditCard.
        Card authorization date/time

        :param card_authorization_dts: The card_authorization_dts of this OrderPaymentCreditCard.
        :type: str
        """

        self._card_authorization_dts = card_authorization_dts

    @property
    def card_authorization_reference_number(self):
        """
        Gets the card_authorization_reference_number of this OrderPaymentCreditCard.
        Card authorization reference number

        :return: The card_authorization_reference_number of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_authorization_reference_number

    @card_authorization_reference_number.setter
    def card_authorization_reference_number(self, card_authorization_reference_number):
        """
        Sets the card_authorization_reference_number of this OrderPaymentCreditCard.
        Card authorization reference number

        :param card_authorization_reference_number: The card_authorization_reference_number of this OrderPaymentCreditCard.
        :type: str
        """

        self._card_authorization_reference_number = card_authorization_reference_number

    @property
    def card_expiration_month(self):
        """
        Gets the card_expiration_month of this OrderPaymentCreditCard.
        Card expiration month (1-12)

        :return: The card_expiration_month of this OrderPaymentCreditCard.
        :rtype: int
        """
        return self._card_expiration_month

    @card_expiration_month.setter
    def card_expiration_month(self, card_expiration_month):
        """
        Sets the card_expiration_month of this OrderPaymentCreditCard.
        Card expiration month (1-12)

        :param card_expiration_month: The card_expiration_month of this OrderPaymentCreditCard.
        :type: int
        """

        self._card_expiration_month = card_expiration_month

    @property
    def card_expiration_year(self):
        """
        Gets the card_expiration_year of this OrderPaymentCreditCard.
        Card expiration year (Four digit year)

        :return: The card_expiration_year of this OrderPaymentCreditCard.
        :rtype: int
        """
        return self._card_expiration_year

    @card_expiration_year.setter
    def card_expiration_year(self, card_expiration_year):
        """
        Sets the card_expiration_year of this OrderPaymentCreditCard.
        Card expiration year (Four digit year)

        :param card_expiration_year: The card_expiration_year of this OrderPaymentCreditCard.
        :type: int
        """

        self._card_expiration_year = card_expiration_year

    @property
    def card_number(self):
        """
        Gets the card_number of this OrderPaymentCreditCard.
        Card number (masked to last 4)

        :return: The card_number of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """
        Sets the card_number of this OrderPaymentCreditCard.
        Card number (masked to last 4)

        :param card_number: The card_number of this OrderPaymentCreditCard.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_number_token(self):
        """
        Gets the card_number_token of this OrderPaymentCreditCard.
        Card number token from hosted fields used to update the cart number

        :return: The card_number_token of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_number_token

    @card_number_token.setter
    def card_number_token(self, card_number_token):
        """
        Sets the card_number_token of this OrderPaymentCreditCard.
        Card number token from hosted fields used to update the cart number

        :param card_number_token: The card_number_token of this OrderPaymentCreditCard.
        :type: str
        """

        self._card_number_token = card_number_token

    @property
    def card_number_truncated(self):
        """
        Gets the card_number_truncated of this OrderPaymentCreditCard.
        True if the card has been truncated

        :return: The card_number_truncated of this OrderPaymentCreditCard.
        :rtype: bool
        """
        return self._card_number_truncated

    @card_number_truncated.setter
    def card_number_truncated(self, card_number_truncated):
        """
        Sets the card_number_truncated of this OrderPaymentCreditCard.
        True if the card has been truncated

        :param card_number_truncated: The card_number_truncated of this OrderPaymentCreditCard.
        :type: bool
        """

        self._card_number_truncated = card_number_truncated

    @property
    def card_type(self):
        """
        Gets the card_type of this OrderPaymentCreditCard.
        Card type

        :return: The card_type of this OrderPaymentCreditCard.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this OrderPaymentCreditCard.
        Card type

        :param card_type: The card_type of this OrderPaymentCreditCard.
        :type: str
        """
        allowed_values = ["AMEX", "Diners Club", "Discover", "JCB", "MasterCard", "VISA", "Visa"]
        if card_type not in allowed_values:
            raise ValueError(
                "Invalid value for `card_type` ({0}), must be one of {1}"
                .format(card_type, allowed_values)
            )

        self._card_type = card_type

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

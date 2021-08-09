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


class PaymentsConfigurationCreditCard(object):
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
        'accept_credit_card': 'bool',
        'billed_by': 'str',
        'charge_during_checkout': 'bool',
        'collect_cvv2': 'bool',
        'configured_gateway_details': 'str',
        'failed_attempts': 'int',
        'hide_connect_single_gateway': 'bool',
        'restrictions': 'list[PaymentsConfigurationRestrictions]',
        'send_customer_billing_update_on_decline': 'bool',
        'supported_cards': 'list[PaymentsConfigurationCreditCardType]',
        'test_methods': 'list[PaymentsConfigurationTestMethod]'
    }

    attribute_map = {
        'accept_credit_card': 'accept_credit_card',
        'billed_by': 'billed_by',
        'charge_during_checkout': 'charge_during_checkout',
        'collect_cvv2': 'collect_cvv2',
        'configured_gateway_details': 'configured_gateway_details',
        'failed_attempts': 'failed_attempts',
        'hide_connect_single_gateway': 'hide_connect_single_gateway',
        'restrictions': 'restrictions',
        'send_customer_billing_update_on_decline': 'send_customer_billing_update_on_decline',
        'supported_cards': 'supported_cards',
        'test_methods': 'test_methods'
    }

    def __init__(self, accept_credit_card=None, billed_by=None, charge_during_checkout=None, collect_cvv2=None, configured_gateway_details=None, failed_attempts=None, hide_connect_single_gateway=None, restrictions=None, send_customer_billing_update_on_decline=None, supported_cards=None, test_methods=None):  # noqa: E501
        """PaymentsConfigurationCreditCard - a model defined in Swagger"""  # noqa: E501

        self._accept_credit_card = None
        self._billed_by = None
        self._charge_during_checkout = None
        self._collect_cvv2 = None
        self._configured_gateway_details = None
        self._failed_attempts = None
        self._hide_connect_single_gateway = None
        self._restrictions = None
        self._send_customer_billing_update_on_decline = None
        self._supported_cards = None
        self._test_methods = None
        self.discriminator = None

        if accept_credit_card is not None:
            self.accept_credit_card = accept_credit_card
        if billed_by is not None:
            self.billed_by = billed_by
        if charge_during_checkout is not None:
            self.charge_during_checkout = charge_during_checkout
        if collect_cvv2 is not None:
            self.collect_cvv2 = collect_cvv2
        if configured_gateway_details is not None:
            self.configured_gateway_details = configured_gateway_details
        if failed_attempts is not None:
            self.failed_attempts = failed_attempts
        if hide_connect_single_gateway is not None:
            self.hide_connect_single_gateway = hide_connect_single_gateway
        if restrictions is not None:
            self.restrictions = restrictions
        if send_customer_billing_update_on_decline is not None:
            self.send_customer_billing_update_on_decline = send_customer_billing_update_on_decline
        if supported_cards is not None:
            self.supported_cards = supported_cards
        if test_methods is not None:
            self.test_methods = test_methods

    @property
    def accept_credit_card(self):
        """Gets the accept_credit_card of this PaymentsConfigurationCreditCard.  # noqa: E501

        Master flag indicating whether this merchant accepts credit card payments  # noqa: E501

        :return: The accept_credit_card of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._accept_credit_card

    @accept_credit_card.setter
    def accept_credit_card(self, accept_credit_card):
        """Sets the accept_credit_card of this PaymentsConfigurationCreditCard.

        Master flag indicating whether this merchant accepts credit card payments  # noqa: E501

        :param accept_credit_card: The accept_credit_card of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: bool
        """

        self._accept_credit_card = accept_credit_card

    @property
    def billed_by(self):
        """Gets the billed_by of this PaymentsConfigurationCreditCard.  # noqa: E501

        Description that appears on customer statements  # noqa: E501

        :return: The billed_by of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._billed_by

    @billed_by.setter
    def billed_by(self, billed_by):
        """Sets the billed_by of this PaymentsConfigurationCreditCard.

        Description that appears on customer statements  # noqa: E501

        :param billed_by: The billed_by of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: str
        """

        self._billed_by = billed_by

    @property
    def charge_during_checkout(self):
        """Gets the charge_during_checkout of this PaymentsConfigurationCreditCard.  # noqa: E501

        If false, order will be accepted and placed into Accounts Receivable without charging card first  # noqa: E501

        :return: The charge_during_checkout of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._charge_during_checkout

    @charge_during_checkout.setter
    def charge_during_checkout(self, charge_during_checkout):
        """Sets the charge_during_checkout of this PaymentsConfigurationCreditCard.

        If false, order will be accepted and placed into Accounts Receivable without charging card first  # noqa: E501

        :param charge_during_checkout: The charge_during_checkout of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: bool
        """

        self._charge_during_checkout = charge_during_checkout

    @property
    def collect_cvv2(self):
        """Gets the collect_cvv2 of this PaymentsConfigurationCreditCard.  # noqa: E501

        UltraCart will require customer to enter cvv if this is true  # noqa: E501

        :return: The collect_cvv2 of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._collect_cvv2

    @collect_cvv2.setter
    def collect_cvv2(self, collect_cvv2):
        """Sets the collect_cvv2 of this PaymentsConfigurationCreditCard.

        UltraCart will require customer to enter cvv if this is true  # noqa: E501

        :param collect_cvv2: The collect_cvv2 of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: bool
        """

        self._collect_cvv2 = collect_cvv2

    @property
    def configured_gateway_details(self):
        """Gets the configured_gateway_details of this PaymentsConfigurationCreditCard.  # noqa: E501

        Human readable description of the credit card gateway currently configured  # noqa: E501

        :return: The configured_gateway_details of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._configured_gateway_details

    @configured_gateway_details.setter
    def configured_gateway_details(self, configured_gateway_details):
        """Sets the configured_gateway_details of this PaymentsConfigurationCreditCard.

        Human readable description of the credit card gateway currently configured  # noqa: E501

        :param configured_gateway_details: The configured_gateway_details of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: str
        """

        self._configured_gateway_details = configured_gateway_details

    @property
    def failed_attempts(self):
        """Gets the failed_attempts of this PaymentsConfigurationCreditCard.  # noqa: E501

        The number of failed attempts before the order is placed into Accounts Receivable for manual intervention  # noqa: E501

        :return: The failed_attempts of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: int
        """
        return self._failed_attempts

    @failed_attempts.setter
    def failed_attempts(self, failed_attempts):
        """Sets the failed_attempts of this PaymentsConfigurationCreditCard.

        The number of failed attempts before the order is placed into Accounts Receivable for manual intervention  # noqa: E501

        :param failed_attempts: The failed_attempts of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: int
        """

        self._failed_attempts = failed_attempts

    @property
    def hide_connect_single_gateway(self):
        """Gets the hide_connect_single_gateway of this PaymentsConfigurationCreditCard.  # noqa: E501

        This internal flag aids the UI in determining which buttons to show.  # noqa: E501

        :return: The hide_connect_single_gateway of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._hide_connect_single_gateway

    @hide_connect_single_gateway.setter
    def hide_connect_single_gateway(self, hide_connect_single_gateway):
        """Sets the hide_connect_single_gateway of this PaymentsConfigurationCreditCard.

        This internal flag aids the UI in determining which buttons to show.  # noqa: E501

        :param hide_connect_single_gateway: The hide_connect_single_gateway of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: bool
        """

        self._hide_connect_single_gateway = hide_connect_single_gateway

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationCreditCard.  # noqa: E501

        Restrictions for this payment method  # noqa: E501

        :return: The restrictions of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: list[PaymentsConfigurationRestrictions]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationCreditCard.

        Restrictions for this payment method  # noqa: E501

        :param restrictions: The restrictions of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: list[PaymentsConfigurationRestrictions]
        """

        self._restrictions = restrictions

    @property
    def send_customer_billing_update_on_decline(self):
        """Gets the send_customer_billing_update_on_decline of this PaymentsConfigurationCreditCard.  # noqa: E501

        UltraCart will send customers emails to update their credit card if the card is declined  # noqa: E501

        :return: The send_customer_billing_update_on_decline of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: bool
        """
        return self._send_customer_billing_update_on_decline

    @send_customer_billing_update_on_decline.setter
    def send_customer_billing_update_on_decline(self, send_customer_billing_update_on_decline):
        """Sets the send_customer_billing_update_on_decline of this PaymentsConfigurationCreditCard.

        UltraCart will send customers emails to update their credit card if the card is declined  # noqa: E501

        :param send_customer_billing_update_on_decline: The send_customer_billing_update_on_decline of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: bool
        """

        self._send_customer_billing_update_on_decline = send_customer_billing_update_on_decline

    @property
    def supported_cards(self):
        """Gets the supported_cards of this PaymentsConfigurationCreditCard.  # noqa: E501

        A list of credit cards the merchant wishes to accept.  # noqa: E501

        :return: The supported_cards of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: list[PaymentsConfigurationCreditCardType]
        """
        return self._supported_cards

    @supported_cards.setter
    def supported_cards(self, supported_cards):
        """Sets the supported_cards of this PaymentsConfigurationCreditCard.

        A list of credit cards the merchant wishes to accept.  # noqa: E501

        :param supported_cards: The supported_cards of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: list[PaymentsConfigurationCreditCardType]
        """

        self._supported_cards = supported_cards

    @property
    def test_methods(self):
        """Gets the test_methods of this PaymentsConfigurationCreditCard.  # noqa: E501

        An array of test methods for placing test orders.  The cards defined here may be real or fake, but any order placed with them will be marked as Test orders  # noqa: E501

        :return: The test_methods of this PaymentsConfigurationCreditCard.  # noqa: E501
        :rtype: list[PaymentsConfigurationTestMethod]
        """
        return self._test_methods

    @test_methods.setter
    def test_methods(self, test_methods):
        """Sets the test_methods of this PaymentsConfigurationCreditCard.

        An array of test methods for placing test orders.  The cards defined here may be real or fake, but any order placed with them will be marked as Test orders  # noqa: E501

        :param test_methods: The test_methods of this PaymentsConfigurationCreditCard.  # noqa: E501
        :type: list[PaymentsConfigurationTestMethod]
        """

        self._test_methods = test_methods

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
        if issubclass(PaymentsConfigurationCreditCard, dict):
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
        if not isinstance(other, PaymentsConfigurationCreditCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

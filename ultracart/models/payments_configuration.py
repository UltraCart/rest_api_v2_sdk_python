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


class PaymentsConfiguration(object):
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
        'affirm': 'PaymentsConfigurationAffirm',
        'amazon': 'PaymentsConfigurationAmazon',
        'cash': 'PaymentsConfigurationCash',
        'check': 'PaymentsConfigurationCheck',
        'cod': 'PaymentsConfigurationCOD',
        'credit_card': 'PaymentsConfigurationCreditCard',
        'echeck': 'PaymentsConfigurationEcheck',
        'loan_hero': 'PaymentsConfigurationLoanHero',
        'money_order': 'PaymentsConfigurationMoneyOrder',
        'paypal': 'PaymentsConfigurationPayPal',
        'purchase_order': 'PaymentsConfigurationPurchaseOrder',
        'quote_request': 'PaymentsConfigurationQuoteRequest',
        'sezzle': 'PaymentsConfigurationSezzle',
        'show_accounting_code': 'bool',
        'switch_to_sub_tab': 'str',
        'switch_to_tab': 'str',
        'ultracart_payments_wepay': 'PaymentsConfigurationWePay',
        'wire_transfer': 'PaymentsConfigurationWireTransfer'
    }

    attribute_map = {
        'affirm': 'affirm',
        'amazon': 'amazon',
        'cash': 'cash',
        'check': 'check',
        'cod': 'cod',
        'credit_card': 'credit_card',
        'echeck': 'echeck',
        'loan_hero': 'loan_hero',
        'money_order': 'money_order',
        'paypal': 'paypal',
        'purchase_order': 'purchase_order',
        'quote_request': 'quote_request',
        'sezzle': 'sezzle',
        'show_accounting_code': 'show_accounting_code',
        'switch_to_sub_tab': 'switchToSubTab',
        'switch_to_tab': 'switchToTab',
        'ultracart_payments_wepay': 'ultracart_payments_wepay',
        'wire_transfer': 'wire_transfer'
    }

    def __init__(self, affirm=None, amazon=None, cash=None, check=None, cod=None, credit_card=None, echeck=None, loan_hero=None, money_order=None, paypal=None, purchase_order=None, quote_request=None, sezzle=None, show_accounting_code=None, switch_to_sub_tab=None, switch_to_tab=None, ultracart_payments_wepay=None, wire_transfer=None):  # noqa: E501
        """PaymentsConfiguration - a model defined in Swagger"""  # noqa: E501

        self._affirm = None
        self._amazon = None
        self._cash = None
        self._check = None
        self._cod = None
        self._credit_card = None
        self._echeck = None
        self._loan_hero = None
        self._money_order = None
        self._paypal = None
        self._purchase_order = None
        self._quote_request = None
        self._sezzle = None
        self._show_accounting_code = None
        self._switch_to_sub_tab = None
        self._switch_to_tab = None
        self._ultracart_payments_wepay = None
        self._wire_transfer = None
        self.discriminator = None

        if affirm is not None:
            self.affirm = affirm
        if amazon is not None:
            self.amazon = amazon
        if cash is not None:
            self.cash = cash
        if check is not None:
            self.check = check
        if cod is not None:
            self.cod = cod
        if credit_card is not None:
            self.credit_card = credit_card
        if echeck is not None:
            self.echeck = echeck
        if loan_hero is not None:
            self.loan_hero = loan_hero
        if money_order is not None:
            self.money_order = money_order
        if paypal is not None:
            self.paypal = paypal
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if quote_request is not None:
            self.quote_request = quote_request
        if sezzle is not None:
            self.sezzle = sezzle
        if show_accounting_code is not None:
            self.show_accounting_code = show_accounting_code
        if switch_to_sub_tab is not None:
            self.switch_to_sub_tab = switch_to_sub_tab
        if switch_to_tab is not None:
            self.switch_to_tab = switch_to_tab
        if ultracart_payments_wepay is not None:
            self.ultracart_payments_wepay = ultracart_payments_wepay
        if wire_transfer is not None:
            self.wire_transfer = wire_transfer

    @property
    def affirm(self):
        """Gets the affirm of this PaymentsConfiguration.  # noqa: E501


        :return: The affirm of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationAffirm
        """
        return self._affirm

    @affirm.setter
    def affirm(self, affirm):
        """Sets the affirm of this PaymentsConfiguration.


        :param affirm: The affirm of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationAffirm
        """

        self._affirm = affirm

    @property
    def amazon(self):
        """Gets the amazon of this PaymentsConfiguration.  # noqa: E501


        :return: The amazon of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationAmazon
        """
        return self._amazon

    @amazon.setter
    def amazon(self, amazon):
        """Sets the amazon of this PaymentsConfiguration.


        :param amazon: The amazon of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationAmazon
        """

        self._amazon = amazon

    @property
    def cash(self):
        """Gets the cash of this PaymentsConfiguration.  # noqa: E501


        :return: The cash of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationCash
        """
        return self._cash

    @cash.setter
    def cash(self, cash):
        """Sets the cash of this PaymentsConfiguration.


        :param cash: The cash of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationCash
        """

        self._cash = cash

    @property
    def check(self):
        """Gets the check of this PaymentsConfiguration.  # noqa: E501


        :return: The check of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationCheck
        """
        return self._check

    @check.setter
    def check(self, check):
        """Sets the check of this PaymentsConfiguration.


        :param check: The check of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationCheck
        """

        self._check = check

    @property
    def cod(self):
        """Gets the cod of this PaymentsConfiguration.  # noqa: E501


        :return: The cod of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationCOD
        """
        return self._cod

    @cod.setter
    def cod(self, cod):
        """Sets the cod of this PaymentsConfiguration.


        :param cod: The cod of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationCOD
        """

        self._cod = cod

    @property
    def credit_card(self):
        """Gets the credit_card of this PaymentsConfiguration.  # noqa: E501


        :return: The credit_card of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this PaymentsConfiguration.


        :param credit_card: The credit_card of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationCreditCard
        """

        self._credit_card = credit_card

    @property
    def echeck(self):
        """Gets the echeck of this PaymentsConfiguration.  # noqa: E501


        :return: The echeck of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationEcheck
        """
        return self._echeck

    @echeck.setter
    def echeck(self, echeck):
        """Sets the echeck of this PaymentsConfiguration.


        :param echeck: The echeck of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationEcheck
        """

        self._echeck = echeck

    @property
    def loan_hero(self):
        """Gets the loan_hero of this PaymentsConfiguration.  # noqa: E501


        :return: The loan_hero of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationLoanHero
        """
        return self._loan_hero

    @loan_hero.setter
    def loan_hero(self, loan_hero):
        """Sets the loan_hero of this PaymentsConfiguration.


        :param loan_hero: The loan_hero of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationLoanHero
        """

        self._loan_hero = loan_hero

    @property
    def money_order(self):
        """Gets the money_order of this PaymentsConfiguration.  # noqa: E501


        :return: The money_order of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationMoneyOrder
        """
        return self._money_order

    @money_order.setter
    def money_order(self, money_order):
        """Sets the money_order of this PaymentsConfiguration.


        :param money_order: The money_order of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationMoneyOrder
        """

        self._money_order = money_order

    @property
    def paypal(self):
        """Gets the paypal of this PaymentsConfiguration.  # noqa: E501


        :return: The paypal of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationPayPal
        """
        return self._paypal

    @paypal.setter
    def paypal(self, paypal):
        """Sets the paypal of this PaymentsConfiguration.


        :param paypal: The paypal of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationPayPal
        """

        self._paypal = paypal

    @property
    def purchase_order(self):
        """Gets the purchase_order of this PaymentsConfiguration.  # noqa: E501


        :return: The purchase_order of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationPurchaseOrder
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this PaymentsConfiguration.


        :param purchase_order: The purchase_order of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationPurchaseOrder
        """

        self._purchase_order = purchase_order

    @property
    def quote_request(self):
        """Gets the quote_request of this PaymentsConfiguration.  # noqa: E501


        :return: The quote_request of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationQuoteRequest
        """
        return self._quote_request

    @quote_request.setter
    def quote_request(self, quote_request):
        """Sets the quote_request of this PaymentsConfiguration.


        :param quote_request: The quote_request of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationQuoteRequest
        """

        self._quote_request = quote_request

    @property
    def sezzle(self):
        """Gets the sezzle of this PaymentsConfiguration.  # noqa: E501


        :return: The sezzle of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationSezzle
        """
        return self._sezzle

    @sezzle.setter
    def sezzle(self, sezzle):
        """Sets the sezzle of this PaymentsConfiguration.


        :param sezzle: The sezzle of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationSezzle
        """

        self._sezzle = sezzle

    @property
    def show_accounting_code(self):
        """Gets the show_accounting_code of this PaymentsConfiguration.  # noqa: E501

        Internal flag used to determine if accounting codes should be shown on the screen or not.  This flag is true if the merchant has a Quickbooks integration configured.  # noqa: E501

        :return: The show_accounting_code of this PaymentsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._show_accounting_code

    @show_accounting_code.setter
    def show_accounting_code(self, show_accounting_code):
        """Sets the show_accounting_code of this PaymentsConfiguration.

        Internal flag used to determine if accounting codes should be shown on the screen or not.  This flag is true if the merchant has a Quickbooks integration configured.  # noqa: E501

        :param show_accounting_code: The show_accounting_code of this PaymentsConfiguration.  # noqa: E501
        :type: bool
        """

        self._show_accounting_code = show_accounting_code

    @property
    def switch_to_sub_tab(self):
        """Gets the switch_to_sub_tab of this PaymentsConfiguration.  # noqa: E501


        :return: The switch_to_sub_tab of this PaymentsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._switch_to_sub_tab

    @switch_to_sub_tab.setter
    def switch_to_sub_tab(self, switch_to_sub_tab):
        """Sets the switch_to_sub_tab of this PaymentsConfiguration.


        :param switch_to_sub_tab: The switch_to_sub_tab of this PaymentsConfiguration.  # noqa: E501
        :type: str
        """

        self._switch_to_sub_tab = switch_to_sub_tab

    @property
    def switch_to_tab(self):
        """Gets the switch_to_tab of this PaymentsConfiguration.  # noqa: E501


        :return: The switch_to_tab of this PaymentsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._switch_to_tab

    @switch_to_tab.setter
    def switch_to_tab(self, switch_to_tab):
        """Sets the switch_to_tab of this PaymentsConfiguration.


        :param switch_to_tab: The switch_to_tab of this PaymentsConfiguration.  # noqa: E501
        :type: str
        """

        self._switch_to_tab = switch_to_tab

    @property
    def ultracart_payments_wepay(self):
        """Gets the ultracart_payments_wepay of this PaymentsConfiguration.  # noqa: E501


        :return: The ultracart_payments_wepay of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationWePay
        """
        return self._ultracart_payments_wepay

    @ultracart_payments_wepay.setter
    def ultracart_payments_wepay(self, ultracart_payments_wepay):
        """Sets the ultracart_payments_wepay of this PaymentsConfiguration.


        :param ultracart_payments_wepay: The ultracart_payments_wepay of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationWePay
        """

        self._ultracart_payments_wepay = ultracart_payments_wepay

    @property
    def wire_transfer(self):
        """Gets the wire_transfer of this PaymentsConfiguration.  # noqa: E501


        :return: The wire_transfer of this PaymentsConfiguration.  # noqa: E501
        :rtype: PaymentsConfigurationWireTransfer
        """
        return self._wire_transfer

    @wire_transfer.setter
    def wire_transfer(self, wire_transfer):
        """Sets the wire_transfer of this PaymentsConfiguration.


        :param wire_transfer: The wire_transfer of this PaymentsConfiguration.  # noqa: E501
        :type: PaymentsConfigurationWireTransfer
        """

        self._wire_transfer = wire_transfer

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
        if issubclass(PaymentsConfiguration, dict):
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
        if not isinstance(other, PaymentsConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

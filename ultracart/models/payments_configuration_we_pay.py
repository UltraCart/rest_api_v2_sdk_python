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


class PaymentsConfigurationWePay(object):
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
        'accept_wepay': 'bool',
        'account_update_uri': 'str',
        'address1': 'str',
        'address2': 'str',
        'canada_accept_debit_cards': 'bool',
        'city': 'str',
        'company': 'str',
        'company_description': 'str',
        'console_hostname': 'str',
        'country': 'str',
        'credit_card_rate': 'str',
        'currency': 'str',
        'expected_revenue': 'str',
        'hide_credit_card_non_ultracart_payments': 'bool',
        'hide_surcharge_amount': 'bool',
        'industry': 'str',
        'owner_email': 'str',
        'owner_name': 'str',
        'owner_phone': 'str',
        'postal_code': 'str',
        'restrictions': 'PaymentsConfigurationRestrictions',
        'short_paypal_marketing_text': 'bool',
        'show_ultracart_payments_disabled': 'bool',
        'show_ultracart_payments_intro': 'bool',
        'show_ultracart_payments_verification': 'bool',
        'show_ultracart_payments_verified': 'bool',
        'state': 'str',
        'website_url': 'str'
    }

    attribute_map = {
        'accept_wepay': 'accept_wepay',
        'account_update_uri': 'account_update_uri',
        'address1': 'address1',
        'address2': 'address2',
        'canada_accept_debit_cards': 'canada_accept_debit_cards',
        'city': 'city',
        'company': 'company',
        'company_description': 'company_description',
        'console_hostname': 'console_hostname',
        'country': 'country',
        'credit_card_rate': 'credit_card_rate',
        'currency': 'currency',
        'expected_revenue': 'expected_revenue',
        'hide_credit_card_non_ultracart_payments': 'hide_credit_card_non_ultracart_payments',
        'hide_surcharge_amount': 'hide_surcharge_amount',
        'industry': 'industry',
        'owner_email': 'owner_email',
        'owner_name': 'owner_name',
        'owner_phone': 'owner_phone',
        'postal_code': 'postal_code',
        'restrictions': 'restrictions',
        'short_paypal_marketing_text': 'short_paypal_marketing_text',
        'show_ultracart_payments_disabled': 'show_ultracart_payments_disabled',
        'show_ultracart_payments_intro': 'show_ultracart_payments_intro',
        'show_ultracart_payments_verification': 'show_ultracart_payments_verification',
        'show_ultracart_payments_verified': 'show_ultracart_payments_verified',
        'state': 'state',
        'website_url': 'website_url'
    }

    def __init__(self, accept_wepay=None, account_update_uri=None, address1=None, address2=None, canada_accept_debit_cards=None, city=None, company=None, company_description=None, console_hostname=None, country=None, credit_card_rate=None, currency=None, expected_revenue=None, hide_credit_card_non_ultracart_payments=None, hide_surcharge_amount=None, industry=None, owner_email=None, owner_name=None, owner_phone=None, postal_code=None, restrictions=None, short_paypal_marketing_text=None, show_ultracart_payments_disabled=None, show_ultracart_payments_intro=None, show_ultracart_payments_verification=None, show_ultracart_payments_verified=None, state=None, website_url=None):  # noqa: E501
        """PaymentsConfigurationWePay - a model defined in Swagger"""  # noqa: E501

        self._accept_wepay = None
        self._account_update_uri = None
        self._address1 = None
        self._address2 = None
        self._canada_accept_debit_cards = None
        self._city = None
        self._company = None
        self._company_description = None
        self._console_hostname = None
        self._country = None
        self._credit_card_rate = None
        self._currency = None
        self._expected_revenue = None
        self._hide_credit_card_non_ultracart_payments = None
        self._hide_surcharge_amount = None
        self._industry = None
        self._owner_email = None
        self._owner_name = None
        self._owner_phone = None
        self._postal_code = None
        self._restrictions = None
        self._short_paypal_marketing_text = None
        self._show_ultracart_payments_disabled = None
        self._show_ultracart_payments_intro = None
        self._show_ultracart_payments_verification = None
        self._show_ultracart_payments_verified = None
        self._state = None
        self._website_url = None
        self.discriminator = None

        if accept_wepay is not None:
            self.accept_wepay = accept_wepay
        if account_update_uri is not None:
            self.account_update_uri = account_update_uri
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if canada_accept_debit_cards is not None:
            self.canada_accept_debit_cards = canada_accept_debit_cards
        if city is not None:
            self.city = city
        if company is not None:
            self.company = company
        if company_description is not None:
            self.company_description = company_description
        if console_hostname is not None:
            self.console_hostname = console_hostname
        if country is not None:
            self.country = country
        if credit_card_rate is not None:
            self.credit_card_rate = credit_card_rate
        if currency is not None:
            self.currency = currency
        if expected_revenue is not None:
            self.expected_revenue = expected_revenue
        if hide_credit_card_non_ultracart_payments is not None:
            self.hide_credit_card_non_ultracart_payments = hide_credit_card_non_ultracart_payments
        if hide_surcharge_amount is not None:
            self.hide_surcharge_amount = hide_surcharge_amount
        if industry is not None:
            self.industry = industry
        if owner_email is not None:
            self.owner_email = owner_email
        if owner_name is not None:
            self.owner_name = owner_name
        if owner_phone is not None:
            self.owner_phone = owner_phone
        if postal_code is not None:
            self.postal_code = postal_code
        if restrictions is not None:
            self.restrictions = restrictions
        if short_paypal_marketing_text is not None:
            self.short_paypal_marketing_text = short_paypal_marketing_text
        if show_ultracart_payments_disabled is not None:
            self.show_ultracart_payments_disabled = show_ultracart_payments_disabled
        if show_ultracart_payments_intro is not None:
            self.show_ultracart_payments_intro = show_ultracart_payments_intro
        if show_ultracart_payments_verification is not None:
            self.show_ultracart_payments_verification = show_ultracart_payments_verification
        if show_ultracart_payments_verified is not None:
            self.show_ultracart_payments_verified = show_ultracart_payments_verified
        if state is not None:
            self.state = state
        if website_url is not None:
            self.website_url = website_url

    @property
    def accept_wepay(self):
        """Gets the accept_wepay of this PaymentsConfigurationWePay.  # noqa: E501

        Master flag indicating this merchant accepts UltraCart Payments WePay  # noqa: E501

        :return: The accept_wepay of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._accept_wepay

    @accept_wepay.setter
    def accept_wepay(self, accept_wepay):
        """Sets the accept_wepay of this PaymentsConfigurationWePay.

        Master flag indicating this merchant accepts UltraCart Payments WePay  # noqa: E501

        :param accept_wepay: The accept_wepay of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._accept_wepay = accept_wepay

    @property
    def account_update_uri(self):
        """Gets the account_update_uri of this PaymentsConfigurationWePay.  # noqa: E501

        URI for updating the WePay account  # noqa: E501

        :return: The account_update_uri of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._account_update_uri

    @account_update_uri.setter
    def account_update_uri(self, account_update_uri):
        """Sets the account_update_uri of this PaymentsConfigurationWePay.

        URI for updating the WePay account  # noqa: E501

        :param account_update_uri: The account_update_uri of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._account_update_uri = account_update_uri

    @property
    def address1(self):
        """Gets the address1 of this PaymentsConfigurationWePay.  # noqa: E501

        Address line 1  # noqa: E501

        :return: The address1 of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this PaymentsConfigurationWePay.

        Address line 1  # noqa: E501

        :param address1: The address1 of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this PaymentsConfigurationWePay.  # noqa: E501

        Address line 2  # noqa: E501

        :return: The address2 of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this PaymentsConfigurationWePay.

        Address line 2  # noqa: E501

        :param address2: The address2 of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def canada_accept_debit_cards(self):
        """Gets the canada_accept_debit_cards of this PaymentsConfigurationWePay.  # noqa: E501

        For Canadian merchants, true if they wish to accept debit cards  # noqa: E501

        :return: The canada_accept_debit_cards of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._canada_accept_debit_cards

    @canada_accept_debit_cards.setter
    def canada_accept_debit_cards(self, canada_accept_debit_cards):
        """Sets the canada_accept_debit_cards of this PaymentsConfigurationWePay.

        For Canadian merchants, true if they wish to accept debit cards  # noqa: E501

        :param canada_accept_debit_cards: The canada_accept_debit_cards of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._canada_accept_debit_cards = canada_accept_debit_cards

    @property
    def city(self):
        """Gets the city of this PaymentsConfigurationWePay.  # noqa: E501

        City  # noqa: E501

        :return: The city of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PaymentsConfigurationWePay.

        City  # noqa: E501

        :param city: The city of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """Gets the company of this PaymentsConfigurationWePay.  # noqa: E501

        Company  # noqa: E501

        :return: The company of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this PaymentsConfigurationWePay.

        Company  # noqa: E501

        :param company: The company of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def company_description(self):
        """Gets the company_description of this PaymentsConfigurationWePay.  # noqa: E501

        Company description  # noqa: E501

        :return: The company_description of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._company_description

    @company_description.setter
    def company_description(self, company_description):
        """Sets the company_description of this PaymentsConfigurationWePay.

        Company description  # noqa: E501

        :param company_description: The company_description of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._company_description = company_description

    @property
    def console_hostname(self):
        """Gets the console_hostname of this PaymentsConfigurationWePay.  # noqa: E501

        Console hostname  # noqa: E501

        :return: The console_hostname of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._console_hostname

    @console_hostname.setter
    def console_hostname(self, console_hostname):
        """Sets the console_hostname of this PaymentsConfigurationWePay.

        Console hostname  # noqa: E501

        :param console_hostname: The console_hostname of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._console_hostname = console_hostname

    @property
    def country(self):
        """Gets the country of this PaymentsConfigurationWePay.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentsConfigurationWePay.

        Country  # noqa: E501

        :param country: The country of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def credit_card_rate(self):
        """Gets the credit_card_rate of this PaymentsConfigurationWePay.  # noqa: E501

        WePay credit card rate  # noqa: E501

        :return: The credit_card_rate of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_rate

    @credit_card_rate.setter
    def credit_card_rate(self, credit_card_rate):
        """Sets the credit_card_rate of this PaymentsConfigurationWePay.

        WePay credit card rate  # noqa: E501

        :param credit_card_rate: The credit_card_rate of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._credit_card_rate = credit_card_rate

    @property
    def currency(self):
        """Gets the currency of this PaymentsConfigurationWePay.  # noqa: E501

        Base currency for transactions  # noqa: E501

        :return: The currency of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentsConfigurationWePay.

        Base currency for transactions  # noqa: E501

        :param currency: The currency of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def expected_revenue(self):
        """Gets the expected_revenue of this PaymentsConfigurationWePay.  # noqa: E501

        Expected Revenue  # noqa: E501

        :return: The expected_revenue of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._expected_revenue

    @expected_revenue.setter
    def expected_revenue(self, expected_revenue):
        """Sets the expected_revenue of this PaymentsConfigurationWePay.

        Expected Revenue  # noqa: E501

        :param expected_revenue: The expected_revenue of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._expected_revenue = expected_revenue

    @property
    def hide_credit_card_non_ultracart_payments(self):
        """Gets the hide_credit_card_non_ultracart_payments of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The hide_credit_card_non_ultracart_payments of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._hide_credit_card_non_ultracart_payments

    @hide_credit_card_non_ultracart_payments.setter
    def hide_credit_card_non_ultracart_payments(self, hide_credit_card_non_ultracart_payments):
        """Sets the hide_credit_card_non_ultracart_payments of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param hide_credit_card_non_ultracart_payments: The hide_credit_card_non_ultracart_payments of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._hide_credit_card_non_ultracart_payments = hide_credit_card_non_ultracart_payments

    @property
    def hide_surcharge_amount(self):
        """Gets the hide_surcharge_amount of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The hide_surcharge_amount of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._hide_surcharge_amount

    @hide_surcharge_amount.setter
    def hide_surcharge_amount(self, hide_surcharge_amount):
        """Sets the hide_surcharge_amount of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param hide_surcharge_amount: The hide_surcharge_amount of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._hide_surcharge_amount = hide_surcharge_amount

    @property
    def industry(self):
        """Gets the industry of this PaymentsConfigurationWePay.  # noqa: E501

        Industry  # noqa: E501

        :return: The industry of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this PaymentsConfigurationWePay.

        Industry  # noqa: E501

        :param industry: The industry of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def owner_email(self):
        """Gets the owner_email of this PaymentsConfigurationWePay.  # noqa: E501

        Owner email  # noqa: E501

        :return: The owner_email of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this PaymentsConfigurationWePay.

        Owner email  # noqa: E501

        :param owner_email: The owner_email of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def owner_name(self):
        """Gets the owner_name of this PaymentsConfigurationWePay.  # noqa: E501

        Owner name  # noqa: E501

        :return: The owner_name of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this PaymentsConfigurationWePay.

        Owner name  # noqa: E501

        :param owner_name: The owner_name of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def owner_phone(self):
        """Gets the owner_phone of this PaymentsConfigurationWePay.  # noqa: E501

        Owner phone  # noqa: E501

        :return: The owner_phone of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._owner_phone

    @owner_phone.setter
    def owner_phone(self, owner_phone):
        """Sets the owner_phone of this PaymentsConfigurationWePay.

        Owner phone  # noqa: E501

        :param owner_phone: The owner_phone of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._owner_phone = owner_phone

    @property
    def postal_code(self):
        """Gets the postal_code of this PaymentsConfigurationWePay.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PaymentsConfigurationWePay.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationWePay.  # noqa: E501


        :return: The restrictions of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: PaymentsConfigurationRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationWePay.


        :param restrictions: The restrictions of this PaymentsConfigurationWePay.  # noqa: E501
        :type: PaymentsConfigurationRestrictions
        """

        self._restrictions = restrictions

    @property
    def short_paypal_marketing_text(self):
        """Gets the short_paypal_marketing_text of this PaymentsConfigurationWePay.  # noqa: E501

        Internal UI aid  # noqa: E501

        :return: The short_paypal_marketing_text of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._short_paypal_marketing_text

    @short_paypal_marketing_text.setter
    def short_paypal_marketing_text(self, short_paypal_marketing_text):
        """Sets the short_paypal_marketing_text of this PaymentsConfigurationWePay.

        Internal UI aid  # noqa: E501

        :param short_paypal_marketing_text: The short_paypal_marketing_text of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._short_paypal_marketing_text = short_paypal_marketing_text

    @property
    def show_ultracart_payments_disabled(self):
        """Gets the show_ultracart_payments_disabled of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The show_ultracart_payments_disabled of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._show_ultracart_payments_disabled

    @show_ultracart_payments_disabled.setter
    def show_ultracart_payments_disabled(self, show_ultracart_payments_disabled):
        """Sets the show_ultracart_payments_disabled of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param show_ultracart_payments_disabled: The show_ultracart_payments_disabled of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._show_ultracart_payments_disabled = show_ultracart_payments_disabled

    @property
    def show_ultracart_payments_intro(self):
        """Gets the show_ultracart_payments_intro of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The show_ultracart_payments_intro of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._show_ultracart_payments_intro

    @show_ultracart_payments_intro.setter
    def show_ultracart_payments_intro(self, show_ultracart_payments_intro):
        """Sets the show_ultracart_payments_intro of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param show_ultracart_payments_intro: The show_ultracart_payments_intro of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._show_ultracart_payments_intro = show_ultracart_payments_intro

    @property
    def show_ultracart_payments_verification(self):
        """Gets the show_ultracart_payments_verification of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The show_ultracart_payments_verification of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._show_ultracart_payments_verification

    @show_ultracart_payments_verification.setter
    def show_ultracart_payments_verification(self, show_ultracart_payments_verification):
        """Sets the show_ultracart_payments_verification of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param show_ultracart_payments_verification: The show_ultracart_payments_verification of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._show_ultracart_payments_verification = show_ultracart_payments_verification

    @property
    def show_ultracart_payments_verified(self):
        """Gets the show_ultracart_payments_verified of this PaymentsConfigurationWePay.  # noqa: E501

        Internal flag to aid UI  # noqa: E501

        :return: The show_ultracart_payments_verified of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: bool
        """
        return self._show_ultracart_payments_verified

    @show_ultracart_payments_verified.setter
    def show_ultracart_payments_verified(self, show_ultracart_payments_verified):
        """Sets the show_ultracart_payments_verified of this PaymentsConfigurationWePay.

        Internal flag to aid UI  # noqa: E501

        :param show_ultracart_payments_verified: The show_ultracart_payments_verified of this PaymentsConfigurationWePay.  # noqa: E501
        :type: bool
        """

        self._show_ultracart_payments_verified = show_ultracart_payments_verified

    @property
    def state(self):
        """Gets the state of this PaymentsConfigurationWePay.  # noqa: E501

        State  # noqa: E501

        :return: The state of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentsConfigurationWePay.

        State  # noqa: E501

        :param state: The state of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def website_url(self):
        """Gets the website_url of this PaymentsConfigurationWePay.  # noqa: E501

        Website URL  # noqa: E501

        :return: The website_url of this PaymentsConfigurationWePay.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this PaymentsConfigurationWePay.

        Website URL  # noqa: E501

        :param website_url: The website_url of this PaymentsConfigurationWePay.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

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
        if issubclass(PaymentsConfigurationWePay, dict):
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
        if not isinstance(other, PaymentsConfigurationWePay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
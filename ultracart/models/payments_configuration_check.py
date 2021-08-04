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


class PaymentsConfigurationCheck(object):
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
        'accept_check_orders': 'bool',
        'check_accounting_code': 'str',
        'check_deposit_to_account': 'str',
        'checks_payable_to': 'str',
        'mail_to_address1': 'str',
        'mail_to_address2': 'str',
        'mail_to_city': 'str',
        'mail_to_country': 'str',
        'mail_to_name': 'str',
        'mail_to_state': 'str',
        'mail_to_zip': 'str',
        'money_order_accounting_code': 'str',
        'money_order_deposit_to_account': 'str',
        'restrictions': 'PaymentsConfigurationRestrictions'
    }

    attribute_map = {
        'accept_check_orders': 'acceptCheckOrders',
        'check_accounting_code': 'checkAccountingCode',
        'check_deposit_to_account': 'checkDepositToAccount',
        'checks_payable_to': 'checksPayableTo',
        'mail_to_address1': 'mailToAddress1',
        'mail_to_address2': 'mailToAddress2',
        'mail_to_city': 'mailToCity',
        'mail_to_country': 'mailToCountry',
        'mail_to_name': 'mailToName',
        'mail_to_state': 'mailToState',
        'mail_to_zip': 'mailToZip',
        'money_order_accounting_code': 'moneyOrderAccountingCode',
        'money_order_deposit_to_account': 'moneyOrderDepositToAccount',
        'restrictions': 'restrictions'
    }

    def __init__(self, accept_check_orders=None, check_accounting_code=None, check_deposit_to_account=None, checks_payable_to=None, mail_to_address1=None, mail_to_address2=None, mail_to_city=None, mail_to_country=None, mail_to_name=None, mail_to_state=None, mail_to_zip=None, money_order_accounting_code=None, money_order_deposit_to_account=None, restrictions=None):  # noqa: E501
        """PaymentsConfigurationCheck - a model defined in Swagger"""  # noqa: E501

        self._accept_check_orders = None
        self._check_accounting_code = None
        self._check_deposit_to_account = None
        self._checks_payable_to = None
        self._mail_to_address1 = None
        self._mail_to_address2 = None
        self._mail_to_city = None
        self._mail_to_country = None
        self._mail_to_name = None
        self._mail_to_state = None
        self._mail_to_zip = None
        self._money_order_accounting_code = None
        self._money_order_deposit_to_account = None
        self._restrictions = None
        self.discriminator = None

        if accept_check_orders is not None:
            self.accept_check_orders = accept_check_orders
        if check_accounting_code is not None:
            self.check_accounting_code = check_accounting_code
        if check_deposit_to_account is not None:
            self.check_deposit_to_account = check_deposit_to_account
        if checks_payable_to is not None:
            self.checks_payable_to = checks_payable_to
        if mail_to_address1 is not None:
            self.mail_to_address1 = mail_to_address1
        if mail_to_address2 is not None:
            self.mail_to_address2 = mail_to_address2
        if mail_to_city is not None:
            self.mail_to_city = mail_to_city
        if mail_to_country is not None:
            self.mail_to_country = mail_to_country
        if mail_to_name is not None:
            self.mail_to_name = mail_to_name
        if mail_to_state is not None:
            self.mail_to_state = mail_to_state
        if mail_to_zip is not None:
            self.mail_to_zip = mail_to_zip
        if money_order_accounting_code is not None:
            self.money_order_accounting_code = money_order_accounting_code
        if money_order_deposit_to_account is not None:
            self.money_order_deposit_to_account = money_order_deposit_to_account
        if restrictions is not None:
            self.restrictions = restrictions

    @property
    def accept_check_orders(self):
        """Gets the accept_check_orders of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The accept_check_orders of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: bool
        """
        return self._accept_check_orders

    @accept_check_orders.setter
    def accept_check_orders(self, accept_check_orders):
        """Sets the accept_check_orders of this PaymentsConfigurationCheck.


        :param accept_check_orders: The accept_check_orders of this PaymentsConfigurationCheck.  # noqa: E501
        :type: bool
        """

        self._accept_check_orders = accept_check_orders

    @property
    def check_accounting_code(self):
        """Gets the check_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The check_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._check_accounting_code

    @check_accounting_code.setter
    def check_accounting_code(self, check_accounting_code):
        """Sets the check_accounting_code of this PaymentsConfigurationCheck.


        :param check_accounting_code: The check_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._check_accounting_code = check_accounting_code

    @property
    def check_deposit_to_account(self):
        """Gets the check_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The check_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._check_deposit_to_account

    @check_deposit_to_account.setter
    def check_deposit_to_account(self, check_deposit_to_account):
        """Sets the check_deposit_to_account of this PaymentsConfigurationCheck.


        :param check_deposit_to_account: The check_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._check_deposit_to_account = check_deposit_to_account

    @property
    def checks_payable_to(self):
        """Gets the checks_payable_to of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The checks_payable_to of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._checks_payable_to

    @checks_payable_to.setter
    def checks_payable_to(self, checks_payable_to):
        """Sets the checks_payable_to of this PaymentsConfigurationCheck.


        :param checks_payable_to: The checks_payable_to of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._checks_payable_to = checks_payable_to

    @property
    def mail_to_address1(self):
        """Gets the mail_to_address1 of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_address1 of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_address1

    @mail_to_address1.setter
    def mail_to_address1(self, mail_to_address1):
        """Sets the mail_to_address1 of this PaymentsConfigurationCheck.


        :param mail_to_address1: The mail_to_address1 of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_address1 = mail_to_address1

    @property
    def mail_to_address2(self):
        """Gets the mail_to_address2 of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_address2 of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_address2

    @mail_to_address2.setter
    def mail_to_address2(self, mail_to_address2):
        """Sets the mail_to_address2 of this PaymentsConfigurationCheck.


        :param mail_to_address2: The mail_to_address2 of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_address2 = mail_to_address2

    @property
    def mail_to_city(self):
        """Gets the mail_to_city of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_city of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_city

    @mail_to_city.setter
    def mail_to_city(self, mail_to_city):
        """Sets the mail_to_city of this PaymentsConfigurationCheck.


        :param mail_to_city: The mail_to_city of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_city = mail_to_city

    @property
    def mail_to_country(self):
        """Gets the mail_to_country of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_country of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_country

    @mail_to_country.setter
    def mail_to_country(self, mail_to_country):
        """Sets the mail_to_country of this PaymentsConfigurationCheck.


        :param mail_to_country: The mail_to_country of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_country = mail_to_country

    @property
    def mail_to_name(self):
        """Gets the mail_to_name of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_name of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_name

    @mail_to_name.setter
    def mail_to_name(self, mail_to_name):
        """Sets the mail_to_name of this PaymentsConfigurationCheck.


        :param mail_to_name: The mail_to_name of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_name = mail_to_name

    @property
    def mail_to_state(self):
        """Gets the mail_to_state of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_state of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_state

    @mail_to_state.setter
    def mail_to_state(self, mail_to_state):
        """Sets the mail_to_state of this PaymentsConfigurationCheck.


        :param mail_to_state: The mail_to_state of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_state = mail_to_state

    @property
    def mail_to_zip(self):
        """Gets the mail_to_zip of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The mail_to_zip of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._mail_to_zip

    @mail_to_zip.setter
    def mail_to_zip(self, mail_to_zip):
        """Sets the mail_to_zip of this PaymentsConfigurationCheck.


        :param mail_to_zip: The mail_to_zip of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._mail_to_zip = mail_to_zip

    @property
    def money_order_accounting_code(self):
        """Gets the money_order_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The money_order_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._money_order_accounting_code

    @money_order_accounting_code.setter
    def money_order_accounting_code(self, money_order_accounting_code):
        """Sets the money_order_accounting_code of this PaymentsConfigurationCheck.


        :param money_order_accounting_code: The money_order_accounting_code of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._money_order_accounting_code = money_order_accounting_code

    @property
    def money_order_deposit_to_account(self):
        """Gets the money_order_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The money_order_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: str
        """
        return self._money_order_deposit_to_account

    @money_order_deposit_to_account.setter
    def money_order_deposit_to_account(self, money_order_deposit_to_account):
        """Sets the money_order_deposit_to_account of this PaymentsConfigurationCheck.


        :param money_order_deposit_to_account: The money_order_deposit_to_account of this PaymentsConfigurationCheck.  # noqa: E501
        :type: str
        """

        self._money_order_deposit_to_account = money_order_deposit_to_account

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationCheck.  # noqa: E501


        :return: The restrictions of this PaymentsConfigurationCheck.  # noqa: E501
        :rtype: PaymentsConfigurationRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationCheck.


        :param restrictions: The restrictions of this PaymentsConfigurationCheck.  # noqa: E501
        :type: PaymentsConfigurationRestrictions
        """

        self._restrictions = restrictions

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
        if issubclass(PaymentsConfigurationCheck, dict):
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
        if not isinstance(other, PaymentsConfigurationCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

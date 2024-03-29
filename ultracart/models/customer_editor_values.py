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


class CustomerEditorValues(object):
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
        'affiliates': 'list[CustomerAffiliate]',
        'card_exp_months': 'list[str]',
        'card_exp_years': 'list[str]',
        'card_types': 'list[str]',
        'countries': 'list[Country]',
        'edi_channel_partners': 'list[ChannelPartner]',
        'loyalty_ledger_descriptions': 'list[str]',
        'loyalty_program_type': 'str',
        'qb_classes': 'list[str]',
        'sales_rep_codes': 'list[str]',
        'state_optional_countries': 'list[Country]',
        'terms': 'list[str]'
    }

    attribute_map = {
        'affiliates': 'affiliates',
        'card_exp_months': 'card_exp_months',
        'card_exp_years': 'card_exp_years',
        'card_types': 'card_types',
        'countries': 'countries',
        'edi_channel_partners': 'edi_channel_partners',
        'loyalty_ledger_descriptions': 'loyalty_ledger_descriptions',
        'loyalty_program_type': 'loyalty_program_type',
        'qb_classes': 'qb_classes',
        'sales_rep_codes': 'sales_rep_codes',
        'state_optional_countries': 'state_optional_countries',
        'terms': 'terms'
    }

    def __init__(self, affiliates=None, card_exp_months=None, card_exp_years=None, card_types=None, countries=None, edi_channel_partners=None, loyalty_ledger_descriptions=None, loyalty_program_type=None, qb_classes=None, sales_rep_codes=None, state_optional_countries=None, terms=None):  # noqa: E501
        """CustomerEditorValues - a model defined in Swagger"""  # noqa: E501

        self._affiliates = None
        self._card_exp_months = None
        self._card_exp_years = None
        self._card_types = None
        self._countries = None
        self._edi_channel_partners = None
        self._loyalty_ledger_descriptions = None
        self._loyalty_program_type = None
        self._qb_classes = None
        self._sales_rep_codes = None
        self._state_optional_countries = None
        self._terms = None
        self.discriminator = None

        if affiliates is not None:
            self.affiliates = affiliates
        if card_exp_months is not None:
            self.card_exp_months = card_exp_months
        if card_exp_years is not None:
            self.card_exp_years = card_exp_years
        if card_types is not None:
            self.card_types = card_types
        if countries is not None:
            self.countries = countries
        if edi_channel_partners is not None:
            self.edi_channel_partners = edi_channel_partners
        if loyalty_ledger_descriptions is not None:
            self.loyalty_ledger_descriptions = loyalty_ledger_descriptions
        if loyalty_program_type is not None:
            self.loyalty_program_type = loyalty_program_type
        if qb_classes is not None:
            self.qb_classes = qb_classes
        if sales_rep_codes is not None:
            self.sales_rep_codes = sales_rep_codes
        if state_optional_countries is not None:
            self.state_optional_countries = state_optional_countries
        if terms is not None:
            self.terms = terms

    @property
    def affiliates(self):
        """Gets the affiliates of this CustomerEditorValues.  # noqa: E501

        affiliates  # noqa: E501

        :return: The affiliates of this CustomerEditorValues.  # noqa: E501
        :rtype: list[CustomerAffiliate]
        """
        return self._affiliates

    @affiliates.setter
    def affiliates(self, affiliates):
        """Sets the affiliates of this CustomerEditorValues.

        affiliates  # noqa: E501

        :param affiliates: The affiliates of this CustomerEditorValues.  # noqa: E501
        :type: list[CustomerAffiliate]
        """

        self._affiliates = affiliates

    @property
    def card_exp_months(self):
        """Gets the card_exp_months of this CustomerEditorValues.  # noqa: E501

        card_exp_months  # noqa: E501

        :return: The card_exp_months of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._card_exp_months

    @card_exp_months.setter
    def card_exp_months(self, card_exp_months):
        """Sets the card_exp_months of this CustomerEditorValues.

        card_exp_months  # noqa: E501

        :param card_exp_months: The card_exp_months of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._card_exp_months = card_exp_months

    @property
    def card_exp_years(self):
        """Gets the card_exp_years of this CustomerEditorValues.  # noqa: E501

        card_exp_years  # noqa: E501

        :return: The card_exp_years of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._card_exp_years

    @card_exp_years.setter
    def card_exp_years(self, card_exp_years):
        """Sets the card_exp_years of this CustomerEditorValues.

        card_exp_years  # noqa: E501

        :param card_exp_years: The card_exp_years of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._card_exp_years = card_exp_years

    @property
    def card_types(self):
        """Gets the card_types of this CustomerEditorValues.  # noqa: E501

        card_types  # noqa: E501

        :return: The card_types of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._card_types

    @card_types.setter
    def card_types(self, card_types):
        """Sets the card_types of this CustomerEditorValues.

        card_types  # noqa: E501

        :param card_types: The card_types of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._card_types = card_types

    @property
    def countries(self):
        """Gets the countries of this CustomerEditorValues.  # noqa: E501

        countries  # noqa: E501

        :return: The countries of this CustomerEditorValues.  # noqa: E501
        :rtype: list[Country]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this CustomerEditorValues.

        countries  # noqa: E501

        :param countries: The countries of this CustomerEditorValues.  # noqa: E501
        :type: list[Country]
        """

        self._countries = countries

    @property
    def edi_channel_partners(self):
        """Gets the edi_channel_partners of this CustomerEditorValues.  # noqa: E501

        EDI channel partners  # noqa: E501

        :return: The edi_channel_partners of this CustomerEditorValues.  # noqa: E501
        :rtype: list[ChannelPartner]
        """
        return self._edi_channel_partners

    @edi_channel_partners.setter
    def edi_channel_partners(self, edi_channel_partners):
        """Sets the edi_channel_partners of this CustomerEditorValues.

        EDI channel partners  # noqa: E501

        :param edi_channel_partners: The edi_channel_partners of this CustomerEditorValues.  # noqa: E501
        :type: list[ChannelPartner]
        """

        self._edi_channel_partners = edi_channel_partners

    @property
    def loyalty_ledger_descriptions(self):
        """Gets the loyalty_ledger_descriptions of this CustomerEditorValues.  # noqa: E501

        loyalty_ledger_descriptions  # noqa: E501

        :return: The loyalty_ledger_descriptions of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._loyalty_ledger_descriptions

    @loyalty_ledger_descriptions.setter
    def loyalty_ledger_descriptions(self, loyalty_ledger_descriptions):
        """Sets the loyalty_ledger_descriptions of this CustomerEditorValues.

        loyalty_ledger_descriptions  # noqa: E501

        :param loyalty_ledger_descriptions: The loyalty_ledger_descriptions of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._loyalty_ledger_descriptions = loyalty_ledger_descriptions

    @property
    def loyalty_program_type(self):
        """Gets the loyalty_program_type of this CustomerEditorValues.  # noqa: E501

        loyalty_program_type  # noqa: E501

        :return: The loyalty_program_type of this CustomerEditorValues.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_program_type

    @loyalty_program_type.setter
    def loyalty_program_type(self, loyalty_program_type):
        """Sets the loyalty_program_type of this CustomerEditorValues.

        loyalty_program_type  # noqa: E501

        :param loyalty_program_type: The loyalty_program_type of this CustomerEditorValues.  # noqa: E501
        :type: str
        """

        self._loyalty_program_type = loyalty_program_type

    @property
    def qb_classes(self):
        """Gets the qb_classes of this CustomerEditorValues.  # noqa: E501

        qb_classes  # noqa: E501

        :return: The qb_classes of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._qb_classes

    @qb_classes.setter
    def qb_classes(self, qb_classes):
        """Sets the qb_classes of this CustomerEditorValues.

        qb_classes  # noqa: E501

        :param qb_classes: The qb_classes of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._qb_classes = qb_classes

    @property
    def sales_rep_codes(self):
        """Gets the sales_rep_codes of this CustomerEditorValues.  # noqa: E501

        sales_rep_codes  # noqa: E501

        :return: The sales_rep_codes of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._sales_rep_codes

    @sales_rep_codes.setter
    def sales_rep_codes(self, sales_rep_codes):
        """Sets the sales_rep_codes of this CustomerEditorValues.

        sales_rep_codes  # noqa: E501

        :param sales_rep_codes: The sales_rep_codes of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._sales_rep_codes = sales_rep_codes

    @property
    def state_optional_countries(self):
        """Gets the state_optional_countries of this CustomerEditorValues.  # noqa: E501

        state_optional_countries  # noqa: E501

        :return: The state_optional_countries of this CustomerEditorValues.  # noqa: E501
        :rtype: list[Country]
        """
        return self._state_optional_countries

    @state_optional_countries.setter
    def state_optional_countries(self, state_optional_countries):
        """Sets the state_optional_countries of this CustomerEditorValues.

        state_optional_countries  # noqa: E501

        :param state_optional_countries: The state_optional_countries of this CustomerEditorValues.  # noqa: E501
        :type: list[Country]
        """

        self._state_optional_countries = state_optional_countries

    @property
    def terms(self):
        """Gets the terms of this CustomerEditorValues.  # noqa: E501

        terms  # noqa: E501

        :return: The terms of this CustomerEditorValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this CustomerEditorValues.

        terms  # noqa: E501

        :param terms: The terms of this CustomerEditorValues.  # noqa: E501
        :type: list[str]
        """

        self._terms = terms

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
        if issubclass(CustomerEditorValues, dict):
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
        if not isinstance(other, CustomerEditorValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

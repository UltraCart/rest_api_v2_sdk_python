# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TaxCounty(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'accounting_code': 'str',
        'cities': 'list[TaxCity]',
        'county': 'str',
        'county_oid': 'int',
        'dont_collect_city': 'bool',
        'dont_collect_county': 'bool',
        'dont_collect_postal_code': 'bool',
        'state_oid': 'int',
        'tax_rate': 'float',
        'tax_rate_formatted': 'str'
    }

    attribute_map = {
        'accounting_code': 'accounting_code',
        'cities': 'cities',
        'county': 'county',
        'county_oid': 'county_oid',
        'dont_collect_city': 'dont_collect_city',
        'dont_collect_county': 'dont_collect_county',
        'dont_collect_postal_code': 'dont_collect_postal_code',
        'state_oid': 'state_oid',
        'tax_rate': 'tax_rate',
        'tax_rate_formatted': 'tax_rate_formatted'
    }

    def __init__(self, accounting_code=None, cities=None, county=None, county_oid=None, dont_collect_city=None, dont_collect_county=None, dont_collect_postal_code=None, state_oid=None, tax_rate=None, tax_rate_formatted=None):
        """
        TaxCounty - a model defined in Swagger
        """

        self._accounting_code = None
        self._cities = None
        self._county = None
        self._county_oid = None
        self._dont_collect_city = None
        self._dont_collect_county = None
        self._dont_collect_postal_code = None
        self._state_oid = None
        self._tax_rate = None
        self._tax_rate_formatted = None
        self.discriminator = None

        if accounting_code is not None:
          self.accounting_code = accounting_code
        if cities is not None:
          self.cities = cities
        if county is not None:
          self.county = county
        if county_oid is not None:
          self.county_oid = county_oid
        if dont_collect_city is not None:
          self.dont_collect_city = dont_collect_city
        if dont_collect_county is not None:
          self.dont_collect_county = dont_collect_county
        if dont_collect_postal_code is not None:
          self.dont_collect_postal_code = dont_collect_postal_code
        if state_oid is not None:
          self.state_oid = state_oid
        if tax_rate is not None:
          self.tax_rate = tax_rate
        if tax_rate_formatted is not None:
          self.tax_rate_formatted = tax_rate_formatted

    @property
    def accounting_code(self):
        """
        Gets the accounting_code of this TaxCounty.
        Accounting code for programs such as QuickBooks

        :return: The accounting_code of this TaxCounty.
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """
        Sets the accounting_code of this TaxCounty.
        Accounting code for programs such as QuickBooks

        :param accounting_code: The accounting_code of this TaxCounty.
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def cities(self):
        """
        Gets the cities of this TaxCounty.
        Cities within this city

        :return: The cities of this TaxCounty.
        :rtype: list[TaxCity]
        """
        return self._cities

    @cities.setter
    def cities(self, cities):
        """
        Sets the cities of this TaxCounty.
        Cities within this city

        :param cities: The cities of this TaxCounty.
        :type: list[TaxCity]
        """

        self._cities = cities

    @property
    def county(self):
        """
        Gets the county of this TaxCounty.
        County

        :return: The county of this TaxCounty.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this TaxCounty.
        County

        :param county: The county of this TaxCounty.
        :type: str
        """

        self._county = county

    @property
    def county_oid(self):
        """
        Gets the county_oid of this TaxCounty.
        Tax record object identifier used internally by database

        :return: The county_oid of this TaxCounty.
        :rtype: int
        """
        return self._county_oid

    @county_oid.setter
    def county_oid(self, county_oid):
        """
        Sets the county_oid of this TaxCounty.
        Tax record object identifier used internally by database

        :param county_oid: The county_oid of this TaxCounty.
        :type: int
        """

        self._county_oid = county_oid

    @property
    def dont_collect_city(self):
        """
        Gets the dont_collect_city of this TaxCounty.
        Flag instructing engine to not collect city tax for this county

        :return: The dont_collect_city of this TaxCounty.
        :rtype: bool
        """
        return self._dont_collect_city

    @dont_collect_city.setter
    def dont_collect_city(self, dont_collect_city):
        """
        Sets the dont_collect_city of this TaxCounty.
        Flag instructing engine to not collect city tax for this county

        :param dont_collect_city: The dont_collect_city of this TaxCounty.
        :type: bool
        """

        self._dont_collect_city = dont_collect_city

    @property
    def dont_collect_county(self):
        """
        Gets the dont_collect_county of this TaxCounty.
        Flag instructing engine to not collect county tax for this county

        :return: The dont_collect_county of this TaxCounty.
        :rtype: bool
        """
        return self._dont_collect_county

    @dont_collect_county.setter
    def dont_collect_county(self, dont_collect_county):
        """
        Sets the dont_collect_county of this TaxCounty.
        Flag instructing engine to not collect county tax for this county

        :param dont_collect_county: The dont_collect_county of this TaxCounty.
        :type: bool
        """

        self._dont_collect_county = dont_collect_county

    @property
    def dont_collect_postal_code(self):
        """
        Gets the dont_collect_postal_code of this TaxCounty.
        Flag instructing engine to not collect postal code tax for this county

        :return: The dont_collect_postal_code of this TaxCounty.
        :rtype: bool
        """
        return self._dont_collect_postal_code

    @dont_collect_postal_code.setter
    def dont_collect_postal_code(self, dont_collect_postal_code):
        """
        Sets the dont_collect_postal_code of this TaxCounty.
        Flag instructing engine to not collect postal code tax for this county

        :param dont_collect_postal_code: The dont_collect_postal_code of this TaxCounty.
        :type: bool
        """

        self._dont_collect_postal_code = dont_collect_postal_code

    @property
    def state_oid(self):
        """
        Gets the state_oid of this TaxCounty.
        Tax record object identifier used internally by database

        :return: The state_oid of this TaxCounty.
        :rtype: int
        """
        return self._state_oid

    @state_oid.setter
    def state_oid(self, state_oid):
        """
        Sets the state_oid of this TaxCounty.
        Tax record object identifier used internally by database

        :param state_oid: The state_oid of this TaxCounty.
        :type: int
        """

        self._state_oid = state_oid

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this TaxCounty.
        Tax Rate

        :return: The tax_rate of this TaxCounty.
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this TaxCounty.
        Tax Rate

        :param tax_rate: The tax_rate of this TaxCounty.
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_formatted(self):
        """
        Gets the tax_rate_formatted of this TaxCounty.
        Tax rate formatted

        :return: The tax_rate_formatted of this TaxCounty.
        :rtype: str
        """
        return self._tax_rate_formatted

    @tax_rate_formatted.setter
    def tax_rate_formatted(self, tax_rate_formatted):
        """
        Sets the tax_rate_formatted of this TaxCounty.
        Tax rate formatted

        :param tax_rate_formatted: The tax_rate_formatted of this TaxCounty.
        :type: str
        """

        self._tax_rate_formatted = tax_rate_formatted

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
        if not isinstance(other, TaxCounty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

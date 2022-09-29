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


class TaxProviderSelf(object):
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
        'configuration': 'SelfConfig',
        'countries': 'list[TaxCountry]',
        'description': 'str',
        'selected': 'bool',
        'title': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'countries': 'countries',
        'description': 'description',
        'selected': 'selected',
        'title': 'title'
    }

    def __init__(self, configuration=None, countries=None, description=None, selected=None, title=None):  # noqa: E501
        """TaxProviderSelf - a model defined in Swagger"""  # noqa: E501

        self._configuration = None
        self._countries = None
        self._description = None
        self._selected = None
        self._title = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if countries is not None:
            self.countries = countries
        if description is not None:
            self.description = description
        if selected is not None:
            self.selected = selected
        if title is not None:
            self.title = title

    @property
    def configuration(self):
        """Gets the configuration of this TaxProviderSelf.  # noqa: E501


        :return: The configuration of this TaxProviderSelf.  # noqa: E501
        :rtype: SelfConfig
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this TaxProviderSelf.


        :param configuration: The configuration of this TaxProviderSelf.  # noqa: E501
        :type: SelfConfig
        """

        self._configuration = configuration

    @property
    def countries(self):
        """Gets the countries of this TaxProviderSelf.  # noqa: E501

        Countries that collect sales tax  # noqa: E501

        :return: The countries of this TaxProviderSelf.  # noqa: E501
        :rtype: list[TaxCountry]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this TaxProviderSelf.

        Countries that collect sales tax  # noqa: E501

        :param countries: The countries of this TaxProviderSelf.  # noqa: E501
        :type: list[TaxCountry]
        """

        self._countries = countries

    @property
    def description(self):
        """Gets the description of this TaxProviderSelf.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this TaxProviderSelf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaxProviderSelf.

        Description  # noqa: E501

        :param description: The description of this TaxProviderSelf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def selected(self):
        """Gets the selected of this TaxProviderSelf.  # noqa: E501

        Selected  # noqa: E501

        :return: The selected of this TaxProviderSelf.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this TaxProviderSelf.

        Selected  # noqa: E501

        :param selected: The selected of this TaxProviderSelf.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def title(self):
        """Gets the title of this TaxProviderSelf.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this TaxProviderSelf.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaxProviderSelf.

        Title  # noqa: E501

        :param title: The title of this TaxProviderSelf.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(TaxProviderSelf, dict):
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
        if not isinstance(other, TaxProviderSelf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
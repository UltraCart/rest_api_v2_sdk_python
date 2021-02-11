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


class TaxProviderUltraCartState(object):
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
        'enabled': 'bool',
        'state_code': 'str',
        'state_name': 'str',
        'tax_gift_charge': 'bool',
        'tax_gift_wrap': 'bool',
        'tax_rate_formatted': 'str',
        'tax_shipping': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'state_code': 'state_code',
        'state_name': 'state_name',
        'tax_gift_charge': 'tax_gift_charge',
        'tax_gift_wrap': 'tax_gift_wrap',
        'tax_rate_formatted': 'tax_rate_formatted',
        'tax_shipping': 'tax_shipping'
    }

    def __init__(self, enabled=None, state_code=None, state_name=None, tax_gift_charge=None, tax_gift_wrap=None, tax_rate_formatted=None, tax_shipping=None):  # noqa: E501
        """TaxProviderUltraCartState - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._state_code = None
        self._state_name = None
        self._tax_gift_charge = None
        self._tax_gift_wrap = None
        self._tax_rate_formatted = None
        self._tax_shipping = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if state_code is not None:
            self.state_code = state_code
        if state_name is not None:
            self.state_name = state_name
        if tax_gift_charge is not None:
            self.tax_gift_charge = tax_gift_charge
        if tax_gift_wrap is not None:
            self.tax_gift_wrap = tax_gift_wrap
        if tax_rate_formatted is not None:
            self.tax_rate_formatted = tax_rate_formatted
        if tax_shipping is not None:
            self.tax_shipping = tax_shipping

    @property
    def enabled(self):
        """Gets the enabled of this TaxProviderUltraCartState.  # noqa: E501

        True if this state taxes are managed by UltraCart  # noqa: E501

        :return: The enabled of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TaxProviderUltraCartState.

        True if this state taxes are managed by UltraCart  # noqa: E501

        :param enabled: The enabled of this TaxProviderUltraCartState.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def state_code(self):
        """Gets the state_code of this TaxProviderUltraCartState.  # noqa: E501

        State Code (2 digits)  # noqa: E501

        :return: The state_code of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this TaxProviderUltraCartState.

        State Code (2 digits)  # noqa: E501

        :param state_code: The state_code of this TaxProviderUltraCartState.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def state_name(self):
        """Gets the state_name of this TaxProviderUltraCartState.  # noqa: E501

        Fully spelled out state name  # noqa: E501

        :return: The state_name of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        """Sets the state_name of this TaxProviderUltraCartState.

        Fully spelled out state name  # noqa: E501

        :param state_name: The state_name of this TaxProviderUltraCartState.  # noqa: E501
        :type: str
        """

        self._state_name = state_name

    @property
    def tax_gift_charge(self):
        """Gets the tax_gift_charge of this TaxProviderUltraCartState.  # noqa: E501

        True if gift charges should be taxed in this state.  # noqa: E501

        :return: The tax_gift_charge of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: bool
        """
        return self._tax_gift_charge

    @tax_gift_charge.setter
    def tax_gift_charge(self, tax_gift_charge):
        """Sets the tax_gift_charge of this TaxProviderUltraCartState.

        True if gift charges should be taxed in this state.  # noqa: E501

        :param tax_gift_charge: The tax_gift_charge of this TaxProviderUltraCartState.  # noqa: E501
        :type: bool
        """

        self._tax_gift_charge = tax_gift_charge

    @property
    def tax_gift_wrap(self):
        """Gets the tax_gift_wrap of this TaxProviderUltraCartState.  # noqa: E501

        True if gift wrap should be taxed in this state.  # noqa: E501

        :return: The tax_gift_wrap of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: bool
        """
        return self._tax_gift_wrap

    @tax_gift_wrap.setter
    def tax_gift_wrap(self, tax_gift_wrap):
        """Sets the tax_gift_wrap of this TaxProviderUltraCartState.

        True if gift wrap should be taxed in this state.  # noqa: E501

        :param tax_gift_wrap: The tax_gift_wrap of this TaxProviderUltraCartState.  # noqa: E501
        :type: bool
        """

        self._tax_gift_wrap = tax_gift_wrap

    @property
    def tax_rate_formatted(self):
        """Gets the tax_rate_formatted of this TaxProviderUltraCartState.  # noqa: E501

        State tax rate formatted for display  # noqa: E501

        :return: The tax_rate_formatted of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_formatted

    @tax_rate_formatted.setter
    def tax_rate_formatted(self, tax_rate_formatted):
        """Sets the tax_rate_formatted of this TaxProviderUltraCartState.

        State tax rate formatted for display  # noqa: E501

        :param tax_rate_formatted: The tax_rate_formatted of this TaxProviderUltraCartState.  # noqa: E501
        :type: str
        """

        self._tax_rate_formatted = tax_rate_formatted

    @property
    def tax_shipping(self):
        """Gets the tax_shipping of this TaxProviderUltraCartState.  # noqa: E501

        True if shipping should be taxed in this state.  # noqa: E501

        :return: The tax_shipping of this TaxProviderUltraCartState.  # noqa: E501
        :rtype: bool
        """
        return self._tax_shipping

    @tax_shipping.setter
    def tax_shipping(self, tax_shipping):
        """Sets the tax_shipping of this TaxProviderUltraCartState.

        True if shipping should be taxed in this state.  # noqa: E501

        :param tax_shipping: The tax_shipping of this TaxProviderUltraCartState.  # noqa: E501
        :type: bool
        """

        self._tax_shipping = tax_shipping

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
        if issubclass(TaxProviderUltraCartState, dict):
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
        if not isinstance(other, TaxProviderUltraCartState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
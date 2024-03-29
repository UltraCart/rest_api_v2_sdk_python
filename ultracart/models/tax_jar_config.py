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


class TaxJarConfig(object):
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
        'active': 'bool',
        'api_key': 'str',
        'estimate_only': 'bool',
        'send_outside_nexus': 'bool',
        'send_test_orders': 'bool',
        'skip_channel_orders': 'bool',
        'use_distribution_center_from': 'bool'
    }

    attribute_map = {
        'active': 'active',
        'api_key': 'api_key',
        'estimate_only': 'estimate_only',
        'send_outside_nexus': 'send_outside_nexus',
        'send_test_orders': 'send_test_orders',
        'skip_channel_orders': 'skip_channel_orders',
        'use_distribution_center_from': 'use_distribution_center_from'
    }

    def __init__(self, active=None, api_key=None, estimate_only=None, send_outside_nexus=None, send_test_orders=None, skip_channel_orders=None, use_distribution_center_from=None):  # noqa: E501
        """TaxJarConfig - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._api_key = None
        self._estimate_only = None
        self._send_outside_nexus = None
        self._send_test_orders = None
        self._skip_channel_orders = None
        self._use_distribution_center_from = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if api_key is not None:
            self.api_key = api_key
        if estimate_only is not None:
            self.estimate_only = estimate_only
        if send_outside_nexus is not None:
            self.send_outside_nexus = send_outside_nexus
        if send_test_orders is not None:
            self.send_test_orders = send_test_orders
        if skip_channel_orders is not None:
            self.skip_channel_orders = skip_channel_orders
        if use_distribution_center_from is not None:
            self.use_distribution_center_from = use_distribution_center_from

    @property
    def active(self):
        """Gets the active of this TaxJarConfig.  # noqa: E501

        True if TaxJar is active for this merchant  # noqa: E501

        :return: The active of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TaxJarConfig.

        True if TaxJar is active for this merchant  # noqa: E501

        :param active: The active of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def api_key(self):
        """Gets the api_key of this TaxJarConfig.  # noqa: E501

        TaxJar API key  # noqa: E501

        :return: The api_key of this TaxJarConfig.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this TaxJarConfig.

        TaxJar API key  # noqa: E501

        :param api_key: The api_key of this TaxJarConfig.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def estimate_only(self):
        """Gets the estimate_only of this TaxJarConfig.  # noqa: E501

        True if this TaxJar configuration is to estimate taxes only and not report placed orders to TaxJar  # noqa: E501

        :return: The estimate_only of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._estimate_only

    @estimate_only.setter
    def estimate_only(self, estimate_only):
        """Sets the estimate_only of this TaxJarConfig.

        True if this TaxJar configuration is to estimate taxes only and not report placed orders to TaxJar  # noqa: E501

        :param estimate_only: The estimate_only of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._estimate_only = estimate_only

    @property
    def send_outside_nexus(self):
        """Gets the send_outside_nexus of this TaxJarConfig.  # noqa: E501

        Send orders outside your nexus TaxJar.  The default is to not transmit outside orders to TaxJar to reduce API calls.  However, this will prevent TaxJar from dynamically creating new Nexus when thresholds are exceeded for a state.  # noqa: E501

        :return: The send_outside_nexus of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._send_outside_nexus

    @send_outside_nexus.setter
    def send_outside_nexus(self, send_outside_nexus):
        """Sets the send_outside_nexus of this TaxJarConfig.

        Send orders outside your nexus TaxJar.  The default is to not transmit outside orders to TaxJar to reduce API calls.  However, this will prevent TaxJar from dynamically creating new Nexus when thresholds are exceeded for a state.  # noqa: E501

        :param send_outside_nexus: The send_outside_nexus of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._send_outside_nexus = send_outside_nexus

    @property
    def send_test_orders(self):
        """Gets the send_test_orders of this TaxJarConfig.  # noqa: E501

        Send test orders through to TaxJar.  The default is to not transmit test orders to TaxJar.  # noqa: E501

        :return: The send_test_orders of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._send_test_orders

    @send_test_orders.setter
    def send_test_orders(self, send_test_orders):
        """Sets the send_test_orders of this TaxJarConfig.

        Send test orders through to TaxJar.  The default is to not transmit test orders to TaxJar.  # noqa: E501

        :param send_test_orders: The send_test_orders of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._send_test_orders = send_test_orders

    @property
    def skip_channel_orders(self):
        """Gets the skip_channel_orders of this TaxJarConfig.  # noqa: E501

        Do not send channel partner orders to TaxJar.  Set this to true if your channel partner reports tax on their own.  # noqa: E501

        :return: The skip_channel_orders of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._skip_channel_orders

    @skip_channel_orders.setter
    def skip_channel_orders(self, skip_channel_orders):
        """Sets the skip_channel_orders of this TaxJarConfig.

        Do not send channel partner orders to TaxJar.  Set this to true if your channel partner reports tax on their own.  # noqa: E501

        :param skip_channel_orders: The skip_channel_orders of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._skip_channel_orders = skip_channel_orders

    @property
    def use_distribution_center_from(self):
        """Gets the use_distribution_center_from of this TaxJarConfig.  # noqa: E501

        Use distribution center from address  # noqa: E501

        :return: The use_distribution_center_from of this TaxJarConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_distribution_center_from

    @use_distribution_center_from.setter
    def use_distribution_center_from(self, use_distribution_center_from):
        """Sets the use_distribution_center_from of this TaxJarConfig.

        Use distribution center from address  # noqa: E501

        :param use_distribution_center_from: The use_distribution_center_from of this TaxJarConfig.  # noqa: E501
        :type: bool
        """

        self._use_distribution_center_from = use_distribution_center_from

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
        if issubclass(TaxJarConfig, dict):
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
        if not isinstance(other, TaxJarConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

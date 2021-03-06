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


class ItemDigitalDelivery(object):
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
        'activation_code_description': 'str',
        'activation_code_low_warning': 'int',
        'activation_code_realtime_url': 'str',
        'activation_code_shared_secret': 'str',
        'activation_code_type': 'str',
        'digital_items': 'list[ItemDigitalItem]'
    }

    attribute_map = {
        'activation_code_description': 'activation_code_description',
        'activation_code_low_warning': 'activation_code_low_warning',
        'activation_code_realtime_url': 'activation_code_realtime_url',
        'activation_code_shared_secret': 'activation_code_shared_secret',
        'activation_code_type': 'activation_code_type',
        'digital_items': 'digital_items'
    }

    def __init__(self, activation_code_description=None, activation_code_low_warning=None, activation_code_realtime_url=None, activation_code_shared_secret=None, activation_code_type=None, digital_items=None):  # noqa: E501
        """ItemDigitalDelivery - a model defined in Swagger"""  # noqa: E501

        self._activation_code_description = None
        self._activation_code_low_warning = None
        self._activation_code_realtime_url = None
        self._activation_code_shared_secret = None
        self._activation_code_type = None
        self._digital_items = None
        self.discriminator = None

        if activation_code_description is not None:
            self.activation_code_description = activation_code_description
        if activation_code_low_warning is not None:
            self.activation_code_low_warning = activation_code_low_warning
        if activation_code_realtime_url is not None:
            self.activation_code_realtime_url = activation_code_realtime_url
        if activation_code_shared_secret is not None:
            self.activation_code_shared_secret = activation_code_shared_secret
        if activation_code_type is not None:
            self.activation_code_type = activation_code_type
        if digital_items is not None:
            self.digital_items = digital_items

    @property
    def activation_code_description(self):
        """Gets the activation_code_description of this ItemDigitalDelivery.  # noqa: E501

        Description of the activation code  # noqa: E501

        :return: The activation_code_description of this ItemDigitalDelivery.  # noqa: E501
        :rtype: str
        """
        return self._activation_code_description

    @activation_code_description.setter
    def activation_code_description(self, activation_code_description):
        """Sets the activation_code_description of this ItemDigitalDelivery.

        Description of the activation code  # noqa: E501

        :param activation_code_description: The activation_code_description of this ItemDigitalDelivery.  # noqa: E501
        :type: str
        """
        if activation_code_description is not None and len(activation_code_description) > 50:
            raise ValueError("Invalid value for `activation_code_description`, length must be less than or equal to `50`")  # noqa: E501

        self._activation_code_description = activation_code_description

    @property
    def activation_code_low_warning(self):
        """Gets the activation_code_low_warning of this ItemDigitalDelivery.  # noqa: E501

        The number of activation codes whcih should generate a warning email  # noqa: E501

        :return: The activation_code_low_warning of this ItemDigitalDelivery.  # noqa: E501
        :rtype: int
        """
        return self._activation_code_low_warning

    @activation_code_low_warning.setter
    def activation_code_low_warning(self, activation_code_low_warning):
        """Sets the activation_code_low_warning of this ItemDigitalDelivery.

        The number of activation codes whcih should generate a warning email  # noqa: E501

        :param activation_code_low_warning: The activation_code_low_warning of this ItemDigitalDelivery.  # noqa: E501
        :type: int
        """

        self._activation_code_low_warning = activation_code_low_warning

    @property
    def activation_code_realtime_url(self):
        """Gets the activation_code_realtime_url of this ItemDigitalDelivery.  # noqa: E501

        The URL to retrieve activation codes from in real-time  # noqa: E501

        :return: The activation_code_realtime_url of this ItemDigitalDelivery.  # noqa: E501
        :rtype: str
        """
        return self._activation_code_realtime_url

    @activation_code_realtime_url.setter
    def activation_code_realtime_url(self, activation_code_realtime_url):
        """Sets the activation_code_realtime_url of this ItemDigitalDelivery.

        The URL to retrieve activation codes from in real-time  # noqa: E501

        :param activation_code_realtime_url: The activation_code_realtime_url of this ItemDigitalDelivery.  # noqa: E501
        :type: str
        """
        if activation_code_realtime_url is not None and len(activation_code_realtime_url) > 350:
            raise ValueError("Invalid value for `activation_code_realtime_url`, length must be less than or equal to `350`")  # noqa: E501

        self._activation_code_realtime_url = activation_code_realtime_url

    @property
    def activation_code_shared_secret(self):
        """Gets the activation_code_shared_secret of this ItemDigitalDelivery.  # noqa: E501

        Shared secret used when communicating with the real-time URL  # noqa: E501

        :return: The activation_code_shared_secret of this ItemDigitalDelivery.  # noqa: E501
        :rtype: str
        """
        return self._activation_code_shared_secret

    @activation_code_shared_secret.setter
    def activation_code_shared_secret(self, activation_code_shared_secret):
        """Sets the activation_code_shared_secret of this ItemDigitalDelivery.

        Shared secret used when communicating with the real-time URL  # noqa: E501

        :param activation_code_shared_secret: The activation_code_shared_secret of this ItemDigitalDelivery.  # noqa: E501
        :type: str
        """
        if activation_code_shared_secret is not None and len(activation_code_shared_secret) > 20:
            raise ValueError("Invalid value for `activation_code_shared_secret`, length must be less than or equal to `20`")  # noqa: E501

        self._activation_code_shared_secret = activation_code_shared_secret

    @property
    def activation_code_type(self):
        """Gets the activation_code_type of this ItemDigitalDelivery.  # noqa: E501

        Type of activation code  # noqa: E501

        :return: The activation_code_type of this ItemDigitalDelivery.  # noqa: E501
        :rtype: str
        """
        return self._activation_code_type

    @activation_code_type.setter
    def activation_code_type(self, activation_code_type):
        """Sets the activation_code_type of this ItemDigitalDelivery.

        Type of activation code  # noqa: E501

        :param activation_code_type: The activation_code_type of this ItemDigitalDelivery.  # noqa: E501
        :type: str
        """

        self._activation_code_type = activation_code_type

    @property
    def digital_items(self):
        """Gets the digital_items of this ItemDigitalDelivery.  # noqa: E501

        Digital items that customer can download when this item is purchased  # noqa: E501

        :return: The digital_items of this ItemDigitalDelivery.  # noqa: E501
        :rtype: list[ItemDigitalItem]
        """
        return self._digital_items

    @digital_items.setter
    def digital_items(self, digital_items):
        """Sets the digital_items of this ItemDigitalDelivery.

        Digital items that customer can download when this item is purchased  # noqa: E501

        :param digital_items: The digital_items of this ItemDigitalDelivery.  # noqa: E501
        :type: list[ItemDigitalItem]
        """

        self._digital_items = digital_items

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
        if issubclass(ItemDigitalDelivery, dict):
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
        if not isinstance(other, ItemDigitalDelivery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

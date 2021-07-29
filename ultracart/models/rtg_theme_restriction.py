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


class RtgThemeRestriction(object):
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
        'restriction': 'str',
        'storefront_host_name': 'str',
        'theme_code': 'str'
    }

    attribute_map = {
        'restriction': 'restriction',
        'storefront_host_name': 'storefront_host_name',
        'theme_code': 'theme_code'
    }

    def __init__(self, restriction=None, storefront_host_name=None, theme_code=None):  # noqa: E501
        """RtgThemeRestriction - a model defined in Swagger"""  # noqa: E501

        self._restriction = None
        self._storefront_host_name = None
        self._theme_code = None
        self.discriminator = None

        if restriction is not None:
            self.restriction = restriction
        if storefront_host_name is not None:
            self.storefront_host_name = storefront_host_name
        if theme_code is not None:
            self.theme_code = theme_code

    @property
    def restriction(self):
        """Gets the restriction of this RtgThemeRestriction.  # noqa: E501

        Any restriction for this theme  # noqa: E501

        :return: The restriction of this RtgThemeRestriction.  # noqa: E501
        :rtype: str
        """
        return self._restriction

    @restriction.setter
    def restriction(self, restriction):
        """Sets the restriction of this RtgThemeRestriction.

        Any restriction for this theme  # noqa: E501

        :param restriction: The restriction of this RtgThemeRestriction.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "valid", "validOnly"]  # noqa: E501
        if restriction not in allowed_values:
            raise ValueError(
                "Invalid value for `restriction` ({0}), must be one of {1}"  # noqa: E501
                .format(restriction, allowed_values)
            )

        self._restriction = restriction

    @property
    def storefront_host_name(self):
        """Gets the storefront_host_name of this RtgThemeRestriction.  # noqa: E501

        The server name for this theme.  This will not be populated for legacy (ancient) themes  # noqa: E501

        :return: The storefront_host_name of this RtgThemeRestriction.  # noqa: E501
        :rtype: str
        """
        return self._storefront_host_name

    @storefront_host_name.setter
    def storefront_host_name(self, storefront_host_name):
        """Sets the storefront_host_name of this RtgThemeRestriction.

        The server name for this theme.  This will not be populated for legacy (ancient) themes  # noqa: E501

        :param storefront_host_name: The storefront_host_name of this RtgThemeRestriction.  # noqa: E501
        :type: str
        """

        self._storefront_host_name = storefront_host_name

    @property
    def theme_code(self):
        """Gets the theme_code of this RtgThemeRestriction.  # noqa: E501

        Human friendly short code for this theme  # noqa: E501

        :return: The theme_code of this RtgThemeRestriction.  # noqa: E501
        :rtype: str
        """
        return self._theme_code

    @theme_code.setter
    def theme_code(self, theme_code):
        """Sets the theme_code of this RtgThemeRestriction.

        Human friendly short code for this theme  # noqa: E501

        :param theme_code: The theme_code of this RtgThemeRestriction.  # noqa: E501
        :type: str
        """

        self._theme_code = theme_code

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
        if issubclass(RtgThemeRestriction, dict):
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
        if not isinstance(other, RtgThemeRestriction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

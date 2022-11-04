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


class SingleSignOnAuthorizeResponse(object):
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
        'expiration_dts': 'str',
        'login_url': 'str'
    }

    attribute_map = {
        'expiration_dts': 'expiration_dts',
        'login_url': 'login_url'
    }

    def __init__(self, expiration_dts=None, login_url=None):  # noqa: E501
        """SingleSignOnAuthorizeResponse - a model defined in Swagger"""  # noqa: E501

        self._expiration_dts = None
        self._login_url = None
        self.discriminator = None

        if expiration_dts is not None:
            self.expiration_dts = expiration_dts
        if login_url is not None:
            self.login_url = login_url

    @property
    def expiration_dts(self):
        """Gets the expiration_dts of this SingleSignOnAuthorizeResponse.  # noqa: E501

        Expiration date/time after which the single sign-on login operation will have timed out  # noqa: E501

        :return: The expiration_dts of this SingleSignOnAuthorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts

    @expiration_dts.setter
    def expiration_dts(self, expiration_dts):
        """Sets the expiration_dts of this SingleSignOnAuthorizeResponse.

        Expiration date/time after which the single sign-on login operation will have timed out  # noqa: E501

        :param expiration_dts: The expiration_dts of this SingleSignOnAuthorizeResponse.  # noqa: E501
        :type: str
        """

        self._expiration_dts = expiration_dts

    @property
    def login_url(self):
        """Gets the login_url of this SingleSignOnAuthorizeResponse.  # noqa: E501

        The URL that you should redirect the customer's browser to.  This URL will begin the login process.  # noqa: E501

        :return: The login_url of this SingleSignOnAuthorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """Sets the login_url of this SingleSignOnAuthorizeResponse.

        The URL that you should redirect the customer's browser to.  This URL will begin the login process.  # noqa: E501

        :param login_url: The login_url of this SingleSignOnAuthorizeResponse.  # noqa: E501
        :type: str
        """

        self._login_url = login_url

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
        if issubclass(SingleSignOnAuthorizeResponse, dict):
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
        if not isinstance(other, SingleSignOnAuthorizeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
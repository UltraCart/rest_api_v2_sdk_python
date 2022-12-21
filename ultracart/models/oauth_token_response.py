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


class OauthTokenResponse(object):
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
        'access_token': 'str',
        'error': 'str',
        'error_description': 'str',
        'error_uri': 'str',
        'expires_in': 'str',
        'refresh_token': 'str',
        'scope': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'error': 'error',
        'error_description': 'error_description',
        'error_uri': 'error_uri',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'scope': 'scope',
        'token_type': 'token_type'
    }

    def __init__(self, access_token=None, error=None, error_description=None, error_uri=None, expires_in=None, refresh_token=None, scope=None, token_type=None):  # noqa: E501
        """OauthTokenResponse - a model defined in Swagger"""  # noqa: E501

        self._access_token = None
        self._error = None
        self._error_description = None
        self._error_uri = None
        self._expires_in = None
        self._refresh_token = None
        self._scope = None
        self._token_type = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if error is not None:
            self.error = error
        if error_description is not None:
            self.error_description = error_description
        if error_uri is not None:
            self.error_uri = error_uri
        if expires_in is not None:
            self.expires_in = expires_in
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if scope is not None:
            self.scope = scope
        if token_type is not None:
            self.token_type = token_type

    @property
    def access_token(self):
        """Gets the access_token of this OauthTokenResponse.  # noqa: E501

        Access token to use in OAuth authenticated API call  # noqa: E501

        :return: The access_token of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OauthTokenResponse.

        Access token to use in OAuth authenticated API call  # noqa: E501

        :param access_token: The access_token of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def error(self):
        """Gets the error of this OauthTokenResponse.  # noqa: E501


        :return: The error of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OauthTokenResponse.


        :param error: The error of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this OauthTokenResponse.  # noqa: E501


        :return: The error_description of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this OauthTokenResponse.


        :param error_description: The error_description of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def error_uri(self):
        """Gets the error_uri of this OauthTokenResponse.  # noqa: E501


        :return: The error_uri of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_uri

    @error_uri.setter
    def error_uri(self, error_uri):
        """Sets the error_uri of this OauthTokenResponse.


        :param error_uri: The error_uri of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._error_uri = error_uri

    @property
    def expires_in(self):
        """Gets the expires_in of this OauthTokenResponse.  # noqa: E501

        The number of seconds since issuance when the access token will expire and need to be refreshed using the refresh token  # noqa: E501

        :return: The expires_in of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this OauthTokenResponse.

        The number of seconds since issuance when the access token will expire and need to be refreshed using the refresh token  # noqa: E501

        :param expires_in: The expires_in of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """Gets the refresh_token of this OauthTokenResponse.  # noqa: E501

        The refresh token that should be used to fetch a new access token when the expiration occurs  # noqa: E501

        :return: The refresh_token of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this OauthTokenResponse.

        The refresh token that should be used to fetch a new access token when the expiration occurs  # noqa: E501

        :param refresh_token: The refresh_token of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """Gets the scope of this OauthTokenResponse.  # noqa: E501

        The scope of permissions associated with teh access token  # noqa: E501

        :return: The scope of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OauthTokenResponse.

        The scope of permissions associated with teh access token  # noqa: E501

        :param scope: The scope of this OauthTokenResponse.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """Gets the token_type of this OauthTokenResponse.  # noqa: E501

        Type of token  # noqa: E501

        :return: The token_type of this OauthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this OauthTokenResponse.

        Type of token  # noqa: E501

        :param token_type: The token_type of this OauthTokenResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["bearer"]  # noqa: E501
        if token_type not in allowed_values:
            raise ValueError(
                "Invalid value for `token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(token_type, allowed_values)
            )

        self._token_type = token_type

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
        if issubclass(OauthTokenResponse, dict):
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
        if not isinstance(other, OauthTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class EmailThirdPartyProvider(object):
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
        'connect_url': 'str',
        'list_count': 'int',
        'lists': 'list[EmailThirdPartyList]',
        'logo_url': 'str',
        'name': 'str'
    }

    attribute_map = {
        'connect_url': 'connect_url',
        'list_count': 'list_count',
        'lists': 'lists',
        'logo_url': 'logo_url',
        'name': 'name'
    }

    def __init__(self, connect_url=None, list_count=None, lists=None, logo_url=None, name=None):
        """
        EmailThirdPartyProvider - a model defined in Swagger
        """

        self._connect_url = None
        self._list_count = None
        self._lists = None
        self._logo_url = None
        self._name = None
        self.discriminator = None

        if connect_url is not None:
          self.connect_url = connect_url
        if list_count is not None:
          self.list_count = list_count
        if lists is not None:
          self.lists = lists
        if logo_url is not None:
          self.logo_url = logo_url
        if name is not None:
          self.name = name

    @property
    def connect_url(self):
        """
        Gets the connect_url of this EmailThirdPartyProvider.
        URL to the settings screen to connect.  Null if the provider is already connected.

        :return: The connect_url of this EmailThirdPartyProvider.
        :rtype: str
        """
        return self._connect_url

    @connect_url.setter
    def connect_url(self, connect_url):
        """
        Sets the connect_url of this EmailThirdPartyProvider.
        URL to the settings screen to connect.  Null if the provider is already connected.

        :param connect_url: The connect_url of this EmailThirdPartyProvider.
        :type: str
        """

        self._connect_url = connect_url

    @property
    def list_count(self):
        """
        Gets the list_count of this EmailThirdPartyProvider.
        list_count

        :return: The list_count of this EmailThirdPartyProvider.
        :rtype: int
        """
        return self._list_count

    @list_count.setter
    def list_count(self, list_count):
        """
        Sets the list_count of this EmailThirdPartyProvider.
        list_count

        :param list_count: The list_count of this EmailThirdPartyProvider.
        :type: int
        """

        self._list_count = list_count

    @property
    def lists(self):
        """
        Gets the lists of this EmailThirdPartyProvider.
        lists

        :return: The lists of this EmailThirdPartyProvider.
        :rtype: list[EmailThirdPartyList]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """
        Sets the lists of this EmailThirdPartyProvider.
        lists

        :param lists: The lists of this EmailThirdPartyProvider.
        :type: list[EmailThirdPartyList]
        """

        self._lists = lists

    @property
    def logo_url(self):
        """
        Gets the logo_url of this EmailThirdPartyProvider.
        logo_url

        :return: The logo_url of this EmailThirdPartyProvider.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this EmailThirdPartyProvider.
        logo_url

        :param logo_url: The logo_url of this EmailThirdPartyProvider.
        :type: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """
        Gets the name of this EmailThirdPartyProvider.
        name

        :return: The name of this EmailThirdPartyProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailThirdPartyProvider.
        name

        :param name: The name of this EmailThirdPartyProvider.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, EmailThirdPartyProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

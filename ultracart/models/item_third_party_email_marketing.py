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


class ItemThirdPartyEmailMarketing(object):
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
        'add_tags': 'list[str]',
        'provider_name': 'str',
        'remove_tags': 'list[str]',
        'subscribe_lists': 'list[str]',
        'unsubscribe_lists': 'list[str]'
    }

    attribute_map = {
        'add_tags': 'add_tags',
        'provider_name': 'provider_name',
        'remove_tags': 'remove_tags',
        'subscribe_lists': 'subscribe_lists',
        'unsubscribe_lists': 'unsubscribe_lists'
    }

    def __init__(self, add_tags=None, provider_name=None, remove_tags=None, subscribe_lists=None, unsubscribe_lists=None):  # noqa: E501
        """ItemThirdPartyEmailMarketing - a model defined in Swagger"""  # noqa: E501

        self._add_tags = None
        self._provider_name = None
        self._remove_tags = None
        self._subscribe_lists = None
        self._unsubscribe_lists = None
        self.discriminator = None

        if add_tags is not None:
            self.add_tags = add_tags
        if provider_name is not None:
            self.provider_name = provider_name
        if remove_tags is not None:
            self.remove_tags = remove_tags
        if subscribe_lists is not None:
            self.subscribe_lists = subscribe_lists
        if unsubscribe_lists is not None:
            self.unsubscribe_lists = unsubscribe_lists

    @property
    def add_tags(self):
        """Gets the add_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501

        Add tags  # noqa: E501

        :return: The add_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_tags

    @add_tags.setter
    def add_tags(self, add_tags):
        """Sets the add_tags of this ItemThirdPartyEmailMarketing.

        Add tags  # noqa: E501

        :param add_tags: The add_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :type: list[str]
        """

        self._add_tags = add_tags

    @property
    def provider_name(self):
        """Gets the provider_name of this ItemThirdPartyEmailMarketing.  # noqa: E501

        Provider name  # noqa: E501

        :return: The provider_name of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ItemThirdPartyEmailMarketing.

        Provider name  # noqa: E501

        :param provider_name: The provider_name of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :type: str
        """
        allowed_values = ["ActiveCampaign", "AWeber", "Campaign Monitor", "ConstantContact", "Emma", "GetResponse", "iContact", "Klaviyo", "Lyris", "LyrisHQ", "MailChimp", "SilverPop"]  # noqa: E501
        if provider_name not in allowed_values:
            raise ValueError(
                "Invalid value for `provider_name` ({0}), must be one of {1}"  # noqa: E501
                .format(provider_name, allowed_values)
            )

        self._provider_name = provider_name

    @property
    def remove_tags(self):
        """Gets the remove_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501

        Remove tags  # noqa: E501

        :return: The remove_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_tags

    @remove_tags.setter
    def remove_tags(self, remove_tags):
        """Sets the remove_tags of this ItemThirdPartyEmailMarketing.

        Remove tags  # noqa: E501

        :param remove_tags: The remove_tags of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :type: list[str]
        """

        self._remove_tags = remove_tags

    @property
    def subscribe_lists(self):
        """Gets the subscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501

        Subscribe to lists  # noqa: E501

        :return: The subscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :rtype: list[str]
        """
        return self._subscribe_lists

    @subscribe_lists.setter
    def subscribe_lists(self, subscribe_lists):
        """Sets the subscribe_lists of this ItemThirdPartyEmailMarketing.

        Subscribe to lists  # noqa: E501

        :param subscribe_lists: The subscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :type: list[str]
        """

        self._subscribe_lists = subscribe_lists

    @property
    def unsubscribe_lists(self):
        """Gets the unsubscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501

        Unsubscribe from lists  # noqa: E501

        :return: The unsubscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :rtype: list[str]
        """
        return self._unsubscribe_lists

    @unsubscribe_lists.setter
    def unsubscribe_lists(self, unsubscribe_lists):
        """Sets the unsubscribe_lists of this ItemThirdPartyEmailMarketing.

        Unsubscribe from lists  # noqa: E501

        :param unsubscribe_lists: The unsubscribe_lists of this ItemThirdPartyEmailMarketing.  # noqa: E501
        :type: list[str]
        """

        self._unsubscribe_lists = unsubscribe_lists

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
        if issubclass(ItemThirdPartyEmailMarketing, dict):
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
        if not isinstance(other, ItemThirdPartyEmailMarketing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class EmailCustomer(object):
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
        'email': 'str',
        'email_customer_uuid': 'str',
        'first_name': 'str',
        'global_unsubscribe': 'bool',
        'last_interaction_dts': 'str',
        'last_name': 'str',
        'list_uuids': 'list[str]'
    }

    attribute_map = {
        'active': 'active',
        'email': 'email',
        'email_customer_uuid': 'email_customer_uuid',
        'first_name': 'first_name',
        'global_unsubscribe': 'global_unsubscribe',
        'last_interaction_dts': 'last_interaction_dts',
        'last_name': 'last_name',
        'list_uuids': 'list_uuids'
    }

    def __init__(self, active=None, email=None, email_customer_uuid=None, first_name=None, global_unsubscribe=None, last_interaction_dts=None, last_name=None, list_uuids=None):  # noqa: E501
        """EmailCustomer - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._email = None
        self._email_customer_uuid = None
        self._first_name = None
        self._global_unsubscribe = None
        self._last_interaction_dts = None
        self._last_name = None
        self._list_uuids = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if email is not None:
            self.email = email
        if email_customer_uuid is not None:
            self.email_customer_uuid = email_customer_uuid
        if first_name is not None:
            self.first_name = first_name
        if global_unsubscribe is not None:
            self.global_unsubscribe = global_unsubscribe
        if last_interaction_dts is not None:
            self.last_interaction_dts = last_interaction_dts
        if last_name is not None:
            self.last_name = last_name
        if list_uuids is not None:
            self.list_uuids = list_uuids

    @property
    def active(self):
        """Gets the active of this EmailCustomer.  # noqa: E501

        True if the customer is flagged as active within StoreFront Communications  # noqa: E501

        :return: The active of this EmailCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EmailCustomer.

        True if the customer is flagged as active within StoreFront Communications  # noqa: E501

        :param active: The active of this EmailCustomer.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def email(self):
        """Gets the email of this EmailCustomer.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this EmailCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmailCustomer.

        Email  # noqa: E501

        :param email: The email of this EmailCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_customer_uuid(self):
        """Gets the email_customer_uuid of this EmailCustomer.  # noqa: E501

        Email customer UUID  # noqa: E501

        :return: The email_customer_uuid of this EmailCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email_customer_uuid

    @email_customer_uuid.setter
    def email_customer_uuid(self, email_customer_uuid):
        """Sets the email_customer_uuid of this EmailCustomer.

        Email customer UUID  # noqa: E501

        :param email_customer_uuid: The email_customer_uuid of this EmailCustomer.  # noqa: E501
        :type: str
        """

        self._email_customer_uuid = email_customer_uuid

    @property
    def first_name(self):
        """Gets the first_name of this EmailCustomer.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this EmailCustomer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EmailCustomer.

        First name  # noqa: E501

        :param first_name: The first_name of this EmailCustomer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def global_unsubscribe(self):
        """Gets the global_unsubscribe of this EmailCustomer.  # noqa: E501

        True if the customer has globally unsubscribed from all communication.  # noqa: E501

        :return: The global_unsubscribe of this EmailCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._global_unsubscribe

    @global_unsubscribe.setter
    def global_unsubscribe(self, global_unsubscribe):
        """Sets the global_unsubscribe of this EmailCustomer.

        True if the customer has globally unsubscribed from all communication.  # noqa: E501

        :param global_unsubscribe: The global_unsubscribe of this EmailCustomer.  # noqa: E501
        :type: bool
        """

        self._global_unsubscribe = global_unsubscribe

    @property
    def last_interaction_dts(self):
        """Gets the last_interaction_dts of this EmailCustomer.  # noqa: E501

        Last interaction  # noqa: E501

        :return: The last_interaction_dts of this EmailCustomer.  # noqa: E501
        :rtype: str
        """
        return self._last_interaction_dts

    @last_interaction_dts.setter
    def last_interaction_dts(self, last_interaction_dts):
        """Sets the last_interaction_dts of this EmailCustomer.

        Last interaction  # noqa: E501

        :param last_interaction_dts: The last_interaction_dts of this EmailCustomer.  # noqa: E501
        :type: str
        """

        self._last_interaction_dts = last_interaction_dts

    @property
    def last_name(self):
        """Gets the last_name of this EmailCustomer.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this EmailCustomer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this EmailCustomer.

        Last name  # noqa: E501

        :param last_name: The last_name of this EmailCustomer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def list_uuids(self):
        """Gets the list_uuids of this EmailCustomer.  # noqa: E501

        UUIDs of the lists they are subscribed to  # noqa: E501

        :return: The list_uuids of this EmailCustomer.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_uuids

    @list_uuids.setter
    def list_uuids(self, list_uuids):
        """Sets the list_uuids of this EmailCustomer.

        UUIDs of the lists they are subscribed to  # noqa: E501

        :param list_uuids: The list_uuids of this EmailCustomer.  # noqa: E501
        :type: list[str]
        """

        self._list_uuids = list_uuids

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
        if issubclass(EmailCustomer, dict):
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
        if not isinstance(other, EmailCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
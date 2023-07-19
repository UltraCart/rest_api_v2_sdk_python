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


class ChannelPartner(object):
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
        'channel_partner_oid': 'int',
        'code': 'str',
        'communication_method': 'str',
        'dont_hold_shipment': 'bool',
        'inactive': 'bool',
        'merchant_id': 'str',
        'name': 'str',
        'skip_customer_emails': 'bool'
    }

    attribute_map = {
        'channel_partner_oid': 'channel_partner_oid',
        'code': 'code',
        'communication_method': 'communication_method',
        'dont_hold_shipment': 'dont_hold_shipment',
        'inactive': 'inactive',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'skip_customer_emails': 'skip_customer_emails'
    }

    def __init__(self, channel_partner_oid=None, code=None, communication_method=None, dont_hold_shipment=None, inactive=None, merchant_id=None, name=None, skip_customer_emails=None):  # noqa: E501
        """ChannelPartner - a model defined in Swagger"""  # noqa: E501

        self._channel_partner_oid = None
        self._code = None
        self._communication_method = None
        self._dont_hold_shipment = None
        self._inactive = None
        self._merchant_id = None
        self._name = None
        self._skip_customer_emails = None
        self.discriminator = None

        if channel_partner_oid is not None:
            self.channel_partner_oid = channel_partner_oid
        if code is not None:
            self.code = code
        if communication_method is not None:
            self.communication_method = communication_method
        if dont_hold_shipment is not None:
            self.dont_hold_shipment = dont_hold_shipment
        if inactive is not None:
            self.inactive = inactive
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if skip_customer_emails is not None:
            self.skip_customer_emails = skip_customer_emails

    @property
    def channel_partner_oid(self):
        """Gets the channel_partner_oid of this ChannelPartner.  # noqa: E501

        Channel partner object id  # noqa: E501

        :return: The channel_partner_oid of this ChannelPartner.  # noqa: E501
        :rtype: int
        """
        return self._channel_partner_oid

    @channel_partner_oid.setter
    def channel_partner_oid(self, channel_partner_oid):
        """Sets the channel_partner_oid of this ChannelPartner.

        Channel partner object id  # noqa: E501

        :param channel_partner_oid: The channel_partner_oid of this ChannelPartner.  # noqa: E501
        :type: int
        """

        self._channel_partner_oid = channel_partner_oid

    @property
    def code(self):
        """Gets the code of this ChannelPartner.  # noqa: E501

        Code associated with the channel partner  # noqa: E501

        :return: The code of this ChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ChannelPartner.

        Code associated with the channel partner  # noqa: E501

        :param code: The code of this ChannelPartner.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def communication_method(self):
        """Gets the communication_method of this ChannelPartner.  # noqa: E501

        Communication method of the channel partner  # noqa: E501

        :return: The communication_method of this ChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._communication_method

    @communication_method.setter
    def communication_method(self, communication_method):
        """Sets the communication_method of this ChannelPartner.

        Communication method of the channel partner  # noqa: E501

        :param communication_method: The communication_method of this ChannelPartner.  # noqa: E501
        :type: str
        """

        self._communication_method = communication_method

    @property
    def dont_hold_shipment(self):
        """Gets the dont_hold_shipment of this ChannelPartner.  # noqa: E501

        True if shipments should immediately process for this channel partner.  # noqa: E501

        :return: The dont_hold_shipment of this ChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._dont_hold_shipment

    @dont_hold_shipment.setter
    def dont_hold_shipment(self, dont_hold_shipment):
        """Sets the dont_hold_shipment of this ChannelPartner.

        True if shipments should immediately process for this channel partner.  # noqa: E501

        :param dont_hold_shipment: The dont_hold_shipment of this ChannelPartner.  # noqa: E501
        :type: bool
        """

        self._dont_hold_shipment = dont_hold_shipment

    @property
    def inactive(self):
        """Gets the inactive of this ChannelPartner.  # noqa: E501

        True if the channel partner is inactive  # noqa: E501

        :return: The inactive of this ChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """Sets the inactive of this ChannelPartner.

        True if the channel partner is inactive  # noqa: E501

        :param inactive: The inactive of this ChannelPartner.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ChannelPartner.  # noqa: E501

        Merchant ID of the channel partner  # noqa: E501

        :return: The merchant_id of this ChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ChannelPartner.

        Merchant ID of the channel partner  # noqa: E501

        :param merchant_id: The merchant_id of this ChannelPartner.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this ChannelPartner.  # noqa: E501

        Name of the channel partner  # noqa: E501

        :return: The name of this ChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelPartner.

        Name of the channel partner  # noqa: E501

        :param name: The name of this ChannelPartner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def skip_customer_emails(self):
        """Gets the skip_customer_emails of this ChannelPartner.  # noqa: E501

        True if emails to the customer are skipped for this channel partner.  # noqa: E501

        :return: The skip_customer_emails of this ChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._skip_customer_emails

    @skip_customer_emails.setter
    def skip_customer_emails(self, skip_customer_emails):
        """Sets the skip_customer_emails of this ChannelPartner.

        True if emails to the customer are skipped for this channel partner.  # noqa: E501

        :param skip_customer_emails: The skip_customer_emails of this ChannelPartner.  # noqa: E501
        :type: bool
        """

        self._skip_customer_emails = skip_customer_emails

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
        if issubclass(ChannelPartner, dict):
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
        if not isinstance(other, ChannelPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class OrderChannelPartner(object):
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
        'auto_approve_purchase_order': 'bool',
        'channel_partner_code': 'str',
        'channel_partner_data': 'str',
        'channel_partner_oid': 'int',
        'channel_partner_order_id': 'str',
        'ignore_invalid_shipping_method': 'bool',
        'no_realtime_payment_processing': 'bool',
        'skip_payment_processing': 'bool',
        'store_completed': 'bool',
        'store_if_payment_declines': 'bool',
        'treat_warnings_as_errors': 'bool'
    }

    attribute_map = {
        'auto_approve_purchase_order': 'auto_approve_purchase_order',
        'channel_partner_code': 'channel_partner_code',
        'channel_partner_data': 'channel_partner_data',
        'channel_partner_oid': 'channel_partner_oid',
        'channel_partner_order_id': 'channel_partner_order_id',
        'ignore_invalid_shipping_method': 'ignore_invalid_shipping_method',
        'no_realtime_payment_processing': 'no_realtime_payment_processing',
        'skip_payment_processing': 'skip_payment_processing',
        'store_completed': 'store_completed',
        'store_if_payment_declines': 'store_if_payment_declines',
        'treat_warnings_as_errors': 'treat_warnings_as_errors'
    }

    def __init__(self, auto_approve_purchase_order=None, channel_partner_code=None, channel_partner_data=None, channel_partner_oid=None, channel_partner_order_id=None, ignore_invalid_shipping_method=None, no_realtime_payment_processing=None, skip_payment_processing=None, store_completed=None, store_if_payment_declines=None, treat_warnings_as_errors=None):  # noqa: E501
        """OrderChannelPartner - a model defined in Swagger"""  # noqa: E501

        self._auto_approve_purchase_order = None
        self._channel_partner_code = None
        self._channel_partner_data = None
        self._channel_partner_oid = None
        self._channel_partner_order_id = None
        self._ignore_invalid_shipping_method = None
        self._no_realtime_payment_processing = None
        self._skip_payment_processing = None
        self._store_completed = None
        self._store_if_payment_declines = None
        self._treat_warnings_as_errors = None
        self.discriminator = None

        if auto_approve_purchase_order is not None:
            self.auto_approve_purchase_order = auto_approve_purchase_order
        if channel_partner_code is not None:
            self.channel_partner_code = channel_partner_code
        if channel_partner_data is not None:
            self.channel_partner_data = channel_partner_data
        if channel_partner_oid is not None:
            self.channel_partner_oid = channel_partner_oid
        if channel_partner_order_id is not None:
            self.channel_partner_order_id = channel_partner_order_id
        if ignore_invalid_shipping_method is not None:
            self.ignore_invalid_shipping_method = ignore_invalid_shipping_method
        if no_realtime_payment_processing is not None:
            self.no_realtime_payment_processing = no_realtime_payment_processing
        if skip_payment_processing is not None:
            self.skip_payment_processing = skip_payment_processing
        if store_completed is not None:
            self.store_completed = store_completed
        if store_if_payment_declines is not None:
            self.store_if_payment_declines = store_if_payment_declines
        if treat_warnings_as_errors is not None:
            self.treat_warnings_as_errors = treat_warnings_as_errors

    @property
    def auto_approve_purchase_order(self):
        """Gets the auto_approve_purchase_order of this OrderChannelPartner.  # noqa: E501

        If true, any purchase order submitted is automatically approved  # noqa: E501

        :return: The auto_approve_purchase_order of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve_purchase_order

    @auto_approve_purchase_order.setter
    def auto_approve_purchase_order(self, auto_approve_purchase_order):
        """Sets the auto_approve_purchase_order of this OrderChannelPartner.

        If true, any purchase order submitted is automatically approved  # noqa: E501

        :param auto_approve_purchase_order: The auto_approve_purchase_order of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._auto_approve_purchase_order = auto_approve_purchase_order

    @property
    def channel_partner_code(self):
        """Gets the channel_partner_code of this OrderChannelPartner.  # noqa: E501

        The code of the channel partner  # noqa: E501

        :return: The channel_partner_code of this OrderChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._channel_partner_code

    @channel_partner_code.setter
    def channel_partner_code(self, channel_partner_code):
        """Sets the channel_partner_code of this OrderChannelPartner.

        The code of the channel partner  # noqa: E501

        :param channel_partner_code: The channel_partner_code of this OrderChannelPartner.  # noqa: E501
        :type: str
        """

        self._channel_partner_code = channel_partner_code

    @property
    def channel_partner_data(self):
        """Gets the channel_partner_data of this OrderChannelPartner.  # noqa: E501

        Additional data provided by the channel partner, read-only  # noqa: E501

        :return: The channel_partner_data of this OrderChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._channel_partner_data

    @channel_partner_data.setter
    def channel_partner_data(self, channel_partner_data):
        """Sets the channel_partner_data of this OrderChannelPartner.

        Additional data provided by the channel partner, read-only  # noqa: E501

        :param channel_partner_data: The channel_partner_data of this OrderChannelPartner.  # noqa: E501
        :type: str
        """

        self._channel_partner_data = channel_partner_data

    @property
    def channel_partner_oid(self):
        """Gets the channel_partner_oid of this OrderChannelPartner.  # noqa: E501

        Channel partner object identifier, read-only and available on existing channel orders only.  # noqa: E501

        :return: The channel_partner_oid of this OrderChannelPartner.  # noqa: E501
        :rtype: int
        """
        return self._channel_partner_oid

    @channel_partner_oid.setter
    def channel_partner_oid(self, channel_partner_oid):
        """Sets the channel_partner_oid of this OrderChannelPartner.

        Channel partner object identifier, read-only and available on existing channel orders only.  # noqa: E501

        :param channel_partner_oid: The channel_partner_oid of this OrderChannelPartner.  # noqa: E501
        :type: int
        """

        self._channel_partner_oid = channel_partner_oid

    @property
    def channel_partner_order_id(self):
        """Gets the channel_partner_order_id of this OrderChannelPartner.  # noqa: E501

        The order ID assigned by the channel partner for this order.  # noqa: E501

        :return: The channel_partner_order_id of this OrderChannelPartner.  # noqa: E501
        :rtype: str
        """
        return self._channel_partner_order_id

    @channel_partner_order_id.setter
    def channel_partner_order_id(self, channel_partner_order_id):
        """Sets the channel_partner_order_id of this OrderChannelPartner.

        The order ID assigned by the channel partner for this order.  # noqa: E501

        :param channel_partner_order_id: The channel_partner_order_id of this OrderChannelPartner.  # noqa: E501
        :type: str
        """
        if channel_partner_order_id is not None and len(channel_partner_order_id) > 50:
            raise ValueError("Invalid value for `channel_partner_order_id`, length must be less than or equal to `50`")  # noqa: E501

        self._channel_partner_order_id = channel_partner_order_id

    @property
    def ignore_invalid_shipping_method(self):
        """Gets the ignore_invalid_shipping_method of this OrderChannelPartner.  # noqa: E501

        Set to true to ignore invalid shipping method being specified.  Only applicable on inserting orders.  # noqa: E501

        :return: The ignore_invalid_shipping_method of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_invalid_shipping_method

    @ignore_invalid_shipping_method.setter
    def ignore_invalid_shipping_method(self, ignore_invalid_shipping_method):
        """Sets the ignore_invalid_shipping_method of this OrderChannelPartner.

        Set to true to ignore invalid shipping method being specified.  Only applicable on inserting orders.  # noqa: E501

        :param ignore_invalid_shipping_method: The ignore_invalid_shipping_method of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._ignore_invalid_shipping_method = ignore_invalid_shipping_method

    @property
    def no_realtime_payment_processing(self):
        """Gets the no_realtime_payment_processing of this OrderChannelPartner.  # noqa: E501

        Indicates this order should be placed in Account Receivable for later payment processing  # noqa: E501

        :return: The no_realtime_payment_processing of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._no_realtime_payment_processing

    @no_realtime_payment_processing.setter
    def no_realtime_payment_processing(self, no_realtime_payment_processing):
        """Sets the no_realtime_payment_processing of this OrderChannelPartner.

        Indicates this order should be placed in Account Receivable for later payment processing  # noqa: E501

        :param no_realtime_payment_processing: The no_realtime_payment_processing of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._no_realtime_payment_processing = no_realtime_payment_processing

    @property
    def skip_payment_processing(self):
        """Gets the skip_payment_processing of this OrderChannelPartner.  # noqa: E501

        Indicates this order was already paid for via a channel purchase and no payment collection should be attempted  # noqa: E501

        :return: The skip_payment_processing of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._skip_payment_processing

    @skip_payment_processing.setter
    def skip_payment_processing(self, skip_payment_processing):
        """Sets the skip_payment_processing of this OrderChannelPartner.

        Indicates this order was already paid for via a channel purchase and no payment collection should be attempted  # noqa: E501

        :param skip_payment_processing: The skip_payment_processing of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._skip_payment_processing = skip_payment_processing

    @property
    def store_completed(self):
        """Gets the store_completed of this OrderChannelPartner.  # noqa: E501

        Instructs UltraCart to skip shipping department and mark this order as fully complete.  This flag defaults to true.  Set this flag to false to shipped product for this order.  # noqa: E501

        :return: The store_completed of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._store_completed

    @store_completed.setter
    def store_completed(self, store_completed):
        """Sets the store_completed of this OrderChannelPartner.

        Instructs UltraCart to skip shipping department and mark this order as fully complete.  This flag defaults to true.  Set this flag to false to shipped product for this order.  # noqa: E501

        :param store_completed: The store_completed of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._store_completed = store_completed

    @property
    def store_if_payment_declines(self):
        """Gets the store_if_payment_declines of this OrderChannelPartner.  # noqa: E501

        If true, any failed payment will place the order in Accounts Receivable rather than rejecting it.  # noqa: E501

        :return: The store_if_payment_declines of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._store_if_payment_declines

    @store_if_payment_declines.setter
    def store_if_payment_declines(self, store_if_payment_declines):
        """Sets the store_if_payment_declines of this OrderChannelPartner.

        If true, any failed payment will place the order in Accounts Receivable rather than rejecting it.  # noqa: E501

        :param store_if_payment_declines: The store_if_payment_declines of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._store_if_payment_declines = store_if_payment_declines

    @property
    def treat_warnings_as_errors(self):
        """Gets the treat_warnings_as_errors of this OrderChannelPartner.  # noqa: E501

        Any warnings are raised as errors and halt the import of the order  # noqa: E501

        :return: The treat_warnings_as_errors of this OrderChannelPartner.  # noqa: E501
        :rtype: bool
        """
        return self._treat_warnings_as_errors

    @treat_warnings_as_errors.setter
    def treat_warnings_as_errors(self, treat_warnings_as_errors):
        """Sets the treat_warnings_as_errors of this OrderChannelPartner.

        Any warnings are raised as errors and halt the import of the order  # noqa: E501

        :param treat_warnings_as_errors: The treat_warnings_as_errors of this OrderChannelPartner.  # noqa: E501
        :type: bool
        """

        self._treat_warnings_as_errors = treat_warnings_as_errors

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
        if issubclass(OrderChannelPartner, dict):
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
        if not isinstance(other, OrderChannelPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

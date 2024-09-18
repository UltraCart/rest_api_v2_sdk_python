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


class EmailSmsStat(object):
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
        'click_count': 'int',
        'click_count_formatted': 'str',
        'conversion_count': 'int',
        'conversion_count_formatted': 'str',
        'deleted': 'bool',
        'delivered_count': 'int',
        'delivered_count_formatted': 'str',
        'merchant_id': 'str',
        'name': 'str',
        'order_count': 'int',
        'order_count_formatted': 'str',
        'profit': 'float',
        'profit_formatted': 'str',
        'revenue': 'float',
        'revenue_formatted': 'str',
        'send_count': 'int',
        'send_count_formatted': 'str',
        'skipped_count': 'int',
        'skipped_count_formatted': 'str',
        'stat_type': 'str',
        'status': 'str',
        'status_dts': 'str',
        'step_uuid': 'str',
        'steps': 'list[EmailSmsStat]',
        'storefront_oid': 'int',
        'unsubscribe_count': 'int',
        'unsubscribe_count_formatted': 'str',
        'uuid': 'str',
        'view_count': 'int',
        'view_count_formatted': 'str'
    }

    attribute_map = {
        'click_count': 'click_count',
        'click_count_formatted': 'click_count_formatted',
        'conversion_count': 'conversion_count',
        'conversion_count_formatted': 'conversion_count_formatted',
        'deleted': 'deleted',
        'delivered_count': 'delivered_count',
        'delivered_count_formatted': 'delivered_count_formatted',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'order_count': 'order_count',
        'order_count_formatted': 'order_count_formatted',
        'profit': 'profit',
        'profit_formatted': 'profit_formatted',
        'revenue': 'revenue',
        'revenue_formatted': 'revenue_formatted',
        'send_count': 'send_count',
        'send_count_formatted': 'send_count_formatted',
        'skipped_count': 'skipped_count',
        'skipped_count_formatted': 'skipped_count_formatted',
        'stat_type': 'stat_type',
        'status': 'status',
        'status_dts': 'status_dts',
        'step_uuid': 'step_uuid',
        'steps': 'steps',
        'storefront_oid': 'storefront_oid',
        'unsubscribe_count': 'unsubscribe_count',
        'unsubscribe_count_formatted': 'unsubscribe_count_formatted',
        'uuid': 'uuid',
        'view_count': 'view_count',
        'view_count_formatted': 'view_count_formatted'
    }

    def __init__(self, click_count=None, click_count_formatted=None, conversion_count=None, conversion_count_formatted=None, deleted=None, delivered_count=None, delivered_count_formatted=None, merchant_id=None, name=None, order_count=None, order_count_formatted=None, profit=None, profit_formatted=None, revenue=None, revenue_formatted=None, send_count=None, send_count_formatted=None, skipped_count=None, skipped_count_formatted=None, stat_type=None, status=None, status_dts=None, step_uuid=None, steps=None, storefront_oid=None, unsubscribe_count=None, unsubscribe_count_formatted=None, uuid=None, view_count=None, view_count_formatted=None):  # noqa: E501
        """EmailSmsStat - a model defined in Swagger"""  # noqa: E501

        self._click_count = None
        self._click_count_formatted = None
        self._conversion_count = None
        self._conversion_count_formatted = None
        self._deleted = None
        self._delivered_count = None
        self._delivered_count_formatted = None
        self._merchant_id = None
        self._name = None
        self._order_count = None
        self._order_count_formatted = None
        self._profit = None
        self._profit_formatted = None
        self._revenue = None
        self._revenue_formatted = None
        self._send_count = None
        self._send_count_formatted = None
        self._skipped_count = None
        self._skipped_count_formatted = None
        self._stat_type = None
        self._status = None
        self._status_dts = None
        self._step_uuid = None
        self._steps = None
        self._storefront_oid = None
        self._unsubscribe_count = None
        self._unsubscribe_count_formatted = None
        self._uuid = None
        self._view_count = None
        self._view_count_formatted = None
        self.discriminator = None

        if click_count is not None:
            self.click_count = click_count
        if click_count_formatted is not None:
            self.click_count_formatted = click_count_formatted
        if conversion_count is not None:
            self.conversion_count = conversion_count
        if conversion_count_formatted is not None:
            self.conversion_count_formatted = conversion_count_formatted
        if deleted is not None:
            self.deleted = deleted
        if delivered_count is not None:
            self.delivered_count = delivered_count
        if delivered_count_formatted is not None:
            self.delivered_count_formatted = delivered_count_formatted
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if order_count is not None:
            self.order_count = order_count
        if order_count_formatted is not None:
            self.order_count_formatted = order_count_formatted
        if profit is not None:
            self.profit = profit
        if profit_formatted is not None:
            self.profit_formatted = profit_formatted
        if revenue is not None:
            self.revenue = revenue
        if revenue_formatted is not None:
            self.revenue_formatted = revenue_formatted
        if send_count is not None:
            self.send_count = send_count
        if send_count_formatted is not None:
            self.send_count_formatted = send_count_formatted
        if skipped_count is not None:
            self.skipped_count = skipped_count
        if skipped_count_formatted is not None:
            self.skipped_count_formatted = skipped_count_formatted
        if stat_type is not None:
            self.stat_type = stat_type
        if status is not None:
            self.status = status
        if status_dts is not None:
            self.status_dts = status_dts
        if step_uuid is not None:
            self.step_uuid = step_uuid
        if steps is not None:
            self.steps = steps
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if unsubscribe_count is not None:
            self.unsubscribe_count = unsubscribe_count
        if unsubscribe_count_formatted is not None:
            self.unsubscribe_count_formatted = unsubscribe_count_formatted
        if uuid is not None:
            self.uuid = uuid
        if view_count is not None:
            self.view_count = view_count
        if view_count_formatted is not None:
            self.view_count_formatted = view_count_formatted

    @property
    def click_count(self):
        """Gets the click_count of this EmailSmsStat.  # noqa: E501

        Count of clicked emails  # noqa: E501

        :return: The click_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._click_count

    @click_count.setter
    def click_count(self, click_count):
        """Sets the click_count of this EmailSmsStat.

        Count of clicked emails  # noqa: E501

        :param click_count: The click_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._click_count = click_count

    @property
    def click_count_formatted(self):
        """Gets the click_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of clicked emails, formatted  # noqa: E501

        :return: The click_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._click_count_formatted

    @click_count_formatted.setter
    def click_count_formatted(self, click_count_formatted):
        """Sets the click_count_formatted of this EmailSmsStat.

        Count of clicked emails, formatted  # noqa: E501

        :param click_count_formatted: The click_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._click_count_formatted = click_count_formatted

    @property
    def conversion_count(self):
        """Gets the conversion_count of this EmailSmsStat.  # noqa: E501

        Count of conversions  # noqa: E501

        :return: The conversion_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._conversion_count

    @conversion_count.setter
    def conversion_count(self, conversion_count):
        """Sets the conversion_count of this EmailSmsStat.

        Count of conversions  # noqa: E501

        :param conversion_count: The conversion_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._conversion_count = conversion_count

    @property
    def conversion_count_formatted(self):
        """Gets the conversion_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of conversions, formatted  # noqa: E501

        :return: The conversion_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._conversion_count_formatted

    @conversion_count_formatted.setter
    def conversion_count_formatted(self, conversion_count_formatted):
        """Sets the conversion_count_formatted of this EmailSmsStat.

        Count of conversions, formatted  # noqa: E501

        :param conversion_count_formatted: The conversion_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._conversion_count_formatted = conversion_count_formatted

    @property
    def deleted(self):
        """Gets the deleted of this EmailSmsStat.  # noqa: E501

        True if campaign/flow has been archived  # noqa: E501

        :return: The deleted of this EmailSmsStat.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this EmailSmsStat.

        True if campaign/flow has been archived  # noqa: E501

        :param deleted: The deleted of this EmailSmsStat.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def delivered_count(self):
        """Gets the delivered_count of this EmailSmsStat.  # noqa: E501

        Count of delivered emails  # noqa: E501

        :return: The delivered_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, delivered_count):
        """Sets the delivered_count of this EmailSmsStat.

        Count of delivered emails  # noqa: E501

        :param delivered_count: The delivered_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._delivered_count = delivered_count

    @property
    def delivered_count_formatted(self):
        """Gets the delivered_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of delivered emails, formatted  # noqa: E501

        :return: The delivered_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._delivered_count_formatted

    @delivered_count_formatted.setter
    def delivered_count_formatted(self, delivered_count_formatted):
        """Sets the delivered_count_formatted of this EmailSmsStat.

        Count of delivered emails, formatted  # noqa: E501

        :param delivered_count_formatted: The delivered_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._delivered_count_formatted = delivered_count_formatted

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EmailSmsStat.  # noqa: E501

        Merchant ID  # noqa: E501

        :return: The merchant_id of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EmailSmsStat.

        Merchant ID  # noqa: E501

        :param merchant_id: The merchant_id of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this EmailSmsStat.  # noqa: E501

        List or segment name  # noqa: E501

        :return: The name of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailSmsStat.

        List or segment name  # noqa: E501

        :param name: The name of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_count(self):
        """Gets the order_count of this EmailSmsStat.  # noqa: E501

        Count of orders  # noqa: E501

        :return: The order_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this EmailSmsStat.

        Count of orders  # noqa: E501

        :param order_count: The order_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._order_count = order_count

    @property
    def order_count_formatted(self):
        """Gets the order_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of orders, formatted  # noqa: E501

        :return: The order_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._order_count_formatted

    @order_count_formatted.setter
    def order_count_formatted(self, order_count_formatted):
        """Sets the order_count_formatted of this EmailSmsStat.

        Count of orders, formatted  # noqa: E501

        :param order_count_formatted: The order_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._order_count_formatted = order_count_formatted

    @property
    def profit(self):
        """Gets the profit of this EmailSmsStat.  # noqa: E501

        Profit  # noqa: E501

        :return: The profit of this EmailSmsStat.  # noqa: E501
        :rtype: float
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """Sets the profit of this EmailSmsStat.

        Profit  # noqa: E501

        :param profit: The profit of this EmailSmsStat.  # noqa: E501
        :type: float
        """

        self._profit = profit

    @property
    def profit_formatted(self):
        """Gets the profit_formatted of this EmailSmsStat.  # noqa: E501

        Profit, formatted  # noqa: E501

        :return: The profit_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._profit_formatted

    @profit_formatted.setter
    def profit_formatted(self, profit_formatted):
        """Sets the profit_formatted of this EmailSmsStat.

        Profit, formatted  # noqa: E501

        :param profit_formatted: The profit_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._profit_formatted = profit_formatted

    @property
    def revenue(self):
        """Gets the revenue of this EmailSmsStat.  # noqa: E501

        Revenue  # noqa: E501

        :return: The revenue of this EmailSmsStat.  # noqa: E501
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this EmailSmsStat.

        Revenue  # noqa: E501

        :param revenue: The revenue of this EmailSmsStat.  # noqa: E501
        :type: float
        """

        self._revenue = revenue

    @property
    def revenue_formatted(self):
        """Gets the revenue_formatted of this EmailSmsStat.  # noqa: E501

        Revenue, formatted  # noqa: E501

        :return: The revenue_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._revenue_formatted

    @revenue_formatted.setter
    def revenue_formatted(self, revenue_formatted):
        """Sets the revenue_formatted of this EmailSmsStat.

        Revenue, formatted  # noqa: E501

        :param revenue_formatted: The revenue_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._revenue_formatted = revenue_formatted

    @property
    def send_count(self):
        """Gets the send_count of this EmailSmsStat.  # noqa: E501

        Count of emails sent  # noqa: E501

        :return: The send_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._send_count

    @send_count.setter
    def send_count(self, send_count):
        """Sets the send_count of this EmailSmsStat.

        Count of emails sent  # noqa: E501

        :param send_count: The send_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._send_count = send_count

    @property
    def send_count_formatted(self):
        """Gets the send_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of emails sent, formatted  # noqa: E501

        :return: The send_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._send_count_formatted

    @send_count_formatted.setter
    def send_count_formatted(self, send_count_formatted):
        """Sets the send_count_formatted of this EmailSmsStat.

        Count of emails sent, formatted  # noqa: E501

        :param send_count_formatted: The send_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._send_count_formatted = send_count_formatted

    @property
    def skipped_count(self):
        """Gets the skipped_count of this EmailSmsStat.  # noqa: E501

        Count of skipped emails  # noqa: E501

        :return: The skipped_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._skipped_count

    @skipped_count.setter
    def skipped_count(self, skipped_count):
        """Sets the skipped_count of this EmailSmsStat.

        Count of skipped emails  # noqa: E501

        :param skipped_count: The skipped_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._skipped_count = skipped_count

    @property
    def skipped_count_formatted(self):
        """Gets the skipped_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of skipped emails, formatted  # noqa: E501

        :return: The skipped_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._skipped_count_formatted

    @skipped_count_formatted.setter
    def skipped_count_formatted(self, skipped_count_formatted):
        """Sets the skipped_count_formatted of this EmailSmsStat.

        Count of skipped emails, formatted  # noqa: E501

        :param skipped_count_formatted: The skipped_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._skipped_count_formatted = skipped_count_formatted

    @property
    def stat_type(self):
        """Gets the stat_type of this EmailSmsStat.  # noqa: E501

        Campaign, Flow or None (for anything else)  # noqa: E501

        :return: The stat_type of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this EmailSmsStat.

        Campaign, Flow or None (for anything else)  # noqa: E501

        :param stat_type: The stat_type of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._stat_type = stat_type

    @property
    def status(self):
        """Gets the status of this EmailSmsStat.  # noqa: E501

        Status of campaign or flow  # noqa: E501

        :return: The status of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmailSmsStat.

        Status of campaign or flow  # noqa: E501

        :param status: The status of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_dts(self):
        """Gets the status_dts of this EmailSmsStat.  # noqa: E501

        Status dts of campaign or flow  # noqa: E501

        :return: The status_dts of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._status_dts

    @status_dts.setter
    def status_dts(self, status_dts):
        """Sets the status_dts of this EmailSmsStat.

        Status dts of campaign or flow  # noqa: E501

        :param status_dts: The status_dts of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._status_dts = status_dts

    @property
    def step_uuid(self):
        """Gets the step_uuid of this EmailSmsStat.  # noqa: E501

        Step UUID if the statistics are at the step/email level  # noqa: E501

        :return: The step_uuid of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._step_uuid

    @step_uuid.setter
    def step_uuid(self, step_uuid):
        """Sets the step_uuid of this EmailSmsStat.

        Step UUID if the statistics are at the step/email level  # noqa: E501

        :param step_uuid: The step_uuid of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._step_uuid = step_uuid

    @property
    def steps(self):
        """Gets the steps of this EmailSmsStat.  # noqa: E501


        :return: The steps of this EmailSmsStat.  # noqa: E501
        :rtype: list[EmailSmsStat]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this EmailSmsStat.


        :param steps: The steps of this EmailSmsStat.  # noqa: E501
        :type: list[EmailSmsStat]
        """

        self._steps = steps

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this EmailSmsStat.  # noqa: E501

        Storefront oid  # noqa: E501

        :return: The storefront_oid of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this EmailSmsStat.

        Storefront oid  # noqa: E501

        :param storefront_oid: The storefront_oid of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def unsubscribe_count(self):
        """Gets the unsubscribe_count of this EmailSmsStat.  # noqa: E501

        Count of emails classified as unsubscribe  # noqa: E501

        :return: The unsubscribe_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribe_count

    @unsubscribe_count.setter
    def unsubscribe_count(self, unsubscribe_count):
        """Sets the unsubscribe_count of this EmailSmsStat.

        Count of emails classified as unsubscribe  # noqa: E501

        :param unsubscribe_count: The unsubscribe_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._unsubscribe_count = unsubscribe_count

    @property
    def unsubscribe_count_formatted(self):
        """Gets the unsubscribe_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of emails classified as unsubscribe, formatted  # noqa: E501

        :return: The unsubscribe_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._unsubscribe_count_formatted

    @unsubscribe_count_formatted.setter
    def unsubscribe_count_formatted(self, unsubscribe_count_formatted):
        """Sets the unsubscribe_count_formatted of this EmailSmsStat.

        Count of emails classified as unsubscribe, formatted  # noqa: E501

        :param unsubscribe_count_formatted: The unsubscribe_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._unsubscribe_count_formatted = unsubscribe_count_formatted

    @property
    def uuid(self):
        """Gets the uuid of this EmailSmsStat.  # noqa: E501

        List/Segment uuid, or Flow/Campaign uuid depending on level of stat aggregation.  # noqa: E501

        :return: The uuid of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this EmailSmsStat.

        List/Segment uuid, or Flow/Campaign uuid depending on level of stat aggregation.  # noqa: E501

        :param uuid: The uuid of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def view_count(self):
        """Gets the view_count of this EmailSmsStat.  # noqa: E501

        Count of views  # noqa: E501

        :return: The view_count of this EmailSmsStat.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this EmailSmsStat.

        Count of views  # noqa: E501

        :param view_count: The view_count of this EmailSmsStat.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def view_count_formatted(self):
        """Gets the view_count_formatted of this EmailSmsStat.  # noqa: E501

        Count of views, formatted  # noqa: E501

        :return: The view_count_formatted of this EmailSmsStat.  # noqa: E501
        :rtype: str
        """
        return self._view_count_formatted

    @view_count_formatted.setter
    def view_count_formatted(self, view_count_formatted):
        """Sets the view_count_formatted of this EmailSmsStat.

        Count of views, formatted  # noqa: E501

        :param view_count_formatted: The view_count_formatted of this EmailSmsStat.  # noqa: E501
        :type: str
        """

        self._view_count_formatted = view_count_formatted

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
        if issubclass(EmailSmsStat, dict):
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
        if not isinstance(other, EmailSmsStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
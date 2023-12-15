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


class EmailCommseqStat(object):
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
        'delivered_count': 'int',
        'delivered_count_formatted': 'str',
        'email_communication_sequence_uuid': 'str',
        'finished_count': 'int',
        'finished_count_formatted': 'str',
        'in_progress_count': 'int',
        'in_progress_count_formatted': 'str',
        'kickbox_count': 'int',
        'kickbox_count_formatted': 'str',
        'merchant_id': 'str',
        'open_count': 'int',
        'open_count_formatted': 'str',
        'order_count': 'int',
        'order_count_formatted': 'str',
        'permanent_bounce_count': 'int',
        'permanent_bounce_count_formatted': 'str',
        'profit': 'float',
        'profit_formatted': 'str',
        'revenue': 'float',
        'revenue_formatted': 'str',
        'send_count': 'int',
        'send_count_formatted': 'str',
        'skipped_count': 'int',
        'skipped_count_formatted': 'str',
        'spam_count': 'int',
        'spam_count_formatted': 'str',
        'started_count': 'int',
        'started_count_formatted': 'str',
        'storefront_oid': 'int',
        'unsubscribe_count': 'int',
        'unsubscribe_count_formatted': 'str',
        'view_count': 'int',
        'view_count_formatted': 'str'
    }

    attribute_map = {
        'click_count': 'click_count',
        'click_count_formatted': 'click_count_formatted',
        'conversion_count': 'conversion_count',
        'conversion_count_formatted': 'conversion_count_formatted',
        'delivered_count': 'delivered_count',
        'delivered_count_formatted': 'delivered_count_formatted',
        'email_communication_sequence_uuid': 'email_communication_sequence_uuid',
        'finished_count': 'finished_count',
        'finished_count_formatted': 'finished_count_formatted',
        'in_progress_count': 'in_progress_count',
        'in_progress_count_formatted': 'in_progress_count_formatted',
        'kickbox_count': 'kickbox_count',
        'kickbox_count_formatted': 'kickbox_count_formatted',
        'merchant_id': 'merchant_id',
        'open_count': 'open_count',
        'open_count_formatted': 'open_count_formatted',
        'order_count': 'order_count',
        'order_count_formatted': 'order_count_formatted',
        'permanent_bounce_count': 'permanent_bounce_count',
        'permanent_bounce_count_formatted': 'permanent_bounce_count_formatted',
        'profit': 'profit',
        'profit_formatted': 'profit_formatted',
        'revenue': 'revenue',
        'revenue_formatted': 'revenue_formatted',
        'send_count': 'send_count',
        'send_count_formatted': 'send_count_formatted',
        'skipped_count': 'skipped_count',
        'skipped_count_formatted': 'skipped_count_formatted',
        'spam_count': 'spam_count',
        'spam_count_formatted': 'spam_count_formatted',
        'started_count': 'started_count',
        'started_count_formatted': 'started_count_formatted',
        'storefront_oid': 'storefront_oid',
        'unsubscribe_count': 'unsubscribe_count',
        'unsubscribe_count_formatted': 'unsubscribe_count_formatted',
        'view_count': 'view_count',
        'view_count_formatted': 'view_count_formatted'
    }

    def __init__(self, click_count=None, click_count_formatted=None, conversion_count=None, conversion_count_formatted=None, delivered_count=None, delivered_count_formatted=None, email_communication_sequence_uuid=None, finished_count=None, finished_count_formatted=None, in_progress_count=None, in_progress_count_formatted=None, kickbox_count=None, kickbox_count_formatted=None, merchant_id=None, open_count=None, open_count_formatted=None, order_count=None, order_count_formatted=None, permanent_bounce_count=None, permanent_bounce_count_formatted=None, profit=None, profit_formatted=None, revenue=None, revenue_formatted=None, send_count=None, send_count_formatted=None, skipped_count=None, skipped_count_formatted=None, spam_count=None, spam_count_formatted=None, started_count=None, started_count_formatted=None, storefront_oid=None, unsubscribe_count=None, unsubscribe_count_formatted=None, view_count=None, view_count_formatted=None):  # noqa: E501
        """EmailCommseqStat - a model defined in Swagger"""  # noqa: E501

        self._click_count = None
        self._click_count_formatted = None
        self._conversion_count = None
        self._conversion_count_formatted = None
        self._delivered_count = None
        self._delivered_count_formatted = None
        self._email_communication_sequence_uuid = None
        self._finished_count = None
        self._finished_count_formatted = None
        self._in_progress_count = None
        self._in_progress_count_formatted = None
        self._kickbox_count = None
        self._kickbox_count_formatted = None
        self._merchant_id = None
        self._open_count = None
        self._open_count_formatted = None
        self._order_count = None
        self._order_count_formatted = None
        self._permanent_bounce_count = None
        self._permanent_bounce_count_formatted = None
        self._profit = None
        self._profit_formatted = None
        self._revenue = None
        self._revenue_formatted = None
        self._send_count = None
        self._send_count_formatted = None
        self._skipped_count = None
        self._skipped_count_formatted = None
        self._spam_count = None
        self._spam_count_formatted = None
        self._started_count = None
        self._started_count_formatted = None
        self._storefront_oid = None
        self._unsubscribe_count = None
        self._unsubscribe_count_formatted = None
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
        if delivered_count is not None:
            self.delivered_count = delivered_count
        if delivered_count_formatted is not None:
            self.delivered_count_formatted = delivered_count_formatted
        if email_communication_sequence_uuid is not None:
            self.email_communication_sequence_uuid = email_communication_sequence_uuid
        if finished_count is not None:
            self.finished_count = finished_count
        if finished_count_formatted is not None:
            self.finished_count_formatted = finished_count_formatted
        if in_progress_count is not None:
            self.in_progress_count = in_progress_count
        if in_progress_count_formatted is not None:
            self.in_progress_count_formatted = in_progress_count_formatted
        if kickbox_count is not None:
            self.kickbox_count = kickbox_count
        if kickbox_count_formatted is not None:
            self.kickbox_count_formatted = kickbox_count_formatted
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if open_count is not None:
            self.open_count = open_count
        if open_count_formatted is not None:
            self.open_count_formatted = open_count_formatted
        if order_count is not None:
            self.order_count = order_count
        if order_count_formatted is not None:
            self.order_count_formatted = order_count_formatted
        if permanent_bounce_count is not None:
            self.permanent_bounce_count = permanent_bounce_count
        if permanent_bounce_count_formatted is not None:
            self.permanent_bounce_count_formatted = permanent_bounce_count_formatted
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
        if spam_count is not None:
            self.spam_count = spam_count
        if spam_count_formatted is not None:
            self.spam_count_formatted = spam_count_formatted
        if started_count is not None:
            self.started_count = started_count
        if started_count_formatted is not None:
            self.started_count_formatted = started_count_formatted
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if unsubscribe_count is not None:
            self.unsubscribe_count = unsubscribe_count
        if unsubscribe_count_formatted is not None:
            self.unsubscribe_count_formatted = unsubscribe_count_formatted
        if view_count is not None:
            self.view_count = view_count
        if view_count_formatted is not None:
            self.view_count_formatted = view_count_formatted

    @property
    def click_count(self):
        """Gets the click_count of this EmailCommseqStat.  # noqa: E501

        Count of clicked emails  # noqa: E501

        :return: The click_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._click_count

    @click_count.setter
    def click_count(self, click_count):
        """Sets the click_count of this EmailCommseqStat.

        Count of clicked emails  # noqa: E501

        :param click_count: The click_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._click_count = click_count

    @property
    def click_count_formatted(self):
        """Gets the click_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of clicked emails, formatted  # noqa: E501

        :return: The click_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._click_count_formatted

    @click_count_formatted.setter
    def click_count_formatted(self, click_count_formatted):
        """Sets the click_count_formatted of this EmailCommseqStat.

        Count of clicked emails, formatted  # noqa: E501

        :param click_count_formatted: The click_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._click_count_formatted = click_count_formatted

    @property
    def conversion_count(self):
        """Gets the conversion_count of this EmailCommseqStat.  # noqa: E501

        Count of conversion  # noqa: E501

        :return: The conversion_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._conversion_count

    @conversion_count.setter
    def conversion_count(self, conversion_count):
        """Sets the conversion_count of this EmailCommseqStat.

        Count of conversion  # noqa: E501

        :param conversion_count: The conversion_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._conversion_count = conversion_count

    @property
    def conversion_count_formatted(self):
        """Gets the conversion_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of conversions, formatted  # noqa: E501

        :return: The conversion_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._conversion_count_formatted

    @conversion_count_formatted.setter
    def conversion_count_formatted(self, conversion_count_formatted):
        """Sets the conversion_count_formatted of this EmailCommseqStat.

        Count of conversions, formatted  # noqa: E501

        :param conversion_count_formatted: The conversion_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._conversion_count_formatted = conversion_count_formatted

    @property
    def delivered_count(self):
        """Gets the delivered_count of this EmailCommseqStat.  # noqa: E501

        Count of delivered emails  # noqa: E501

        :return: The delivered_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, delivered_count):
        """Sets the delivered_count of this EmailCommseqStat.

        Count of delivered emails  # noqa: E501

        :param delivered_count: The delivered_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._delivered_count = delivered_count

    @property
    def delivered_count_formatted(self):
        """Gets the delivered_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of delivered emails, formatted  # noqa: E501

        :return: The delivered_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._delivered_count_formatted

    @delivered_count_formatted.setter
    def delivered_count_formatted(self, delivered_count_formatted):
        """Sets the delivered_count_formatted of this EmailCommseqStat.

        Count of delivered emails, formatted  # noqa: E501

        :param delivered_count_formatted: The delivered_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._delivered_count_formatted = delivered_count_formatted

    @property
    def email_communication_sequence_uuid(self):
        """Gets the email_communication_sequence_uuid of this EmailCommseqStat.  # noqa: E501

        UUID associated with the communication sequence  # noqa: E501

        :return: The email_communication_sequence_uuid of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._email_communication_sequence_uuid

    @email_communication_sequence_uuid.setter
    def email_communication_sequence_uuid(self, email_communication_sequence_uuid):
        """Sets the email_communication_sequence_uuid of this EmailCommseqStat.

        UUID associated with the communication sequence  # noqa: E501

        :param email_communication_sequence_uuid: The email_communication_sequence_uuid of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._email_communication_sequence_uuid = email_communication_sequence_uuid

    @property
    def finished_count(self):
        """Gets the finished_count of this EmailCommseqStat.  # noqa: E501

        Count of customers that finished the sequence  # noqa: E501

        :return: The finished_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._finished_count

    @finished_count.setter
    def finished_count(self, finished_count):
        """Sets the finished_count of this EmailCommseqStat.

        Count of customers that finished the sequence  # noqa: E501

        :param finished_count: The finished_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._finished_count = finished_count

    @property
    def finished_count_formatted(self):
        """Gets the finished_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of customers that finished the sequence, formatted  # noqa: E501

        :return: The finished_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._finished_count_formatted

    @finished_count_formatted.setter
    def finished_count_formatted(self, finished_count_formatted):
        """Sets the finished_count_formatted of this EmailCommseqStat.

        Count of customers that finished the sequence, formatted  # noqa: E501

        :param finished_count_formatted: The finished_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._finished_count_formatted = finished_count_formatted

    @property
    def in_progress_count(self):
        """Gets the in_progress_count of this EmailCommseqStat.  # noqa: E501

        Count of customers in progress  # noqa: E501

        :return: The in_progress_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._in_progress_count

    @in_progress_count.setter
    def in_progress_count(self, in_progress_count):
        """Sets the in_progress_count of this EmailCommseqStat.

        Count of customers in progress  # noqa: E501

        :param in_progress_count: The in_progress_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._in_progress_count = in_progress_count

    @property
    def in_progress_count_formatted(self):
        """Gets the in_progress_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of customers in progress, formatted  # noqa: E501

        :return: The in_progress_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._in_progress_count_formatted

    @in_progress_count_formatted.setter
    def in_progress_count_formatted(self, in_progress_count_formatted):
        """Sets the in_progress_count_formatted of this EmailCommseqStat.

        Count of customers in progress, formatted  # noqa: E501

        :param in_progress_count_formatted: The in_progress_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._in_progress_count_formatted = in_progress_count_formatted

    @property
    def kickbox_count(self):
        """Gets the kickbox_count of this EmailCommseqStat.  # noqa: E501

        Count of emails kicked  # noqa: E501

        :return: The kickbox_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._kickbox_count

    @kickbox_count.setter
    def kickbox_count(self, kickbox_count):
        """Sets the kickbox_count of this EmailCommseqStat.

        Count of emails kicked  # noqa: E501

        :param kickbox_count: The kickbox_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._kickbox_count = kickbox_count

    @property
    def kickbox_count_formatted(self):
        """Gets the kickbox_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of emails kicked, formatted  # noqa: E501

        :return: The kickbox_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._kickbox_count_formatted

    @kickbox_count_formatted.setter
    def kickbox_count_formatted(self, kickbox_count_formatted):
        """Sets the kickbox_count_formatted of this EmailCommseqStat.

        Count of emails kicked, formatted  # noqa: E501

        :param kickbox_count_formatted: The kickbox_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._kickbox_count_formatted = kickbox_count_formatted

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EmailCommseqStat.  # noqa: E501

        Merchant ID  # noqa: E501

        :return: The merchant_id of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EmailCommseqStat.

        Merchant ID  # noqa: E501

        :param merchant_id: The merchant_id of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def open_count(self):
        """Gets the open_count of this EmailCommseqStat.  # noqa: E501

        Count of opened emails  # noqa: E501

        :return: The open_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._open_count

    @open_count.setter
    def open_count(self, open_count):
        """Sets the open_count of this EmailCommseqStat.

        Count of opened emails  # noqa: E501

        :param open_count: The open_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._open_count = open_count

    @property
    def open_count_formatted(self):
        """Gets the open_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of opened emails, formatted  # noqa: E501

        :return: The open_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._open_count_formatted

    @open_count_formatted.setter
    def open_count_formatted(self, open_count_formatted):
        """Sets the open_count_formatted of this EmailCommseqStat.

        Count of opened emails, formatted  # noqa: E501

        :param open_count_formatted: The open_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._open_count_formatted = open_count_formatted

    @property
    def order_count(self):
        """Gets the order_count of this EmailCommseqStat.  # noqa: E501

        Count of orders  # noqa: E501

        :return: The order_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this EmailCommseqStat.

        Count of orders  # noqa: E501

        :param order_count: The order_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._order_count = order_count

    @property
    def order_count_formatted(self):
        """Gets the order_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of orders, formatted  # noqa: E501

        :return: The order_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._order_count_formatted

    @order_count_formatted.setter
    def order_count_formatted(self, order_count_formatted):
        """Sets the order_count_formatted of this EmailCommseqStat.

        Count of orders, formatted  # noqa: E501

        :param order_count_formatted: The order_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._order_count_formatted = order_count_formatted

    @property
    def permanent_bounce_count(self):
        """Gets the permanent_bounce_count of this EmailCommseqStat.  # noqa: E501

        Count of emails permanently bounced  # noqa: E501

        :return: The permanent_bounce_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._permanent_bounce_count

    @permanent_bounce_count.setter
    def permanent_bounce_count(self, permanent_bounce_count):
        """Sets the permanent_bounce_count of this EmailCommseqStat.

        Count of emails permanently bounced  # noqa: E501

        :param permanent_bounce_count: The permanent_bounce_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._permanent_bounce_count = permanent_bounce_count

    @property
    def permanent_bounce_count_formatted(self):
        """Gets the permanent_bounce_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of emails permanently bounced, formatted  # noqa: E501

        :return: The permanent_bounce_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._permanent_bounce_count_formatted

    @permanent_bounce_count_formatted.setter
    def permanent_bounce_count_formatted(self, permanent_bounce_count_formatted):
        """Sets the permanent_bounce_count_formatted of this EmailCommseqStat.

        Count of emails permanently bounced, formatted  # noqa: E501

        :param permanent_bounce_count_formatted: The permanent_bounce_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._permanent_bounce_count_formatted = permanent_bounce_count_formatted

    @property
    def profit(self):
        """Gets the profit of this EmailCommseqStat.  # noqa: E501

        Profit  # noqa: E501

        :return: The profit of this EmailCommseqStat.  # noqa: E501
        :rtype: float
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """Sets the profit of this EmailCommseqStat.

        Profit  # noqa: E501

        :param profit: The profit of this EmailCommseqStat.  # noqa: E501
        :type: float
        """

        self._profit = profit

    @property
    def profit_formatted(self):
        """Gets the profit_formatted of this EmailCommseqStat.  # noqa: E501

        Profit, formatted  # noqa: E501

        :return: The profit_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._profit_formatted

    @profit_formatted.setter
    def profit_formatted(self, profit_formatted):
        """Sets the profit_formatted of this EmailCommseqStat.

        Profit, formatted  # noqa: E501

        :param profit_formatted: The profit_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._profit_formatted = profit_formatted

    @property
    def revenue(self):
        """Gets the revenue of this EmailCommseqStat.  # noqa: E501

        Revenue  # noqa: E501

        :return: The revenue of this EmailCommseqStat.  # noqa: E501
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this EmailCommseqStat.

        Revenue  # noqa: E501

        :param revenue: The revenue of this EmailCommseqStat.  # noqa: E501
        :type: float
        """

        self._revenue = revenue

    @property
    def revenue_formatted(self):
        """Gets the revenue_formatted of this EmailCommseqStat.  # noqa: E501

        Revenue, formatted  # noqa: E501

        :return: The revenue_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._revenue_formatted

    @revenue_formatted.setter
    def revenue_formatted(self, revenue_formatted):
        """Sets the revenue_formatted of this EmailCommseqStat.

        Revenue, formatted  # noqa: E501

        :param revenue_formatted: The revenue_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._revenue_formatted = revenue_formatted

    @property
    def send_count(self):
        """Gets the send_count of this EmailCommseqStat.  # noqa: E501

        Count of emails sent  # noqa: E501

        :return: The send_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._send_count

    @send_count.setter
    def send_count(self, send_count):
        """Sets the send_count of this EmailCommseqStat.

        Count of emails sent  # noqa: E501

        :param send_count: The send_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._send_count = send_count

    @property
    def send_count_formatted(self):
        """Gets the send_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of emails sent, formatted  # noqa: E501

        :return: The send_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._send_count_formatted

    @send_count_formatted.setter
    def send_count_formatted(self, send_count_formatted):
        """Sets the send_count_formatted of this EmailCommseqStat.

        Count of emails sent, formatted  # noqa: E501

        :param send_count_formatted: The send_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._send_count_formatted = send_count_formatted

    @property
    def skipped_count(self):
        """Gets the skipped_count of this EmailCommseqStat.  # noqa: E501

        Count of skipped emails  # noqa: E501

        :return: The skipped_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._skipped_count

    @skipped_count.setter
    def skipped_count(self, skipped_count):
        """Sets the skipped_count of this EmailCommseqStat.

        Count of skipped emails  # noqa: E501

        :param skipped_count: The skipped_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._skipped_count = skipped_count

    @property
    def skipped_count_formatted(self):
        """Gets the skipped_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of skipped emails, formatted  # noqa: E501

        :return: The skipped_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._skipped_count_formatted

    @skipped_count_formatted.setter
    def skipped_count_formatted(self, skipped_count_formatted):
        """Sets the skipped_count_formatted of this EmailCommseqStat.

        Count of skipped emails, formatted  # noqa: E501

        :param skipped_count_formatted: The skipped_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._skipped_count_formatted = skipped_count_formatted

    @property
    def spam_count(self):
        """Gets the spam_count of this EmailCommseqStat.  # noqa: E501

        Count of emails classified as spam  # noqa: E501

        :return: The spam_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._spam_count

    @spam_count.setter
    def spam_count(self, spam_count):
        """Sets the spam_count of this EmailCommseqStat.

        Count of emails classified as spam  # noqa: E501

        :param spam_count: The spam_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._spam_count = spam_count

    @property
    def spam_count_formatted(self):
        """Gets the spam_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of emails classified as spam, formatted  # noqa: E501

        :return: The spam_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._spam_count_formatted

    @spam_count_formatted.setter
    def spam_count_formatted(self, spam_count_formatted):
        """Sets the spam_count_formatted of this EmailCommseqStat.

        Count of emails classified as spam, formatted  # noqa: E501

        :param spam_count_formatted: The spam_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._spam_count_formatted = spam_count_formatted

    @property
    def started_count(self):
        """Gets the started_count of this EmailCommseqStat.  # noqa: E501

        Count of customers that started the sequence  # noqa: E501

        :return: The started_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._started_count

    @started_count.setter
    def started_count(self, started_count):
        """Sets the started_count of this EmailCommseqStat.

        Count of customers that started the sequence  # noqa: E501

        :param started_count: The started_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._started_count = started_count

    @property
    def started_count_formatted(self):
        """Gets the started_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of customers that started the sequence, formatted  # noqa: E501

        :return: The started_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._started_count_formatted

    @started_count_formatted.setter
    def started_count_formatted(self, started_count_formatted):
        """Sets the started_count_formatted of this EmailCommseqStat.

        Count of customers that started the sequence, formatted  # noqa: E501

        :param started_count_formatted: The started_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._started_count_formatted = started_count_formatted

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this EmailCommseqStat.  # noqa: E501

        Storefront oid  # noqa: E501

        :return: The storefront_oid of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this EmailCommseqStat.

        Storefront oid  # noqa: E501

        :param storefront_oid: The storefront_oid of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def unsubscribe_count(self):
        """Gets the unsubscribe_count of this EmailCommseqStat.  # noqa: E501

        Count of unsubscribes caused  # noqa: E501

        :return: The unsubscribe_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribe_count

    @unsubscribe_count.setter
    def unsubscribe_count(self, unsubscribe_count):
        """Sets the unsubscribe_count of this EmailCommseqStat.

        Count of unsubscribes caused  # noqa: E501

        :param unsubscribe_count: The unsubscribe_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._unsubscribe_count = unsubscribe_count

    @property
    def unsubscribe_count_formatted(self):
        """Gets the unsubscribe_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of unsubscribes caused, formatted  # noqa: E501

        :return: The unsubscribe_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._unsubscribe_count_formatted

    @unsubscribe_count_formatted.setter
    def unsubscribe_count_formatted(self, unsubscribe_count_formatted):
        """Sets the unsubscribe_count_formatted of this EmailCommseqStat.

        Count of unsubscribes caused, formatted  # noqa: E501

        :param unsubscribe_count_formatted: The unsubscribe_count_formatted of this EmailCommseqStat.  # noqa: E501
        :type: str
        """

        self._unsubscribe_count_formatted = unsubscribe_count_formatted

    @property
    def view_count(self):
        """Gets the view_count of this EmailCommseqStat.  # noqa: E501

        Count of views  # noqa: E501

        :return: The view_count of this EmailCommseqStat.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this EmailCommseqStat.

        Count of views  # noqa: E501

        :param view_count: The view_count of this EmailCommseqStat.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def view_count_formatted(self):
        """Gets the view_count_formatted of this EmailCommseqStat.  # noqa: E501

        Count of views, formatted  # noqa: E501

        :return: The view_count_formatted of this EmailCommseqStat.  # noqa: E501
        :rtype: str
        """
        return self._view_count_formatted

    @view_count_formatted.setter
    def view_count_formatted(self, view_count_formatted):
        """Sets the view_count_formatted of this EmailCommseqStat.

        Count of views, formatted  # noqa: E501

        :param view_count_formatted: The view_count_formatted of this EmailCommseqStat.  # noqa: E501
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
        if issubclass(EmailCommseqStat, dict):
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
        if not isinstance(other, EmailCommseqStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

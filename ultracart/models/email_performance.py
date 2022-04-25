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


class EmailPerformance(object):
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
        'active_customers': 'int',
        'actual_customers': 'int',
        'bounce_count': 'int',
        'bounce_percentage': 'float',
        'bounce_percentage_formatted': 'str',
        'customer_histogram': 'EmailPerformanceCustomerHistogram',
        'daily_stats': 'list[EmailPerformanceDaily]',
        'delivered_count': 'int',
        'loyalty_program_type': 'str',
        'max_active_customers': 'int',
        'max_emails_per_day': 'int',
        'max_emails_per_hour': 'int',
        'max_emails_per_month': 'int',
        'paused_for_spam': 'bool',
        'revenue': 'float',
        'sent_emails_per_day': 'int',
        'sent_emails_per_hour': 'int',
        'sent_emails_per_month': 'int',
        'sequence_send_count': 'int',
        'spam_count': 'int',
        'spam_percentage': 'float',
        'spam_percentage_formatted': 'str',
        'transactional_send_count': 'int'
    }

    attribute_map = {
        'active_customers': 'active_customers',
        'actual_customers': 'actual_customers',
        'bounce_count': 'bounce_count',
        'bounce_percentage': 'bounce_percentage',
        'bounce_percentage_formatted': 'bounce_percentage_formatted',
        'customer_histogram': 'customer_histogram',
        'daily_stats': 'daily_stats',
        'delivered_count': 'delivered_count',
        'loyalty_program_type': 'loyalty_program_type',
        'max_active_customers': 'max_active_customers',
        'max_emails_per_day': 'max_emails_per_day',
        'max_emails_per_hour': 'max_emails_per_hour',
        'max_emails_per_month': 'max_emails_per_month',
        'paused_for_spam': 'paused_for_spam',
        'revenue': 'revenue',
        'sent_emails_per_day': 'sent_emails_per_day',
        'sent_emails_per_hour': 'sent_emails_per_hour',
        'sent_emails_per_month': 'sent_emails_per_month',
        'sequence_send_count': 'sequence_send_count',
        'spam_count': 'spam_count',
        'spam_percentage': 'spam_percentage',
        'spam_percentage_formatted': 'spam_percentage_formatted',
        'transactional_send_count': 'transactional_send_count'
    }

    def __init__(self, active_customers=None, actual_customers=None, bounce_count=None, bounce_percentage=None, bounce_percentage_formatted=None, customer_histogram=None, daily_stats=None, delivered_count=None, loyalty_program_type=None, max_active_customers=None, max_emails_per_day=None, max_emails_per_hour=None, max_emails_per_month=None, paused_for_spam=None, revenue=None, sent_emails_per_day=None, sent_emails_per_hour=None, sent_emails_per_month=None, sequence_send_count=None, spam_count=None, spam_percentage=None, spam_percentage_formatted=None, transactional_send_count=None):  # noqa: E501
        """EmailPerformance - a model defined in Swagger"""  # noqa: E501

        self._active_customers = None
        self._actual_customers = None
        self._bounce_count = None
        self._bounce_percentage = None
        self._bounce_percentage_formatted = None
        self._customer_histogram = None
        self._daily_stats = None
        self._delivered_count = None
        self._loyalty_program_type = None
        self._max_active_customers = None
        self._max_emails_per_day = None
        self._max_emails_per_hour = None
        self._max_emails_per_month = None
        self._paused_for_spam = None
        self._revenue = None
        self._sent_emails_per_day = None
        self._sent_emails_per_hour = None
        self._sent_emails_per_month = None
        self._sequence_send_count = None
        self._spam_count = None
        self._spam_percentage = None
        self._spam_percentage_formatted = None
        self._transactional_send_count = None
        self.discriminator = None

        if active_customers is not None:
            self.active_customers = active_customers
        if actual_customers is not None:
            self.actual_customers = actual_customers
        if bounce_count is not None:
            self.bounce_count = bounce_count
        if bounce_percentage is not None:
            self.bounce_percentage = bounce_percentage
        if bounce_percentage_formatted is not None:
            self.bounce_percentage_formatted = bounce_percentage_formatted
        if customer_histogram is not None:
            self.customer_histogram = customer_histogram
        if daily_stats is not None:
            self.daily_stats = daily_stats
        if delivered_count is not None:
            self.delivered_count = delivered_count
        if loyalty_program_type is not None:
            self.loyalty_program_type = loyalty_program_type
        if max_active_customers is not None:
            self.max_active_customers = max_active_customers
        if max_emails_per_day is not None:
            self.max_emails_per_day = max_emails_per_day
        if max_emails_per_hour is not None:
            self.max_emails_per_hour = max_emails_per_hour
        if max_emails_per_month is not None:
            self.max_emails_per_month = max_emails_per_month
        if paused_for_spam is not None:
            self.paused_for_spam = paused_for_spam
        if revenue is not None:
            self.revenue = revenue
        if sent_emails_per_day is not None:
            self.sent_emails_per_day = sent_emails_per_day
        if sent_emails_per_hour is not None:
            self.sent_emails_per_hour = sent_emails_per_hour
        if sent_emails_per_month is not None:
            self.sent_emails_per_month = sent_emails_per_month
        if sequence_send_count is not None:
            self.sequence_send_count = sequence_send_count
        if spam_count is not None:
            self.spam_count = spam_count
        if spam_percentage is not None:
            self.spam_percentage = spam_percentage
        if spam_percentage_formatted is not None:
            self.spam_percentage_formatted = spam_percentage_formatted
        if transactional_send_count is not None:
            self.transactional_send_count = transactional_send_count

    @property
    def active_customers(self):
        """Gets the active_customers of this EmailPerformance.  # noqa: E501

        Active customers.  The value will be -1 if calculation is pending.  # noqa: E501

        :return: The active_customers of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._active_customers

    @active_customers.setter
    def active_customers(self, active_customers):
        """Sets the active_customers of this EmailPerformance.

        Active customers.  The value will be -1 if calculation is pending.  # noqa: E501

        :param active_customers: The active_customers of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._active_customers = active_customers

    @property
    def actual_customers(self):
        """Gets the actual_customers of this EmailPerformance.  # noqa: E501

        Actual customers that they have regardless of active state.  The value will be -1 if calculation is pending.  # noqa: E501

        :return: The actual_customers of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._actual_customers

    @actual_customers.setter
    def actual_customers(self, actual_customers):
        """Sets the actual_customers of this EmailPerformance.

        Actual customers that they have regardless of active state.  The value will be -1 if calculation is pending.  # noqa: E501

        :param actual_customers: The actual_customers of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._actual_customers = actual_customers

    @property
    def bounce_count(self):
        """Gets the bounce_count of this EmailPerformance.  # noqa: E501

        Bounce count  # noqa: E501

        :return: The bounce_count of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._bounce_count

    @bounce_count.setter
    def bounce_count(self, bounce_count):
        """Sets the bounce_count of this EmailPerformance.

        Bounce count  # noqa: E501

        :param bounce_count: The bounce_count of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._bounce_count = bounce_count

    @property
    def bounce_percentage(self):
        """Gets the bounce_percentage of this EmailPerformance.  # noqa: E501

        bounce percentage rate based upon our look back window.  This should be under five percent or the account will be paused for sending.  # noqa: E501

        :return: The bounce_percentage of this EmailPerformance.  # noqa: E501
        :rtype: float
        """
        return self._bounce_percentage

    @bounce_percentage.setter
    def bounce_percentage(self, bounce_percentage):
        """Sets the bounce_percentage of this EmailPerformance.

        bounce percentage rate based upon our look back window.  This should be under five percent or the account will be paused for sending.  # noqa: E501

        :param bounce_percentage: The bounce_percentage of this EmailPerformance.  # noqa: E501
        :type: float
        """

        self._bounce_percentage = bounce_percentage

    @property
    def bounce_percentage_formatted(self):
        """Gets the bounce_percentage_formatted of this EmailPerformance.  # noqa: E501

        bounce percentage rate (formatted) based upon our look back window.  This should be under five percent or the account will be paused for sending.  # noqa: E501

        :return: The bounce_percentage_formatted of this EmailPerformance.  # noqa: E501
        :rtype: str
        """
        return self._bounce_percentage_formatted

    @bounce_percentage_formatted.setter
    def bounce_percentage_formatted(self, bounce_percentage_formatted):
        """Sets the bounce_percentage_formatted of this EmailPerformance.

        bounce percentage rate (formatted) based upon our look back window.  This should be under five percent or the account will be paused for sending.  # noqa: E501

        :param bounce_percentage_formatted: The bounce_percentage_formatted of this EmailPerformance.  # noqa: E501
        :type: str
        """

        self._bounce_percentage_formatted = bounce_percentage_formatted

    @property
    def customer_histogram(self):
        """Gets the customer_histogram of this EmailPerformance.  # noqa: E501


        :return: The customer_histogram of this EmailPerformance.  # noqa: E501
        :rtype: EmailPerformanceCustomerHistogram
        """
        return self._customer_histogram

    @customer_histogram.setter
    def customer_histogram(self, customer_histogram):
        """Sets the customer_histogram of this EmailPerformance.


        :param customer_histogram: The customer_histogram of this EmailPerformance.  # noqa: E501
        :type: EmailPerformanceCustomerHistogram
        """

        self._customer_histogram = customer_histogram

    @property
    def daily_stats(self):
        """Gets the daily_stats of this EmailPerformance.  # noqa: E501

        Daily statistics used for charting  # noqa: E501

        :return: The daily_stats of this EmailPerformance.  # noqa: E501
        :rtype: list[EmailPerformanceDaily]
        """
        return self._daily_stats

    @daily_stats.setter
    def daily_stats(self, daily_stats):
        """Sets the daily_stats of this EmailPerformance.

        Daily statistics used for charting  # noqa: E501

        :param daily_stats: The daily_stats of this EmailPerformance.  # noqa: E501
        :type: list[EmailPerformanceDaily]
        """

        self._daily_stats = daily_stats

    @property
    def delivered_count(self):
        """Gets the delivered_count of this EmailPerformance.  # noqa: E501

        Delivered count  # noqa: E501

        :return: The delivered_count of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, delivered_count):
        """Sets the delivered_count of this EmailPerformance.

        Delivered count  # noqa: E501

        :param delivered_count: The delivered_count of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._delivered_count = delivered_count

    @property
    def loyalty_program_type(self):
        """Gets the loyalty_program_type of this EmailPerformance.  # noqa: E501

        Loyalty Program Type  # noqa: E501

        :return: The loyalty_program_type of this EmailPerformance.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_program_type

    @loyalty_program_type.setter
    def loyalty_program_type(self, loyalty_program_type):
        """Sets the loyalty_program_type of this EmailPerformance.

        Loyalty Program Type  # noqa: E501

        :param loyalty_program_type: The loyalty_program_type of this EmailPerformance.  # noqa: E501
        :type: str
        """
        allowed_values = ["disabled", "points", "cashback"]  # noqa: E501
        if loyalty_program_type not in allowed_values:
            raise ValueError(
                "Invalid value for `loyalty_program_type` ({0}), must be one of {1}"  # noqa: E501
                .format(loyalty_program_type, allowed_values)
            )

        self._loyalty_program_type = loyalty_program_type

    @property
    def max_active_customers(self):
        """Gets the max_active_customers of this EmailPerformance.  # noqa: E501

        Maximum active customers allowed under their billing plan  # noqa: E501

        :return: The max_active_customers of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._max_active_customers

    @max_active_customers.setter
    def max_active_customers(self, max_active_customers):
        """Sets the max_active_customers of this EmailPerformance.

        Maximum active customers allowed under their billing plan  # noqa: E501

        :param max_active_customers: The max_active_customers of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._max_active_customers = max_active_customers

    @property
    def max_emails_per_day(self):
        """Gets the max_emails_per_day of this EmailPerformance.  # noqa: E501

        Max emails per day  # noqa: E501

        :return: The max_emails_per_day of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._max_emails_per_day

    @max_emails_per_day.setter
    def max_emails_per_day(self, max_emails_per_day):
        """Sets the max_emails_per_day of this EmailPerformance.

        Max emails per day  # noqa: E501

        :param max_emails_per_day: The max_emails_per_day of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._max_emails_per_day = max_emails_per_day

    @property
    def max_emails_per_hour(self):
        """Gets the max_emails_per_hour of this EmailPerformance.  # noqa: E501

        Max emails per hour  # noqa: E501

        :return: The max_emails_per_hour of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._max_emails_per_hour

    @max_emails_per_hour.setter
    def max_emails_per_hour(self, max_emails_per_hour):
        """Sets the max_emails_per_hour of this EmailPerformance.

        Max emails per hour  # noqa: E501

        :param max_emails_per_hour: The max_emails_per_hour of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._max_emails_per_hour = max_emails_per_hour

    @property
    def max_emails_per_month(self):
        """Gets the max_emails_per_month of this EmailPerformance.  # noqa: E501

        Max emails per month  # noqa: E501

        :return: The max_emails_per_month of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._max_emails_per_month

    @max_emails_per_month.setter
    def max_emails_per_month(self, max_emails_per_month):
        """Sets the max_emails_per_month of this EmailPerformance.

        Max emails per month  # noqa: E501

        :param max_emails_per_month: The max_emails_per_month of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._max_emails_per_month = max_emails_per_month

    @property
    def paused_for_spam(self):
        """Gets the paused_for_spam of this EmailPerformance.  # noqa: E501

        True if campaign/flow emails are paused due to spam complaints.  # noqa: E501

        :return: The paused_for_spam of this EmailPerformance.  # noqa: E501
        :rtype: bool
        """
        return self._paused_for_spam

    @paused_for_spam.setter
    def paused_for_spam(self, paused_for_spam):
        """Sets the paused_for_spam of this EmailPerformance.

        True if campaign/flow emails are paused due to spam complaints.  # noqa: E501

        :param paused_for_spam: The paused_for_spam of this EmailPerformance.  # noqa: E501
        :type: bool
        """

        self._paused_for_spam = paused_for_spam

    @property
    def revenue(self):
        """Gets the revenue of this EmailPerformance.  # noqa: E501

        Revenue  # noqa: E501

        :return: The revenue of this EmailPerformance.  # noqa: E501
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this EmailPerformance.

        Revenue  # noqa: E501

        :param revenue: The revenue of this EmailPerformance.  # noqa: E501
        :type: float
        """

        self._revenue = revenue

    @property
    def sent_emails_per_day(self):
        """Gets the sent_emails_per_day of this EmailPerformance.  # noqa: E501

        Sent emails last 24 hours  # noqa: E501

        :return: The sent_emails_per_day of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails_per_day

    @sent_emails_per_day.setter
    def sent_emails_per_day(self, sent_emails_per_day):
        """Sets the sent_emails_per_day of this EmailPerformance.

        Sent emails last 24 hours  # noqa: E501

        :param sent_emails_per_day: The sent_emails_per_day of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._sent_emails_per_day = sent_emails_per_day

    @property
    def sent_emails_per_hour(self):
        """Gets the sent_emails_per_hour of this EmailPerformance.  # noqa: E501

        Sent emails last hour  # noqa: E501

        :return: The sent_emails_per_hour of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails_per_hour

    @sent_emails_per_hour.setter
    def sent_emails_per_hour(self, sent_emails_per_hour):
        """Sets the sent_emails_per_hour of this EmailPerformance.

        Sent emails last hour  # noqa: E501

        :param sent_emails_per_hour: The sent_emails_per_hour of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._sent_emails_per_hour = sent_emails_per_hour

    @property
    def sent_emails_per_month(self):
        """Gets the sent_emails_per_month of this EmailPerformance.  # noqa: E501

        Sent emails last 31 days  # noqa: E501

        :return: The sent_emails_per_month of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails_per_month

    @sent_emails_per_month.setter
    def sent_emails_per_month(self, sent_emails_per_month):
        """Sets the sent_emails_per_month of this EmailPerformance.

        Sent emails last 31 days  # noqa: E501

        :param sent_emails_per_month: The sent_emails_per_month of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._sent_emails_per_month = sent_emails_per_month

    @property
    def sequence_send_count(self):
        """Gets the sequence_send_count of this EmailPerformance.  # noqa: E501

        Total sequence (campaign/flow) emails sent  # noqa: E501

        :return: The sequence_send_count of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._sequence_send_count

    @sequence_send_count.setter
    def sequence_send_count(self, sequence_send_count):
        """Sets the sequence_send_count of this EmailPerformance.

        Total sequence (campaign/flow) emails sent  # noqa: E501

        :param sequence_send_count: The sequence_send_count of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._sequence_send_count = sequence_send_count

    @property
    def spam_count(self):
        """Gets the spam_count of this EmailPerformance.  # noqa: E501

        Spam complaints  # noqa: E501

        :return: The spam_count of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._spam_count

    @spam_count.setter
    def spam_count(self, spam_count):
        """Sets the spam_count of this EmailPerformance.

        Spam complaints  # noqa: E501

        :param spam_count: The spam_count of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._spam_count = spam_count

    @property
    def spam_percentage(self):
        """Gets the spam_percentage of this EmailPerformance.  # noqa: E501

        Spam percentage rate based upon our look back window.  This should be under one half a percent or the account will be paused for sending.  # noqa: E501

        :return: The spam_percentage of this EmailPerformance.  # noqa: E501
        :rtype: float
        """
        return self._spam_percentage

    @spam_percentage.setter
    def spam_percentage(self, spam_percentage):
        """Sets the spam_percentage of this EmailPerformance.

        Spam percentage rate based upon our look back window.  This should be under one half a percent or the account will be paused for sending.  # noqa: E501

        :param spam_percentage: The spam_percentage of this EmailPerformance.  # noqa: E501
        :type: float
        """

        self._spam_percentage = spam_percentage

    @property
    def spam_percentage_formatted(self):
        """Gets the spam_percentage_formatted of this EmailPerformance.  # noqa: E501

        Spam percentage rate (formatted) based upon our look back window.  This should be under one half a percent or the account will be paused for sending.  # noqa: E501

        :return: The spam_percentage_formatted of this EmailPerformance.  # noqa: E501
        :rtype: str
        """
        return self._spam_percentage_formatted

    @spam_percentage_formatted.setter
    def spam_percentage_formatted(self, spam_percentage_formatted):
        """Sets the spam_percentage_formatted of this EmailPerformance.

        Spam percentage rate (formatted) based upon our look back window.  This should be under one half a percent or the account will be paused for sending.  # noqa: E501

        :param spam_percentage_formatted: The spam_percentage_formatted of this EmailPerformance.  # noqa: E501
        :type: str
        """

        self._spam_percentage_formatted = spam_percentage_formatted

    @property
    def transactional_send_count(self):
        """Gets the transactional_send_count of this EmailPerformance.  # noqa: E501

        Total transactions emails sent  # noqa: E501

        :return: The transactional_send_count of this EmailPerformance.  # noqa: E501
        :rtype: int
        """
        return self._transactional_send_count

    @transactional_send_count.setter
    def transactional_send_count(self, transactional_send_count):
        """Sets the transactional_send_count of this EmailPerformance.

        Total transactions emails sent  # noqa: E501

        :param transactional_send_count: The transactional_send_count of this EmailPerformance.  # noqa: E501
        :type: int
        """

        self._transactional_send_count = transactional_send_count

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
        if issubclass(EmailPerformance, dict):
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
        if not isinstance(other, EmailPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

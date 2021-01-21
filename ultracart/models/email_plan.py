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


class EmailPlan(object):
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
        'additional_customers': 'int',
        'additional_emails': 'int',
        'allow_list_import': 'bool',
        'allow_tracking_emails': 'bool',
        'customer_tiers': 'list[EmailPlanAdditional]',
        'initial_sending_limits': 'int',
        'plan_customers': 'int',
        'plan_emails': 'int',
        'plan_name': 'str',
        'plan_name_formatted': 'str',
        'require_order_within_last_days': 'int',
        'revenue_percent': 'int',
        'spam_percent_limit': 'int',
        'total_customers': 'int',
        'total_emails': 'int',
        'upgrade_to': 'int'
    }

    attribute_map = {
        'additional_customers': 'additional_customers',
        'additional_emails': 'additional_emails',
        'allow_list_import': 'allow_list_import',
        'allow_tracking_emails': 'allow_tracking_emails',
        'customer_tiers': 'customer_tiers',
        'initial_sending_limits': 'initial_sending_limits',
        'plan_customers': 'plan_customers',
        'plan_emails': 'plan_emails',
        'plan_name': 'plan_name',
        'plan_name_formatted': 'plan_name_formatted',
        'require_order_within_last_days': 'require_order_within_last_days',
        'revenue_percent': 'revenue_percent',
        'spam_percent_limit': 'spam_percent_limit',
        'total_customers': 'total_customers',
        'total_emails': 'total_emails',
        'upgrade_to': 'upgrade_to'
    }

    def __init__(self, additional_customers=None, additional_emails=None, allow_list_import=None, allow_tracking_emails=None, customer_tiers=None, initial_sending_limits=None, plan_customers=None, plan_emails=None, plan_name=None, plan_name_formatted=None, require_order_within_last_days=None, revenue_percent=None, spam_percent_limit=None, total_customers=None, total_emails=None, upgrade_to=None):  # noqa: E501
        """EmailPlan - a model defined in Swagger"""  # noqa: E501

        self._additional_customers = None
        self._additional_emails = None
        self._allow_list_import = None
        self._allow_tracking_emails = None
        self._customer_tiers = None
        self._initial_sending_limits = None
        self._plan_customers = None
        self._plan_emails = None
        self._plan_name = None
        self._plan_name_formatted = None
        self._require_order_within_last_days = None
        self._revenue_percent = None
        self._spam_percent_limit = None
        self._total_customers = None
        self._total_emails = None
        self._upgrade_to = None
        self.discriminator = None

        if additional_customers is not None:
            self.additional_customers = additional_customers
        if additional_emails is not None:
            self.additional_emails = additional_emails
        if allow_list_import is not None:
            self.allow_list_import = allow_list_import
        if allow_tracking_emails is not None:
            self.allow_tracking_emails = allow_tracking_emails
        if customer_tiers is not None:
            self.customer_tiers = customer_tiers
        if initial_sending_limits is not None:
            self.initial_sending_limits = initial_sending_limits
        if plan_customers is not None:
            self.plan_customers = plan_customers
        if plan_emails is not None:
            self.plan_emails = plan_emails
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_name_formatted is not None:
            self.plan_name_formatted = plan_name_formatted
        if require_order_within_last_days is not None:
            self.require_order_within_last_days = require_order_within_last_days
        if revenue_percent is not None:
            self.revenue_percent = revenue_percent
        if spam_percent_limit is not None:
            self.spam_percent_limit = spam_percent_limit
        if total_customers is not None:
            self.total_customers = total_customers
        if total_emails is not None:
            self.total_emails = total_emails
        if upgrade_to is not None:
            self.upgrade_to = upgrade_to

    @property
    def additional_customers(self):
        """Gets the additional_customers of this EmailPlan.  # noqa: E501


        :return: The additional_customers of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._additional_customers

    @additional_customers.setter
    def additional_customers(self, additional_customers):
        """Sets the additional_customers of this EmailPlan.


        :param additional_customers: The additional_customers of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._additional_customers = additional_customers

    @property
    def additional_emails(self):
        """Gets the additional_emails of this EmailPlan.  # noqa: E501


        :return: The additional_emails of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._additional_emails

    @additional_emails.setter
    def additional_emails(self, additional_emails):
        """Sets the additional_emails of this EmailPlan.


        :param additional_emails: The additional_emails of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._additional_emails = additional_emails

    @property
    def allow_list_import(self):
        """Gets the allow_list_import of this EmailPlan.  # noqa: E501


        :return: The allow_list_import of this EmailPlan.  # noqa: E501
        :rtype: bool
        """
        return self._allow_list_import

    @allow_list_import.setter
    def allow_list_import(self, allow_list_import):
        """Sets the allow_list_import of this EmailPlan.


        :param allow_list_import: The allow_list_import of this EmailPlan.  # noqa: E501
        :type: bool
        """

        self._allow_list_import = allow_list_import

    @property
    def allow_tracking_emails(self):
        """Gets the allow_tracking_emails of this EmailPlan.  # noqa: E501


        :return: The allow_tracking_emails of this EmailPlan.  # noqa: E501
        :rtype: bool
        """
        return self._allow_tracking_emails

    @allow_tracking_emails.setter
    def allow_tracking_emails(self, allow_tracking_emails):
        """Sets the allow_tracking_emails of this EmailPlan.


        :param allow_tracking_emails: The allow_tracking_emails of this EmailPlan.  # noqa: E501
        :type: bool
        """

        self._allow_tracking_emails = allow_tracking_emails

    @property
    def customer_tiers(self):
        """Gets the customer_tiers of this EmailPlan.  # noqa: E501


        :return: The customer_tiers of this EmailPlan.  # noqa: E501
        :rtype: list[EmailPlanAdditional]
        """
        return self._customer_tiers

    @customer_tiers.setter
    def customer_tiers(self, customer_tiers):
        """Sets the customer_tiers of this EmailPlan.


        :param customer_tiers: The customer_tiers of this EmailPlan.  # noqa: E501
        :type: list[EmailPlanAdditional]
        """

        self._customer_tiers = customer_tiers

    @property
    def initial_sending_limits(self):
        """Gets the initial_sending_limits of this EmailPlan.  # noqa: E501


        :return: The initial_sending_limits of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._initial_sending_limits

    @initial_sending_limits.setter
    def initial_sending_limits(self, initial_sending_limits):
        """Sets the initial_sending_limits of this EmailPlan.


        :param initial_sending_limits: The initial_sending_limits of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._initial_sending_limits = initial_sending_limits

    @property
    def plan_customers(self):
        """Gets the plan_customers of this EmailPlan.  # noqa: E501


        :return: The plan_customers of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._plan_customers

    @plan_customers.setter
    def plan_customers(self, plan_customers):
        """Sets the plan_customers of this EmailPlan.


        :param plan_customers: The plan_customers of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._plan_customers = plan_customers

    @property
    def plan_emails(self):
        """Gets the plan_emails of this EmailPlan.  # noqa: E501


        :return: The plan_emails of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._plan_emails

    @plan_emails.setter
    def plan_emails(self, plan_emails):
        """Sets the plan_emails of this EmailPlan.


        :param plan_emails: The plan_emails of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._plan_emails = plan_emails

    @property
    def plan_name(self):
        """Gets the plan_name of this EmailPlan.  # noqa: E501


        :return: The plan_name of this EmailPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this EmailPlan.


        :param plan_name: The plan_name of this EmailPlan.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def plan_name_formatted(self):
        """Gets the plan_name_formatted of this EmailPlan.  # noqa: E501


        :return: The plan_name_formatted of this EmailPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_name_formatted

    @plan_name_formatted.setter
    def plan_name_formatted(self, plan_name_formatted):
        """Sets the plan_name_formatted of this EmailPlan.


        :param plan_name_formatted: The plan_name_formatted of this EmailPlan.  # noqa: E501
        :type: str
        """

        self._plan_name_formatted = plan_name_formatted

    @property
    def require_order_within_last_days(self):
        """Gets the require_order_within_last_days of this EmailPlan.  # noqa: E501


        :return: The require_order_within_last_days of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._require_order_within_last_days

    @require_order_within_last_days.setter
    def require_order_within_last_days(self, require_order_within_last_days):
        """Sets the require_order_within_last_days of this EmailPlan.


        :param require_order_within_last_days: The require_order_within_last_days of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._require_order_within_last_days = require_order_within_last_days

    @property
    def revenue_percent(self):
        """Gets the revenue_percent of this EmailPlan.  # noqa: E501


        :return: The revenue_percent of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._revenue_percent

    @revenue_percent.setter
    def revenue_percent(self, revenue_percent):
        """Sets the revenue_percent of this EmailPlan.


        :param revenue_percent: The revenue_percent of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._revenue_percent = revenue_percent

    @property
    def spam_percent_limit(self):
        """Gets the spam_percent_limit of this EmailPlan.  # noqa: E501


        :return: The spam_percent_limit of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._spam_percent_limit

    @spam_percent_limit.setter
    def spam_percent_limit(self, spam_percent_limit):
        """Sets the spam_percent_limit of this EmailPlan.


        :param spam_percent_limit: The spam_percent_limit of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._spam_percent_limit = spam_percent_limit

    @property
    def total_customers(self):
        """Gets the total_customers of this EmailPlan.  # noqa: E501


        :return: The total_customers of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._total_customers

    @total_customers.setter
    def total_customers(self, total_customers):
        """Sets the total_customers of this EmailPlan.


        :param total_customers: The total_customers of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._total_customers = total_customers

    @property
    def total_emails(self):
        """Gets the total_emails of this EmailPlan.  # noqa: E501


        :return: The total_emails of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._total_emails

    @total_emails.setter
    def total_emails(self, total_emails):
        """Sets the total_emails of this EmailPlan.


        :param total_emails: The total_emails of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._total_emails = total_emails

    @property
    def upgrade_to(self):
        """Gets the upgrade_to of this EmailPlan.  # noqa: E501


        :return: The upgrade_to of this EmailPlan.  # noqa: E501
        :rtype: int
        """
        return self._upgrade_to

    @upgrade_to.setter
    def upgrade_to(self, upgrade_to):
        """Sets the upgrade_to of this EmailPlan.


        :param upgrade_to: The upgrade_to of this EmailPlan.  # noqa: E501
        :type: int
        """

        self._upgrade_to = upgrade_to

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
        if issubclass(EmailPlan, dict):
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
        if not isinstance(other, EmailPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

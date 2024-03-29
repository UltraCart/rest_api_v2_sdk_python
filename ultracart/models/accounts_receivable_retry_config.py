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


class AccountsReceivableRetryConfig(object):
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
        'allow_process_linked_accounts': 'bool',
        'cancel_auto_order': 'bool',
        'current_service_plan': 'str',
        'daily_activity_list': 'list[AccountsReceivableRetryDayActivity]',
        'managed_by_linked_account_merchant_id': 'bool',
        'merchant_id': 'str',
        'notify_emails': 'list[str]',
        'notify_rejections': 'bool',
        'notify_successes': 'bool',
        'process_linked_accounts': 'bool',
        'processing_percentage': 'str',
        'reject_at_end': 'bool',
        'transaction_rejects': 'list[AccountsReceivableRetryTransactionReject]',
        'trial_mode': 'bool',
        'trial_mode_expiration_dts': 'str'
    }

    attribute_map = {
        'active': 'active',
        'allow_process_linked_accounts': 'allow_process_linked_accounts',
        'cancel_auto_order': 'cancel_auto_order',
        'current_service_plan': 'current_service_plan',
        'daily_activity_list': 'daily_activity_list',
        'managed_by_linked_account_merchant_id': 'managed_by_linked_account_merchant_id',
        'merchant_id': 'merchant_id',
        'notify_emails': 'notify_emails',
        'notify_rejections': 'notify_rejections',
        'notify_successes': 'notify_successes',
        'process_linked_accounts': 'process_linked_accounts',
        'processing_percentage': 'processing_percentage',
        'reject_at_end': 'reject_at_end',
        'transaction_rejects': 'transaction_rejects',
        'trial_mode': 'trial_mode',
        'trial_mode_expiration_dts': 'trial_mode_expiration_dts'
    }

    def __init__(self, active=None, allow_process_linked_accounts=None, cancel_auto_order=None, current_service_plan=None, daily_activity_list=None, managed_by_linked_account_merchant_id=None, merchant_id=None, notify_emails=None, notify_rejections=None, notify_successes=None, process_linked_accounts=None, processing_percentage=None, reject_at_end=None, transaction_rejects=None, trial_mode=None, trial_mode_expiration_dts=None):  # noqa: E501
        """AccountsReceivableRetryConfig - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._allow_process_linked_accounts = None
        self._cancel_auto_order = None
        self._current_service_plan = None
        self._daily_activity_list = None
        self._managed_by_linked_account_merchant_id = None
        self._merchant_id = None
        self._notify_emails = None
        self._notify_rejections = None
        self._notify_successes = None
        self._process_linked_accounts = None
        self._processing_percentage = None
        self._reject_at_end = None
        self._transaction_rejects = None
        self._trial_mode = None
        self._trial_mode_expiration_dts = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if allow_process_linked_accounts is not None:
            self.allow_process_linked_accounts = allow_process_linked_accounts
        if cancel_auto_order is not None:
            self.cancel_auto_order = cancel_auto_order
        if current_service_plan is not None:
            self.current_service_plan = current_service_plan
        if daily_activity_list is not None:
            self.daily_activity_list = daily_activity_list
        if managed_by_linked_account_merchant_id is not None:
            self.managed_by_linked_account_merchant_id = managed_by_linked_account_merchant_id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if notify_emails is not None:
            self.notify_emails = notify_emails
        if notify_rejections is not None:
            self.notify_rejections = notify_rejections
        if notify_successes is not None:
            self.notify_successes = notify_successes
        if process_linked_accounts is not None:
            self.process_linked_accounts = process_linked_accounts
        if processing_percentage is not None:
            self.processing_percentage = processing_percentage
        if reject_at_end is not None:
            self.reject_at_end = reject_at_end
        if transaction_rejects is not None:
            self.transaction_rejects = transaction_rejects
        if trial_mode is not None:
            self.trial_mode = trial_mode
        if trial_mode_expiration_dts is not None:
            self.trial_mode_expiration_dts = trial_mode_expiration_dts

    @property
    def active(self):
        """Gets the active of this AccountsReceivableRetryConfig.  # noqa: E501

        True if the retry should run daily.  False puts the retry service into an inactive state for this merchant.  # noqa: E501

        :return: The active of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AccountsReceivableRetryConfig.

        True if the retry should run daily.  False puts the retry service into an inactive state for this merchant.  # noqa: E501

        :param active: The active of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def allow_process_linked_accounts(self):
        """Gets the allow_process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501

        True if this account has linked accounts that it can process.  # noqa: E501

        :return: The allow_process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._allow_process_linked_accounts

    @allow_process_linked_accounts.setter
    def allow_process_linked_accounts(self, allow_process_linked_accounts):
        """Sets the allow_process_linked_accounts of this AccountsReceivableRetryConfig.

        True if this account has linked accounts that it can process.  # noqa: E501

        :param allow_process_linked_accounts: The allow_process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._allow_process_linked_accounts = allow_process_linked_accounts

    @property
    def cancel_auto_order(self):
        """Gets the cancel_auto_order of this AccountsReceivableRetryConfig.  # noqa: E501

        If true also cancel the auto order if the order is rejected at the end  # noqa: E501

        :return: The cancel_auto_order of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_auto_order

    @cancel_auto_order.setter
    def cancel_auto_order(self, cancel_auto_order):
        """Sets the cancel_auto_order of this AccountsReceivableRetryConfig.

        If true also cancel the auto order if the order is rejected at the end  # noqa: E501

        :param cancel_auto_order: The cancel_auto_order of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._cancel_auto_order = cancel_auto_order

    @property
    def current_service_plan(self):
        """Gets the current_service_plan of this AccountsReceivableRetryConfig.  # noqa: E501

        The current service plan that the account is on.  # noqa: E501

        :return: The current_service_plan of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: str
        """
        return self._current_service_plan

    @current_service_plan.setter
    def current_service_plan(self, current_service_plan):
        """Sets the current_service_plan of this AccountsReceivableRetryConfig.

        The current service plan that the account is on.  # noqa: E501

        :param current_service_plan: The current_service_plan of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: str
        """

        self._current_service_plan = current_service_plan

    @property
    def daily_activity_list(self):
        """Gets the daily_activity_list of this AccountsReceivableRetryConfig.  # noqa: E501

        A list of days and what actions should take place on those days after an order reaches accounts receivable  # noqa: E501

        :return: The daily_activity_list of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: list[AccountsReceivableRetryDayActivity]
        """
        return self._daily_activity_list

    @daily_activity_list.setter
    def daily_activity_list(self, daily_activity_list):
        """Sets the daily_activity_list of this AccountsReceivableRetryConfig.

        A list of days and what actions should take place on those days after an order reaches accounts receivable  # noqa: E501

        :param daily_activity_list: The daily_activity_list of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: list[AccountsReceivableRetryDayActivity]
        """

        self._daily_activity_list = daily_activity_list

    @property
    def managed_by_linked_account_merchant_id(self):
        """Gets the managed_by_linked_account_merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501

        If not null, this account is managed by the specified parent merchant id.  # noqa: E501

        :return: The managed_by_linked_account_merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._managed_by_linked_account_merchant_id

    @managed_by_linked_account_merchant_id.setter
    def managed_by_linked_account_merchant_id(self, managed_by_linked_account_merchant_id):
        """Sets the managed_by_linked_account_merchant_id of this AccountsReceivableRetryConfig.

        If not null, this account is managed by the specified parent merchant id.  # noqa: E501

        :param managed_by_linked_account_merchant_id: The managed_by_linked_account_merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._managed_by_linked_account_merchant_id = managed_by_linked_account_merchant_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501

        UltraCart merchant ID  # noqa: E501

        :return: The merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this AccountsReceivableRetryConfig.

        UltraCart merchant ID  # noqa: E501

        :param merchant_id: The merchant_id of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def notify_emails(self):
        """Gets the notify_emails of this AccountsReceivableRetryConfig.  # noqa: E501

        A list of email addresses to receive summary notifications from the retry service.  # noqa: E501

        :return: The notify_emails of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_emails

    @notify_emails.setter
    def notify_emails(self, notify_emails):
        """Sets the notify_emails of this AccountsReceivableRetryConfig.

        A list of email addresses to receive summary notifications from the retry service.  # noqa: E501

        :param notify_emails: The notify_emails of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: list[str]
        """

        self._notify_emails = notify_emails

    @property
    def notify_rejections(self):
        """Gets the notify_rejections of this AccountsReceivableRetryConfig.  # noqa: E501

        If true, email addresses are notified of rejections.  # noqa: E501

        :return: The notify_rejections of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._notify_rejections

    @notify_rejections.setter
    def notify_rejections(self, notify_rejections):
        """Sets the notify_rejections of this AccountsReceivableRetryConfig.

        If true, email addresses are notified of rejections.  # noqa: E501

        :param notify_rejections: The notify_rejections of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._notify_rejections = notify_rejections

    @property
    def notify_successes(self):
        """Gets the notify_successes of this AccountsReceivableRetryConfig.  # noqa: E501

        If true, email addresses are notified of successful charges.  # noqa: E501

        :return: The notify_successes of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._notify_successes

    @notify_successes.setter
    def notify_successes(self, notify_successes):
        """Sets the notify_successes of this AccountsReceivableRetryConfig.

        If true, email addresses are notified of successful charges.  # noqa: E501

        :param notify_successes: The notify_successes of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._notify_successes = notify_successes

    @property
    def process_linked_accounts(self):
        """Gets the process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501

        If true, all linked accounts are also processed using the same rules.  # noqa: E501

        :return: The process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._process_linked_accounts

    @process_linked_accounts.setter
    def process_linked_accounts(self, process_linked_accounts):
        """Sets the process_linked_accounts of this AccountsReceivableRetryConfig.

        If true, all linked accounts are also processed using the same rules.  # noqa: E501

        :param process_linked_accounts: The process_linked_accounts of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._process_linked_accounts = process_linked_accounts

    @property
    def processing_percentage(self):
        """Gets the processing_percentage of this AccountsReceivableRetryConfig.  # noqa: E501

        The percentage rate charged for the service.  # noqa: E501

        :return: The processing_percentage of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: str
        """
        return self._processing_percentage

    @processing_percentage.setter
    def processing_percentage(self, processing_percentage):
        """Sets the processing_percentage of this AccountsReceivableRetryConfig.

        The percentage rate charged for the service.  # noqa: E501

        :param processing_percentage: The processing_percentage of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: str
        """

        self._processing_percentage = processing_percentage

    @property
    def reject_at_end(self):
        """Gets the reject_at_end of this AccountsReceivableRetryConfig.  # noqa: E501

        If true, the order is rejected the day after the last configured activity day  # noqa: E501

        :return: The reject_at_end of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._reject_at_end

    @reject_at_end.setter
    def reject_at_end(self, reject_at_end):
        """Sets the reject_at_end of this AccountsReceivableRetryConfig.

        If true, the order is rejected the day after the last configured activity day  # noqa: E501

        :param reject_at_end: The reject_at_end of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._reject_at_end = reject_at_end

    @property
    def transaction_rejects(self):
        """Gets the transaction_rejects of this AccountsReceivableRetryConfig.  # noqa: E501

        Array of key/value pairs that when found in the response cause the rejection of the transaction.  # noqa: E501

        :return: The transaction_rejects of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: list[AccountsReceivableRetryTransactionReject]
        """
        return self._transaction_rejects

    @transaction_rejects.setter
    def transaction_rejects(self, transaction_rejects):
        """Sets the transaction_rejects of this AccountsReceivableRetryConfig.

        Array of key/value pairs that when found in the response cause the rejection of the transaction.  # noqa: E501

        :param transaction_rejects: The transaction_rejects of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: list[AccountsReceivableRetryTransactionReject]
        """

        self._transaction_rejects = transaction_rejects

    @property
    def trial_mode(self):
        """Gets the trial_mode of this AccountsReceivableRetryConfig.  # noqa: E501

        True if the account is currently in trial mode.  Set to false to exit trial mode.  # noqa: E501

        :return: The trial_mode of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: bool
        """
        return self._trial_mode

    @trial_mode.setter
    def trial_mode(self, trial_mode):
        """Sets the trial_mode of this AccountsReceivableRetryConfig.

        True if the account is currently in trial mode.  Set to false to exit trial mode.  # noqa: E501

        :param trial_mode: The trial_mode of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: bool
        """

        self._trial_mode = trial_mode

    @property
    def trial_mode_expiration_dts(self):
        """Gets the trial_mode_expiration_dts of this AccountsReceivableRetryConfig.  # noqa: E501

        The date when trial mode expires.  If this date is reached without exiting trial mode, the service will de-activate.  # noqa: E501

        :return: The trial_mode_expiration_dts of this AccountsReceivableRetryConfig.  # noqa: E501
        :rtype: str
        """
        return self._trial_mode_expiration_dts

    @trial_mode_expiration_dts.setter
    def trial_mode_expiration_dts(self, trial_mode_expiration_dts):
        """Sets the trial_mode_expiration_dts of this AccountsReceivableRetryConfig.

        The date when trial mode expires.  If this date is reached without exiting trial mode, the service will de-activate.  # noqa: E501

        :param trial_mode_expiration_dts: The trial_mode_expiration_dts of this AccountsReceivableRetryConfig.  # noqa: E501
        :type: str
        """

        self._trial_mode_expiration_dts = trial_mode_expiration_dts

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
        if issubclass(AccountsReceivableRetryConfig, dict):
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
        if not isinstance(other, AccountsReceivableRetryConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

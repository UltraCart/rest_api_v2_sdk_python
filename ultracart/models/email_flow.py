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


class EmailFlow(object):
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
        'allow_multiple_concurrent_enrollments': 'bool',
        'back_populating': 'bool',
        'click_rate_formatted': 'str',
        'created_dts': 'str',
        'deleted': 'bool',
        'email_communication_sequence_uuid': 'str',
        'email_flow_uuid': 'str',
        'end_once_customer_purchases': 'bool',
        'end_once_customer_purchases_anywhere': 'bool',
        'enrolled_customers': 'int',
        'esp_domain_user': 'str',
        'esp_domain_uuid': 'str',
        'esp_flow_folder_uuid': 'str',
        'esp_friendly_name': 'str',
        'filter_profile_equation_json': 'str',
        'library_item_oid': 'int',
        'merchant_id': 'str',
        'name': 'str',
        'open_rate_formatted': 'str',
        'revenue_formatted': 'str',
        'revenue_per_customer_formatted': 'str',
        'screenshot_large_full_url': 'str',
        'sms_esp_twilio_uuid': 'str',
        'sms_phone_number': 'str',
        'status': 'str',
        'status_dts': 'str',
        'storefront_oid': 'int',
        'trigger_parameter': 'str',
        'trigger_parameter_name': 'str',
        'trigger_type': 'str'
    }

    attribute_map = {
        'allow_multiple_concurrent_enrollments': 'allow_multiple_concurrent_enrollments',
        'back_populating': 'back_populating',
        'click_rate_formatted': 'click_rate_formatted',
        'created_dts': 'created_dts',
        'deleted': 'deleted',
        'email_communication_sequence_uuid': 'email_communication_sequence_uuid',
        'email_flow_uuid': 'email_flow_uuid',
        'end_once_customer_purchases': 'end_once_customer_purchases',
        'end_once_customer_purchases_anywhere': 'end_once_customer_purchases_anywhere',
        'enrolled_customers': 'enrolled_customers',
        'esp_domain_user': 'esp_domain_user',
        'esp_domain_uuid': 'esp_domain_uuid',
        'esp_flow_folder_uuid': 'esp_flow_folder_uuid',
        'esp_friendly_name': 'esp_friendly_name',
        'filter_profile_equation_json': 'filter_profile_equation_json',
        'library_item_oid': 'library_item_oid',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'open_rate_formatted': 'open_rate_formatted',
        'revenue_formatted': 'revenue_formatted',
        'revenue_per_customer_formatted': 'revenue_per_customer_formatted',
        'screenshot_large_full_url': 'screenshot_large_full_url',
        'sms_esp_twilio_uuid': 'sms_esp_twilio_uuid',
        'sms_phone_number': 'sms_phone_number',
        'status': 'status',
        'status_dts': 'status_dts',
        'storefront_oid': 'storefront_oid',
        'trigger_parameter': 'trigger_parameter',
        'trigger_parameter_name': 'trigger_parameter_name',
        'trigger_type': 'trigger_type'
    }

    def __init__(self, allow_multiple_concurrent_enrollments=None, back_populating=None, click_rate_formatted=None, created_dts=None, deleted=None, email_communication_sequence_uuid=None, email_flow_uuid=None, end_once_customer_purchases=None, end_once_customer_purchases_anywhere=None, enrolled_customers=None, esp_domain_user=None, esp_domain_uuid=None, esp_flow_folder_uuid=None, esp_friendly_name=None, filter_profile_equation_json=None, library_item_oid=None, merchant_id=None, name=None, open_rate_formatted=None, revenue_formatted=None, revenue_per_customer_formatted=None, screenshot_large_full_url=None, sms_esp_twilio_uuid=None, sms_phone_number=None, status=None, status_dts=None, storefront_oid=None, trigger_parameter=None, trigger_parameter_name=None, trigger_type=None):  # noqa: E501
        """EmailFlow - a model defined in Swagger"""  # noqa: E501

        self._allow_multiple_concurrent_enrollments = None
        self._back_populating = None
        self._click_rate_formatted = None
        self._created_dts = None
        self._deleted = None
        self._email_communication_sequence_uuid = None
        self._email_flow_uuid = None
        self._end_once_customer_purchases = None
        self._end_once_customer_purchases_anywhere = None
        self._enrolled_customers = None
        self._esp_domain_user = None
        self._esp_domain_uuid = None
        self._esp_flow_folder_uuid = None
        self._esp_friendly_name = None
        self._filter_profile_equation_json = None
        self._library_item_oid = None
        self._merchant_id = None
        self._name = None
        self._open_rate_formatted = None
        self._revenue_formatted = None
        self._revenue_per_customer_formatted = None
        self._screenshot_large_full_url = None
        self._sms_esp_twilio_uuid = None
        self._sms_phone_number = None
        self._status = None
        self._status_dts = None
        self._storefront_oid = None
        self._trigger_parameter = None
        self._trigger_parameter_name = None
        self._trigger_type = None
        self.discriminator = None

        if allow_multiple_concurrent_enrollments is not None:
            self.allow_multiple_concurrent_enrollments = allow_multiple_concurrent_enrollments
        if back_populating is not None:
            self.back_populating = back_populating
        if click_rate_formatted is not None:
            self.click_rate_formatted = click_rate_formatted
        if created_dts is not None:
            self.created_dts = created_dts
        if deleted is not None:
            self.deleted = deleted
        if email_communication_sequence_uuid is not None:
            self.email_communication_sequence_uuid = email_communication_sequence_uuid
        if email_flow_uuid is not None:
            self.email_flow_uuid = email_flow_uuid
        if end_once_customer_purchases is not None:
            self.end_once_customer_purchases = end_once_customer_purchases
        if end_once_customer_purchases_anywhere is not None:
            self.end_once_customer_purchases_anywhere = end_once_customer_purchases_anywhere
        if enrolled_customers is not None:
            self.enrolled_customers = enrolled_customers
        if esp_domain_user is not None:
            self.esp_domain_user = esp_domain_user
        if esp_domain_uuid is not None:
            self.esp_domain_uuid = esp_domain_uuid
        if esp_flow_folder_uuid is not None:
            self.esp_flow_folder_uuid = esp_flow_folder_uuid
        if esp_friendly_name is not None:
            self.esp_friendly_name = esp_friendly_name
        if filter_profile_equation_json is not None:
            self.filter_profile_equation_json = filter_profile_equation_json
        if library_item_oid is not None:
            self.library_item_oid = library_item_oid
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if open_rate_formatted is not None:
            self.open_rate_formatted = open_rate_formatted
        if revenue_formatted is not None:
            self.revenue_formatted = revenue_formatted
        if revenue_per_customer_formatted is not None:
            self.revenue_per_customer_formatted = revenue_per_customer_formatted
        if screenshot_large_full_url is not None:
            self.screenshot_large_full_url = screenshot_large_full_url
        if sms_esp_twilio_uuid is not None:
            self.sms_esp_twilio_uuid = sms_esp_twilio_uuid
        if sms_phone_number is not None:
            self.sms_phone_number = sms_phone_number
        if status is not None:
            self.status = status
        if status_dts is not None:
            self.status_dts = status_dts
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if trigger_parameter is not None:
            self.trigger_parameter = trigger_parameter
        if trigger_parameter_name is not None:
            self.trigger_parameter_name = trigger_parameter_name
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def allow_multiple_concurrent_enrollments(self):
        """Gets the allow_multiple_concurrent_enrollments of this EmailFlow.  # noqa: E501

        True if a customer may be enrolled in this flow multiple times  # noqa: E501

        :return: The allow_multiple_concurrent_enrollments of this EmailFlow.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_concurrent_enrollments

    @allow_multiple_concurrent_enrollments.setter
    def allow_multiple_concurrent_enrollments(self, allow_multiple_concurrent_enrollments):
        """Sets the allow_multiple_concurrent_enrollments of this EmailFlow.

        True if a customer may be enrolled in this flow multiple times  # noqa: E501

        :param allow_multiple_concurrent_enrollments: The allow_multiple_concurrent_enrollments of this EmailFlow.  # noqa: E501
        :type: bool
        """

        self._allow_multiple_concurrent_enrollments = allow_multiple_concurrent_enrollments

    @property
    def back_populating(self):
        """Gets the back_populating of this EmailFlow.  # noqa: E501

        True if the flow is currently performing a back population.  # noqa: E501

        :return: The back_populating of this EmailFlow.  # noqa: E501
        :rtype: bool
        """
        return self._back_populating

    @back_populating.setter
    def back_populating(self, back_populating):
        """Sets the back_populating of this EmailFlow.

        True if the flow is currently performing a back population.  # noqa: E501

        :param back_populating: The back_populating of this EmailFlow.  # noqa: E501
        :type: bool
        """

        self._back_populating = back_populating

    @property
    def click_rate_formatted(self):
        """Gets the click_rate_formatted of this EmailFlow.  # noqa: E501

        Click rate of emails, formatted  # noqa: E501

        :return: The click_rate_formatted of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._click_rate_formatted

    @click_rate_formatted.setter
    def click_rate_formatted(self, click_rate_formatted):
        """Sets the click_rate_formatted of this EmailFlow.

        Click rate of emails, formatted  # noqa: E501

        :param click_rate_formatted: The click_rate_formatted of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._click_rate_formatted = click_rate_formatted

    @property
    def created_dts(self):
        """Gets the created_dts of this EmailFlow.  # noqa: E501

        Created date  # noqa: E501

        :return: The created_dts of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._created_dts

    @created_dts.setter
    def created_dts(self, created_dts):
        """Sets the created_dts of this EmailFlow.

        Created date  # noqa: E501

        :param created_dts: The created_dts of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._created_dts = created_dts

    @property
    def deleted(self):
        """Gets the deleted of this EmailFlow.  # noqa: E501

        True if this campaign was deleted  # noqa: E501

        :return: The deleted of this EmailFlow.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this EmailFlow.

        True if this campaign was deleted  # noqa: E501

        :param deleted: The deleted of this EmailFlow.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def email_communication_sequence_uuid(self):
        """Gets the email_communication_sequence_uuid of this EmailFlow.  # noqa: E501

        Email communication sequence UUID  # noqa: E501

        :return: The email_communication_sequence_uuid of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._email_communication_sequence_uuid

    @email_communication_sequence_uuid.setter
    def email_communication_sequence_uuid(self, email_communication_sequence_uuid):
        """Sets the email_communication_sequence_uuid of this EmailFlow.

        Email communication sequence UUID  # noqa: E501

        :param email_communication_sequence_uuid: The email_communication_sequence_uuid of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._email_communication_sequence_uuid = email_communication_sequence_uuid

    @property
    def email_flow_uuid(self):
        """Gets the email_flow_uuid of this EmailFlow.  # noqa: E501

        Email flow UUID  # noqa: E501

        :return: The email_flow_uuid of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._email_flow_uuid

    @email_flow_uuid.setter
    def email_flow_uuid(self, email_flow_uuid):
        """Sets the email_flow_uuid of this EmailFlow.

        Email flow UUID  # noqa: E501

        :param email_flow_uuid: The email_flow_uuid of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._email_flow_uuid = email_flow_uuid

    @property
    def end_once_customer_purchases(self):
        """Gets the end_once_customer_purchases of this EmailFlow.  # noqa: E501

        True if the customer should end the flow once they purchase from an email on this flow  # noqa: E501

        :return: The end_once_customer_purchases of this EmailFlow.  # noqa: E501
        :rtype: bool
        """
        return self._end_once_customer_purchases

    @end_once_customer_purchases.setter
    def end_once_customer_purchases(self, end_once_customer_purchases):
        """Sets the end_once_customer_purchases of this EmailFlow.

        True if the customer should end the flow once they purchase from an email on this flow  # noqa: E501

        :param end_once_customer_purchases: The end_once_customer_purchases of this EmailFlow.  # noqa: E501
        :type: bool
        """

        self._end_once_customer_purchases = end_once_customer_purchases

    @property
    def end_once_customer_purchases_anywhere(self):
        """Gets the end_once_customer_purchases_anywhere of this EmailFlow.  # noqa: E501

        True if the customer should end the flow once they purchase from any source  # noqa: E501

        :return: The end_once_customer_purchases_anywhere of this EmailFlow.  # noqa: E501
        :rtype: bool
        """
        return self._end_once_customer_purchases_anywhere

    @end_once_customer_purchases_anywhere.setter
    def end_once_customer_purchases_anywhere(self, end_once_customer_purchases_anywhere):
        """Sets the end_once_customer_purchases_anywhere of this EmailFlow.

        True if the customer should end the flow once they purchase from any source  # noqa: E501

        :param end_once_customer_purchases_anywhere: The end_once_customer_purchases_anywhere of this EmailFlow.  # noqa: E501
        :type: bool
        """

        self._end_once_customer_purchases_anywhere = end_once_customer_purchases_anywhere

    @property
    def enrolled_customers(self):
        """Gets the enrolled_customers of this EmailFlow.  # noqa: E501

        Number of enrolled customers.  # noqa: E501

        :return: The enrolled_customers of this EmailFlow.  # noqa: E501
        :rtype: int
        """
        return self._enrolled_customers

    @enrolled_customers.setter
    def enrolled_customers(self, enrolled_customers):
        """Sets the enrolled_customers of this EmailFlow.

        Number of enrolled customers.  # noqa: E501

        :param enrolled_customers: The enrolled_customers of this EmailFlow.  # noqa: E501
        :type: int
        """

        self._enrolled_customers = enrolled_customers

    @property
    def esp_domain_user(self):
        """Gets the esp_domain_user of this EmailFlow.  # noqa: E501

        Username of sending email  # noqa: E501

        :return: The esp_domain_user of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._esp_domain_user

    @esp_domain_user.setter
    def esp_domain_user(self, esp_domain_user):
        """Sets the esp_domain_user of this EmailFlow.

        Username of sending email  # noqa: E501

        :param esp_domain_user: The esp_domain_user of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._esp_domain_user = esp_domain_user

    @property
    def esp_domain_uuid(self):
        """Gets the esp_domain_uuid of this EmailFlow.  # noqa: E501

        UUID of sending domain  # noqa: E501

        :return: The esp_domain_uuid of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._esp_domain_uuid

    @esp_domain_uuid.setter
    def esp_domain_uuid(self, esp_domain_uuid):
        """Sets the esp_domain_uuid of this EmailFlow.

        UUID of sending domain  # noqa: E501

        :param esp_domain_uuid: The esp_domain_uuid of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._esp_domain_uuid = esp_domain_uuid

    @property
    def esp_flow_folder_uuid(self):
        """Gets the esp_flow_folder_uuid of this EmailFlow.  # noqa: E501

        Flow folder UUID.  Null for uncategorized  # noqa: E501

        :return: The esp_flow_folder_uuid of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._esp_flow_folder_uuid

    @esp_flow_folder_uuid.setter
    def esp_flow_folder_uuid(self, esp_flow_folder_uuid):
        """Sets the esp_flow_folder_uuid of this EmailFlow.

        Flow folder UUID.  Null for uncategorized  # noqa: E501

        :param esp_flow_folder_uuid: The esp_flow_folder_uuid of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._esp_flow_folder_uuid = esp_flow_folder_uuid

    @property
    def esp_friendly_name(self):
        """Gets the esp_friendly_name of this EmailFlow.  # noqa: E501

        Friendly name of the sending email  # noqa: E501

        :return: The esp_friendly_name of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._esp_friendly_name

    @esp_friendly_name.setter
    def esp_friendly_name(self, esp_friendly_name):
        """Sets the esp_friendly_name of this EmailFlow.

        Friendly name of the sending email  # noqa: E501

        :param esp_friendly_name: The esp_friendly_name of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._esp_friendly_name = esp_friendly_name

    @property
    def filter_profile_equation_json(self):
        """Gets the filter_profile_equation_json of this EmailFlow.  # noqa: E501

        File profile equation json  # noqa: E501

        :return: The filter_profile_equation_json of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._filter_profile_equation_json

    @filter_profile_equation_json.setter
    def filter_profile_equation_json(self, filter_profile_equation_json):
        """Sets the filter_profile_equation_json of this EmailFlow.

        File profile equation json  # noqa: E501

        :param filter_profile_equation_json: The filter_profile_equation_json of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._filter_profile_equation_json = filter_profile_equation_json

    @property
    def library_item_oid(self):
        """Gets the library_item_oid of this EmailFlow.  # noqa: E501

        If this item was ever added to the Code Library, this is the oid for that library item, or 0 if never added before.  This value is used to determine if a library item should be inserted or updated.  # noqa: E501

        :return: The library_item_oid of this EmailFlow.  # noqa: E501
        :rtype: int
        """
        return self._library_item_oid

    @library_item_oid.setter
    def library_item_oid(self, library_item_oid):
        """Sets the library_item_oid of this EmailFlow.

        If this item was ever added to the Code Library, this is the oid for that library item, or 0 if never added before.  This value is used to determine if a library item should be inserted or updated.  # noqa: E501

        :param library_item_oid: The library_item_oid of this EmailFlow.  # noqa: E501
        :type: int
        """

        self._library_item_oid = library_item_oid

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EmailFlow.  # noqa: E501

        Merchant ID  # noqa: E501

        :return: The merchant_id of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EmailFlow.

        Merchant ID  # noqa: E501

        :param merchant_id: The merchant_id of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this EmailFlow.  # noqa: E501

        Name of email flow  # noqa: E501

        :return: The name of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailFlow.

        Name of email flow  # noqa: E501

        :param name: The name of this EmailFlow.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501

        self._name = name

    @property
    def open_rate_formatted(self):
        """Gets the open_rate_formatted of this EmailFlow.  # noqa: E501

        Open rate of emails, formatted  # noqa: E501

        :return: The open_rate_formatted of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._open_rate_formatted

    @open_rate_formatted.setter
    def open_rate_formatted(self, open_rate_formatted):
        """Sets the open_rate_formatted of this EmailFlow.

        Open rate of emails, formatted  # noqa: E501

        :param open_rate_formatted: The open_rate_formatted of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._open_rate_formatted = open_rate_formatted

    @property
    def revenue_formatted(self):
        """Gets the revenue_formatted of this EmailFlow.  # noqa: E501

        Revenue, formatted  # noqa: E501

        :return: The revenue_formatted of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._revenue_formatted

    @revenue_formatted.setter
    def revenue_formatted(self, revenue_formatted):
        """Sets the revenue_formatted of this EmailFlow.

        Revenue, formatted  # noqa: E501

        :param revenue_formatted: The revenue_formatted of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._revenue_formatted = revenue_formatted

    @property
    def revenue_per_customer_formatted(self):
        """Gets the revenue_per_customer_formatted of this EmailFlow.  # noqa: E501

        Revenue per customer, formatted  # noqa: E501

        :return: The revenue_per_customer_formatted of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._revenue_per_customer_formatted

    @revenue_per_customer_formatted.setter
    def revenue_per_customer_formatted(self, revenue_per_customer_formatted):
        """Sets the revenue_per_customer_formatted of this EmailFlow.

        Revenue per customer, formatted  # noqa: E501

        :param revenue_per_customer_formatted: The revenue_per_customer_formatted of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._revenue_per_customer_formatted = revenue_per_customer_formatted

    @property
    def screenshot_large_full_url(self):
        """Gets the screenshot_large_full_url of this EmailFlow.  # noqa: E501

        URL to a large full length screenshot  # noqa: E501

        :return: The screenshot_large_full_url of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._screenshot_large_full_url

    @screenshot_large_full_url.setter
    def screenshot_large_full_url(self, screenshot_large_full_url):
        """Sets the screenshot_large_full_url of this EmailFlow.

        URL to a large full length screenshot  # noqa: E501

        :param screenshot_large_full_url: The screenshot_large_full_url of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._screenshot_large_full_url = screenshot_large_full_url

    @property
    def sms_esp_twilio_uuid(self):
        """Gets the sms_esp_twilio_uuid of this EmailFlow.  # noqa: E501

        Twilio Account UUID.  Null for none  # noqa: E501

        :return: The sms_esp_twilio_uuid of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._sms_esp_twilio_uuid

    @sms_esp_twilio_uuid.setter
    def sms_esp_twilio_uuid(self, sms_esp_twilio_uuid):
        """Sets the sms_esp_twilio_uuid of this EmailFlow.

        Twilio Account UUID.  Null for none  # noqa: E501

        :param sms_esp_twilio_uuid: The sms_esp_twilio_uuid of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._sms_esp_twilio_uuid = sms_esp_twilio_uuid

    @property
    def sms_phone_number(self):
        """Gets the sms_phone_number of this EmailFlow.  # noqa: E501

        Twilio SMS Phone Number.  Null for none  # noqa: E501

        :return: The sms_phone_number of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._sms_phone_number

    @sms_phone_number.setter
    def sms_phone_number(self, sms_phone_number):
        """Sets the sms_phone_number of this EmailFlow.

        Twilio SMS Phone Number.  Null for none  # noqa: E501

        :param sms_phone_number: The sms_phone_number of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._sms_phone_number = sms_phone_number

    @property
    def status(self):
        """Gets the status of this EmailFlow.  # noqa: E501

        Status of the campaign of draft, archived, active, and inactive  # noqa: E501

        :return: The status of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmailFlow.

        Status of the campaign of draft, archived, active, and inactive  # noqa: E501

        :param status: The status of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_dts(self):
        """Gets the status_dts of this EmailFlow.  # noqa: E501

        Timestamp when the last status change happened  # noqa: E501

        :return: The status_dts of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._status_dts

    @status_dts.setter
    def status_dts(self, status_dts):
        """Sets the status_dts of this EmailFlow.

        Timestamp when the last status change happened  # noqa: E501

        :param status_dts: The status_dts of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._status_dts = status_dts

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this EmailFlow.  # noqa: E501

        Storefront oid  # noqa: E501

        :return: The storefront_oid of this EmailFlow.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this EmailFlow.

        Storefront oid  # noqa: E501

        :param storefront_oid: The storefront_oid of this EmailFlow.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def trigger_parameter(self):
        """Gets the trigger_parameter of this EmailFlow.  # noqa: E501

        Trigger parameter  # noqa: E501

        :return: The trigger_parameter of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._trigger_parameter

    @trigger_parameter.setter
    def trigger_parameter(self, trigger_parameter):
        """Sets the trigger_parameter of this EmailFlow.

        Trigger parameter  # noqa: E501

        :param trigger_parameter: The trigger_parameter of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._trigger_parameter = trigger_parameter

    @property
    def trigger_parameter_name(self):
        """Gets the trigger_parameter_name of this EmailFlow.  # noqa: E501

        Trigger parameter name  # noqa: E501

        :return: The trigger_parameter_name of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._trigger_parameter_name

    @trigger_parameter_name.setter
    def trigger_parameter_name(self, trigger_parameter_name):
        """Sets the trigger_parameter_name of this EmailFlow.

        Trigger parameter name  # noqa: E501

        :param trigger_parameter_name: The trigger_parameter_name of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._trigger_parameter_name = trigger_parameter_name

    @property
    def trigger_type(self):
        """Gets the trigger_type of this EmailFlow.  # noqa: E501

        Trigger type  # noqa: E501

        :return: The trigger_type of this EmailFlow.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this EmailFlow.

        Trigger type  # noqa: E501

        :param trigger_type: The trigger_type of this EmailFlow.  # noqa: E501
        :type: str
        """

        self._trigger_type = trigger_type

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
        if issubclass(EmailFlow, dict):
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
        if not isinstance(other, EmailFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

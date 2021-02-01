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


class OrderFormat(object):
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
        'context': 'str',
        'dont_link_email_to_search': 'bool',
        'email_as_link': 'bool',
        'filter_distribution_center_oid': 'int',
        'filter_to_items_in_contact_oid': 'int',
        'format': 'str',
        'hide_bill_to_address': 'bool',
        'hide_price_information': 'bool',
        'link_file_attachments': 'bool',
        'show_contact_info': 'bool',
        'show_in_merchant_currency': 'bool',
        'show_internal_information': 'bool',
        'show_merchant_notes': 'bool',
        'show_non_sensitive_payment_info': 'bool',
        'show_payment_info': 'bool',
        'translate': 'bool'
    }

    attribute_map = {
        'context': 'context',
        'dont_link_email_to_search': 'dont_link_email_to_search',
        'email_as_link': 'email_as_link',
        'filter_distribution_center_oid': 'filter_distribution_center_oid',
        'filter_to_items_in_contact_oid': 'filter_to_items_in_contact_oid',
        'format': 'format',
        'hide_bill_to_address': 'hide_bill_to_address',
        'hide_price_information': 'hide_price_information',
        'link_file_attachments': 'link_file_attachments',
        'show_contact_info': 'show_contact_info',
        'show_in_merchant_currency': 'show_in_merchant_currency',
        'show_internal_information': 'show_internal_information',
        'show_merchant_notes': 'show_merchant_notes',
        'show_non_sensitive_payment_info': 'show_non_sensitive_payment_info',
        'show_payment_info': 'show_payment_info',
        'translate': 'translate'
    }

    def __init__(self, context=None, dont_link_email_to_search=None, email_as_link=None, filter_distribution_center_oid=None, filter_to_items_in_contact_oid=None, format=None, hide_bill_to_address=None, hide_price_information=None, link_file_attachments=None, show_contact_info=None, show_in_merchant_currency=None, show_internal_information=None, show_merchant_notes=None, show_non_sensitive_payment_info=None, show_payment_info=None, translate=None):  # noqa: E501
        """OrderFormat - a model defined in Swagger"""  # noqa: E501

        self._context = None
        self._dont_link_email_to_search = None
        self._email_as_link = None
        self._filter_distribution_center_oid = None
        self._filter_to_items_in_contact_oid = None
        self._format = None
        self._hide_bill_to_address = None
        self._hide_price_information = None
        self._link_file_attachments = None
        self._show_contact_info = None
        self._show_in_merchant_currency = None
        self._show_internal_information = None
        self._show_merchant_notes = None
        self._show_non_sensitive_payment_info = None
        self._show_payment_info = None
        self._translate = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if dont_link_email_to_search is not None:
            self.dont_link_email_to_search = dont_link_email_to_search
        if email_as_link is not None:
            self.email_as_link = email_as_link
        if filter_distribution_center_oid is not None:
            self.filter_distribution_center_oid = filter_distribution_center_oid
        if filter_to_items_in_contact_oid is not None:
            self.filter_to_items_in_contact_oid = filter_to_items_in_contact_oid
        if format is not None:
            self.format = format
        if hide_bill_to_address is not None:
            self.hide_bill_to_address = hide_bill_to_address
        if hide_price_information is not None:
            self.hide_price_information = hide_price_information
        if link_file_attachments is not None:
            self.link_file_attachments = link_file_attachments
        if show_contact_info is not None:
            self.show_contact_info = show_contact_info
        if show_in_merchant_currency is not None:
            self.show_in_merchant_currency = show_in_merchant_currency
        if show_internal_information is not None:
            self.show_internal_information = show_internal_information
        if show_merchant_notes is not None:
            self.show_merchant_notes = show_merchant_notes
        if show_non_sensitive_payment_info is not None:
            self.show_non_sensitive_payment_info = show_non_sensitive_payment_info
        if show_payment_info is not None:
            self.show_payment_info = show_payment_info
        if translate is not None:
            self.translate = translate

    @property
    def context(self):
        """Gets the context of this OrderFormat.  # noqa: E501

        The context to generate the order view for.  # noqa: E501

        :return: The context of this OrderFormat.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this OrderFormat.

        The context to generate the order view for.  # noqa: E501

        :param context: The context of this OrderFormat.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def dont_link_email_to_search(self):
        """Gets the dont_link_email_to_search of this OrderFormat.  # noqa: E501

        True to not link the email address to the order search  # noqa: E501

        :return: The dont_link_email_to_search of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._dont_link_email_to_search

    @dont_link_email_to_search.setter
    def dont_link_email_to_search(self, dont_link_email_to_search):
        """Sets the dont_link_email_to_search of this OrderFormat.

        True to not link the email address to the order search  # noqa: E501

        :param dont_link_email_to_search: The dont_link_email_to_search of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._dont_link_email_to_search = dont_link_email_to_search

    @property
    def email_as_link(self):
        """Gets the email_as_link of this OrderFormat.  # noqa: E501

        True to make the email address a clickable mailto link  # noqa: E501

        :return: The email_as_link of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._email_as_link

    @email_as_link.setter
    def email_as_link(self, email_as_link):
        """Sets the email_as_link of this OrderFormat.

        True to make the email address a clickable mailto link  # noqa: E501

        :param email_as_link: The email_as_link of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._email_as_link = email_as_link

    @property
    def filter_distribution_center_oid(self):
        """Gets the filter_distribution_center_oid of this OrderFormat.  # noqa: E501

        Specify a distribution center oid to filter the items displayed to that particular distribution center.  # noqa: E501

        :return: The filter_distribution_center_oid of this OrderFormat.  # noqa: E501
        :rtype: int
        """
        return self._filter_distribution_center_oid

    @filter_distribution_center_oid.setter
    def filter_distribution_center_oid(self, filter_distribution_center_oid):
        """Sets the filter_distribution_center_oid of this OrderFormat.

        Specify a distribution center oid to filter the items displayed to that particular distribution center.  # noqa: E501

        :param filter_distribution_center_oid: The filter_distribution_center_oid of this OrderFormat.  # noqa: E501
        :type: int
        """

        self._filter_distribution_center_oid = filter_distribution_center_oid

    @property
    def filter_to_items_in_contact_oid(self):
        """Gets the filter_to_items_in_contact_oid of this OrderFormat.  # noqa: E501

        The container oid to filter items to.  # noqa: E501

        :return: The filter_to_items_in_contact_oid of this OrderFormat.  # noqa: E501
        :rtype: int
        """
        return self._filter_to_items_in_contact_oid

    @filter_to_items_in_contact_oid.setter
    def filter_to_items_in_contact_oid(self, filter_to_items_in_contact_oid):
        """Sets the filter_to_items_in_contact_oid of this OrderFormat.

        The container oid to filter items to.  # noqa: E501

        :param filter_to_items_in_contact_oid: The filter_to_items_in_contact_oid of this OrderFormat.  # noqa: E501
        :type: int
        """

        self._filter_to_items_in_contact_oid = filter_to_items_in_contact_oid

    @property
    def format(self):
        """Gets the format of this OrderFormat.  # noqa: E501

        The desired format.  # noqa: E501

        :return: The format of this OrderFormat.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this OrderFormat.

        The desired format.  # noqa: E501

        :param format: The format of this OrderFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "div", "table", "email"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def hide_bill_to_address(self):
        """Gets the hide_bill_to_address of this OrderFormat.  # noqa: E501

        True to ide the bill to address  # noqa: E501

        :return: The hide_bill_to_address of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._hide_bill_to_address

    @hide_bill_to_address.setter
    def hide_bill_to_address(self, hide_bill_to_address):
        """Sets the hide_bill_to_address of this OrderFormat.

        True to ide the bill to address  # noqa: E501

        :param hide_bill_to_address: The hide_bill_to_address of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._hide_bill_to_address = hide_bill_to_address

    @property
    def hide_price_information(self):
        """Gets the hide_price_information of this OrderFormat.  # noqa: E501

        True to hide price information  # noqa: E501

        :return: The hide_price_information of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._hide_price_information

    @hide_price_information.setter
    def hide_price_information(self, hide_price_information):
        """Sets the hide_price_information of this OrderFormat.

        True to hide price information  # noqa: E501

        :param hide_price_information: The hide_price_information of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._hide_price_information = hide_price_information

    @property
    def link_file_attachments(self):
        """Gets the link_file_attachments of this OrderFormat.  # noqa: E501

        True to link file attachments for download  # noqa: E501

        :return: The link_file_attachments of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._link_file_attachments

    @link_file_attachments.setter
    def link_file_attachments(self, link_file_attachments):
        """Sets the link_file_attachments of this OrderFormat.

        True to link file attachments for download  # noqa: E501

        :param link_file_attachments: The link_file_attachments of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._link_file_attachments = link_file_attachments

    @property
    def show_contact_info(self):
        """Gets the show_contact_info of this OrderFormat.  # noqa: E501

        True to show contact information  # noqa: E501

        :return: The show_contact_info of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_contact_info

    @show_contact_info.setter
    def show_contact_info(self, show_contact_info):
        """Sets the show_contact_info of this OrderFormat.

        True to show contact information  # noqa: E501

        :param show_contact_info: The show_contact_info of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_contact_info = show_contact_info

    @property
    def show_in_merchant_currency(self):
        """Gets the show_in_merchant_currency of this OrderFormat.  # noqa: E501

        True to show the order in the merchant currency  # noqa: E501

        :return: The show_in_merchant_currency of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_merchant_currency

    @show_in_merchant_currency.setter
    def show_in_merchant_currency(self, show_in_merchant_currency):
        """Sets the show_in_merchant_currency of this OrderFormat.

        True to show the order in the merchant currency  # noqa: E501

        :param show_in_merchant_currency: The show_in_merchant_currency of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_in_merchant_currency = show_in_merchant_currency

    @property
    def show_internal_information(self):
        """Gets the show_internal_information of this OrderFormat.  # noqa: E501

        True to show internal information about the order  # noqa: E501

        :return: The show_internal_information of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_internal_information

    @show_internal_information.setter
    def show_internal_information(self, show_internal_information):
        """Sets the show_internal_information of this OrderFormat.

        True to show internal information about the order  # noqa: E501

        :param show_internal_information: The show_internal_information of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_internal_information = show_internal_information

    @property
    def show_merchant_notes(self):
        """Gets the show_merchant_notes of this OrderFormat.  # noqa: E501

        True to show merchant notes  # noqa: E501

        :return: The show_merchant_notes of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_merchant_notes

    @show_merchant_notes.setter
    def show_merchant_notes(self, show_merchant_notes):
        """Sets the show_merchant_notes of this OrderFormat.

        True to show merchant notes  # noqa: E501

        :param show_merchant_notes: The show_merchant_notes of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_merchant_notes = show_merchant_notes

    @property
    def show_non_sensitive_payment_info(self):
        """Gets the show_non_sensitive_payment_info of this OrderFormat.  # noqa: E501

        True to show non-sensitive payment information  # noqa: E501

        :return: The show_non_sensitive_payment_info of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_non_sensitive_payment_info

    @show_non_sensitive_payment_info.setter
    def show_non_sensitive_payment_info(self, show_non_sensitive_payment_info):
        """Sets the show_non_sensitive_payment_info of this OrderFormat.

        True to show non-sensitive payment information  # noqa: E501

        :param show_non_sensitive_payment_info: The show_non_sensitive_payment_info of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_non_sensitive_payment_info = show_non_sensitive_payment_info

    @property
    def show_payment_info(self):
        """Gets the show_payment_info of this OrderFormat.  # noqa: E501

        True to show payment information  # noqa: E501

        :return: The show_payment_info of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._show_payment_info

    @show_payment_info.setter
    def show_payment_info(self, show_payment_info):
        """Sets the show_payment_info of this OrderFormat.

        True to show payment information  # noqa: E501

        :param show_payment_info: The show_payment_info of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._show_payment_info = show_payment_info

    @property
    def translate(self):
        """Gets the translate of this OrderFormat.  # noqa: E501

        True to translate the order into the native language of the customer  # noqa: E501

        :return: The translate of this OrderFormat.  # noqa: E501
        :rtype: bool
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        """Sets the translate of this OrderFormat.

        True to translate the order into the native language of the customer  # noqa: E501

        :param translate: The translate of this OrderFormat.  # noqa: E501
        :type: bool
        """

        self._translate = translate

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
        if issubclass(OrderFormat, dict):
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
        if not isinstance(other, OrderFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

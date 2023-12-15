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


class CustomerQuery(object):
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
        'all_tags': 'list[str]',
        'any_tags': 'list[str]',
        'billing_city': 'str',
        'billing_company': 'str',
        'billing_country_code': 'str',
        'billing_day_phone': 'str',
        'billing_evening_phone': 'str',
        'billing_first_name': 'str',
        'billing_last_name': 'str',
        'billing_postal_code': 'str',
        'billing_state': 'str',
        'email': 'str',
        'last_modified_dts_end': 'str',
        'last_modified_dts_start': 'str',
        'pricing_tier_name': 'str',
        'pricing_tier_oid': 'int',
        'qb_class': 'str',
        'quickbooks_code': 'str',
        'shipping_city': 'str',
        'shipping_company': 'str',
        'shipping_country_code': 'str',
        'shipping_day_phone': 'str',
        'shipping_evening_phone': 'str',
        'shipping_first_name': 'str',
        'shipping_last_name': 'str',
        'shipping_postal_code': 'str',
        'shipping_state': 'str',
        'signup_dts_end': 'str',
        'signup_dts_start': 'str'
    }

    attribute_map = {
        'all_tags': 'all_tags',
        'any_tags': 'any_tags',
        'billing_city': 'billing_city',
        'billing_company': 'billing_company',
        'billing_country_code': 'billing_country_code',
        'billing_day_phone': 'billing_day_phone',
        'billing_evening_phone': 'billing_evening_phone',
        'billing_first_name': 'billing_first_name',
        'billing_last_name': 'billing_last_name',
        'billing_postal_code': 'billing_postal_code',
        'billing_state': 'billing_state',
        'email': 'email',
        'last_modified_dts_end': 'last_modified_dts_end',
        'last_modified_dts_start': 'last_modified_dts_start',
        'pricing_tier_name': 'pricing_tier_name',
        'pricing_tier_oid': 'pricing_tier_oid',
        'qb_class': 'qb_class',
        'quickbooks_code': 'quickbooks_code',
        'shipping_city': 'shipping_city',
        'shipping_company': 'shipping_company',
        'shipping_country_code': 'shipping_country_code',
        'shipping_day_phone': 'shipping_day_phone',
        'shipping_evening_phone': 'shipping_evening_phone',
        'shipping_first_name': 'shipping_first_name',
        'shipping_last_name': 'shipping_last_name',
        'shipping_postal_code': 'shipping_postal_code',
        'shipping_state': 'shipping_state',
        'signup_dts_end': 'signup_dts_end',
        'signup_dts_start': 'signup_dts_start'
    }

    def __init__(self, all_tags=None, any_tags=None, billing_city=None, billing_company=None, billing_country_code=None, billing_day_phone=None, billing_evening_phone=None, billing_first_name=None, billing_last_name=None, billing_postal_code=None, billing_state=None, email=None, last_modified_dts_end=None, last_modified_dts_start=None, pricing_tier_name=None, pricing_tier_oid=None, qb_class=None, quickbooks_code=None, shipping_city=None, shipping_company=None, shipping_country_code=None, shipping_day_phone=None, shipping_evening_phone=None, shipping_first_name=None, shipping_last_name=None, shipping_postal_code=None, shipping_state=None, signup_dts_end=None, signup_dts_start=None):  # noqa: E501
        """CustomerQuery - a model defined in Swagger"""  # noqa: E501

        self._all_tags = None
        self._any_tags = None
        self._billing_city = None
        self._billing_company = None
        self._billing_country_code = None
        self._billing_day_phone = None
        self._billing_evening_phone = None
        self._billing_first_name = None
        self._billing_last_name = None
        self._billing_postal_code = None
        self._billing_state = None
        self._email = None
        self._last_modified_dts_end = None
        self._last_modified_dts_start = None
        self._pricing_tier_name = None
        self._pricing_tier_oid = None
        self._qb_class = None
        self._quickbooks_code = None
        self._shipping_city = None
        self._shipping_company = None
        self._shipping_country_code = None
        self._shipping_day_phone = None
        self._shipping_evening_phone = None
        self._shipping_first_name = None
        self._shipping_last_name = None
        self._shipping_postal_code = None
        self._shipping_state = None
        self._signup_dts_end = None
        self._signup_dts_start = None
        self.discriminator = None

        if all_tags is not None:
            self.all_tags = all_tags
        if any_tags is not None:
            self.any_tags = any_tags
        if billing_city is not None:
            self.billing_city = billing_city
        if billing_company is not None:
            self.billing_company = billing_company
        if billing_country_code is not None:
            self.billing_country_code = billing_country_code
        if billing_day_phone is not None:
            self.billing_day_phone = billing_day_phone
        if billing_evening_phone is not None:
            self.billing_evening_phone = billing_evening_phone
        if billing_first_name is not None:
            self.billing_first_name = billing_first_name
        if billing_last_name is not None:
            self.billing_last_name = billing_last_name
        if billing_postal_code is not None:
            self.billing_postal_code = billing_postal_code
        if billing_state is not None:
            self.billing_state = billing_state
        if email is not None:
            self.email = email
        if last_modified_dts_end is not None:
            self.last_modified_dts_end = last_modified_dts_end
        if last_modified_dts_start is not None:
            self.last_modified_dts_start = last_modified_dts_start
        if pricing_tier_name is not None:
            self.pricing_tier_name = pricing_tier_name
        if pricing_tier_oid is not None:
            self.pricing_tier_oid = pricing_tier_oid
        if qb_class is not None:
            self.qb_class = qb_class
        if quickbooks_code is not None:
            self.quickbooks_code = quickbooks_code
        if shipping_city is not None:
            self.shipping_city = shipping_city
        if shipping_company is not None:
            self.shipping_company = shipping_company
        if shipping_country_code is not None:
            self.shipping_country_code = shipping_country_code
        if shipping_day_phone is not None:
            self.shipping_day_phone = shipping_day_phone
        if shipping_evening_phone is not None:
            self.shipping_evening_phone = shipping_evening_phone
        if shipping_first_name is not None:
            self.shipping_first_name = shipping_first_name
        if shipping_last_name is not None:
            self.shipping_last_name = shipping_last_name
        if shipping_postal_code is not None:
            self.shipping_postal_code = shipping_postal_code
        if shipping_state is not None:
            self.shipping_state = shipping_state
        if signup_dts_end is not None:
            self.signup_dts_end = signup_dts_end
        if signup_dts_start is not None:
            self.signup_dts_start = signup_dts_start

    @property
    def all_tags(self):
        """Gets the all_tags of this CustomerQuery.  # noqa: E501

        All tags the customer must have  # noqa: E501

        :return: The all_tags of this CustomerQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._all_tags

    @all_tags.setter
    def all_tags(self, all_tags):
        """Sets the all_tags of this CustomerQuery.

        All tags the customer must have  # noqa: E501

        :param all_tags: The all_tags of this CustomerQuery.  # noqa: E501
        :type: list[str]
        """

        self._all_tags = all_tags

    @property
    def any_tags(self):
        """Gets the any_tags of this CustomerQuery.  # noqa: E501

        Any of these tags the customer must have  # noqa: E501

        :return: The any_tags of this CustomerQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._any_tags

    @any_tags.setter
    def any_tags(self, any_tags):
        """Sets the any_tags of this CustomerQuery.

        Any of these tags the customer must have  # noqa: E501

        :param any_tags: The any_tags of this CustomerQuery.  # noqa: E501
        :type: list[str]
        """

        self._any_tags = any_tags

    @property
    def billing_city(self):
        """Gets the billing_city of this CustomerQuery.  # noqa: E501

        Billing city  # noqa: E501

        :return: The billing_city of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_city

    @billing_city.setter
    def billing_city(self, billing_city):
        """Sets the billing_city of this CustomerQuery.

        Billing city  # noqa: E501

        :param billing_city: The billing_city of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_city is not None and len(billing_city) > 32:
            raise ValueError("Invalid value for `billing_city`, length must be less than or equal to `32`")  # noqa: E501

        self._billing_city = billing_city

    @property
    def billing_company(self):
        """Gets the billing_company of this CustomerQuery.  # noqa: E501

        Billing company  # noqa: E501

        :return: The billing_company of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_company

    @billing_company.setter
    def billing_company(self, billing_company):
        """Sets the billing_company of this CustomerQuery.

        Billing company  # noqa: E501

        :param billing_company: The billing_company of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_company is not None and len(billing_company) > 50:
            raise ValueError("Invalid value for `billing_company`, length must be less than or equal to `50`")  # noqa: E501

        self._billing_company = billing_company

    @property
    def billing_country_code(self):
        """Gets the billing_country_code of this CustomerQuery.  # noqa: E501

        Billing country code  # noqa: E501

        :return: The billing_country_code of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_country_code

    @billing_country_code.setter
    def billing_country_code(self, billing_country_code):
        """Sets the billing_country_code of this CustomerQuery.

        Billing country code  # noqa: E501

        :param billing_country_code: The billing_country_code of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_country_code is not None and len(billing_country_code) > 2:
            raise ValueError("Invalid value for `billing_country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._billing_country_code = billing_country_code

    @property
    def billing_day_phone(self):
        """Gets the billing_day_phone of this CustomerQuery.  # noqa: E501

        Billing day phone  # noqa: E501

        :return: The billing_day_phone of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_day_phone

    @billing_day_phone.setter
    def billing_day_phone(self, billing_day_phone):
        """Sets the billing_day_phone of this CustomerQuery.

        Billing day phone  # noqa: E501

        :param billing_day_phone: The billing_day_phone of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_day_phone is not None and len(billing_day_phone) > 25:
            raise ValueError("Invalid value for `billing_day_phone`, length must be less than or equal to `25`")  # noqa: E501

        self._billing_day_phone = billing_day_phone

    @property
    def billing_evening_phone(self):
        """Gets the billing_evening_phone of this CustomerQuery.  # noqa: E501

        Billing evening phone  # noqa: E501

        :return: The billing_evening_phone of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_evening_phone

    @billing_evening_phone.setter
    def billing_evening_phone(self, billing_evening_phone):
        """Sets the billing_evening_phone of this CustomerQuery.

        Billing evening phone  # noqa: E501

        :param billing_evening_phone: The billing_evening_phone of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_evening_phone is not None and len(billing_evening_phone) > 25:
            raise ValueError("Invalid value for `billing_evening_phone`, length must be less than or equal to `25`")  # noqa: E501

        self._billing_evening_phone = billing_evening_phone

    @property
    def billing_first_name(self):
        """Gets the billing_first_name of this CustomerQuery.  # noqa: E501

        Billing first name  # noqa: E501

        :return: The billing_first_name of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_first_name

    @billing_first_name.setter
    def billing_first_name(self, billing_first_name):
        """Sets the billing_first_name of this CustomerQuery.

        Billing first name  # noqa: E501

        :param billing_first_name: The billing_first_name of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_first_name is not None and len(billing_first_name) > 30:
            raise ValueError("Invalid value for `billing_first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._billing_first_name = billing_first_name

    @property
    def billing_last_name(self):
        """Gets the billing_last_name of this CustomerQuery.  # noqa: E501

        Billing last name  # noqa: E501

        :return: The billing_last_name of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_last_name

    @billing_last_name.setter
    def billing_last_name(self, billing_last_name):
        """Sets the billing_last_name of this CustomerQuery.

        Billing last name  # noqa: E501

        :param billing_last_name: The billing_last_name of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_last_name is not None and len(billing_last_name) > 30:
            raise ValueError("Invalid value for `billing_last_name`, length must be less than or equal to `30`")  # noqa: E501

        self._billing_last_name = billing_last_name

    @property
    def billing_postal_code(self):
        """Gets the billing_postal_code of this CustomerQuery.  # noqa: E501

        Billing postal code  # noqa: E501

        :return: The billing_postal_code of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_postal_code

    @billing_postal_code.setter
    def billing_postal_code(self, billing_postal_code):
        """Sets the billing_postal_code of this CustomerQuery.

        Billing postal code  # noqa: E501

        :param billing_postal_code: The billing_postal_code of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_postal_code is not None and len(billing_postal_code) > 20:
            raise ValueError("Invalid value for `billing_postal_code`, length must be less than or equal to `20`")  # noqa: E501

        self._billing_postal_code = billing_postal_code

    @property
    def billing_state(self):
        """Gets the billing_state of this CustomerQuery.  # noqa: E501

        Billing state  # noqa: E501

        :return: The billing_state of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._billing_state

    @billing_state.setter
    def billing_state(self, billing_state):
        """Sets the billing_state of this CustomerQuery.

        Billing state  # noqa: E501

        :param billing_state: The billing_state of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if billing_state is not None and len(billing_state) > 32:
            raise ValueError("Invalid value for `billing_state`, length must be less than or equal to `32`")  # noqa: E501

        self._billing_state = billing_state

    @property
    def email(self):
        """Gets the email of this CustomerQuery.  # noqa: E501

        Email address of this customer profile  # noqa: E501

        :return: The email of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerQuery.

        Email address of this customer profile  # noqa: E501

        :param email: The email of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def last_modified_dts_end(self):
        """Gets the last_modified_dts_end of this CustomerQuery.  # noqa: E501

        Last modified date end  # noqa: E501

        :return: The last_modified_dts_end of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_dts_end

    @last_modified_dts_end.setter
    def last_modified_dts_end(self, last_modified_dts_end):
        """Sets the last_modified_dts_end of this CustomerQuery.

        Last modified date end  # noqa: E501

        :param last_modified_dts_end: The last_modified_dts_end of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._last_modified_dts_end = last_modified_dts_end

    @property
    def last_modified_dts_start(self):
        """Gets the last_modified_dts_start of this CustomerQuery.  # noqa: E501

        Last modified date start  # noqa: E501

        :return: The last_modified_dts_start of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_dts_start

    @last_modified_dts_start.setter
    def last_modified_dts_start(self, last_modified_dts_start):
        """Sets the last_modified_dts_start of this CustomerQuery.

        Last modified date start  # noqa: E501

        :param last_modified_dts_start: The last_modified_dts_start of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._last_modified_dts_start = last_modified_dts_start

    @property
    def pricing_tier_name(self):
        """Gets the pricing_tier_name of this CustomerQuery.  # noqa: E501

        Pricing tier name  # noqa: E501

        :return: The pricing_tier_name of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._pricing_tier_name

    @pricing_tier_name.setter
    def pricing_tier_name(self, pricing_tier_name):
        """Sets the pricing_tier_name of this CustomerQuery.

        Pricing tier name  # noqa: E501

        :param pricing_tier_name: The pricing_tier_name of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if pricing_tier_name is not None and len(pricing_tier_name) > 50:
            raise ValueError("Invalid value for `pricing_tier_name`, length must be less than or equal to `50`")  # noqa: E501

        self._pricing_tier_name = pricing_tier_name

    @property
    def pricing_tier_oid(self):
        """Gets the pricing_tier_oid of this CustomerQuery.  # noqa: E501

        Pricing tier oid  # noqa: E501

        :return: The pricing_tier_oid of this CustomerQuery.  # noqa: E501
        :rtype: int
        """
        return self._pricing_tier_oid

    @pricing_tier_oid.setter
    def pricing_tier_oid(self, pricing_tier_oid):
        """Sets the pricing_tier_oid of this CustomerQuery.

        Pricing tier oid  # noqa: E501

        :param pricing_tier_oid: The pricing_tier_oid of this CustomerQuery.  # noqa: E501
        :type: int
        """

        self._pricing_tier_oid = pricing_tier_oid

    @property
    def qb_class(self):
        """Gets the qb_class of this CustomerQuery.  # noqa: E501

        QuickBooks class to import this customer as  # noqa: E501

        :return: The qb_class of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._qb_class

    @qb_class.setter
    def qb_class(self, qb_class):
        """Sets the qb_class of this CustomerQuery.

        QuickBooks class to import this customer as  # noqa: E501

        :param qb_class: The qb_class of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._qb_class = qb_class

    @property
    def quickbooks_code(self):
        """Gets the quickbooks_code of this CustomerQuery.  # noqa: E501

        QuickBooks name to import this customer as  # noqa: E501

        :return: The quickbooks_code of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._quickbooks_code

    @quickbooks_code.setter
    def quickbooks_code(self, quickbooks_code):
        """Sets the quickbooks_code of this CustomerQuery.

        QuickBooks name to import this customer as  # noqa: E501

        :param quickbooks_code: The quickbooks_code of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._quickbooks_code = quickbooks_code

    @property
    def shipping_city(self):
        """Gets the shipping_city of this CustomerQuery.  # noqa: E501

        Billing city  # noqa: E501

        :return: The shipping_city of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_city

    @shipping_city.setter
    def shipping_city(self, shipping_city):
        """Sets the shipping_city of this CustomerQuery.

        Billing city  # noqa: E501

        :param shipping_city: The shipping_city of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_city is not None and len(shipping_city) > 32:
            raise ValueError("Invalid value for `shipping_city`, length must be less than or equal to `32`")  # noqa: E501

        self._shipping_city = shipping_city

    @property
    def shipping_company(self):
        """Gets the shipping_company of this CustomerQuery.  # noqa: E501

        Billing company  # noqa: E501

        :return: The shipping_company of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, shipping_company):
        """Sets the shipping_company of this CustomerQuery.

        Billing company  # noqa: E501

        :param shipping_company: The shipping_company of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_company is not None and len(shipping_company) > 50:
            raise ValueError("Invalid value for `shipping_company`, length must be less than or equal to `50`")  # noqa: E501

        self._shipping_company = shipping_company

    @property
    def shipping_country_code(self):
        """Gets the shipping_country_code of this CustomerQuery.  # noqa: E501

        Billing country code  # noqa: E501

        :return: The shipping_country_code of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_country_code

    @shipping_country_code.setter
    def shipping_country_code(self, shipping_country_code):
        """Sets the shipping_country_code of this CustomerQuery.

        Billing country code  # noqa: E501

        :param shipping_country_code: The shipping_country_code of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_country_code is not None and len(shipping_country_code) > 2:
            raise ValueError("Invalid value for `shipping_country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._shipping_country_code = shipping_country_code

    @property
    def shipping_day_phone(self):
        """Gets the shipping_day_phone of this CustomerQuery.  # noqa: E501

        Billing day phone  # noqa: E501

        :return: The shipping_day_phone of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_day_phone

    @shipping_day_phone.setter
    def shipping_day_phone(self, shipping_day_phone):
        """Sets the shipping_day_phone of this CustomerQuery.

        Billing day phone  # noqa: E501

        :param shipping_day_phone: The shipping_day_phone of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_day_phone is not None and len(shipping_day_phone) > 25:
            raise ValueError("Invalid value for `shipping_day_phone`, length must be less than or equal to `25`")  # noqa: E501

        self._shipping_day_phone = shipping_day_phone

    @property
    def shipping_evening_phone(self):
        """Gets the shipping_evening_phone of this CustomerQuery.  # noqa: E501

        Billing evening phone  # noqa: E501

        :return: The shipping_evening_phone of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_evening_phone

    @shipping_evening_phone.setter
    def shipping_evening_phone(self, shipping_evening_phone):
        """Sets the shipping_evening_phone of this CustomerQuery.

        Billing evening phone  # noqa: E501

        :param shipping_evening_phone: The shipping_evening_phone of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_evening_phone is not None and len(shipping_evening_phone) > 25:
            raise ValueError("Invalid value for `shipping_evening_phone`, length must be less than or equal to `25`")  # noqa: E501

        self._shipping_evening_phone = shipping_evening_phone

    @property
    def shipping_first_name(self):
        """Gets the shipping_first_name of this CustomerQuery.  # noqa: E501

        Billing first name  # noqa: E501

        :return: The shipping_first_name of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_first_name

    @shipping_first_name.setter
    def shipping_first_name(self, shipping_first_name):
        """Sets the shipping_first_name of this CustomerQuery.

        Billing first name  # noqa: E501

        :param shipping_first_name: The shipping_first_name of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_first_name is not None and len(shipping_first_name) > 30:
            raise ValueError("Invalid value for `shipping_first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._shipping_first_name = shipping_first_name

    @property
    def shipping_last_name(self):
        """Gets the shipping_last_name of this CustomerQuery.  # noqa: E501

        Billing last name  # noqa: E501

        :return: The shipping_last_name of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_last_name

    @shipping_last_name.setter
    def shipping_last_name(self, shipping_last_name):
        """Sets the shipping_last_name of this CustomerQuery.

        Billing last name  # noqa: E501

        :param shipping_last_name: The shipping_last_name of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_last_name is not None and len(shipping_last_name) > 30:
            raise ValueError("Invalid value for `shipping_last_name`, length must be less than or equal to `30`")  # noqa: E501

        self._shipping_last_name = shipping_last_name

    @property
    def shipping_postal_code(self):
        """Gets the shipping_postal_code of this CustomerQuery.  # noqa: E501

        Billing postal code  # noqa: E501

        :return: The shipping_postal_code of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_postal_code

    @shipping_postal_code.setter
    def shipping_postal_code(self, shipping_postal_code):
        """Sets the shipping_postal_code of this CustomerQuery.

        Billing postal code  # noqa: E501

        :param shipping_postal_code: The shipping_postal_code of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_postal_code is not None and len(shipping_postal_code) > 20:
            raise ValueError("Invalid value for `shipping_postal_code`, length must be less than or equal to `20`")  # noqa: E501

        self._shipping_postal_code = shipping_postal_code

    @property
    def shipping_state(self):
        """Gets the shipping_state of this CustomerQuery.  # noqa: E501

        Billing state  # noqa: E501

        :return: The shipping_state of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipping_state

    @shipping_state.setter
    def shipping_state(self, shipping_state):
        """Sets the shipping_state of this CustomerQuery.

        Billing state  # noqa: E501

        :param shipping_state: The shipping_state of this CustomerQuery.  # noqa: E501
        :type: str
        """
        if shipping_state is not None and len(shipping_state) > 32:
            raise ValueError("Invalid value for `shipping_state`, length must be less than or equal to `32`")  # noqa: E501

        self._shipping_state = shipping_state

    @property
    def signup_dts_end(self):
        """Gets the signup_dts_end of this CustomerQuery.  # noqa: E501

        Signup date end  # noqa: E501

        :return: The signup_dts_end of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._signup_dts_end

    @signup_dts_end.setter
    def signup_dts_end(self, signup_dts_end):
        """Sets the signup_dts_end of this CustomerQuery.

        Signup date end  # noqa: E501

        :param signup_dts_end: The signup_dts_end of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._signup_dts_end = signup_dts_end

    @property
    def signup_dts_start(self):
        """Gets the signup_dts_start of this CustomerQuery.  # noqa: E501

        Signup date start  # noqa: E501

        :return: The signup_dts_start of this CustomerQuery.  # noqa: E501
        :rtype: str
        """
        return self._signup_dts_start

    @signup_dts_start.setter
    def signup_dts_start(self, signup_dts_start):
        """Sets the signup_dts_start of this CustomerQuery.

        Signup date start  # noqa: E501

        :param signup_dts_start: The signup_dts_start of this CustomerQuery.  # noqa: E501
        :type: str
        """

        self._signup_dts_start = signup_dts_start

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
        if issubclass(CustomerQuery, dict):
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
        if not isinstance(other, CustomerQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

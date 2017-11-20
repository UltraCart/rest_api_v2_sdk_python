# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CustomerQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billing_city=None, billing_company=None, billing_country_code=None, billing_day_phone=None, billing_evening_phone=None, billing_first_name=None, billing_last_name=None, billing_postal_code=None, billing_state=None, email=None, last_modified_dts_end=None, last_modified_dts_start=None, pricing_tier_name=None, pricing_tier_oid=None, qb_class=None, quickbooks_code=None, shipping_city=None, shipping_company=None, shipping_country_code=None, shipping_day_phone=None, shipping_evening_phone=None, shipping_first_name=None, shipping_last_name=None, shipping_postal_code=None, shipping_state=None, signup_dts_end=None, signup_dts_start=None):
        """
        CustomerQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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

        self.attribute_map = {
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

        self._billing_city = billing_city
        self._billing_company = billing_company
        self._billing_country_code = billing_country_code
        self._billing_day_phone = billing_day_phone
        self._billing_evening_phone = billing_evening_phone
        self._billing_first_name = billing_first_name
        self._billing_last_name = billing_last_name
        self._billing_postal_code = billing_postal_code
        self._billing_state = billing_state
        self._email = email
        self._last_modified_dts_end = last_modified_dts_end
        self._last_modified_dts_start = last_modified_dts_start
        self._pricing_tier_name = pricing_tier_name
        self._pricing_tier_oid = pricing_tier_oid
        self._qb_class = qb_class
        self._quickbooks_code = quickbooks_code
        self._shipping_city = shipping_city
        self._shipping_company = shipping_company
        self._shipping_country_code = shipping_country_code
        self._shipping_day_phone = shipping_day_phone
        self._shipping_evening_phone = shipping_evening_phone
        self._shipping_first_name = shipping_first_name
        self._shipping_last_name = shipping_last_name
        self._shipping_postal_code = shipping_postal_code
        self._shipping_state = shipping_state
        self._signup_dts_end = signup_dts_end
        self._signup_dts_start = signup_dts_start

    @property
    def billing_city(self):
        """
        Gets the billing_city of this CustomerQuery.
        Billing city

        :return: The billing_city of this CustomerQuery.
        :rtype: str
        """
        return self._billing_city

    @billing_city.setter
    def billing_city(self, billing_city):
        """
        Sets the billing_city of this CustomerQuery.
        Billing city

        :param billing_city: The billing_city of this CustomerQuery.
        :type: str
        """

        if not billing_city:
            raise ValueError("Invalid value for `billing_city`, must not be `None`")
        if len(billing_city) > 32:
            raise ValueError("Invalid value for `billing_city`, length must be less than `32`")

        self._billing_city = billing_city

    @property
    def billing_company(self):
        """
        Gets the billing_company of this CustomerQuery.
        Billing company

        :return: The billing_company of this CustomerQuery.
        :rtype: str
        """
        return self._billing_company

    @billing_company.setter
    def billing_company(self, billing_company):
        """
        Sets the billing_company of this CustomerQuery.
        Billing company

        :param billing_company: The billing_company of this CustomerQuery.
        :type: str
        """

        if not billing_company:
            raise ValueError("Invalid value for `billing_company`, must not be `None`")
        if len(billing_company) > 50:
            raise ValueError("Invalid value for `billing_company`, length must be less than `50`")

        self._billing_company = billing_company

    @property
    def billing_country_code(self):
        """
        Gets the billing_country_code of this CustomerQuery.
        Billing country code

        :return: The billing_country_code of this CustomerQuery.
        :rtype: str
        """
        return self._billing_country_code

    @billing_country_code.setter
    def billing_country_code(self, billing_country_code):
        """
        Sets the billing_country_code of this CustomerQuery.
        Billing country code

        :param billing_country_code: The billing_country_code of this CustomerQuery.
        :type: str
        """

        if not billing_country_code:
            raise ValueError("Invalid value for `billing_country_code`, must not be `None`")
        if len(billing_country_code) > 2:
            raise ValueError("Invalid value for `billing_country_code`, length must be less than `2`")

        self._billing_country_code = billing_country_code

    @property
    def billing_day_phone(self):
        """
        Gets the billing_day_phone of this CustomerQuery.
        Billing day phone

        :return: The billing_day_phone of this CustomerQuery.
        :rtype: str
        """
        return self._billing_day_phone

    @billing_day_phone.setter
    def billing_day_phone(self, billing_day_phone):
        """
        Sets the billing_day_phone of this CustomerQuery.
        Billing day phone

        :param billing_day_phone: The billing_day_phone of this CustomerQuery.
        :type: str
        """

        if not billing_day_phone:
            raise ValueError("Invalid value for `billing_day_phone`, must not be `None`")
        if len(billing_day_phone) > 25:
            raise ValueError("Invalid value for `billing_day_phone`, length must be less than `25`")

        self._billing_day_phone = billing_day_phone

    @property
    def billing_evening_phone(self):
        """
        Gets the billing_evening_phone of this CustomerQuery.
        Billing evening phone

        :return: The billing_evening_phone of this CustomerQuery.
        :rtype: str
        """
        return self._billing_evening_phone

    @billing_evening_phone.setter
    def billing_evening_phone(self, billing_evening_phone):
        """
        Sets the billing_evening_phone of this CustomerQuery.
        Billing evening phone

        :param billing_evening_phone: The billing_evening_phone of this CustomerQuery.
        :type: str
        """

        if not billing_evening_phone:
            raise ValueError("Invalid value for `billing_evening_phone`, must not be `None`")
        if len(billing_evening_phone) > 25:
            raise ValueError("Invalid value for `billing_evening_phone`, length must be less than `25`")

        self._billing_evening_phone = billing_evening_phone

    @property
    def billing_first_name(self):
        """
        Gets the billing_first_name of this CustomerQuery.
        Billing first name

        :return: The billing_first_name of this CustomerQuery.
        :rtype: str
        """
        return self._billing_first_name

    @billing_first_name.setter
    def billing_first_name(self, billing_first_name):
        """
        Sets the billing_first_name of this CustomerQuery.
        Billing first name

        :param billing_first_name: The billing_first_name of this CustomerQuery.
        :type: str
        """

        if not billing_first_name:
            raise ValueError("Invalid value for `billing_first_name`, must not be `None`")
        if len(billing_first_name) > 30:
            raise ValueError("Invalid value for `billing_first_name`, length must be less than `30`")

        self._billing_first_name = billing_first_name

    @property
    def billing_last_name(self):
        """
        Gets the billing_last_name of this CustomerQuery.
        Billing last name

        :return: The billing_last_name of this CustomerQuery.
        :rtype: str
        """
        return self._billing_last_name

    @billing_last_name.setter
    def billing_last_name(self, billing_last_name):
        """
        Sets the billing_last_name of this CustomerQuery.
        Billing last name

        :param billing_last_name: The billing_last_name of this CustomerQuery.
        :type: str
        """

        if not billing_last_name:
            raise ValueError("Invalid value for `billing_last_name`, must not be `None`")
        if len(billing_last_name) > 30:
            raise ValueError("Invalid value for `billing_last_name`, length must be less than `30`")

        self._billing_last_name = billing_last_name

    @property
    def billing_postal_code(self):
        """
        Gets the billing_postal_code of this CustomerQuery.
        Billing postal code

        :return: The billing_postal_code of this CustomerQuery.
        :rtype: str
        """
        return self._billing_postal_code

    @billing_postal_code.setter
    def billing_postal_code(self, billing_postal_code):
        """
        Sets the billing_postal_code of this CustomerQuery.
        Billing postal code

        :param billing_postal_code: The billing_postal_code of this CustomerQuery.
        :type: str
        """

        if not billing_postal_code:
            raise ValueError("Invalid value for `billing_postal_code`, must not be `None`")
        if len(billing_postal_code) > 20:
            raise ValueError("Invalid value for `billing_postal_code`, length must be less than `20`")

        self._billing_postal_code = billing_postal_code

    @property
    def billing_state(self):
        """
        Gets the billing_state of this CustomerQuery.
        Billing state

        :return: The billing_state of this CustomerQuery.
        :rtype: str
        """
        return self._billing_state

    @billing_state.setter
    def billing_state(self, billing_state):
        """
        Sets the billing_state of this CustomerQuery.
        Billing state

        :param billing_state: The billing_state of this CustomerQuery.
        :type: str
        """

        if not billing_state:
            raise ValueError("Invalid value for `billing_state`, must not be `None`")
        if len(billing_state) > 32:
            raise ValueError("Invalid value for `billing_state`, length must be less than `32`")

        self._billing_state = billing_state

    @property
    def email(self):
        """
        Gets the email of this CustomerQuery.
        Email address of this customer profile

        :return: The email of this CustomerQuery.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerQuery.
        Email address of this customer profile

        :param email: The email of this CustomerQuery.
        :type: str
        """

        self._email = email

    @property
    def last_modified_dts_end(self):
        """
        Gets the last_modified_dts_end of this CustomerQuery.
        Last modified date end

        :return: The last_modified_dts_end of this CustomerQuery.
        :rtype: str
        """
        return self._last_modified_dts_end

    @last_modified_dts_end.setter
    def last_modified_dts_end(self, last_modified_dts_end):
        """
        Sets the last_modified_dts_end of this CustomerQuery.
        Last modified date end

        :param last_modified_dts_end: The last_modified_dts_end of this CustomerQuery.
        :type: str
        """

        self._last_modified_dts_end = last_modified_dts_end

    @property
    def last_modified_dts_start(self):
        """
        Gets the last_modified_dts_start of this CustomerQuery.
        Last modified date start

        :return: The last_modified_dts_start of this CustomerQuery.
        :rtype: str
        """
        return self._last_modified_dts_start

    @last_modified_dts_start.setter
    def last_modified_dts_start(self, last_modified_dts_start):
        """
        Sets the last_modified_dts_start of this CustomerQuery.
        Last modified date start

        :param last_modified_dts_start: The last_modified_dts_start of this CustomerQuery.
        :type: str
        """

        self._last_modified_dts_start = last_modified_dts_start

    @property
    def pricing_tier_name(self):
        """
        Gets the pricing_tier_name of this CustomerQuery.
        Pricing tier name

        :return: The pricing_tier_name of this CustomerQuery.
        :rtype: str
        """
        return self._pricing_tier_name

    @pricing_tier_name.setter
    def pricing_tier_name(self, pricing_tier_name):
        """
        Sets the pricing_tier_name of this CustomerQuery.
        Pricing tier name

        :param pricing_tier_name: The pricing_tier_name of this CustomerQuery.
        :type: str
        """

        if not pricing_tier_name:
            raise ValueError("Invalid value for `pricing_tier_name`, must not be `None`")
        if len(pricing_tier_name) > 50:
            raise ValueError("Invalid value for `pricing_tier_name`, length must be less than `50`")

        self._pricing_tier_name = pricing_tier_name

    @property
    def pricing_tier_oid(self):
        """
        Gets the pricing_tier_oid of this CustomerQuery.
        Pricing tier oid

        :return: The pricing_tier_oid of this CustomerQuery.
        :rtype: int
        """
        return self._pricing_tier_oid

    @pricing_tier_oid.setter
    def pricing_tier_oid(self, pricing_tier_oid):
        """
        Sets the pricing_tier_oid of this CustomerQuery.
        Pricing tier oid

        :param pricing_tier_oid: The pricing_tier_oid of this CustomerQuery.
        :type: int
        """

        self._pricing_tier_oid = pricing_tier_oid

    @property
    def qb_class(self):
        """
        Gets the qb_class of this CustomerQuery.
        QuickBooks class to import this customer as

        :return: The qb_class of this CustomerQuery.
        :rtype: str
        """
        return self._qb_class

    @qb_class.setter
    def qb_class(self, qb_class):
        """
        Sets the qb_class of this CustomerQuery.
        QuickBooks class to import this customer as

        :param qb_class: The qb_class of this CustomerQuery.
        :type: str
        """

        self._qb_class = qb_class

    @property
    def quickbooks_code(self):
        """
        Gets the quickbooks_code of this CustomerQuery.
        QuickBooks name to import this customer as

        :return: The quickbooks_code of this CustomerQuery.
        :rtype: str
        """
        return self._quickbooks_code

    @quickbooks_code.setter
    def quickbooks_code(self, quickbooks_code):
        """
        Sets the quickbooks_code of this CustomerQuery.
        QuickBooks name to import this customer as

        :param quickbooks_code: The quickbooks_code of this CustomerQuery.
        :type: str
        """

        self._quickbooks_code = quickbooks_code

    @property
    def shipping_city(self):
        """
        Gets the shipping_city of this CustomerQuery.
        Billing city

        :return: The shipping_city of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_city

    @shipping_city.setter
    def shipping_city(self, shipping_city):
        """
        Sets the shipping_city of this CustomerQuery.
        Billing city

        :param shipping_city: The shipping_city of this CustomerQuery.
        :type: str
        """

        if not shipping_city:
            raise ValueError("Invalid value for `shipping_city`, must not be `None`")
        if len(shipping_city) > 32:
            raise ValueError("Invalid value for `shipping_city`, length must be less than `32`")

        self._shipping_city = shipping_city

    @property
    def shipping_company(self):
        """
        Gets the shipping_company of this CustomerQuery.
        Billing company

        :return: The shipping_company of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, shipping_company):
        """
        Sets the shipping_company of this CustomerQuery.
        Billing company

        :param shipping_company: The shipping_company of this CustomerQuery.
        :type: str
        """

        if not shipping_company:
            raise ValueError("Invalid value for `shipping_company`, must not be `None`")
        if len(shipping_company) > 50:
            raise ValueError("Invalid value for `shipping_company`, length must be less than `50`")

        self._shipping_company = shipping_company

    @property
    def shipping_country_code(self):
        """
        Gets the shipping_country_code of this CustomerQuery.
        Billing country code

        :return: The shipping_country_code of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_country_code

    @shipping_country_code.setter
    def shipping_country_code(self, shipping_country_code):
        """
        Sets the shipping_country_code of this CustomerQuery.
        Billing country code

        :param shipping_country_code: The shipping_country_code of this CustomerQuery.
        :type: str
        """

        if not shipping_country_code:
            raise ValueError("Invalid value for `shipping_country_code`, must not be `None`")
        if len(shipping_country_code) > 2:
            raise ValueError("Invalid value for `shipping_country_code`, length must be less than `2`")

        self._shipping_country_code = shipping_country_code

    @property
    def shipping_day_phone(self):
        """
        Gets the shipping_day_phone of this CustomerQuery.
        Billing day phone

        :return: The shipping_day_phone of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_day_phone

    @shipping_day_phone.setter
    def shipping_day_phone(self, shipping_day_phone):
        """
        Sets the shipping_day_phone of this CustomerQuery.
        Billing day phone

        :param shipping_day_phone: The shipping_day_phone of this CustomerQuery.
        :type: str
        """

        if not shipping_day_phone:
            raise ValueError("Invalid value for `shipping_day_phone`, must not be `None`")
        if len(shipping_day_phone) > 25:
            raise ValueError("Invalid value for `shipping_day_phone`, length must be less than `25`")

        self._shipping_day_phone = shipping_day_phone

    @property
    def shipping_evening_phone(self):
        """
        Gets the shipping_evening_phone of this CustomerQuery.
        Billing evening phone

        :return: The shipping_evening_phone of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_evening_phone

    @shipping_evening_phone.setter
    def shipping_evening_phone(self, shipping_evening_phone):
        """
        Sets the shipping_evening_phone of this CustomerQuery.
        Billing evening phone

        :param shipping_evening_phone: The shipping_evening_phone of this CustomerQuery.
        :type: str
        """

        if not shipping_evening_phone:
            raise ValueError("Invalid value for `shipping_evening_phone`, must not be `None`")
        if len(shipping_evening_phone) > 25:
            raise ValueError("Invalid value for `shipping_evening_phone`, length must be less than `25`")

        self._shipping_evening_phone = shipping_evening_phone

    @property
    def shipping_first_name(self):
        """
        Gets the shipping_first_name of this CustomerQuery.
        Billing first name

        :return: The shipping_first_name of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_first_name

    @shipping_first_name.setter
    def shipping_first_name(self, shipping_first_name):
        """
        Sets the shipping_first_name of this CustomerQuery.
        Billing first name

        :param shipping_first_name: The shipping_first_name of this CustomerQuery.
        :type: str
        """

        if not shipping_first_name:
            raise ValueError("Invalid value for `shipping_first_name`, must not be `None`")
        if len(shipping_first_name) > 30:
            raise ValueError("Invalid value for `shipping_first_name`, length must be less than `30`")

        self._shipping_first_name = shipping_first_name

    @property
    def shipping_last_name(self):
        """
        Gets the shipping_last_name of this CustomerQuery.
        Billing last name

        :return: The shipping_last_name of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_last_name

    @shipping_last_name.setter
    def shipping_last_name(self, shipping_last_name):
        """
        Sets the shipping_last_name of this CustomerQuery.
        Billing last name

        :param shipping_last_name: The shipping_last_name of this CustomerQuery.
        :type: str
        """

        if not shipping_last_name:
            raise ValueError("Invalid value for `shipping_last_name`, must not be `None`")
        if len(shipping_last_name) > 30:
            raise ValueError("Invalid value for `shipping_last_name`, length must be less than `30`")

        self._shipping_last_name = shipping_last_name

    @property
    def shipping_postal_code(self):
        """
        Gets the shipping_postal_code of this CustomerQuery.
        Billing postal code

        :return: The shipping_postal_code of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_postal_code

    @shipping_postal_code.setter
    def shipping_postal_code(self, shipping_postal_code):
        """
        Sets the shipping_postal_code of this CustomerQuery.
        Billing postal code

        :param shipping_postal_code: The shipping_postal_code of this CustomerQuery.
        :type: str
        """

        if not shipping_postal_code:
            raise ValueError("Invalid value for `shipping_postal_code`, must not be `None`")
        if len(shipping_postal_code) > 20:
            raise ValueError("Invalid value for `shipping_postal_code`, length must be less than `20`")

        self._shipping_postal_code = shipping_postal_code

    @property
    def shipping_state(self):
        """
        Gets the shipping_state of this CustomerQuery.
        Billing state

        :return: The shipping_state of this CustomerQuery.
        :rtype: str
        """
        return self._shipping_state

    @shipping_state.setter
    def shipping_state(self, shipping_state):
        """
        Sets the shipping_state of this CustomerQuery.
        Billing state

        :param shipping_state: The shipping_state of this CustomerQuery.
        :type: str
        """

        if not shipping_state:
            raise ValueError("Invalid value for `shipping_state`, must not be `None`")
        if len(shipping_state) > 32:
            raise ValueError("Invalid value for `shipping_state`, length must be less than `32`")

        self._shipping_state = shipping_state

    @property
    def signup_dts_end(self):
        """
        Gets the signup_dts_end of this CustomerQuery.
        Signup date end

        :return: The signup_dts_end of this CustomerQuery.
        :rtype: str
        """
        return self._signup_dts_end

    @signup_dts_end.setter
    def signup_dts_end(self, signup_dts_end):
        """
        Sets the signup_dts_end of this CustomerQuery.
        Signup date end

        :param signup_dts_end: The signup_dts_end of this CustomerQuery.
        :type: str
        """

        self._signup_dts_end = signup_dts_end

    @property
    def signup_dts_start(self):
        """
        Gets the signup_dts_start of this CustomerQuery.
        Signup date start

        :return: The signup_dts_start of this CustomerQuery.
        :rtype: str
        """
        return self._signup_dts_start

    @signup_dts_start.setter
    def signup_dts_start(self, signup_dts_start):
        """
        Sets the signup_dts_start of this CustomerQuery.
        Signup date start

        :param signup_dts_start: The signup_dts_start of this CustomerQuery.
        :type: str
        """

        self._signup_dts_start = signup_dts_start

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

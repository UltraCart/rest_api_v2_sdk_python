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


class ConversationEngagementEquationFunction(object):
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
        'any_page_url_logic': 'str',
        'any_page_url_value': 'str',
        'current_page_url_logic': 'str',
        'current_page_url_value': 'str',
        'customers_browsing_time_logic': 'str',
        'customers_browsing_time_seconds': 'int',
        'customers_location_country': 'str',
        'customers_location_logic': 'str',
        'customers_location_state': 'str',
        'number_of_viewed_pages_logic': 'str',
        'number_of_viewed_pages_value': 'int',
        'referring_website_logic': 'str',
        'referring_website_value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'any_page_url_logic': 'any_page_url_logic',
        'any_page_url_value': 'any_page_url_value',
        'current_page_url_logic': 'current_page_url_logic',
        'current_page_url_value': 'current_page_url_value',
        'customers_browsing_time_logic': 'customers_browsing_time_logic',
        'customers_browsing_time_seconds': 'customers_browsing_time_seconds',
        'customers_location_country': 'customers_location_country',
        'customers_location_logic': 'customers_location_logic',
        'customers_location_state': 'customers_location_state',
        'number_of_viewed_pages_logic': 'number_of_viewed_pages_logic',
        'number_of_viewed_pages_value': 'number_of_viewed_pages_value',
        'referring_website_logic': 'referring_website_logic',
        'referring_website_value': 'referring_website_value',
        'type': 'type'
    }

    def __init__(self, any_page_url_logic=None, any_page_url_value=None, current_page_url_logic=None, current_page_url_value=None, customers_browsing_time_logic=None, customers_browsing_time_seconds=None, customers_location_country=None, customers_location_logic=None, customers_location_state=None, number_of_viewed_pages_logic=None, number_of_viewed_pages_value=None, referring_website_logic=None, referring_website_value=None, type=None):  # noqa: E501
        """ConversationEngagementEquationFunction - a model defined in Swagger"""  # noqa: E501

        self._any_page_url_logic = None
        self._any_page_url_value = None
        self._current_page_url_logic = None
        self._current_page_url_value = None
        self._customers_browsing_time_logic = None
        self._customers_browsing_time_seconds = None
        self._customers_location_country = None
        self._customers_location_logic = None
        self._customers_location_state = None
        self._number_of_viewed_pages_logic = None
        self._number_of_viewed_pages_value = None
        self._referring_website_logic = None
        self._referring_website_value = None
        self._type = None
        self.discriminator = None

        if any_page_url_logic is not None:
            self.any_page_url_logic = any_page_url_logic
        if any_page_url_value is not None:
            self.any_page_url_value = any_page_url_value
        if current_page_url_logic is not None:
            self.current_page_url_logic = current_page_url_logic
        if current_page_url_value is not None:
            self.current_page_url_value = current_page_url_value
        if customers_browsing_time_logic is not None:
            self.customers_browsing_time_logic = customers_browsing_time_logic
        if customers_browsing_time_seconds is not None:
            self.customers_browsing_time_seconds = customers_browsing_time_seconds
        if customers_location_country is not None:
            self.customers_location_country = customers_location_country
        if customers_location_logic is not None:
            self.customers_location_logic = customers_location_logic
        if customers_location_state is not None:
            self.customers_location_state = customers_location_state
        if number_of_viewed_pages_logic is not None:
            self.number_of_viewed_pages_logic = number_of_viewed_pages_logic
        if number_of_viewed_pages_value is not None:
            self.number_of_viewed_pages_value = number_of_viewed_pages_value
        if referring_website_logic is not None:
            self.referring_website_logic = referring_website_logic
        if referring_website_value is not None:
            self.referring_website_value = referring_website_value
        if type is not None:
            self.type = type

    @property
    def any_page_url_logic(self):
        """Gets the any_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on an any page url function type  # noqa: E501

        :return: The any_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._any_page_url_logic

    @any_page_url_logic.setter
    def any_page_url_logic(self, any_page_url_logic):
        """Sets the any_page_url_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on an any page url function type  # noqa: E501

        :param any_page_url_logic: The any_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["contains", "does not contain", "is exactly", "is not"]  # noqa: E501
        if any_page_url_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `any_page_url_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(any_page_url_logic, allowed_values)
            )

        self._any_page_url_logic = any_page_url_logic

    @property
    def any_page_url_value(self):
        """Gets the any_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The any_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._any_page_url_value

    @any_page_url_value.setter
    def any_page_url_value(self, any_page_url_value):
        """Sets the any_page_url_value of this ConversationEngagementEquationFunction.


        :param any_page_url_value: The any_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """

        self._any_page_url_value = any_page_url_value

    @property
    def current_page_url_logic(self):
        """Gets the current_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on a current page url function type  # noqa: E501

        :return: The current_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._current_page_url_logic

    @current_page_url_logic.setter
    def current_page_url_logic(self, current_page_url_logic):
        """Sets the current_page_url_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on a current page url function type  # noqa: E501

        :param current_page_url_logic: The current_page_url_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["contains", "does not contain", "is exactly", "is not"]  # noqa: E501
        if current_page_url_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `current_page_url_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(current_page_url_logic, allowed_values)
            )

        self._current_page_url_logic = current_page_url_logic

    @property
    def current_page_url_value(self):
        """Gets the current_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The current_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._current_page_url_value

    @current_page_url_value.setter
    def current_page_url_value(self, current_page_url_value):
        """Sets the current_page_url_value of this ConversationEngagementEquationFunction.


        :param current_page_url_value: The current_page_url_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """

        self._current_page_url_value = current_page_url_value

    @property
    def customers_browsing_time_logic(self):
        """Gets the customers_browsing_time_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on a customer's browsing time function type  # noqa: E501

        :return: The customers_browsing_time_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._customers_browsing_time_logic

    @customers_browsing_time_logic.setter
    def customers_browsing_time_logic(self, customers_browsing_time_logic):
        """Sets the customers_browsing_time_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on a customer's browsing time function type  # noqa: E501

        :param customers_browsing_time_logic: The customers_browsing_time_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["is at least", "is more than", "is less than", "is at most"]  # noqa: E501
        if customers_browsing_time_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `customers_browsing_time_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(customers_browsing_time_logic, allowed_values)
            )

        self._customers_browsing_time_logic = customers_browsing_time_logic

    @property
    def customers_browsing_time_seconds(self):
        """Gets the customers_browsing_time_seconds of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The customers_browsing_time_seconds of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: int
        """
        return self._customers_browsing_time_seconds

    @customers_browsing_time_seconds.setter
    def customers_browsing_time_seconds(self, customers_browsing_time_seconds):
        """Sets the customers_browsing_time_seconds of this ConversationEngagementEquationFunction.


        :param customers_browsing_time_seconds: The customers_browsing_time_seconds of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: int
        """

        self._customers_browsing_time_seconds = customers_browsing_time_seconds

    @property
    def customers_location_country(self):
        """Gets the customers_location_country of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The customers_location_country of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._customers_location_country

    @customers_location_country.setter
    def customers_location_country(self, customers_location_country):
        """Sets the customers_location_country of this ConversationEngagementEquationFunction.


        :param customers_location_country: The customers_location_country of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """

        self._customers_location_country = customers_location_country

    @property
    def customers_location_logic(self):
        """Gets the customers_location_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on a customer's location function type  # noqa: E501

        :return: The customers_location_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._customers_location_logic

    @customers_location_logic.setter
    def customers_location_logic(self, customers_location_logic):
        """Sets the customers_location_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on a customer's location function type  # noqa: E501

        :param customers_location_logic: The customers_location_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["is", "is not"]  # noqa: E501
        if customers_location_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `customers_location_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(customers_location_logic, allowed_values)
            )

        self._customers_location_logic = customers_location_logic

    @property
    def customers_location_state(self):
        """Gets the customers_location_state of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The customers_location_state of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._customers_location_state

    @customers_location_state.setter
    def customers_location_state(self, customers_location_state):
        """Sets the customers_location_state of this ConversationEngagementEquationFunction.


        :param customers_location_state: The customers_location_state of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """

        self._customers_location_state = customers_location_state

    @property
    def number_of_viewed_pages_logic(self):
        """Gets the number_of_viewed_pages_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on a customer's browsing time function type  # noqa: E501

        :return: The number_of_viewed_pages_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._number_of_viewed_pages_logic

    @number_of_viewed_pages_logic.setter
    def number_of_viewed_pages_logic(self, number_of_viewed_pages_logic):
        """Sets the number_of_viewed_pages_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on a customer's browsing time function type  # noqa: E501

        :param number_of_viewed_pages_logic: The number_of_viewed_pages_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["is at least", "is more than", "is less than", "is at most"]  # noqa: E501
        if number_of_viewed_pages_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `number_of_viewed_pages_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(number_of_viewed_pages_logic, allowed_values)
            )

        self._number_of_viewed_pages_logic = number_of_viewed_pages_logic

    @property
    def number_of_viewed_pages_value(self):
        """Gets the number_of_viewed_pages_value of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The number_of_viewed_pages_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: int
        """
        return self._number_of_viewed_pages_value

    @number_of_viewed_pages_value.setter
    def number_of_viewed_pages_value(self, number_of_viewed_pages_value):
        """Sets the number_of_viewed_pages_value of this ConversationEngagementEquationFunction.


        :param number_of_viewed_pages_value: The number_of_viewed_pages_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: int
        """

        self._number_of_viewed_pages_value = number_of_viewed_pages_value

    @property
    def referring_website_logic(self):
        """Gets the referring_website_logic of this ConversationEngagementEquationFunction.  # noqa: E501

        Logic operation to perform on a referring website function type  # noqa: E501

        :return: The referring_website_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._referring_website_logic

    @referring_website_logic.setter
    def referring_website_logic(self, referring_website_logic):
        """Sets the referring_website_logic of this ConversationEngagementEquationFunction.

        Logic operation to perform on a referring website function type  # noqa: E501

        :param referring_website_logic: The referring_website_logic of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["contains", "does not contain", "is exactly", "is not"]  # noqa: E501
        if referring_website_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `referring_website_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(referring_website_logic, allowed_values)
            )

        self._referring_website_logic = referring_website_logic

    @property
    def referring_website_value(self):
        """Gets the referring_website_value of this ConversationEngagementEquationFunction.  # noqa: E501


        :return: The referring_website_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._referring_website_value

    @referring_website_value.setter
    def referring_website_value(self, referring_website_value):
        """Sets the referring_website_value of this ConversationEngagementEquationFunction.


        :param referring_website_value: The referring_website_value of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """

        self._referring_website_value = referring_website_value

    @property
    def type(self):
        """Gets the type of this ConversationEngagementEquationFunction.  # noqa: E501

        Type of function  # noqa: E501

        :return: The type of this ConversationEngagementEquationFunction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationEngagementEquationFunction.

        Type of function  # noqa: E501

        :param type: The type of this ConversationEngagementEquationFunction.  # noqa: E501
        :type: str
        """
        allowed_values = ["current page url", "customers location", "customers browsing time", "number of viewed pages", "referring website address", "any page from session"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ConversationEngagementEquationFunction, dict):
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
        if not isinstance(other, ConversationEngagementEquationFunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

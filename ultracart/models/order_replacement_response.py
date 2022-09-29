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


class OrderReplacementResponse(object):
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
        'charge_successful': 'bool',
        'error_message': 'str',
        'feedback': 'str',
        'free': 'bool',
        'order_id': 'str',
        'successful': 'bool'
    }

    attribute_map = {
        'charge_successful': 'chargeSuccessful',
        'error_message': 'errorMessage',
        'feedback': 'feedback',
        'free': 'free',
        'order_id': 'orderId',
        'successful': 'successful'
    }

    def __init__(self, charge_successful=None, error_message=None, feedback=None, free=None, order_id=None, successful=None):  # noqa: E501
        """OrderReplacementResponse - a model defined in Swagger"""  # noqa: E501

        self._charge_successful = None
        self._error_message = None
        self._feedback = None
        self._free = None
        self._order_id = None
        self._successful = None
        self.discriminator = None

        if charge_successful is not None:
            self.charge_successful = charge_successful
        if error_message is not None:
            self.error_message = error_message
        if feedback is not None:
            self.feedback = feedback
        if free is not None:
            self.free = free
        if order_id is not None:
            self.order_id = order_id
        if successful is not None:
            self.successful = successful

    @property
    def charge_successful(self):
        """Gets the charge_successful of this OrderReplacementResponse.  # noqa: E501


        :return: The charge_successful of this OrderReplacementResponse.  # noqa: E501
        :rtype: bool
        """
        return self._charge_successful

    @charge_successful.setter
    def charge_successful(self, charge_successful):
        """Sets the charge_successful of this OrderReplacementResponse.


        :param charge_successful: The charge_successful of this OrderReplacementResponse.  # noqa: E501
        :type: bool
        """

        self._charge_successful = charge_successful

    @property
    def error_message(self):
        """Gets the error_message of this OrderReplacementResponse.  # noqa: E501


        :return: The error_message of this OrderReplacementResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this OrderReplacementResponse.


        :param error_message: The error_message of this OrderReplacementResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def feedback(self):
        """Gets the feedback of this OrderReplacementResponse.  # noqa: E501


        :return: The feedback of this OrderReplacementResponse.  # noqa: E501
        :rtype: str
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this OrderReplacementResponse.


        :param feedback: The feedback of this OrderReplacementResponse.  # noqa: E501
        :type: str
        """

        self._feedback = feedback

    @property
    def free(self):
        """Gets the free of this OrderReplacementResponse.  # noqa: E501


        :return: The free of this OrderReplacementResponse.  # noqa: E501
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this OrderReplacementResponse.


        :param free: The free of this OrderReplacementResponse.  # noqa: E501
        :type: bool
        """

        self._free = free

    @property
    def order_id(self):
        """Gets the order_id of this OrderReplacementResponse.  # noqa: E501


        :return: The order_id of this OrderReplacementResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderReplacementResponse.


        :param order_id: The order_id of this OrderReplacementResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def successful(self):
        """Gets the successful of this OrderReplacementResponse.  # noqa: E501


        :return: The successful of this OrderReplacementResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this OrderReplacementResponse.


        :param successful: The successful of this OrderReplacementResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

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
        if issubclass(OrderReplacementResponse, dict):
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
        if not isinstance(other, OrderReplacementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
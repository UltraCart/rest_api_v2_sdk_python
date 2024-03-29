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


class OrderPaymentTransaction(object):
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
        'details': 'list[OrderPaymentTransactionDetail]',
        'successful': 'bool',
        'transaction_gateway': 'str',
        'transaction_id': 'int',
        'transaction_timestamp': 'str'
    }

    attribute_map = {
        'details': 'details',
        'successful': 'successful',
        'transaction_gateway': 'transaction_gateway',
        'transaction_id': 'transaction_id',
        'transaction_timestamp': 'transaction_timestamp'
    }

    def __init__(self, details=None, successful=None, transaction_gateway=None, transaction_id=None, transaction_timestamp=None):  # noqa: E501
        """OrderPaymentTransaction - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._successful = None
        self._transaction_gateway = None
        self._transaction_id = None
        self._transaction_timestamp = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if successful is not None:
            self.successful = successful
        if transaction_gateway is not None:
            self.transaction_gateway = transaction_gateway
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_timestamp is not None:
            self.transaction_timestamp = transaction_timestamp

    @property
    def details(self):
        """Gets the details of this OrderPaymentTransaction.  # noqa: E501

        Details  # noqa: E501

        :return: The details of this OrderPaymentTransaction.  # noqa: E501
        :rtype: list[OrderPaymentTransactionDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this OrderPaymentTransaction.

        Details  # noqa: E501

        :param details: The details of this OrderPaymentTransaction.  # noqa: E501
        :type: list[OrderPaymentTransactionDetail]
        """

        self._details = details

    @property
    def successful(self):
        """Gets the successful of this OrderPaymentTransaction.  # noqa: E501

        True if the transaction was successful  # noqa: E501

        :return: The successful of this OrderPaymentTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this OrderPaymentTransaction.

        True if the transaction was successful  # noqa: E501

        :param successful: The successful of this OrderPaymentTransaction.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def transaction_gateway(self):
        """Gets the transaction_gateway of this OrderPaymentTransaction.  # noqa: E501

        Transaction gateway  # noqa: E501

        :return: The transaction_gateway of this OrderPaymentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_gateway

    @transaction_gateway.setter
    def transaction_gateway(self, transaction_gateway):
        """Sets the transaction_gateway of this OrderPaymentTransaction.

        Transaction gateway  # noqa: E501

        :param transaction_gateway: The transaction_gateway of this OrderPaymentTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_gateway = transaction_gateway

    @property
    def transaction_id(self):
        """Gets the transaction_id of this OrderPaymentTransaction.  # noqa: E501

        Transaction ID  # noqa: E501

        :return: The transaction_id of this OrderPaymentTransaction.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this OrderPaymentTransaction.

        Transaction ID  # noqa: E501

        :param transaction_id: The transaction_id of this OrderPaymentTransaction.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def transaction_timestamp(self):
        """Gets the transaction_timestamp of this OrderPaymentTransaction.  # noqa: E501

        Transaction date/time  # noqa: E501

        :return: The transaction_timestamp of this OrderPaymentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_timestamp

    @transaction_timestamp.setter
    def transaction_timestamp(self, transaction_timestamp):
        """Sets the transaction_timestamp of this OrderPaymentTransaction.

        Transaction date/time  # noqa: E501

        :param transaction_timestamp: The transaction_timestamp of this OrderPaymentTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_timestamp = transaction_timestamp

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
        if issubclass(OrderPaymentTransaction, dict):
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
        if not isinstance(other, OrderPaymentTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class ConversationPbxCustomerSnapshotResponse(object):
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
        'auto_orders': 'list[AutoOrder]',
        'customers': 'list[Customer]',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'orders': 'list[Order]',
        'success': 'bool',
        'warning': 'Warning'
    }

    attribute_map = {
        'auto_orders': 'auto_orders',
        'customers': 'customers',
        'error': 'error',
        'metadata': 'metadata',
        'orders': 'orders',
        'success': 'success',
        'warning': 'warning'
    }

    def __init__(self, auto_orders=None, customers=None, error=None, metadata=None, orders=None, success=None, warning=None):  # noqa: E501
        """ConversationPbxCustomerSnapshotResponse - a model defined in Swagger"""  # noqa: E501

        self._auto_orders = None
        self._customers = None
        self._error = None
        self._metadata = None
        self._orders = None
        self._success = None
        self._warning = None
        self.discriminator = None

        if auto_orders is not None:
            self.auto_orders = auto_orders
        if customers is not None:
            self.customers = customers
        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if orders is not None:
            self.orders = orders
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning

    @property
    def auto_orders(self):
        """Gets the auto_orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The auto_orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: list[AutoOrder]
        """
        return self._auto_orders

    @auto_orders.setter
    def auto_orders(self, auto_orders):
        """Sets the auto_orders of this ConversationPbxCustomerSnapshotResponse.


        :param auto_orders: The auto_orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: list[AutoOrder]
        """

        self._auto_orders = auto_orders

    @property
    def customers(self):
        """Gets the customers of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The customers of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: list[Customer]
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this ConversationPbxCustomerSnapshotResponse.


        :param customers: The customers of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: list[Customer]
        """

        self._customers = customers

    @property
    def error(self):
        """Gets the error of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The error of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ConversationPbxCustomerSnapshotResponse.


        :param error: The error of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The metadata of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ConversationPbxCustomerSnapshotResponse.


        :param metadata: The metadata of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def orders(self):
        """Gets the orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this ConversationPbxCustomerSnapshotResponse.


        :param orders: The orders of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

    @property
    def success(self):
        """Gets the success of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ConversationPbxCustomerSnapshotResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501


        :return: The warning of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this ConversationPbxCustomerSnapshotResponse.


        :param warning: The warning of this ConversationPbxCustomerSnapshotResponse.  # noqa: E501
        :type: Warning
        """

        self._warning = warning

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
        if issubclass(ConversationPbxCustomerSnapshotResponse, dict):
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
        if not isinstance(other, ConversationPbxCustomerSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
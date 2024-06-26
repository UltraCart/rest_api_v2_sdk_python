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


class OrderRefundableResponse(object):
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
        'error': 'Error',
        'item_level_refund_reason_required': 'bool',
        'item_level_refund_reasons': 'list[OrderReason]',
        'item_level_return_reasons': 'list[OrderReason]',
        'manual_because_multiple_charges': 'bool',
        'metadata': 'ResponseMetadata',
        'order_level_refund_reason_required': 'bool',
        'order_level_refund_reasons': 'list[OrderReason]',
        'order_level_reject_reason_required': 'bool',
        'order_level_reject_reasons': 'list[OrderReason]',
        'refundable': 'bool',
        'success': 'bool',
        'warning': 'Warning'
    }

    attribute_map = {
        'error': 'error',
        'item_level_refund_reason_required': 'item_level_refund_reason_required',
        'item_level_refund_reasons': 'item_level_refund_reasons',
        'item_level_return_reasons': 'item_level_return_reasons',
        'manual_because_multiple_charges': 'manual_because_multiple_charges',
        'metadata': 'metadata',
        'order_level_refund_reason_required': 'order_level_refund_reason_required',
        'order_level_refund_reasons': 'order_level_refund_reasons',
        'order_level_reject_reason_required': 'order_level_reject_reason_required',
        'order_level_reject_reasons': 'order_level_reject_reasons',
        'refundable': 'refundable',
        'success': 'success',
        'warning': 'warning'
    }

    def __init__(self, error=None, item_level_refund_reason_required=None, item_level_refund_reasons=None, item_level_return_reasons=None, manual_because_multiple_charges=None, metadata=None, order_level_refund_reason_required=None, order_level_refund_reasons=None, order_level_reject_reason_required=None, order_level_reject_reasons=None, refundable=None, success=None, warning=None):  # noqa: E501
        """OrderRefundableResponse - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._item_level_refund_reason_required = None
        self._item_level_refund_reasons = None
        self._item_level_return_reasons = None
        self._manual_because_multiple_charges = None
        self._metadata = None
        self._order_level_refund_reason_required = None
        self._order_level_refund_reasons = None
        self._order_level_reject_reason_required = None
        self._order_level_reject_reasons = None
        self._refundable = None
        self._success = None
        self._warning = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if item_level_refund_reason_required is not None:
            self.item_level_refund_reason_required = item_level_refund_reason_required
        if item_level_refund_reasons is not None:
            self.item_level_refund_reasons = item_level_refund_reasons
        if item_level_return_reasons is not None:
            self.item_level_return_reasons = item_level_return_reasons
        if manual_because_multiple_charges is not None:
            self.manual_because_multiple_charges = manual_because_multiple_charges
        if metadata is not None:
            self.metadata = metadata
        if order_level_refund_reason_required is not None:
            self.order_level_refund_reason_required = order_level_refund_reason_required
        if order_level_refund_reasons is not None:
            self.order_level_refund_reasons = order_level_refund_reasons
        if order_level_reject_reason_required is not None:
            self.order_level_reject_reason_required = order_level_reject_reason_required
        if order_level_reject_reasons is not None:
            self.order_level_reject_reasons = order_level_reject_reasons
        if refundable is not None:
            self.refundable = refundable
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning

    @property
    def error(self):
        """Gets the error of this OrderRefundableResponse.  # noqa: E501


        :return: The error of this OrderRefundableResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OrderRefundableResponse.


        :param error: The error of this OrderRefundableResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def item_level_refund_reason_required(self):
        """Gets the item_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501

        True if the item level refund reason is required  # noqa: E501

        :return: The item_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._item_level_refund_reason_required

    @item_level_refund_reason_required.setter
    def item_level_refund_reason_required(self, item_level_refund_reason_required):
        """Sets the item_level_refund_reason_required of this OrderRefundableResponse.

        True if the item level refund reason is required  # noqa: E501

        :param item_level_refund_reason_required: The item_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._item_level_refund_reason_required = item_level_refund_reason_required

    @property
    def item_level_refund_reasons(self):
        """Gets the item_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501

        Reason codes available at the item level.  # noqa: E501

        :return: The item_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501
        :rtype: list[OrderReason]
        """
        return self._item_level_refund_reasons

    @item_level_refund_reasons.setter
    def item_level_refund_reasons(self, item_level_refund_reasons):
        """Sets the item_level_refund_reasons of this OrderRefundableResponse.

        Reason codes available at the item level.  # noqa: E501

        :param item_level_refund_reasons: The item_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501
        :type: list[OrderReason]
        """

        self._item_level_refund_reasons = item_level_refund_reasons

    @property
    def item_level_return_reasons(self):
        """Gets the item_level_return_reasons of this OrderRefundableResponse.  # noqa: E501

        Return codes available at the item level.  # noqa: E501

        :return: The item_level_return_reasons of this OrderRefundableResponse.  # noqa: E501
        :rtype: list[OrderReason]
        """
        return self._item_level_return_reasons

    @item_level_return_reasons.setter
    def item_level_return_reasons(self, item_level_return_reasons):
        """Sets the item_level_return_reasons of this OrderRefundableResponse.

        Return codes available at the item level.  # noqa: E501

        :param item_level_return_reasons: The item_level_return_reasons of this OrderRefundableResponse.  # noqa: E501
        :type: list[OrderReason]
        """

        self._item_level_return_reasons = item_level_return_reasons

    @property
    def manual_because_multiple_charges(self):
        """Gets the manual_because_multiple_charges of this OrderRefundableResponse.  # noqa: E501

        If true, this refund will have to be manually done because of additional charges with the virtual terminal were made  # noqa: E501

        :return: The manual_because_multiple_charges of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._manual_because_multiple_charges

    @manual_because_multiple_charges.setter
    def manual_because_multiple_charges(self, manual_because_multiple_charges):
        """Sets the manual_because_multiple_charges of this OrderRefundableResponse.

        If true, this refund will have to be manually done because of additional charges with the virtual terminal were made  # noqa: E501

        :param manual_because_multiple_charges: The manual_because_multiple_charges of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._manual_because_multiple_charges = manual_because_multiple_charges

    @property
    def metadata(self):
        """Gets the metadata of this OrderRefundableResponse.  # noqa: E501


        :return: The metadata of this OrderRefundableResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OrderRefundableResponse.


        :param metadata: The metadata of this OrderRefundableResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def order_level_refund_reason_required(self):
        """Gets the order_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501

        True if the order level refund reason is required  # noqa: E501

        :return: The order_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._order_level_refund_reason_required

    @order_level_refund_reason_required.setter
    def order_level_refund_reason_required(self, order_level_refund_reason_required):
        """Sets the order_level_refund_reason_required of this OrderRefundableResponse.

        True if the order level refund reason is required  # noqa: E501

        :param order_level_refund_reason_required: The order_level_refund_reason_required of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._order_level_refund_reason_required = order_level_refund_reason_required

    @property
    def order_level_refund_reasons(self):
        """Gets the order_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501

        Reason codes available at the order level.  # noqa: E501

        :return: The order_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501
        :rtype: list[OrderReason]
        """
        return self._order_level_refund_reasons

    @order_level_refund_reasons.setter
    def order_level_refund_reasons(self, order_level_refund_reasons):
        """Sets the order_level_refund_reasons of this OrderRefundableResponse.

        Reason codes available at the order level.  # noqa: E501

        :param order_level_refund_reasons: The order_level_refund_reasons of this OrderRefundableResponse.  # noqa: E501
        :type: list[OrderReason]
        """

        self._order_level_refund_reasons = order_level_refund_reasons

    @property
    def order_level_reject_reason_required(self):
        """Gets the order_level_reject_reason_required of this OrderRefundableResponse.  # noqa: E501

        True if the order level reject reason is required  # noqa: E501

        :return: The order_level_reject_reason_required of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._order_level_reject_reason_required

    @order_level_reject_reason_required.setter
    def order_level_reject_reason_required(self, order_level_reject_reason_required):
        """Sets the order_level_reject_reason_required of this OrderRefundableResponse.

        True if the order level reject reason is required  # noqa: E501

        :param order_level_reject_reason_required: The order_level_reject_reason_required of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._order_level_reject_reason_required = order_level_reject_reason_required

    @property
    def order_level_reject_reasons(self):
        """Gets the order_level_reject_reasons of this OrderRefundableResponse.  # noqa: E501

        Reject codes available at the order level.  # noqa: E501

        :return: The order_level_reject_reasons of this OrderRefundableResponse.  # noqa: E501
        :rtype: list[OrderReason]
        """
        return self._order_level_reject_reasons

    @order_level_reject_reasons.setter
    def order_level_reject_reasons(self, order_level_reject_reasons):
        """Sets the order_level_reject_reasons of this OrderRefundableResponse.

        Reject codes available at the order level.  # noqa: E501

        :param order_level_reject_reasons: The order_level_reject_reasons of this OrderRefundableResponse.  # noqa: E501
        :type: list[OrderReason]
        """

        self._order_level_reject_reasons = order_level_reject_reasons

    @property
    def refundable(self):
        """Gets the refundable of this OrderRefundableResponse.  # noqa: E501

        Whether the order is refundable or not.  Null should be interpreted as false.  # noqa: E501

        :return: The refundable of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._refundable

    @refundable.setter
    def refundable(self, refundable):
        """Sets the refundable of this OrderRefundableResponse.

        Whether the order is refundable or not.  Null should be interpreted as false.  # noqa: E501

        :param refundable: The refundable of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._refundable = refundable

    @property
    def success(self):
        """Gets the success of this OrderRefundableResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this OrderRefundableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this OrderRefundableResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this OrderRefundableResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this OrderRefundableResponse.  # noqa: E501


        :return: The warning of this OrderRefundableResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this OrderRefundableResponse.


        :param warning: The warning of this OrderRefundableResponse.  # noqa: E501
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
        if issubclass(OrderRefundableResponse, dict):
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
        if not isinstance(other, OrderRefundableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

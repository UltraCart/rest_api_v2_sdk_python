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


class PointOfSaleReader(object):
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
        'device_type': 'str',
        'label': 'str',
        'merchant_id': 'str',
        'payment_provider': 'str',
        'pos_reader_id': 'int',
        'pos_register_oid': 'int',
        'serial_number': 'str',
        'stripe_account_id': 'str',
        'stripe_reader_id': 'str'
    }

    attribute_map = {
        'device_type': 'device_type',
        'label': 'label',
        'merchant_id': 'merchant_id',
        'payment_provider': 'payment_provider',
        'pos_reader_id': 'pos_reader_id',
        'pos_register_oid': 'pos_register_oid',
        'serial_number': 'serial_number',
        'stripe_account_id': 'stripe_account_id',
        'stripe_reader_id': 'stripe_reader_id'
    }

    def __init__(self, device_type=None, label=None, merchant_id=None, payment_provider=None, pos_reader_id=None, pos_register_oid=None, serial_number=None, stripe_account_id=None, stripe_reader_id=None):  # noqa: E501
        """PointOfSaleReader - a model defined in Swagger"""  # noqa: E501

        self._device_type = None
        self._label = None
        self._merchant_id = None
        self._payment_provider = None
        self._pos_reader_id = None
        self._pos_register_oid = None
        self._serial_number = None
        self._stripe_account_id = None
        self._stripe_reader_id = None
        self.discriminator = None

        if device_type is not None:
            self.device_type = device_type
        if label is not None:
            self.label = label
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if payment_provider is not None:
            self.payment_provider = payment_provider
        if pos_reader_id is not None:
            self.pos_reader_id = pos_reader_id
        if pos_register_oid is not None:
            self.pos_register_oid = pos_register_oid
        if serial_number is not None:
            self.serial_number = serial_number
        if stripe_account_id is not None:
            self.stripe_account_id = stripe_account_id
        if stripe_reader_id is not None:
            self.stripe_reader_id = stripe_reader_id

    @property
    def device_type(self):
        """Gets the device_type of this PointOfSaleReader.  # noqa: E501

        The device type of the reader.  # noqa: E501

        :return: The device_type of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this PointOfSaleReader.

        The device type of the reader.  # noqa: E501

        :param device_type: The device_type of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def label(self):
        """Gets the label of this PointOfSaleReader.  # noqa: E501

        The label of the reader.  # noqa: E501

        :return: The label of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PointOfSaleReader.

        The label of the reader.  # noqa: E501

        :param label: The label of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def merchant_id(self):
        """Gets the merchant_id of this PointOfSaleReader.  # noqa: E501

        The merchant id that owns this point of sale reader.  # noqa: E501

        :return: The merchant_id of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this PointOfSaleReader.

        The merchant id that owns this point of sale reader.  # noqa: E501

        :param merchant_id: The merchant_id of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def payment_provider(self):
        """Gets the payment_provider of this PointOfSaleReader.  # noqa: E501

        The payment provider for the card reader.  # noqa: E501

        :return: The payment_provider of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._payment_provider

    @payment_provider.setter
    def payment_provider(self, payment_provider):
        """Sets the payment_provider of this PointOfSaleReader.

        The payment provider for the card reader.  # noqa: E501

        :param payment_provider: The payment_provider of this PointOfSaleReader.  # noqa: E501
        :type: str
        """
        allowed_values = ["stripe"]  # noqa: E501
        if payment_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_provider` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_provider, allowed_values)
            )

        self._payment_provider = payment_provider

    @property
    def pos_reader_id(self):
        """Gets the pos_reader_id of this PointOfSaleReader.  # noqa: E501

        Object identifier of the point of sale reader.  # noqa: E501

        :return: The pos_reader_id of this PointOfSaleReader.  # noqa: E501
        :rtype: int
        """
        return self._pos_reader_id

    @pos_reader_id.setter
    def pos_reader_id(self, pos_reader_id):
        """Sets the pos_reader_id of this PointOfSaleReader.

        Object identifier of the point of sale reader.  # noqa: E501

        :param pos_reader_id: The pos_reader_id of this PointOfSaleReader.  # noqa: E501
        :type: int
        """

        self._pos_reader_id = pos_reader_id

    @property
    def pos_register_oid(self):
        """Gets the pos_register_oid of this PointOfSaleReader.  # noqa: E501

        Object identifier of the point of sale register this reader is assigned to.  # noqa: E501

        :return: The pos_register_oid of this PointOfSaleReader.  # noqa: E501
        :rtype: int
        """
        return self._pos_register_oid

    @pos_register_oid.setter
    def pos_register_oid(self, pos_register_oid):
        """Sets the pos_register_oid of this PointOfSaleReader.

        Object identifier of the point of sale register this reader is assigned to.  # noqa: E501

        :param pos_register_oid: The pos_register_oid of this PointOfSaleReader.  # noqa: E501
        :type: int
        """

        self._pos_register_oid = pos_register_oid

    @property
    def serial_number(self):
        """Gets the serial_number of this PointOfSaleReader.  # noqa: E501

        The serial number of the reader.  # noqa: E501

        :return: The serial_number of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this PointOfSaleReader.

        The serial number of the reader.  # noqa: E501

        :param serial_number: The serial_number of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def stripe_account_id(self):
        """Gets the stripe_account_id of this PointOfSaleReader.  # noqa: E501

        If the payment provider is Stripe, this is the Stripe account id  # noqa: E501

        :return: The stripe_account_id of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._stripe_account_id

    @stripe_account_id.setter
    def stripe_account_id(self, stripe_account_id):
        """Sets the stripe_account_id of this PointOfSaleReader.

        If the payment provider is Stripe, this is the Stripe account id  # noqa: E501

        :param stripe_account_id: The stripe_account_id of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._stripe_account_id = stripe_account_id

    @property
    def stripe_reader_id(self):
        """Gets the stripe_reader_id of this PointOfSaleReader.  # noqa: E501

        If the payment provide is Stripe, this is the Stripe terminal reader id  # noqa: E501

        :return: The stripe_reader_id of this PointOfSaleReader.  # noqa: E501
        :rtype: str
        """
        return self._stripe_reader_id

    @stripe_reader_id.setter
    def stripe_reader_id(self, stripe_reader_id):
        """Sets the stripe_reader_id of this PointOfSaleReader.

        If the payment provide is Stripe, this is the Stripe terminal reader id  # noqa: E501

        :param stripe_reader_id: The stripe_reader_id of this PointOfSaleReader.  # noqa: E501
        :type: str
        """

        self._stripe_reader_id = stripe_reader_id

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
        if issubclass(PointOfSaleReader, dict):
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
        if not isinstance(other, PointOfSaleReader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
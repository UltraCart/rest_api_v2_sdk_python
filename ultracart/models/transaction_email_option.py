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


class TransactionEmailOption(object):
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
        'description': 'str',
        'merchant_email_delivery_option_oid': 'int',
        'merchant_id': 'str',
        'name': 'str',
        'selected': 'bool',
        'store_front_oid': 'int',
        'template_display': 'str',
        'template_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'merchant_email_delivery_option_oid': 'merchantEmailDeliveryOptionOid',
        'merchant_id': 'merchantId',
        'name': 'name',
        'selected': 'selected',
        'store_front_oid': 'storeFrontOid',
        'template_display': 'templateDisplay',
        'template_type': 'templateType'
    }

    def __init__(self, description=None, merchant_email_delivery_option_oid=None, merchant_id=None, name=None, selected=None, store_front_oid=None, template_display=None, template_type=None):  # noqa: E501
        """TransactionEmailOption - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._merchant_email_delivery_option_oid = None
        self._merchant_id = None
        self._name = None
        self._selected = None
        self._store_front_oid = None
        self._template_display = None
        self._template_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if merchant_email_delivery_option_oid is not None:
            self.merchant_email_delivery_option_oid = merchant_email_delivery_option_oid
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if selected is not None:
            self.selected = selected
        if store_front_oid is not None:
            self.store_front_oid = store_front_oid
        if template_display is not None:
            self.template_display = template_display
        if template_type is not None:
            self.template_type = template_type

    @property
    def description(self):
        """Gets the description of this TransactionEmailOption.  # noqa: E501


        :return: The description of this TransactionEmailOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionEmailOption.


        :param description: The description of this TransactionEmailOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def merchant_email_delivery_option_oid(self):
        """Gets the merchant_email_delivery_option_oid of this TransactionEmailOption.  # noqa: E501


        :return: The merchant_email_delivery_option_oid of this TransactionEmailOption.  # noqa: E501
        :rtype: int
        """
        return self._merchant_email_delivery_option_oid

    @merchant_email_delivery_option_oid.setter
    def merchant_email_delivery_option_oid(self, merchant_email_delivery_option_oid):
        """Sets the merchant_email_delivery_option_oid of this TransactionEmailOption.


        :param merchant_email_delivery_option_oid: The merchant_email_delivery_option_oid of this TransactionEmailOption.  # noqa: E501
        :type: int
        """

        self._merchant_email_delivery_option_oid = merchant_email_delivery_option_oid

    @property
    def merchant_id(self):
        """Gets the merchant_id of this TransactionEmailOption.  # noqa: E501


        :return: The merchant_id of this TransactionEmailOption.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this TransactionEmailOption.


        :param merchant_id: The merchant_id of this TransactionEmailOption.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this TransactionEmailOption.  # noqa: E501


        :return: The name of this TransactionEmailOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransactionEmailOption.


        :param name: The name of this TransactionEmailOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def selected(self):
        """Gets the selected of this TransactionEmailOption.  # noqa: E501


        :return: The selected of this TransactionEmailOption.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this TransactionEmailOption.


        :param selected: The selected of this TransactionEmailOption.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def store_front_oid(self):
        """Gets the store_front_oid of this TransactionEmailOption.  # noqa: E501


        :return: The store_front_oid of this TransactionEmailOption.  # noqa: E501
        :rtype: int
        """
        return self._store_front_oid

    @store_front_oid.setter
    def store_front_oid(self, store_front_oid):
        """Sets the store_front_oid of this TransactionEmailOption.


        :param store_front_oid: The store_front_oid of this TransactionEmailOption.  # noqa: E501
        :type: int
        """

        self._store_front_oid = store_front_oid

    @property
    def template_display(self):
        """Gets the template_display of this TransactionEmailOption.  # noqa: E501


        :return: The template_display of this TransactionEmailOption.  # noqa: E501
        :rtype: str
        """
        return self._template_display

    @template_display.setter
    def template_display(self, template_display):
        """Sets the template_display of this TransactionEmailOption.


        :param template_display: The template_display of this TransactionEmailOption.  # noqa: E501
        :type: str
        """

        self._template_display = template_display

    @property
    def template_type(self):
        """Gets the template_type of this TransactionEmailOption.  # noqa: E501


        :return: The template_type of this TransactionEmailOption.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this TransactionEmailOption.


        :param template_type: The template_type of this TransactionEmailOption.  # noqa: E501
        :type: str
        """

        self._template_type = template_type

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
        if issubclass(TransactionEmailOption, dict):
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
        if not isinstance(other, TransactionEmailOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
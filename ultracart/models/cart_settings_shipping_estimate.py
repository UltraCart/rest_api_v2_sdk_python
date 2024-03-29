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


class CartSettingsShippingEstimate(object):
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
        'allow_3rd_party_billing': 'bool',
        'comment': 'str',
        'cost': 'Currency',
        'cost_before_discount': 'Currency',
        'default_method': 'bool',
        'discount': 'Currency',
        'discounted': 'bool',
        'display_name': 'str',
        'estimated_delivery': 'str',
        'lift_gate_option': 'bool',
        'name': 'str',
        'pickup': 'bool',
        'tax': 'Currency',
        'total_tax': 'Currency'
    }

    attribute_map = {
        'allow_3rd_party_billing': 'allow_3rd_party_billing',
        'comment': 'comment',
        'cost': 'cost',
        'cost_before_discount': 'cost_before_discount',
        'default_method': 'default_method',
        'discount': 'discount',
        'discounted': 'discounted',
        'display_name': 'display_name',
        'estimated_delivery': 'estimated_delivery',
        'lift_gate_option': 'lift_gate_option',
        'name': 'name',
        'pickup': 'pickup',
        'tax': 'tax',
        'total_tax': 'total_tax'
    }

    def __init__(self, allow_3rd_party_billing=None, comment=None, cost=None, cost_before_discount=None, default_method=None, discount=None, discounted=None, display_name=None, estimated_delivery=None, lift_gate_option=None, name=None, pickup=None, tax=None, total_tax=None):  # noqa: E501
        """CartSettingsShippingEstimate - a model defined in Swagger"""  # noqa: E501

        self._allow_3rd_party_billing = None
        self._comment = None
        self._cost = None
        self._cost_before_discount = None
        self._default_method = None
        self._discount = None
        self._discounted = None
        self._display_name = None
        self._estimated_delivery = None
        self._lift_gate_option = None
        self._name = None
        self._pickup = None
        self._tax = None
        self._total_tax = None
        self.discriminator = None

        if allow_3rd_party_billing is not None:
            self.allow_3rd_party_billing = allow_3rd_party_billing
        if comment is not None:
            self.comment = comment
        if cost is not None:
            self.cost = cost
        if cost_before_discount is not None:
            self.cost_before_discount = cost_before_discount
        if default_method is not None:
            self.default_method = default_method
        if discount is not None:
            self.discount = discount
        if discounted is not None:
            self.discounted = discounted
        if display_name is not None:
            self.display_name = display_name
        if estimated_delivery is not None:
            self.estimated_delivery = estimated_delivery
        if lift_gate_option is not None:
            self.lift_gate_option = lift_gate_option
        if name is not None:
            self.name = name
        if pickup is not None:
            self.pickup = pickup
        if tax is not None:
            self.tax = tax
        if total_tax is not None:
            self.total_tax = total_tax

    @property
    def allow_3rd_party_billing(self):
        """Gets the allow_3rd_party_billing of this CartSettingsShippingEstimate.  # noqa: E501

        True if this method allows the customer to use their own shipper account number  # noqa: E501

        :return: The allow_3rd_party_billing of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: bool
        """
        return self._allow_3rd_party_billing

    @allow_3rd_party_billing.setter
    def allow_3rd_party_billing(self, allow_3rd_party_billing):
        """Sets the allow_3rd_party_billing of this CartSettingsShippingEstimate.

        True if this method allows the customer to use their own shipper account number  # noqa: E501

        :param allow_3rd_party_billing: The allow_3rd_party_billing of this CartSettingsShippingEstimate.  # noqa: E501
        :type: bool
        """

        self._allow_3rd_party_billing = allow_3rd_party_billing

    @property
    def comment(self):
        """Gets the comment of this CartSettingsShippingEstimate.  # noqa: E501

        Comment to display to the customer about this method  # noqa: E501

        :return: The comment of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CartSettingsShippingEstimate.

        Comment to display to the customer about this method  # noqa: E501

        :param comment: The comment of this CartSettingsShippingEstimate.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def cost(self):
        """Gets the cost of this CartSettingsShippingEstimate.  # noqa: E501


        :return: The cost of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: Currency
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CartSettingsShippingEstimate.


        :param cost: The cost of this CartSettingsShippingEstimate.  # noqa: E501
        :type: Currency
        """

        self._cost = cost

    @property
    def cost_before_discount(self):
        """Gets the cost_before_discount of this CartSettingsShippingEstimate.  # noqa: E501


        :return: The cost_before_discount of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: Currency
        """
        return self._cost_before_discount

    @cost_before_discount.setter
    def cost_before_discount(self, cost_before_discount):
        """Sets the cost_before_discount of this CartSettingsShippingEstimate.


        :param cost_before_discount: The cost_before_discount of this CartSettingsShippingEstimate.  # noqa: E501
        :type: Currency
        """

        self._cost_before_discount = cost_before_discount

    @property
    def default_method(self):
        """Gets the default_method of this CartSettingsShippingEstimate.  # noqa: E501

        True if this is the default method  # noqa: E501

        :return: The default_method of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: bool
        """
        return self._default_method

    @default_method.setter
    def default_method(self, default_method):
        """Sets the default_method of this CartSettingsShippingEstimate.

        True if this is the default method  # noqa: E501

        :param default_method: The default_method of this CartSettingsShippingEstimate.  # noqa: E501
        :type: bool
        """

        self._default_method = default_method

    @property
    def discount(self):
        """Gets the discount of this CartSettingsShippingEstimate.  # noqa: E501


        :return: The discount of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: Currency
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this CartSettingsShippingEstimate.


        :param discount: The discount of this CartSettingsShippingEstimate.  # noqa: E501
        :type: Currency
        """

        self._discount = discount

    @property
    def discounted(self):
        """Gets the discounted of this CartSettingsShippingEstimate.  # noqa: E501

        True if this method is discounted because of a coupon  # noqa: E501

        :return: The discounted of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: bool
        """
        return self._discounted

    @discounted.setter
    def discounted(self, discounted):
        """Sets the discounted of this CartSettingsShippingEstimate.

        True if this method is discounted because of a coupon  # noqa: E501

        :param discounted: The discounted of this CartSettingsShippingEstimate.  # noqa: E501
        :type: bool
        """

        self._discounted = discounted

    @property
    def display_name(self):
        """Gets the display_name of this CartSettingsShippingEstimate.  # noqa: E501

        The name to display to the customer  # noqa: E501

        :return: The display_name of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CartSettingsShippingEstimate.

        The name to display to the customer  # noqa: E501

        :param display_name: The display_name of this CartSettingsShippingEstimate.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def estimated_delivery(self):
        """Gets the estimated_delivery of this CartSettingsShippingEstimate.  # noqa: E501

        Date of the estimated delivery (or range)  # noqa: E501

        :return: The estimated_delivery of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: str
        """
        return self._estimated_delivery

    @estimated_delivery.setter
    def estimated_delivery(self, estimated_delivery):
        """Sets the estimated_delivery of this CartSettingsShippingEstimate.

        Date of the estimated delivery (or range)  # noqa: E501

        :param estimated_delivery: The estimated_delivery of this CartSettingsShippingEstimate.  # noqa: E501
        :type: str
        """

        self._estimated_delivery = estimated_delivery

    @property
    def lift_gate_option(self):
        """Gets the lift_gate_option of this CartSettingsShippingEstimate.  # noqa: E501

        True if a lift gate option for this method should be offered to the customer  # noqa: E501

        :return: The lift_gate_option of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: bool
        """
        return self._lift_gate_option

    @lift_gate_option.setter
    def lift_gate_option(self, lift_gate_option):
        """Sets the lift_gate_option of this CartSettingsShippingEstimate.

        True if a lift gate option for this method should be offered to the customer  # noqa: E501

        :param lift_gate_option: The lift_gate_option of this CartSettingsShippingEstimate.  # noqa: E501
        :type: bool
        """

        self._lift_gate_option = lift_gate_option

    @property
    def name(self):
        """Gets the name of this CartSettingsShippingEstimate.  # noqa: E501

        Shipping method name  # noqa: E501

        :return: The name of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartSettingsShippingEstimate.

        Shipping method name  # noqa: E501

        :param name: The name of this CartSettingsShippingEstimate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pickup(self):
        """Gets the pickup of this CartSettingsShippingEstimate.  # noqa: E501

        True if this shipping method requires customers to physically pickup product themselves  # noqa: E501

        :return: The pickup of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: bool
        """
        return self._pickup

    @pickup.setter
    def pickup(self, pickup):
        """Sets the pickup of this CartSettingsShippingEstimate.

        True if this shipping method requires customers to physically pickup product themselves  # noqa: E501

        :param pickup: The pickup of this CartSettingsShippingEstimate.  # noqa: E501
        :type: bool
        """

        self._pickup = pickup

    @property
    def tax(self):
        """Gets the tax of this CartSettingsShippingEstimate.  # noqa: E501


        :return: The tax of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: Currency
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this CartSettingsShippingEstimate.


        :param tax: The tax of this CartSettingsShippingEstimate.  # noqa: E501
        :type: Currency
        """

        self._tax = tax

    @property
    def total_tax(self):
        """Gets the total_tax of this CartSettingsShippingEstimate.  # noqa: E501


        :return: The total_tax of this CartSettingsShippingEstimate.  # noqa: E501
        :rtype: Currency
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this CartSettingsShippingEstimate.


        :param total_tax: The total_tax of this CartSettingsShippingEstimate.  # noqa: E501
        :type: Currency
        """

        self._total_tax = total_tax

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
        if issubclass(CartSettingsShippingEstimate, dict):
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
        if not isinstance(other, CartSettingsShippingEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

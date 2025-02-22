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


class ChannelPartnerOrderItem(object):
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
        'arbitrary_unit_cost': 'float',
        'auto_order_last_rebill_dts': 'str',
        'auto_order_schedule': 'str',
        'merchant_item_id': 'str',
        'options': 'list[ChannelPartnerOrderItemOption]',
        'quantity': 'float',
        'upsell': 'bool'
    }

    attribute_map = {
        'arbitrary_unit_cost': 'arbitrary_unit_cost',
        'auto_order_last_rebill_dts': 'auto_order_last_rebill_dts',
        'auto_order_schedule': 'auto_order_schedule',
        'merchant_item_id': 'merchant_item_id',
        'options': 'options',
        'quantity': 'quantity',
        'upsell': 'upsell'
    }

    def __init__(self, arbitrary_unit_cost=None, auto_order_last_rebill_dts=None, auto_order_schedule=None, merchant_item_id=None, options=None, quantity=None, upsell=None):  # noqa: E501
        """ChannelPartnerOrderItem - a model defined in Swagger"""  # noqa: E501

        self._arbitrary_unit_cost = None
        self._auto_order_last_rebill_dts = None
        self._auto_order_schedule = None
        self._merchant_item_id = None
        self._options = None
        self._quantity = None
        self._upsell = None
        self.discriminator = None

        if arbitrary_unit_cost is not None:
            self.arbitrary_unit_cost = arbitrary_unit_cost
        if auto_order_last_rebill_dts is not None:
            self.auto_order_last_rebill_dts = auto_order_last_rebill_dts
        if auto_order_schedule is not None:
            self.auto_order_schedule = auto_order_schedule
        if merchant_item_id is not None:
            self.merchant_item_id = merchant_item_id
        if options is not None:
            self.options = options
        if quantity is not None:
            self.quantity = quantity
        if upsell is not None:
            self.upsell = upsell

    @property
    def arbitrary_unit_cost(self):
        """Gets the arbitrary_unit_cost of this ChannelPartnerOrderItem.  # noqa: E501

        Arbitrary unit cost for this item that differs from the listed price  # noqa: E501

        :return: The arbitrary_unit_cost of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: float
        """
        return self._arbitrary_unit_cost

    @arbitrary_unit_cost.setter
    def arbitrary_unit_cost(self, arbitrary_unit_cost):
        """Sets the arbitrary_unit_cost of this ChannelPartnerOrderItem.

        Arbitrary unit cost for this item that differs from the listed price  # noqa: E501

        :param arbitrary_unit_cost: The arbitrary_unit_cost of this ChannelPartnerOrderItem.  # noqa: E501
        :type: float
        """

        self._arbitrary_unit_cost = arbitrary_unit_cost

    @property
    def auto_order_last_rebill_dts(self):
        """Gets the auto_order_last_rebill_dts of this ChannelPartnerOrderItem.  # noqa: E501

        Optional date/time of the last rebill if this item is part of an auto (recurring) order  # noqa: E501

        :return: The auto_order_last_rebill_dts of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: str
        """
        return self._auto_order_last_rebill_dts

    @auto_order_last_rebill_dts.setter
    def auto_order_last_rebill_dts(self, auto_order_last_rebill_dts):
        """Sets the auto_order_last_rebill_dts of this ChannelPartnerOrderItem.

        Optional date/time of the last rebill if this item is part of an auto (recurring) order  # noqa: E501

        :param auto_order_last_rebill_dts: The auto_order_last_rebill_dts of this ChannelPartnerOrderItem.  # noqa: E501
        :type: str
        """

        self._auto_order_last_rebill_dts = auto_order_last_rebill_dts

    @property
    def auto_order_schedule(self):
        """Gets the auto_order_schedule of this ChannelPartnerOrderItem.  # noqa: E501

        The frequency schedule for this item if this item is part of an auto (recurring) order  # noqa: E501

        :return: The auto_order_schedule of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: str
        """
        return self._auto_order_schedule

    @auto_order_schedule.setter
    def auto_order_schedule(self, auto_order_schedule):
        """Sets the auto_order_schedule of this ChannelPartnerOrderItem.

        The frequency schedule for this item if this item is part of an auto (recurring) order  # noqa: E501

        :param auto_order_schedule: The auto_order_schedule of this ChannelPartnerOrderItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Weekly", "Every 10 Days", "Biweekly", "Every 24 Days", "Every 28 Days", "Monthly", "Every 45 Days", "Every 2 Months", "Every 3 Months", "Every 4 Months", "Every 5 Months", "Every 6 Months", "Yearly", "Every 4 Weeks", "Every 6 Weeks", "Every 8 Weeks"]  # noqa: E501
        if auto_order_schedule not in allowed_values:
            raise ValueError(
                "Invalid value for `auto_order_schedule` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_order_schedule, allowed_values)
            )

        self._auto_order_schedule = auto_order_schedule

    @property
    def merchant_item_id(self):
        """Gets the merchant_item_id of this ChannelPartnerOrderItem.  # noqa: E501

        Item ID  # noqa: E501

        :return: The merchant_item_id of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: str
        """
        return self._merchant_item_id

    @merchant_item_id.setter
    def merchant_item_id(self, merchant_item_id):
        """Sets the merchant_item_id of this ChannelPartnerOrderItem.

        Item ID  # noqa: E501

        :param merchant_item_id: The merchant_item_id of this ChannelPartnerOrderItem.  # noqa: E501
        :type: str
        """
        if merchant_item_id is not None and len(merchant_item_id) > 20:
            raise ValueError("Invalid value for `merchant_item_id`, length must be less than or equal to `20`")  # noqa: E501

        self._merchant_item_id = merchant_item_id

    @property
    def options(self):
        """Gets the options of this ChannelPartnerOrderItem.  # noqa: E501

        Item options  # noqa: E501

        :return: The options of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: list[ChannelPartnerOrderItemOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ChannelPartnerOrderItem.

        Item options  # noqa: E501

        :param options: The options of this ChannelPartnerOrderItem.  # noqa: E501
        :type: list[ChannelPartnerOrderItemOption]
        """

        self._options = options

    @property
    def quantity(self):
        """Gets the quantity of this ChannelPartnerOrderItem.  # noqa: E501

        Quantity  # noqa: E501

        :return: The quantity of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ChannelPartnerOrderItem.

        Quantity  # noqa: E501

        :param quantity: The quantity of this ChannelPartnerOrderItem.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def upsell(self):
        """Gets the upsell of this ChannelPartnerOrderItem.  # noqa: E501

        True if this item was an upsell item.  # noqa: E501

        :return: The upsell of this ChannelPartnerOrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._upsell

    @upsell.setter
    def upsell(self, upsell):
        """Sets the upsell of this ChannelPartnerOrderItem.

        True if this item was an upsell item.  # noqa: E501

        :param upsell: The upsell of this ChannelPartnerOrderItem.  # noqa: E501
        :type: bool
        """

        self._upsell = upsell

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
        if issubclass(ChannelPartnerOrderItem, dict):
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
        if not isinstance(other, ChannelPartnerOrderItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

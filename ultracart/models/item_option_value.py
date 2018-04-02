# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ItemOptionValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'additional_dimension_application': 'str',
        'additional_items': 'list[ItemOptionValueAdditionalItem]',
        'cost_change': 'float',
        'default_value': 'bool',
        'digital_items': 'list[ItemOptionValueDigitalItem]',
        'height': 'Distance',
        'length': 'Distance',
        'merchant_item_multimedia_oid': 'int',
        'option_value_oid': 'int',
        'percent_cost_change': 'float',
        'translated_text_instance_oid': 'int',
        'value': 'str',
        'weight_change': 'Weight',
        'weight_change_percent': 'float',
        'width': 'Distance'
    }

    attribute_map = {
        'additional_dimension_application': 'additional_dimension_application',
        'additional_items': 'additional_items',
        'cost_change': 'cost_change',
        'default_value': 'default_value',
        'digital_items': 'digital_items',
        'height': 'height',
        'length': 'length',
        'merchant_item_multimedia_oid': 'merchant_item_multimedia_oid',
        'option_value_oid': 'option_value_oid',
        'percent_cost_change': 'percent_cost_change',
        'translated_text_instance_oid': 'translated_text_instance_oid',
        'value': 'value',
        'weight_change': 'weight_change',
        'weight_change_percent': 'weight_change_percent',
        'width': 'width'
    }

    def __init__(self, additional_dimension_application=None, additional_items=None, cost_change=None, default_value=None, digital_items=None, height=None, length=None, merchant_item_multimedia_oid=None, option_value_oid=None, percent_cost_change=None, translated_text_instance_oid=None, value=None, weight_change=None, weight_change_percent=None, width=None):
        """
        ItemOptionValue - a model defined in Swagger
        """

        self._additional_dimension_application = None
        self._additional_items = None
        self._cost_change = None
        self._default_value = None
        self._digital_items = None
        self._height = None
        self._length = None
        self._merchant_item_multimedia_oid = None
        self._option_value_oid = None
        self._percent_cost_change = None
        self._translated_text_instance_oid = None
        self._value = None
        self._weight_change = None
        self._weight_change_percent = None
        self._width = None
        self.discriminator = None

        if additional_dimension_application is not None:
          self.additional_dimension_application = additional_dimension_application
        if additional_items is not None:
          self.additional_items = additional_items
        if cost_change is not None:
          self.cost_change = cost_change
        if default_value is not None:
          self.default_value = default_value
        if digital_items is not None:
          self.digital_items = digital_items
        if height is not None:
          self.height = height
        if length is not None:
          self.length = length
        if merchant_item_multimedia_oid is not None:
          self.merchant_item_multimedia_oid = merchant_item_multimedia_oid
        if option_value_oid is not None:
          self.option_value_oid = option_value_oid
        if percent_cost_change is not None:
          self.percent_cost_change = percent_cost_change
        if translated_text_instance_oid is not None:
          self.translated_text_instance_oid = translated_text_instance_oid
        if value is not None:
          self.value = value
        if weight_change is not None:
          self.weight_change = weight_change
        if weight_change_percent is not None:
          self.weight_change_percent = weight_change_percent
        if width is not None:
          self.width = width

    @property
    def additional_dimension_application(self):
        """
        Gets the additional_dimension_application of this ItemOptionValue.
        Additional dimensions application

        :return: The additional_dimension_application of this ItemOptionValue.
        :rtype: str
        """
        return self._additional_dimension_application

    @additional_dimension_application.setter
    def additional_dimension_application(self, additional_dimension_application):
        """
        Sets the additional_dimension_application of this ItemOptionValue.
        Additional dimensions application

        :param additional_dimension_application: The additional_dimension_application of this ItemOptionValue.
        :type: str
        """
        allowed_values = ["none", "set item to", "add item"]
        if additional_dimension_application not in allowed_values:
            raise ValueError(
                "Invalid value for `additional_dimension_application` ({0}), must be one of {1}"
                .format(additional_dimension_application, allowed_values)
            )

        self._additional_dimension_application = additional_dimension_application

    @property
    def additional_items(self):
        """
        Gets the additional_items of this ItemOptionValue.
        Additional items to add to the order if this value is selected

        :return: The additional_items of this ItemOptionValue.
        :rtype: list[ItemOptionValueAdditionalItem]
        """
        return self._additional_items

    @additional_items.setter
    def additional_items(self, additional_items):
        """
        Sets the additional_items of this ItemOptionValue.
        Additional items to add to the order if this value is selected

        :param additional_items: The additional_items of this ItemOptionValue.
        :type: list[ItemOptionValueAdditionalItem]
        """

        self._additional_items = additional_items

    @property
    def cost_change(self):
        """
        Gets the cost_change of this ItemOptionValue.
        Cost change

        :return: The cost_change of this ItemOptionValue.
        :rtype: float
        """
        return self._cost_change

    @cost_change.setter
    def cost_change(self, cost_change):
        """
        Sets the cost_change of this ItemOptionValue.
        Cost change

        :param cost_change: The cost_change of this ItemOptionValue.
        :type: float
        """

        self._cost_change = cost_change

    @property
    def default_value(self):
        """
        Gets the default_value of this ItemOptionValue.
        True if default value

        :return: The default_value of this ItemOptionValue.
        :rtype: bool
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ItemOptionValue.
        True if default value

        :param default_value: The default_value of this ItemOptionValue.
        :type: bool
        """

        self._default_value = default_value

    @property
    def digital_items(self):
        """
        Gets the digital_items of this ItemOptionValue.
        Digital items to allow the customer to download if this option value is selected

        :return: The digital_items of this ItemOptionValue.
        :rtype: list[ItemOptionValueDigitalItem]
        """
        return self._digital_items

    @digital_items.setter
    def digital_items(self, digital_items):
        """
        Sets the digital_items of this ItemOptionValue.
        Digital items to allow the customer to download if this option value is selected

        :param digital_items: The digital_items of this ItemOptionValue.
        :type: list[ItemOptionValueDigitalItem]
        """

        self._digital_items = digital_items

    @property
    def height(self):
        """
        Gets the height of this ItemOptionValue.

        :return: The height of this ItemOptionValue.
        :rtype: Distance
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ItemOptionValue.

        :param height: The height of this ItemOptionValue.
        :type: Distance
        """

        self._height = height

    @property
    def length(self):
        """
        Gets the length of this ItemOptionValue.

        :return: The length of this ItemOptionValue.
        :rtype: Distance
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this ItemOptionValue.

        :param length: The length of this ItemOptionValue.
        :type: Distance
        """

        self._length = length

    @property
    def merchant_item_multimedia_oid(self):
        """
        Gets the merchant_item_multimedia_oid of this ItemOptionValue.
        Multimedia object identifier associated with this option value

        :return: The merchant_item_multimedia_oid of this ItemOptionValue.
        :rtype: int
        """
        return self._merchant_item_multimedia_oid

    @merchant_item_multimedia_oid.setter
    def merchant_item_multimedia_oid(self, merchant_item_multimedia_oid):
        """
        Sets the merchant_item_multimedia_oid of this ItemOptionValue.
        Multimedia object identifier associated with this option value

        :param merchant_item_multimedia_oid: The merchant_item_multimedia_oid of this ItemOptionValue.
        :type: int
        """

        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid

    @property
    def option_value_oid(self):
        """
        Gets the option_value_oid of this ItemOptionValue.
        Option value object identifier

        :return: The option_value_oid of this ItemOptionValue.
        :rtype: int
        """
        return self._option_value_oid

    @option_value_oid.setter
    def option_value_oid(self, option_value_oid):
        """
        Sets the option_value_oid of this ItemOptionValue.
        Option value object identifier

        :param option_value_oid: The option_value_oid of this ItemOptionValue.
        :type: int
        """

        self._option_value_oid = option_value_oid

    @property
    def percent_cost_change(self):
        """
        Gets the percent_cost_change of this ItemOptionValue.
        Percentage cost change

        :return: The percent_cost_change of this ItemOptionValue.
        :rtype: float
        """
        return self._percent_cost_change

    @percent_cost_change.setter
    def percent_cost_change(self, percent_cost_change):
        """
        Sets the percent_cost_change of this ItemOptionValue.
        Percentage cost change

        :param percent_cost_change: The percent_cost_change of this ItemOptionValue.
        :type: float
        """

        self._percent_cost_change = percent_cost_change

    @property
    def translated_text_instance_oid(self):
        """
        Gets the translated_text_instance_oid of this ItemOptionValue.
        Translated text instance id

        :return: The translated_text_instance_oid of this ItemOptionValue.
        :rtype: int
        """
        return self._translated_text_instance_oid

    @translated_text_instance_oid.setter
    def translated_text_instance_oid(self, translated_text_instance_oid):
        """
        Sets the translated_text_instance_oid of this ItemOptionValue.
        Translated text instance id

        :param translated_text_instance_oid: The translated_text_instance_oid of this ItemOptionValue.
        :type: int
        """

        self._translated_text_instance_oid = translated_text_instance_oid

    @property
    def value(self):
        """
        Gets the value of this ItemOptionValue.
        Value

        :return: The value of this ItemOptionValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ItemOptionValue.
        Value

        :param value: The value of this ItemOptionValue.
        :type: str
        """
        if value is not None and len(value) > 1024:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `1024`")

        self._value = value

    @property
    def weight_change(self):
        """
        Gets the weight_change of this ItemOptionValue.

        :return: The weight_change of this ItemOptionValue.
        :rtype: Weight
        """
        return self._weight_change

    @weight_change.setter
    def weight_change(self, weight_change):
        """
        Sets the weight_change of this ItemOptionValue.

        :param weight_change: The weight_change of this ItemOptionValue.
        :type: Weight
        """

        self._weight_change = weight_change

    @property
    def weight_change_percent(self):
        """
        Gets the weight_change_percent of this ItemOptionValue.
        Percentage weight change

        :return: The weight_change_percent of this ItemOptionValue.
        :rtype: float
        """
        return self._weight_change_percent

    @weight_change_percent.setter
    def weight_change_percent(self, weight_change_percent):
        """
        Sets the weight_change_percent of this ItemOptionValue.
        Percentage weight change

        :param weight_change_percent: The weight_change_percent of this ItemOptionValue.
        :type: float
        """

        self._weight_change_percent = weight_change_percent

    @property
    def width(self):
        """
        Gets the width of this ItemOptionValue.

        :return: The width of this ItemOptionValue.
        :rtype: Distance
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ItemOptionValue.

        :param width: The width of this ItemOptionValue.
        :type: Distance
        """

        self._width = width

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
        if not isinstance(other, ItemOptionValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

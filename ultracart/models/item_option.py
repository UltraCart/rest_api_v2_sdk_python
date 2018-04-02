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


class ItemOption(object):
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
        'cost_if_specified': 'float',
        'cost_per_letter': 'float',
        'cost_per_line': 'float',
        'ignore_if_default': 'bool',
        'label': 'str',
        'label_translated_text_instance_oid': 'int',
        'name': 'str',
        'name_translated_text_instance_oid': 'int',
        'one_time_fee': 'bool',
        'option_oid': 'int',
        'required': 'bool',
        'system_option': 'bool',
        'type': 'str',
        'values': 'list[ItemOptionValue]'
    }

    attribute_map = {
        'cost_if_specified': 'cost_if_specified',
        'cost_per_letter': 'cost_per_letter',
        'cost_per_line': 'cost_per_line',
        'ignore_if_default': 'ignore_if_default',
        'label': 'label',
        'label_translated_text_instance_oid': 'label_translated_text_instance_oid',
        'name': 'name',
        'name_translated_text_instance_oid': 'name_translated_text_instance_oid',
        'one_time_fee': 'one_time_fee',
        'option_oid': 'option_oid',
        'required': 'required',
        'system_option': 'system_option',
        'type': 'type',
        'values': 'values'
    }

    def __init__(self, cost_if_specified=None, cost_per_letter=None, cost_per_line=None, ignore_if_default=None, label=None, label_translated_text_instance_oid=None, name=None, name_translated_text_instance_oid=None, one_time_fee=None, option_oid=None, required=None, system_option=None, type=None, values=None):
        """
        ItemOption - a model defined in Swagger
        """

        self._cost_if_specified = None
        self._cost_per_letter = None
        self._cost_per_line = None
        self._ignore_if_default = None
        self._label = None
        self._label_translated_text_instance_oid = None
        self._name = None
        self._name_translated_text_instance_oid = None
        self._one_time_fee = None
        self._option_oid = None
        self._required = None
        self._system_option = None
        self._type = None
        self._values = None
        self.discriminator = None

        if cost_if_specified is not None:
          self.cost_if_specified = cost_if_specified
        if cost_per_letter is not None:
          self.cost_per_letter = cost_per_letter
        if cost_per_line is not None:
          self.cost_per_line = cost_per_line
        if ignore_if_default is not None:
          self.ignore_if_default = ignore_if_default
        if label is not None:
          self.label = label
        if label_translated_text_instance_oid is not None:
          self.label_translated_text_instance_oid = label_translated_text_instance_oid
        if name is not None:
          self.name = name
        if name_translated_text_instance_oid is not None:
          self.name_translated_text_instance_oid = name_translated_text_instance_oid
        if one_time_fee is not None:
          self.one_time_fee = one_time_fee
        if option_oid is not None:
          self.option_oid = option_oid
        if required is not None:
          self.required = required
        if system_option is not None:
          self.system_option = system_option
        if type is not None:
          self.type = type
        if values is not None:
          self.values = values

    @property
    def cost_if_specified(self):
        """
        Gets the cost_if_specified of this ItemOption.
        Cost if specified

        :return: The cost_if_specified of this ItemOption.
        :rtype: float
        """
        return self._cost_if_specified

    @cost_if_specified.setter
    def cost_if_specified(self, cost_if_specified):
        """
        Sets the cost_if_specified of this ItemOption.
        Cost if specified

        :param cost_if_specified: The cost_if_specified of this ItemOption.
        :type: float
        """

        self._cost_if_specified = cost_if_specified

    @property
    def cost_per_letter(self):
        """
        Gets the cost_per_letter of this ItemOption.
        Cost per letter

        :return: The cost_per_letter of this ItemOption.
        :rtype: float
        """
        return self._cost_per_letter

    @cost_per_letter.setter
    def cost_per_letter(self, cost_per_letter):
        """
        Sets the cost_per_letter of this ItemOption.
        Cost per letter

        :param cost_per_letter: The cost_per_letter of this ItemOption.
        :type: float
        """

        self._cost_per_letter = cost_per_letter

    @property
    def cost_per_line(self):
        """
        Gets the cost_per_line of this ItemOption.
        Cost per line

        :return: The cost_per_line of this ItemOption.
        :rtype: float
        """
        return self._cost_per_line

    @cost_per_line.setter
    def cost_per_line(self, cost_per_line):
        """
        Sets the cost_per_line of this ItemOption.
        Cost per line

        :param cost_per_line: The cost_per_line of this ItemOption.
        :type: float
        """

        self._cost_per_line = cost_per_line

    @property
    def ignore_if_default(self):
        """
        Gets the ignore_if_default of this ItemOption.
        Ignore this option on the order if the default value is selected

        :return: The ignore_if_default of this ItemOption.
        :rtype: bool
        """
        return self._ignore_if_default

    @ignore_if_default.setter
    def ignore_if_default(self, ignore_if_default):
        """
        Sets the ignore_if_default of this ItemOption.
        Ignore this option on the order if the default value is selected

        :param ignore_if_default: The ignore_if_default of this ItemOption.
        :type: bool
        """

        self._ignore_if_default = ignore_if_default

    @property
    def label(self):
        """
        Gets the label of this ItemOption.
        Label

        :return: The label of this ItemOption.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ItemOption.
        Label

        :param label: The label of this ItemOption.
        :type: str
        """
        if label is not None and len(label) > 50:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `50`")

        self._label = label

    @property
    def label_translated_text_instance_oid(self):
        """
        Gets the label_translated_text_instance_oid of this ItemOption.
        Label translated text instance ID

        :return: The label_translated_text_instance_oid of this ItemOption.
        :rtype: int
        """
        return self._label_translated_text_instance_oid

    @label_translated_text_instance_oid.setter
    def label_translated_text_instance_oid(self, label_translated_text_instance_oid):
        """
        Sets the label_translated_text_instance_oid of this ItemOption.
        Label translated text instance ID

        :param label_translated_text_instance_oid: The label_translated_text_instance_oid of this ItemOption.
        :type: int
        """

        self._label_translated_text_instance_oid = label_translated_text_instance_oid

    @property
    def name(self):
        """
        Gets the name of this ItemOption.
        Name

        :return: The name of this ItemOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ItemOption.
        Name

        :param name: The name of this ItemOption.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name

    @property
    def name_translated_text_instance_oid(self):
        """
        Gets the name_translated_text_instance_oid of this ItemOption.
        Name translated text instance ID

        :return: The name_translated_text_instance_oid of this ItemOption.
        :rtype: int
        """
        return self._name_translated_text_instance_oid

    @name_translated_text_instance_oid.setter
    def name_translated_text_instance_oid(self, name_translated_text_instance_oid):
        """
        Sets the name_translated_text_instance_oid of this ItemOption.
        Name translated text instance ID

        :param name_translated_text_instance_oid: The name_translated_text_instance_oid of this ItemOption.
        :type: int
        """

        self._name_translated_text_instance_oid = name_translated_text_instance_oid

    @property
    def one_time_fee(self):
        """
        Gets the one_time_fee of this ItemOption.
        One time fee

        :return: The one_time_fee of this ItemOption.
        :rtype: bool
        """
        return self._one_time_fee

    @one_time_fee.setter
    def one_time_fee(self, one_time_fee):
        """
        Sets the one_time_fee of this ItemOption.
        One time fee

        :param one_time_fee: The one_time_fee of this ItemOption.
        :type: bool
        """

        self._one_time_fee = one_time_fee

    @property
    def option_oid(self):
        """
        Gets the option_oid of this ItemOption.
        Option object identifier

        :return: The option_oid of this ItemOption.
        :rtype: int
        """
        return self._option_oid

    @option_oid.setter
    def option_oid(self, option_oid):
        """
        Sets the option_oid of this ItemOption.
        Option object identifier

        :param option_oid: The option_oid of this ItemOption.
        :type: int
        """

        self._option_oid = option_oid

    @property
    def required(self):
        """
        Gets the required of this ItemOption.
        True if the customer is required to specify an answer

        :return: The required of this ItemOption.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ItemOption.
        True if the customer is required to specify an answer

        :param required: The required of this ItemOption.
        :type: bool
        """

        self._required = required

    @property
    def system_option(self):
        """
        Gets the system_option of this ItemOption.
        True if this is a system option

        :return: The system_option of this ItemOption.
        :rtype: bool
        """
        return self._system_option

    @system_option.setter
    def system_option(self, system_option):
        """
        Sets the system_option of this ItemOption.
        True if this is a system option

        :param system_option: The system_option of this ItemOption.
        :type: bool
        """

        self._system_option = system_option

    @property
    def type(self):
        """
        Gets the type of this ItemOption.
        Type of option

        :return: The type of this ItemOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemOption.
        Type of option

        :param type: The type of this ItemOption.
        :type: str
        """
        allowed_values = ["dropdown", "file attachment", "fixed", "hidden", "multiline", "radio", "single"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def values(self):
        """
        Gets the values of this ItemOption.
        Values

        :return: The values of this ItemOption.
        :rtype: list[ItemOptionValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this ItemOption.
        Values

        :param values: The values of this ItemOption.
        :type: list[ItemOptionValue]
        """

        self._values = values

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
        if not isinstance(other, ItemOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

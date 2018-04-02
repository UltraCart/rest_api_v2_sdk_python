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


class Weight(object):
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
        'uom': 'str',
        'value': 'float'
    }

    attribute_map = {
        'uom': 'uom',
        'value': 'value'
    }

    def __init__(self, uom=None, value=None):
        """
        Weight - a model defined in Swagger
        """

        self._uom = None
        self._value = None
        self.discriminator = None

        if uom is not None:
          self.uom = uom
        if value is not None:
          self.value = value

    @property
    def uom(self):
        """
        Gets the uom of this Weight.
        Unit of measure

        :return: The uom of this Weight.
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """
        Sets the uom of this Weight.
        Unit of measure

        :param uom: The uom of this Weight.
        :type: str
        """
        allowed_values = ["KG", "LB", "OZ"]
        if uom not in allowed_values:
            raise ValueError(
                "Invalid value for `uom` ({0}), must be one of {1}"
                .format(uom, allowed_values)
            )

        self._uom = uom

    @property
    def value(self):
        """
        Gets the value of this Weight.
        Weight

        :return: The value of this Weight.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Weight.
        Weight

        :param value: The value of this Weight.
        :type: float
        """

        self._value = value

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
        if not isinstance(other, Weight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

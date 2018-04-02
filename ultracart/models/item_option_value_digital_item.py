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


class ItemOptionValueDigitalItem(object):
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
        'digital_item_oid': 'int',
        'original_filename': 'str'
    }

    attribute_map = {
        'digital_item_oid': 'digital_item_oid',
        'original_filename': 'original_filename'
    }

    def __init__(self, digital_item_oid=None, original_filename=None):
        """
        ItemOptionValueDigitalItem - a model defined in Swagger
        """

        self._digital_item_oid = None
        self._original_filename = None
        self.discriminator = None

        if digital_item_oid is not None:
          self.digital_item_oid = digital_item_oid
        if original_filename is not None:
          self.original_filename = original_filename

    @property
    def digital_item_oid(self):
        """
        Gets the digital_item_oid of this ItemOptionValueDigitalItem.
        Digital item object identifier

        :return: The digital_item_oid of this ItemOptionValueDigitalItem.
        :rtype: int
        """
        return self._digital_item_oid

    @digital_item_oid.setter
    def digital_item_oid(self, digital_item_oid):
        """
        Sets the digital_item_oid of this ItemOptionValueDigitalItem.
        Digital item object identifier

        :param digital_item_oid: The digital_item_oid of this ItemOptionValueDigitalItem.
        :type: int
        """

        self._digital_item_oid = digital_item_oid

    @property
    def original_filename(self):
        """
        Gets the original_filename of this ItemOptionValueDigitalItem.
        Original filename

        :return: The original_filename of this ItemOptionValueDigitalItem.
        :rtype: str
        """
        return self._original_filename

    @original_filename.setter
    def original_filename(self, original_filename):
        """
        Sets the original_filename of this ItemOptionValueDigitalItem.
        Original filename

        :param original_filename: The original_filename of this ItemOptionValueDigitalItem.
        :type: str
        """

        self._original_filename = original_filename

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
        if not isinstance(other, ItemOptionValueDigitalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

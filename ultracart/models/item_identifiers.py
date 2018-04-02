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


class ItemIdentifiers(object):
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
        'barcode': 'str',
        'manufacturer_name': 'str',
        'manufacturer_sku': 'str',
        'unspsc': 'str'
    }

    attribute_map = {
        'barcode': 'barcode',
        'manufacturer_name': 'manufacturer_name',
        'manufacturer_sku': 'manufacturer_sku',
        'unspsc': 'unspsc'
    }

    def __init__(self, barcode=None, manufacturer_name=None, manufacturer_sku=None, unspsc=None):
        """
        ItemIdentifiers - a model defined in Swagger
        """

        self._barcode = None
        self._manufacturer_name = None
        self._manufacturer_sku = None
        self._unspsc = None
        self.discriminator = None

        if barcode is not None:
          self.barcode = barcode
        if manufacturer_name is not None:
          self.manufacturer_name = manufacturer_name
        if manufacturer_sku is not None:
          self.manufacturer_sku = manufacturer_sku
        if unspsc is not None:
          self.unspsc = unspsc

    @property
    def barcode(self):
        """
        Gets the barcode of this ItemIdentifiers.
        Barcode

        :return: The barcode of this ItemIdentifiers.
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """
        Sets the barcode of this ItemIdentifiers.
        Barcode

        :param barcode: The barcode of this ItemIdentifiers.
        :type: str
        """
        if barcode is not None and len(barcode) > 30:
            raise ValueError("Invalid value for `barcode`, length must be less than or equal to `30`")

        self._barcode = barcode

    @property
    def manufacturer_name(self):
        """
        Gets the manufacturer_name of this ItemIdentifiers.
        Manufacturer Name

        :return: The manufacturer_name of this ItemIdentifiers.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """
        Sets the manufacturer_name of this ItemIdentifiers.
        Manufacturer Name

        :param manufacturer_name: The manufacturer_name of this ItemIdentifiers.
        :type: str
        """
        if manufacturer_name is not None and len(manufacturer_name) > 50:
            raise ValueError("Invalid value for `manufacturer_name`, length must be less than or equal to `50`")

        self._manufacturer_name = manufacturer_name

    @property
    def manufacturer_sku(self):
        """
        Gets the manufacturer_sku of this ItemIdentifiers.
        Manufacturer SKU

        :return: The manufacturer_sku of this ItemIdentifiers.
        :rtype: str
        """
        return self._manufacturer_sku

    @manufacturer_sku.setter
    def manufacturer_sku(self, manufacturer_sku):
        """
        Sets the manufacturer_sku of this ItemIdentifiers.
        Manufacturer SKU

        :param manufacturer_sku: The manufacturer_sku of this ItemIdentifiers.
        :type: str
        """
        if manufacturer_sku is not None and len(manufacturer_sku) > 25:
            raise ValueError("Invalid value for `manufacturer_sku`, length must be less than or equal to `25`")

        self._manufacturer_sku = manufacturer_sku

    @property
    def unspsc(self):
        """
        Gets the unspsc of this ItemIdentifiers.
        UNSPSC

        :return: The unspsc of this ItemIdentifiers.
        :rtype: str
        """
        return self._unspsc

    @unspsc.setter
    def unspsc(self, unspsc):
        """
        Sets the unspsc of this ItemIdentifiers.
        UNSPSC

        :param unspsc: The unspsc of this ItemIdentifiers.
        :type: str
        """
        if unspsc is not None and len(unspsc) > 20:
            raise ValueError("Invalid value for `unspsc`, length must be less than or equal to `20`")

        self._unspsc = unspsc

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
        if not isinstance(other, ItemIdentifiers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

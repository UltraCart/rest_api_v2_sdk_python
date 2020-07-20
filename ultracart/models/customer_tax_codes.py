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


class CustomerTaxCodes(object):
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
        'avalara_customer_code': 'str',
        'avalara_entity_use_code': 'str',
        'sovos_customer_code': 'str',
        'taxjar_customer_id': 'str'
    }

    attribute_map = {
        'avalara_customer_code': 'avalara_customer_code',
        'avalara_entity_use_code': 'avalara_entity_use_code',
        'sovos_customer_code': 'sovos_customer_code',
        'taxjar_customer_id': 'taxjar_customer_id'
    }

    def __init__(self, avalara_customer_code=None, avalara_entity_use_code=None, sovos_customer_code=None, taxjar_customer_id=None):
        """
        CustomerTaxCodes - a model defined in Swagger
        """

        self._avalara_customer_code = None
        self._avalara_entity_use_code = None
        self._sovos_customer_code = None
        self._taxjar_customer_id = None
        self.discriminator = None

        if avalara_customer_code is not None:
          self.avalara_customer_code = avalara_customer_code
        if avalara_entity_use_code is not None:
          self.avalara_entity_use_code = avalara_entity_use_code
        if sovos_customer_code is not None:
          self.sovos_customer_code = sovos_customer_code
        if taxjar_customer_id is not None:
          self.taxjar_customer_id = taxjar_customer_id

    @property
    def avalara_customer_code(self):
        """
        Gets the avalara_customer_code of this CustomerTaxCodes.
        Avalara customer code

        :return: The avalara_customer_code of this CustomerTaxCodes.
        :rtype: str
        """
        return self._avalara_customer_code

    @avalara_customer_code.setter
    def avalara_customer_code(self, avalara_customer_code):
        """
        Sets the avalara_customer_code of this CustomerTaxCodes.
        Avalara customer code

        :param avalara_customer_code: The avalara_customer_code of this CustomerTaxCodes.
        :type: str
        """

        self._avalara_customer_code = avalara_customer_code

    @property
    def avalara_entity_use_code(self):
        """
        Gets the avalara_entity_use_code of this CustomerTaxCodes.
        Avalara entity use code

        :return: The avalara_entity_use_code of this CustomerTaxCodes.
        :rtype: str
        """
        return self._avalara_entity_use_code

    @avalara_entity_use_code.setter
    def avalara_entity_use_code(self, avalara_entity_use_code):
        """
        Sets the avalara_entity_use_code of this CustomerTaxCodes.
        Avalara entity use code

        :param avalara_entity_use_code: The avalara_entity_use_code of this CustomerTaxCodes.
        :type: str
        """

        self._avalara_entity_use_code = avalara_entity_use_code

    @property
    def sovos_customer_code(self):
        """
        Gets the sovos_customer_code of this CustomerTaxCodes.
        Sovos customer code

        :return: The sovos_customer_code of this CustomerTaxCodes.
        :rtype: str
        """
        return self._sovos_customer_code

    @sovos_customer_code.setter
    def sovos_customer_code(self, sovos_customer_code):
        """
        Sets the sovos_customer_code of this CustomerTaxCodes.
        Sovos customer code

        :param sovos_customer_code: The sovos_customer_code of this CustomerTaxCodes.
        :type: str
        """

        self._sovos_customer_code = sovos_customer_code

    @property
    def taxjar_customer_id(self):
        """
        Gets the taxjar_customer_id of this CustomerTaxCodes.
        TaxJar customer id

        :return: The taxjar_customer_id of this CustomerTaxCodes.
        :rtype: str
        """
        return self._taxjar_customer_id

    @taxjar_customer_id.setter
    def taxjar_customer_id(self, taxjar_customer_id):
        """
        Sets the taxjar_customer_id of this CustomerTaxCodes.
        TaxJar customer id

        :param taxjar_customer_id: The taxjar_customer_id of this CustomerTaxCodes.
        :type: str
        """

        self._taxjar_customer_id = taxjar_customer_id

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
        if not isinstance(other, CustomerTaxCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

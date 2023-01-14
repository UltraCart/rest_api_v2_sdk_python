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


class PointOfSaleLocation(object):
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
        'adddress2': 'str',
        'address1': 'str',
        'city': 'str',
        'country': 'str',
        'distribution_center_code': 'str',
        'external_id': 'str',
        'merchant_id': 'str',
        'pos_location_oid': 'int',
        'postal_code': 'str',
        'state_province': 'str'
    }

    attribute_map = {
        'adddress2': 'adddress2',
        'address1': 'address1',
        'city': 'city',
        'country': 'country',
        'distribution_center_code': 'distribution_center_code',
        'external_id': 'external_id',
        'merchant_id': 'merchant_id',
        'pos_location_oid': 'pos_location_oid',
        'postal_code': 'postal_code',
        'state_province': 'state_province'
    }

    def __init__(self, adddress2=None, address1=None, city=None, country=None, distribution_center_code=None, external_id=None, merchant_id=None, pos_location_oid=None, postal_code=None, state_province=None):  # noqa: E501
        """PointOfSaleLocation - a model defined in Swagger"""  # noqa: E501

        self._adddress2 = None
        self._address1 = None
        self._city = None
        self._country = None
        self._distribution_center_code = None
        self._external_id = None
        self._merchant_id = None
        self._pos_location_oid = None
        self._postal_code = None
        self._state_province = None
        self.discriminator = None

        if adddress2 is not None:
            self.adddress2 = adddress2
        if address1 is not None:
            self.address1 = address1
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if distribution_center_code is not None:
            self.distribution_center_code = distribution_center_code
        if external_id is not None:
            self.external_id = external_id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if pos_location_oid is not None:
            self.pos_location_oid = pos_location_oid
        if postal_code is not None:
            self.postal_code = postal_code
        if state_province is not None:
            self.state_province = state_province

    @property
    def adddress2(self):
        """Gets the adddress2 of this PointOfSaleLocation.  # noqa: E501

        Address line 2  # noqa: E501

        :return: The adddress2 of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._adddress2

    @adddress2.setter
    def adddress2(self, adddress2):
        """Sets the adddress2 of this PointOfSaleLocation.

        Address line 2  # noqa: E501

        :param adddress2: The adddress2 of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._adddress2 = adddress2

    @property
    def address1(self):
        """Gets the address1 of this PointOfSaleLocation.  # noqa: E501

        Address line 1  # noqa: E501

        :return: The address1 of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this PointOfSaleLocation.

        Address line 1  # noqa: E501

        :param address1: The address1 of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def city(self):
        """Gets the city of this PointOfSaleLocation.  # noqa: E501

        City  # noqa: E501

        :return: The city of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PointOfSaleLocation.

        City  # noqa: E501

        :param city: The city of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this PointOfSaleLocation.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PointOfSaleLocation.

        Country  # noqa: E501

        :param country: The country of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def distribution_center_code(self):
        """Gets the distribution_center_code of this PointOfSaleLocation.  # noqa: E501

        The distribution center code where inventory is reduced from for this sale.  # noqa: E501

        :return: The distribution_center_code of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._distribution_center_code

    @distribution_center_code.setter
    def distribution_center_code(self, distribution_center_code):
        """Sets the distribution_center_code of this PointOfSaleLocation.

        The distribution center code where inventory is reduced from for this sale.  # noqa: E501

        :param distribution_center_code: The distribution_center_code of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._distribution_center_code = distribution_center_code

    @property
    def external_id(self):
        """Gets the external_id of this PointOfSaleLocation.  # noqa: E501

        External Id useful for syncing with a remote filesystem, this may be an MD5 hash or whatever suits your needs.  # noqa: E501

        :return: The external_id of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PointOfSaleLocation.

        External Id useful for syncing with a remote filesystem, this may be an MD5 hash or whatever suits your needs.  # noqa: E501

        :param external_id: The external_id of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")  # noqa: E501

        self._external_id = external_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this PointOfSaleLocation.  # noqa: E501

        Merchant ID that owns this location  # noqa: E501

        :return: The merchant_id of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this PointOfSaleLocation.

        Merchant ID that owns this location  # noqa: E501

        :param merchant_id: The merchant_id of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def pos_location_oid(self):
        """Gets the pos_location_oid of this PointOfSaleLocation.  # noqa: E501

        Object identifier of the point of sale location.  # noqa: E501

        :return: The pos_location_oid of this PointOfSaleLocation.  # noqa: E501
        :rtype: int
        """
        return self._pos_location_oid

    @pos_location_oid.setter
    def pos_location_oid(self, pos_location_oid):
        """Sets the pos_location_oid of this PointOfSaleLocation.

        Object identifier of the point of sale location.  # noqa: E501

        :param pos_location_oid: The pos_location_oid of this PointOfSaleLocation.  # noqa: E501
        :type: int
        """

        self._pos_location_oid = pos_location_oid

    @property
    def postal_code(self):
        """Gets the postal_code of this PointOfSaleLocation.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PointOfSaleLocation.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_province(self):
        """Gets the state_province of this PointOfSaleLocation.  # noqa: E501

        State/province  # noqa: E501

        :return: The state_province of this PointOfSaleLocation.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this PointOfSaleLocation.

        State/province  # noqa: E501

        :param state_province: The state_province of this PointOfSaleLocation.  # noqa: E501
        :type: str
        """

        self._state_province = state_province

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
        if issubclass(PointOfSaleLocation, dict):
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
        if not isinstance(other, PointOfSaleLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class TaxProvidersResponse(object):
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
        'avalara': 'TaxProviderAvalara',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        '_self': 'TaxProviderSelf',
        'sovos': 'TaxProviderSovos',
        'success': 'bool',
        'taxjar': 'TaxProviderTaxJar',
        'ultracart': 'TaxProviderUltraCart'
    }

    attribute_map = {
        'avalara': 'avalara',
        'error': 'error',
        'metadata': 'metadata',
        '_self': 'self',
        'sovos': 'sovos',
        'success': 'success',
        'taxjar': 'taxjar',
        'ultracart': 'ultracart'
    }

    def __init__(self, avalara=None, error=None, metadata=None, _self=None, sovos=None, success=None, taxjar=None, ultracart=None):  # noqa: E501
        """TaxProvidersResponse - a model defined in Swagger"""  # noqa: E501

        self._avalara = None
        self._error = None
        self._metadata = None
        self.__self = None
        self._sovos = None
        self._success = None
        self._taxjar = None
        self._ultracart = None
        self.discriminator = None

        if avalara is not None:
            self.avalara = avalara
        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if _self is not None:
            self._self = _self
        if sovos is not None:
            self.sovos = sovos
        if success is not None:
            self.success = success
        if taxjar is not None:
            self.taxjar = taxjar
        if ultracart is not None:
            self.ultracart = ultracart

    @property
    def avalara(self):
        """Gets the avalara of this TaxProvidersResponse.  # noqa: E501


        :return: The avalara of this TaxProvidersResponse.  # noqa: E501
        :rtype: TaxProviderAvalara
        """
        return self._avalara

    @avalara.setter
    def avalara(self, avalara):
        """Sets the avalara of this TaxProvidersResponse.


        :param avalara: The avalara of this TaxProvidersResponse.  # noqa: E501
        :type: TaxProviderAvalara
        """

        self._avalara = avalara

    @property
    def error(self):
        """Gets the error of this TaxProvidersResponse.  # noqa: E501


        :return: The error of this TaxProvidersResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TaxProvidersResponse.


        :param error: The error of this TaxProvidersResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this TaxProvidersResponse.  # noqa: E501


        :return: The metadata of this TaxProvidersResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TaxProvidersResponse.


        :param metadata: The metadata of this TaxProvidersResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def _self(self):
        """Gets the _self of this TaxProvidersResponse.  # noqa: E501


        :return: The _self of this TaxProvidersResponse.  # noqa: E501
        :rtype: TaxProviderSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this TaxProvidersResponse.


        :param _self: The _self of this TaxProvidersResponse.  # noqa: E501
        :type: TaxProviderSelf
        """

        self.__self = _self

    @property
    def sovos(self):
        """Gets the sovos of this TaxProvidersResponse.  # noqa: E501


        :return: The sovos of this TaxProvidersResponse.  # noqa: E501
        :rtype: TaxProviderSovos
        """
        return self._sovos

    @sovos.setter
    def sovos(self, sovos):
        """Sets the sovos of this TaxProvidersResponse.


        :param sovos: The sovos of this TaxProvidersResponse.  # noqa: E501
        :type: TaxProviderSovos
        """

        self._sovos = sovos

    @property
    def success(self):
        """Gets the success of this TaxProvidersResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this TaxProvidersResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TaxProvidersResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this TaxProvidersResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def taxjar(self):
        """Gets the taxjar of this TaxProvidersResponse.  # noqa: E501


        :return: The taxjar of this TaxProvidersResponse.  # noqa: E501
        :rtype: TaxProviderTaxJar
        """
        return self._taxjar

    @taxjar.setter
    def taxjar(self, taxjar):
        """Sets the taxjar of this TaxProvidersResponse.


        :param taxjar: The taxjar of this TaxProvidersResponse.  # noqa: E501
        :type: TaxProviderTaxJar
        """

        self._taxjar = taxjar

    @property
    def ultracart(self):
        """Gets the ultracart of this TaxProvidersResponse.  # noqa: E501


        :return: The ultracart of this TaxProvidersResponse.  # noqa: E501
        :rtype: TaxProviderUltraCart
        """
        return self._ultracart

    @ultracart.setter
    def ultracart(self, ultracart):
        """Sets the ultracart of this TaxProvidersResponse.


        :param ultracart: The ultracart of this TaxProvidersResponse.  # noqa: E501
        :type: TaxProviderUltraCart
        """

        self._ultracart = ultracart

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
        if issubclass(TaxProvidersResponse, dict):
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
        if not isinstance(other, TaxProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

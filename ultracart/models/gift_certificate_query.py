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


class GiftCertificateQuery(object):
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
        'code': 'str',
        'email': 'str',
        'expiration_dts_end': 'str',
        'expiration_dts_start': 'str',
        'original_balance_end': 'float',
        'original_balance_start': 'float',
        'reference_order_id': 'str',
        'remaining_balance_end': 'float',
        'remaining_balance_start': 'float'
    }

    attribute_map = {
        'code': 'code',
        'email': 'email',
        'expiration_dts_end': 'expiration_dts_end',
        'expiration_dts_start': 'expiration_dts_start',
        'original_balance_end': 'original_balance_end',
        'original_balance_start': 'original_balance_start',
        'reference_order_id': 'reference_order_id',
        'remaining_balance_end': 'remaining_balance_end',
        'remaining_balance_start': 'remaining_balance_start'
    }

    def __init__(self, code=None, email=None, expiration_dts_end=None, expiration_dts_start=None, original_balance_end=None, original_balance_start=None, reference_order_id=None, remaining_balance_end=None, remaining_balance_start=None):  # noqa: E501
        """GiftCertificateQuery - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._email = None
        self._expiration_dts_end = None
        self._expiration_dts_start = None
        self._original_balance_end = None
        self._original_balance_start = None
        self._reference_order_id = None
        self._remaining_balance_end = None
        self._remaining_balance_start = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if email is not None:
            self.email = email
        if expiration_dts_end is not None:
            self.expiration_dts_end = expiration_dts_end
        if expiration_dts_start is not None:
            self.expiration_dts_start = expiration_dts_start
        if original_balance_end is not None:
            self.original_balance_end = original_balance_end
        if original_balance_start is not None:
            self.original_balance_start = original_balance_start
        if reference_order_id is not None:
            self.reference_order_id = reference_order_id
        if remaining_balance_end is not None:
            self.remaining_balance_end = remaining_balance_end
        if remaining_balance_start is not None:
            self.remaining_balance_start = remaining_balance_start

    @property
    def code(self):
        """Gets the code of this GiftCertificateQuery.  # noqa: E501

        Gift certificate code  # noqa: E501

        :return: The code of this GiftCertificateQuery.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GiftCertificateQuery.

        Gift certificate code  # noqa: E501

        :param code: The code of this GiftCertificateQuery.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def email(self):
        """Gets the email of this GiftCertificateQuery.  # noqa: E501

        Email address of this gift certificate  # noqa: E501

        :return: The email of this GiftCertificateQuery.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GiftCertificateQuery.

        Email address of this gift certificate  # noqa: E501

        :param email: The email of this GiftCertificateQuery.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def expiration_dts_end(self):
        """Gets the expiration_dts_end of this GiftCertificateQuery.  # noqa: E501

        Expiration date end  # noqa: E501

        :return: The expiration_dts_end of this GiftCertificateQuery.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts_end

    @expiration_dts_end.setter
    def expiration_dts_end(self, expiration_dts_end):
        """Sets the expiration_dts_end of this GiftCertificateQuery.

        Expiration date end  # noqa: E501

        :param expiration_dts_end: The expiration_dts_end of this GiftCertificateQuery.  # noqa: E501
        :type: str
        """

        self._expiration_dts_end = expiration_dts_end

    @property
    def expiration_dts_start(self):
        """Gets the expiration_dts_start of this GiftCertificateQuery.  # noqa: E501

        Expiration date start  # noqa: E501

        :return: The expiration_dts_start of this GiftCertificateQuery.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts_start

    @expiration_dts_start.setter
    def expiration_dts_start(self, expiration_dts_start):
        """Sets the expiration_dts_start of this GiftCertificateQuery.

        Expiration date start  # noqa: E501

        :param expiration_dts_start: The expiration_dts_start of this GiftCertificateQuery.  # noqa: E501
        :type: str
        """

        self._expiration_dts_start = expiration_dts_start

    @property
    def original_balance_end(self):
        """Gets the original_balance_end of this GiftCertificateQuery.  # noqa: E501

        Original balance end  # noqa: E501

        :return: The original_balance_end of this GiftCertificateQuery.  # noqa: E501
        :rtype: float
        """
        return self._original_balance_end

    @original_balance_end.setter
    def original_balance_end(self, original_balance_end):
        """Sets the original_balance_end of this GiftCertificateQuery.

        Original balance end  # noqa: E501

        :param original_balance_end: The original_balance_end of this GiftCertificateQuery.  # noqa: E501
        :type: float
        """

        self._original_balance_end = original_balance_end

    @property
    def original_balance_start(self):
        """Gets the original_balance_start of this GiftCertificateQuery.  # noqa: E501

        Original balance start  # noqa: E501

        :return: The original_balance_start of this GiftCertificateQuery.  # noqa: E501
        :rtype: float
        """
        return self._original_balance_start

    @original_balance_start.setter
    def original_balance_start(self, original_balance_start):
        """Sets the original_balance_start of this GiftCertificateQuery.

        Original balance start  # noqa: E501

        :param original_balance_start: The original_balance_start of this GiftCertificateQuery.  # noqa: E501
        :type: float
        """

        self._original_balance_start = original_balance_start

    @property
    def reference_order_id(self):
        """Gets the reference_order_id of this GiftCertificateQuery.  # noqa: E501

        Gift certificate reference order id  # noqa: E501

        :return: The reference_order_id of this GiftCertificateQuery.  # noqa: E501
        :rtype: str
        """
        return self._reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, reference_order_id):
        """Sets the reference_order_id of this GiftCertificateQuery.

        Gift certificate reference order id  # noqa: E501

        :param reference_order_id: The reference_order_id of this GiftCertificateQuery.  # noqa: E501
        :type: str
        """

        self._reference_order_id = reference_order_id

    @property
    def remaining_balance_end(self):
        """Gets the remaining_balance_end of this GiftCertificateQuery.  # noqa: E501

        Remaining balance end  # noqa: E501

        :return: The remaining_balance_end of this GiftCertificateQuery.  # noqa: E501
        :rtype: float
        """
        return self._remaining_balance_end

    @remaining_balance_end.setter
    def remaining_balance_end(self, remaining_balance_end):
        """Sets the remaining_balance_end of this GiftCertificateQuery.

        Remaining balance end  # noqa: E501

        :param remaining_balance_end: The remaining_balance_end of this GiftCertificateQuery.  # noqa: E501
        :type: float
        """

        self._remaining_balance_end = remaining_balance_end

    @property
    def remaining_balance_start(self):
        """Gets the remaining_balance_start of this GiftCertificateQuery.  # noqa: E501

        Remaining balance start  # noqa: E501

        :return: The remaining_balance_start of this GiftCertificateQuery.  # noqa: E501
        :rtype: float
        """
        return self._remaining_balance_start

    @remaining_balance_start.setter
    def remaining_balance_start(self, remaining_balance_start):
        """Sets the remaining_balance_start of this GiftCertificateQuery.

        Remaining balance start  # noqa: E501

        :param remaining_balance_start: The remaining_balance_start of this GiftCertificateQuery.  # noqa: E501
        :type: float
        """

        self._remaining_balance_start = remaining_balance_start

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
        if issubclass(GiftCertificateQuery, dict):
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
        if not isinstance(other, GiftCertificateQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

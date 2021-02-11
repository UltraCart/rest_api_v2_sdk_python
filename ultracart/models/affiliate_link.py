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


class AffiliateLink(object):
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
        'affiliate_link_oid': 'int',
        'affiliate_managed_link_oid': 'int',
        'affiliate_oid': 'int',
        'affiliate_program_item_oid': 'int',
        'code': 'str',
        'creative_oid': 'int',
        'custom_html': 'str',
        'custom_html_approval_status': 'str',
        'custom_landing_url': 'str',
        'deleted': 'bool',
        'invisible_link_approval_status': 'str',
        'invisible_link_url_prefix': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'affiliate_link_oid': 'affiliate_link_oid',
        'affiliate_managed_link_oid': 'affiliate_managed_link_oid',
        'affiliate_oid': 'affiliate_oid',
        'affiliate_program_item_oid': 'affiliate_program_item_oid',
        'code': 'code',
        'creative_oid': 'creative_oid',
        'custom_html': 'custom_html',
        'custom_html_approval_status': 'custom_html_approval_status',
        'custom_landing_url': 'custom_landing_url',
        'deleted': 'deleted',
        'invisible_link_approval_status': 'invisible_link_approval_status',
        'invisible_link_url_prefix': 'invisible_link_url_prefix',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, affiliate_link_oid=None, affiliate_managed_link_oid=None, affiliate_oid=None, affiliate_program_item_oid=None, code=None, creative_oid=None, custom_html=None, custom_html_approval_status=None, custom_landing_url=None, deleted=None, invisible_link_approval_status=None, invisible_link_url_prefix=None, name=None, type=None):  # noqa: E501
        """AffiliateLink - a model defined in Swagger"""  # noqa: E501

        self._affiliate_link_oid = None
        self._affiliate_managed_link_oid = None
        self._affiliate_oid = None
        self._affiliate_program_item_oid = None
        self._code = None
        self._creative_oid = None
        self._custom_html = None
        self._custom_html_approval_status = None
        self._custom_landing_url = None
        self._deleted = None
        self._invisible_link_approval_status = None
        self._invisible_link_url_prefix = None
        self._name = None
        self._type = None
        self.discriminator = None

        if affiliate_link_oid is not None:
            self.affiliate_link_oid = affiliate_link_oid
        if affiliate_managed_link_oid is not None:
            self.affiliate_managed_link_oid = affiliate_managed_link_oid
        if affiliate_oid is not None:
            self.affiliate_oid = affiliate_oid
        if affiliate_program_item_oid is not None:
            self.affiliate_program_item_oid = affiliate_program_item_oid
        if code is not None:
            self.code = code
        if creative_oid is not None:
            self.creative_oid = creative_oid
        if custom_html is not None:
            self.custom_html = custom_html
        if custom_html_approval_status is not None:
            self.custom_html_approval_status = custom_html_approval_status
        if custom_landing_url is not None:
            self.custom_landing_url = custom_landing_url
        if deleted is not None:
            self.deleted = deleted
        if invisible_link_approval_status is not None:
            self.invisible_link_approval_status = invisible_link_approval_status
        if invisible_link_url_prefix is not None:
            self.invisible_link_url_prefix = invisible_link_url_prefix
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def affiliate_link_oid(self):
        """Gets the affiliate_link_oid of this AffiliateLink.  # noqa: E501

        Unique object identifier associated with this link  # noqa: E501

        :return: The affiliate_link_oid of this AffiliateLink.  # noqa: E501
        :rtype: int
        """
        return self._affiliate_link_oid

    @affiliate_link_oid.setter
    def affiliate_link_oid(self, affiliate_link_oid):
        """Sets the affiliate_link_oid of this AffiliateLink.

        Unique object identifier associated with this link  # noqa: E501

        :param affiliate_link_oid: The affiliate_link_oid of this AffiliateLink.  # noqa: E501
        :type: int
        """

        self._affiliate_link_oid = affiliate_link_oid

    @property
    def affiliate_managed_link_oid(self):
        """Gets the affiliate_managed_link_oid of this AffiliateLink.  # noqa: E501

        Managed link OID that this link object was generated from  # noqa: E501

        :return: The affiliate_managed_link_oid of this AffiliateLink.  # noqa: E501
        :rtype: int
        """
        return self._affiliate_managed_link_oid

    @affiliate_managed_link_oid.setter
    def affiliate_managed_link_oid(self, affiliate_managed_link_oid):
        """Sets the affiliate_managed_link_oid of this AffiliateLink.

        Managed link OID that this link object was generated from  # noqa: E501

        :param affiliate_managed_link_oid: The affiliate_managed_link_oid of this AffiliateLink.  # noqa: E501
        :type: int
        """

        self._affiliate_managed_link_oid = affiliate_managed_link_oid

    @property
    def affiliate_oid(self):
        """Gets the affiliate_oid of this AffiliateLink.  # noqa: E501

        Affiliate object ID associated with this link  # noqa: E501

        :return: The affiliate_oid of this AffiliateLink.  # noqa: E501
        :rtype: int
        """
        return self._affiliate_oid

    @affiliate_oid.setter
    def affiliate_oid(self, affiliate_oid):
        """Sets the affiliate_oid of this AffiliateLink.

        Affiliate object ID associated with this link  # noqa: E501

        :param affiliate_oid: The affiliate_oid of this AffiliateLink.  # noqa: E501
        :type: int
        """

        self._affiliate_oid = affiliate_oid

    @property
    def affiliate_program_item_oid(self):
        """Gets the affiliate_program_item_oid of this AffiliateLink.  # noqa: E501

        The affiliate program item this managed link is associated with  # noqa: E501

        :return: The affiliate_program_item_oid of this AffiliateLink.  # noqa: E501
        :rtype: int
        """
        return self._affiliate_program_item_oid

    @affiliate_program_item_oid.setter
    def affiliate_program_item_oid(self, affiliate_program_item_oid):
        """Sets the affiliate_program_item_oid of this AffiliateLink.

        The affiliate program item this managed link is associated with  # noqa: E501

        :param affiliate_program_item_oid: The affiliate_program_item_oid of this AffiliateLink.  # noqa: E501
        :type: int
        """

        self._affiliate_program_item_oid = affiliate_program_item_oid

    @property
    def code(self):
        """Gets the code of this AffiliateLink.  # noqa: E501

        Code associated with the link  # noqa: E501

        :return: The code of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AffiliateLink.

        Code associated with the link  # noqa: E501

        :param code: The code of this AffiliateLink.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def creative_oid(self):
        """Gets the creative_oid of this AffiliateLink.  # noqa: E501

        Creative (image or text) associated with this link  # noqa: E501

        :return: The creative_oid of this AffiliateLink.  # noqa: E501
        :rtype: int
        """
        return self._creative_oid

    @creative_oid.setter
    def creative_oid(self, creative_oid):
        """Sets the creative_oid of this AffiliateLink.

        Creative (image or text) associated with this link  # noqa: E501

        :param creative_oid: The creative_oid of this AffiliateLink.  # noqa: E501
        :type: int
        """

        self._creative_oid = creative_oid

    @property
    def custom_html(self):
        """Gets the custom_html of this AffiliateLink.  # noqa: E501

        Custom HTML associated with this link  # noqa: E501

        :return: The custom_html of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._custom_html

    @custom_html.setter
    def custom_html(self, custom_html):
        """Sets the custom_html of this AffiliateLink.

        Custom HTML associated with this link  # noqa: E501

        :param custom_html: The custom_html of this AffiliateLink.  # noqa: E501
        :type: str
        """

        self._custom_html = custom_html

    @property
    def custom_html_approval_status(self):
        """Gets the custom_html_approval_status of this AffiliateLink.  # noqa: E501

        Approved status of the custom html  # noqa: E501

        :return: The custom_html_approval_status of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._custom_html_approval_status

    @custom_html_approval_status.setter
    def custom_html_approval_status(self, custom_html_approval_status):
        """Sets the custom_html_approval_status of this AffiliateLink.

        Approved status of the custom html  # noqa: E501

        :param custom_html_approval_status: The custom_html_approval_status of this AffiliateLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Approved", "Rejected"]  # noqa: E501
        if custom_html_approval_status not in allowed_values:
            raise ValueError(
                "Invalid value for `custom_html_approval_status` ({0}), must be one of {1}"  # noqa: E501
                .format(custom_html_approval_status, allowed_values)
            )

        self._custom_html_approval_status = custom_html_approval_status

    @property
    def custom_landing_url(self):
        """Gets the custom_landing_url of this AffiliateLink.  # noqa: E501

        Custom landing page URL if configured  # noqa: E501

        :return: The custom_landing_url of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._custom_landing_url

    @custom_landing_url.setter
    def custom_landing_url(self, custom_landing_url):
        """Sets the custom_landing_url of this AffiliateLink.

        Custom landing page URL if configured  # noqa: E501

        :param custom_landing_url: The custom_landing_url of this AffiliateLink.  # noqa: E501
        :type: str
        """

        self._custom_landing_url = custom_landing_url

    @property
    def deleted(self):
        """Gets the deleted of this AffiliateLink.  # noqa: E501

        True if the link has been deleted  # noqa: E501

        :return: The deleted of this AffiliateLink.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AffiliateLink.

        True if the link has been deleted  # noqa: E501

        :param deleted: The deleted of this AffiliateLink.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def invisible_link_approval_status(self):
        """Gets the invisible_link_approval_status of this AffiliateLink.  # noqa: E501

        Invisible link approval status  # noqa: E501

        :return: The invisible_link_approval_status of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._invisible_link_approval_status

    @invisible_link_approval_status.setter
    def invisible_link_approval_status(self, invisible_link_approval_status):
        """Sets the invisible_link_approval_status of this AffiliateLink.

        Invisible link approval status  # noqa: E501

        :param invisible_link_approval_status: The invisible_link_approval_status of this AffiliateLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Approved", "Rejected"]  # noqa: E501
        if invisible_link_approval_status not in allowed_values:
            raise ValueError(
                "Invalid value for `invisible_link_approval_status` ({0}), must be one of {1}"  # noqa: E501
                .format(invisible_link_approval_status, allowed_values)
            )

        self._invisible_link_approval_status = invisible_link_approval_status

    @property
    def invisible_link_url_prefix(self):
        """Gets the invisible_link_url_prefix of this AffiliateLink.  # noqa: E501

        Invisible link URL prefix  # noqa: E501

        :return: The invisible_link_url_prefix of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._invisible_link_url_prefix

    @invisible_link_url_prefix.setter
    def invisible_link_url_prefix(self, invisible_link_url_prefix):
        """Sets the invisible_link_url_prefix of this AffiliateLink.

        Invisible link URL prefix  # noqa: E501

        :param invisible_link_url_prefix: The invisible_link_url_prefix of this AffiliateLink.  # noqa: E501
        :type: str
        """

        self._invisible_link_url_prefix = invisible_link_url_prefix

    @property
    def name(self):
        """Gets the name of this AffiliateLink.  # noqa: E501

        Name of the link  # noqa: E501

        :return: The name of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AffiliateLink.

        Name of the link  # noqa: E501

        :param name: The name of this AffiliateLink.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this AffiliateLink.  # noqa: E501

        Type of link  # noqa: E501

        :return: The type of this AffiliateLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AffiliateLink.

        Type of link  # noqa: E501

        :param type: The type of this AffiliateLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["image", "text", "invisible", "direct"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(AffiliateLink, dict):
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
        if not isinstance(other, AffiliateLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class EmailSegment(object):
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
        'allow_csv_download': 'bool',
        'allow_facebook_audiences': 'bool',
        'created_dts': 'str',
        'deleted': 'bool',
        'email_segment_uuid': 'str',
        'esp_list_segment_folder_uuid': 'str',
        'facebook_custom_audience': 'bool',
        'filter_profile_equation_json': 'str',
        'member_count': 'int',
        'merchant_id': 'str',
        'name': 'str',
        'rank_json': 'str',
        'rebuild_required': 'bool',
        'storefront_oid': 'int',
        'thirdparty_join_add_tags': 'list[str]',
        'thirdparty_join_remove_tags': 'list[str]',
        'thirdparty_leave_add_tags': 'list[str]',
        'thirdparty_leave_remove_tags': 'list[str]',
        'thirdparty_list_id': 'str',
        'thirdparty_provider_name': 'str',
        'used_by': 'list[EmailListSegmentUsedBy]'
    }

    attribute_map = {
        'allow_csv_download': 'allow_csv_download',
        'allow_facebook_audiences': 'allow_facebook_audiences',
        'created_dts': 'created_dts',
        'deleted': 'deleted',
        'email_segment_uuid': 'email_segment_uuid',
        'esp_list_segment_folder_uuid': 'esp_list_segment_folder_uuid',
        'facebook_custom_audience': 'facebook_custom_audience',
        'filter_profile_equation_json': 'filter_profile_equation_json',
        'member_count': 'member_count',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'rank_json': 'rank_json',
        'rebuild_required': 'rebuild_required',
        'storefront_oid': 'storefront_oid',
        'thirdparty_join_add_tags': 'thirdparty_join_add_tags',
        'thirdparty_join_remove_tags': 'thirdparty_join_remove_tags',
        'thirdparty_leave_add_tags': 'thirdparty_leave_add_tags',
        'thirdparty_leave_remove_tags': 'thirdparty_leave_remove_tags',
        'thirdparty_list_id': 'thirdparty_list_id',
        'thirdparty_provider_name': 'thirdparty_provider_name',
        'used_by': 'used_by'
    }

    def __init__(self, allow_csv_download=None, allow_facebook_audiences=None, created_dts=None, deleted=None, email_segment_uuid=None, esp_list_segment_folder_uuid=None, facebook_custom_audience=None, filter_profile_equation_json=None, member_count=None, merchant_id=None, name=None, rank_json=None, rebuild_required=None, storefront_oid=None, thirdparty_join_add_tags=None, thirdparty_join_remove_tags=None, thirdparty_leave_add_tags=None, thirdparty_leave_remove_tags=None, thirdparty_list_id=None, thirdparty_provider_name=None, used_by=None):  # noqa: E501
        """EmailSegment - a model defined in Swagger"""  # noqa: E501

        self._allow_csv_download = None
        self._allow_facebook_audiences = None
        self._created_dts = None
        self._deleted = None
        self._email_segment_uuid = None
        self._esp_list_segment_folder_uuid = None
        self._facebook_custom_audience = None
        self._filter_profile_equation_json = None
        self._member_count = None
        self._merchant_id = None
        self._name = None
        self._rank_json = None
        self._rebuild_required = None
        self._storefront_oid = None
        self._thirdparty_join_add_tags = None
        self._thirdparty_join_remove_tags = None
        self._thirdparty_leave_add_tags = None
        self._thirdparty_leave_remove_tags = None
        self._thirdparty_list_id = None
        self._thirdparty_provider_name = None
        self._used_by = None
        self.discriminator = None

        if allow_csv_download is not None:
            self.allow_csv_download = allow_csv_download
        if allow_facebook_audiences is not None:
            self.allow_facebook_audiences = allow_facebook_audiences
        if created_dts is not None:
            self.created_dts = created_dts
        if deleted is not None:
            self.deleted = deleted
        if email_segment_uuid is not None:
            self.email_segment_uuid = email_segment_uuid
        if esp_list_segment_folder_uuid is not None:
            self.esp_list_segment_folder_uuid = esp_list_segment_folder_uuid
        if facebook_custom_audience is not None:
            self.facebook_custom_audience = facebook_custom_audience
        if filter_profile_equation_json is not None:
            self.filter_profile_equation_json = filter_profile_equation_json
        if member_count is not None:
            self.member_count = member_count
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if rank_json is not None:
            self.rank_json = rank_json
        if rebuild_required is not None:
            self.rebuild_required = rebuild_required
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if thirdparty_join_add_tags is not None:
            self.thirdparty_join_add_tags = thirdparty_join_add_tags
        if thirdparty_join_remove_tags is not None:
            self.thirdparty_join_remove_tags = thirdparty_join_remove_tags
        if thirdparty_leave_add_tags is not None:
            self.thirdparty_leave_add_tags = thirdparty_leave_add_tags
        if thirdparty_leave_remove_tags is not None:
            self.thirdparty_leave_remove_tags = thirdparty_leave_remove_tags
        if thirdparty_list_id is not None:
            self.thirdparty_list_id = thirdparty_list_id
        if thirdparty_provider_name is not None:
            self.thirdparty_provider_name = thirdparty_provider_name
        if used_by is not None:
            self.used_by = used_by

    @property
    def allow_csv_download(self):
        """Gets the allow_csv_download of this EmailSegment.  # noqa: E501

        True if the current user has the rights to download this segment.  # noqa: E501

        :return: The allow_csv_download of this EmailSegment.  # noqa: E501
        :rtype: bool
        """
        return self._allow_csv_download

    @allow_csv_download.setter
    def allow_csv_download(self, allow_csv_download):
        """Sets the allow_csv_download of this EmailSegment.

        True if the current user has the rights to download this segment.  # noqa: E501

        :param allow_csv_download: The allow_csv_download of this EmailSegment.  # noqa: E501
        :type: bool
        """

        self._allow_csv_download = allow_csv_download

    @property
    def allow_facebook_audiences(self):
        """Gets the allow_facebook_audiences of this EmailSegment.  # noqa: E501

        True if this StoreFront has the Facebook Analytics app connected and supports them  # noqa: E501

        :return: The allow_facebook_audiences of this EmailSegment.  # noqa: E501
        :rtype: bool
        """
        return self._allow_facebook_audiences

    @allow_facebook_audiences.setter
    def allow_facebook_audiences(self, allow_facebook_audiences):
        """Sets the allow_facebook_audiences of this EmailSegment.

        True if this StoreFront has the Facebook Analytics app connected and supports them  # noqa: E501

        :param allow_facebook_audiences: The allow_facebook_audiences of this EmailSegment.  # noqa: E501
        :type: bool
        """

        self._allow_facebook_audiences = allow_facebook_audiences

    @property
    def created_dts(self):
        """Gets the created_dts of this EmailSegment.  # noqa: E501

        Created date  # noqa: E501

        :return: The created_dts of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._created_dts

    @created_dts.setter
    def created_dts(self, created_dts):
        """Sets the created_dts of this EmailSegment.

        Created date  # noqa: E501

        :param created_dts: The created_dts of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._created_dts = created_dts

    @property
    def deleted(self):
        """Gets the deleted of this EmailSegment.  # noqa: E501

        True if this campaign was deleted  # noqa: E501

        :return: The deleted of this EmailSegment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this EmailSegment.

        True if this campaign was deleted  # noqa: E501

        :param deleted: The deleted of this EmailSegment.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def email_segment_uuid(self):
        """Gets the email_segment_uuid of this EmailSegment.  # noqa: E501

        Email segment UUID  # noqa: E501

        :return: The email_segment_uuid of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._email_segment_uuid

    @email_segment_uuid.setter
    def email_segment_uuid(self, email_segment_uuid):
        """Sets the email_segment_uuid of this EmailSegment.

        Email segment UUID  # noqa: E501

        :param email_segment_uuid: The email_segment_uuid of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._email_segment_uuid = email_segment_uuid

    @property
    def esp_list_segment_folder_uuid(self):
        """Gets the esp_list_segment_folder_uuid of this EmailSegment.  # noqa: E501

        List/Segment folder UUID  # noqa: E501

        :return: The esp_list_segment_folder_uuid of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._esp_list_segment_folder_uuid

    @esp_list_segment_folder_uuid.setter
    def esp_list_segment_folder_uuid(self, esp_list_segment_folder_uuid):
        """Sets the esp_list_segment_folder_uuid of this EmailSegment.

        List/Segment folder UUID  # noqa: E501

        :param esp_list_segment_folder_uuid: The esp_list_segment_folder_uuid of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._esp_list_segment_folder_uuid = esp_list_segment_folder_uuid

    @property
    def facebook_custom_audience(self):
        """Gets the facebook_custom_audience of this EmailSegment.  # noqa: E501

        True if you want to sync to a facebook custom audience  # noqa: E501

        :return: The facebook_custom_audience of this EmailSegment.  # noqa: E501
        :rtype: bool
        """
        return self._facebook_custom_audience

    @facebook_custom_audience.setter
    def facebook_custom_audience(self, facebook_custom_audience):
        """Sets the facebook_custom_audience of this EmailSegment.

        True if you want to sync to a facebook custom audience  # noqa: E501

        :param facebook_custom_audience: The facebook_custom_audience of this EmailSegment.  # noqa: E501
        :type: bool
        """

        self._facebook_custom_audience = facebook_custom_audience

    @property
    def filter_profile_equation_json(self):
        """Gets the filter_profile_equation_json of this EmailSegment.  # noqa: E501

        File profile equation json  # noqa: E501

        :return: The filter_profile_equation_json of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._filter_profile_equation_json

    @filter_profile_equation_json.setter
    def filter_profile_equation_json(self, filter_profile_equation_json):
        """Sets the filter_profile_equation_json of this EmailSegment.

        File profile equation json  # noqa: E501

        :param filter_profile_equation_json: The filter_profile_equation_json of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._filter_profile_equation_json = filter_profile_equation_json

    @property
    def member_count(self):
        """Gets the member_count of this EmailSegment.  # noqa: E501

        Count of members in this segment  # noqa: E501

        :return: The member_count of this EmailSegment.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this EmailSegment.

        Count of members in this segment  # noqa: E501

        :param member_count: The member_count of this EmailSegment.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EmailSegment.  # noqa: E501

        Merchant ID  # noqa: E501

        :return: The merchant_id of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EmailSegment.

        Merchant ID  # noqa: E501

        :param merchant_id: The merchant_id of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this EmailSegment.  # noqa: E501

        Name of email segment  # noqa: E501

        :return: The name of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailSegment.

        Name of email segment  # noqa: E501

        :param name: The name of this EmailSegment.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501

        self._name = name

    @property
    def rank_json(self):
        """Gets the rank_json of this EmailSegment.  # noqa: E501

        Rank settings json  # noqa: E501

        :return: The rank_json of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._rank_json

    @rank_json.setter
    def rank_json(self, rank_json):
        """Sets the rank_json of this EmailSegment.

        Rank settings json  # noqa: E501

        :param rank_json: The rank_json of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._rank_json = rank_json

    @property
    def rebuild_required(self):
        """Gets the rebuild_required of this EmailSegment.  # noqa: E501

        True if a rebuild is required because some part of the segment has changed  # noqa: E501

        :return: The rebuild_required of this EmailSegment.  # noqa: E501
        :rtype: bool
        """
        return self._rebuild_required

    @rebuild_required.setter
    def rebuild_required(self, rebuild_required):
        """Sets the rebuild_required of this EmailSegment.

        True if a rebuild is required because some part of the segment has changed  # noqa: E501

        :param rebuild_required: The rebuild_required of this EmailSegment.  # noqa: E501
        :type: bool
        """

        self._rebuild_required = rebuild_required

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this EmailSegment.  # noqa: E501

        Storefront oid  # noqa: E501

        :return: The storefront_oid of this EmailSegment.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this EmailSegment.

        Storefront oid  # noqa: E501

        :param storefront_oid: The storefront_oid of this EmailSegment.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def thirdparty_join_add_tags(self):
        """Gets the thirdparty_join_add_tags of this EmailSegment.  # noqa: E501

        Third party provider tags to add when a customer joins the segment.  # noqa: E501

        :return: The thirdparty_join_add_tags of this EmailSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._thirdparty_join_add_tags

    @thirdparty_join_add_tags.setter
    def thirdparty_join_add_tags(self, thirdparty_join_add_tags):
        """Sets the thirdparty_join_add_tags of this EmailSegment.

        Third party provider tags to add when a customer joins the segment.  # noqa: E501

        :param thirdparty_join_add_tags: The thirdparty_join_add_tags of this EmailSegment.  # noqa: E501
        :type: list[str]
        """

        self._thirdparty_join_add_tags = thirdparty_join_add_tags

    @property
    def thirdparty_join_remove_tags(self):
        """Gets the thirdparty_join_remove_tags of this EmailSegment.  # noqa: E501

        Third party provider tags to remove when a customer joins the segment.  # noqa: E501

        :return: The thirdparty_join_remove_tags of this EmailSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._thirdparty_join_remove_tags

    @thirdparty_join_remove_tags.setter
    def thirdparty_join_remove_tags(self, thirdparty_join_remove_tags):
        """Sets the thirdparty_join_remove_tags of this EmailSegment.

        Third party provider tags to remove when a customer joins the segment.  # noqa: E501

        :param thirdparty_join_remove_tags: The thirdparty_join_remove_tags of this EmailSegment.  # noqa: E501
        :type: list[str]
        """

        self._thirdparty_join_remove_tags = thirdparty_join_remove_tags

    @property
    def thirdparty_leave_add_tags(self):
        """Gets the thirdparty_leave_add_tags of this EmailSegment.  # noqa: E501

        Third party provider tags to add when a customer leaves the segment.  # noqa: E501

        :return: The thirdparty_leave_add_tags of this EmailSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._thirdparty_leave_add_tags

    @thirdparty_leave_add_tags.setter
    def thirdparty_leave_add_tags(self, thirdparty_leave_add_tags):
        """Sets the thirdparty_leave_add_tags of this EmailSegment.

        Third party provider tags to add when a customer leaves the segment.  # noqa: E501

        :param thirdparty_leave_add_tags: The thirdparty_leave_add_tags of this EmailSegment.  # noqa: E501
        :type: list[str]
        """

        self._thirdparty_leave_add_tags = thirdparty_leave_add_tags

    @property
    def thirdparty_leave_remove_tags(self):
        """Gets the thirdparty_leave_remove_tags of this EmailSegment.  # noqa: E501

        Third party provider tags to remove when a customer leaves the segment.  # noqa: E501

        :return: The thirdparty_leave_remove_tags of this EmailSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._thirdparty_leave_remove_tags

    @thirdparty_leave_remove_tags.setter
    def thirdparty_leave_remove_tags(self, thirdparty_leave_remove_tags):
        """Sets the thirdparty_leave_remove_tags of this EmailSegment.

        Third party provider tags to remove when a customer leaves the segment.  # noqa: E501

        :param thirdparty_leave_remove_tags: The thirdparty_leave_remove_tags of this EmailSegment.  # noqa: E501
        :type: list[str]
        """

        self._thirdparty_leave_remove_tags = thirdparty_leave_remove_tags

    @property
    def thirdparty_list_id(self):
        """Gets the thirdparty_list_id of this EmailSegment.  # noqa: E501

        List id of third party provider to sync with.  # noqa: E501

        :return: The thirdparty_list_id of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._thirdparty_list_id

    @thirdparty_list_id.setter
    def thirdparty_list_id(self, thirdparty_list_id):
        """Sets the thirdparty_list_id of this EmailSegment.

        List id of third party provider to sync with.  # noqa: E501

        :param thirdparty_list_id: The thirdparty_list_id of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._thirdparty_list_id = thirdparty_list_id

    @property
    def thirdparty_provider_name(self):
        """Gets the thirdparty_provider_name of this EmailSegment.  # noqa: E501

        Name of third party provider to sync segment to a list with.  # noqa: E501

        :return: The thirdparty_provider_name of this EmailSegment.  # noqa: E501
        :rtype: str
        """
        return self._thirdparty_provider_name

    @thirdparty_provider_name.setter
    def thirdparty_provider_name(self, thirdparty_provider_name):
        """Sets the thirdparty_provider_name of this EmailSegment.

        Name of third party provider to sync segment to a list with.  # noqa: E501

        :param thirdparty_provider_name: The thirdparty_provider_name of this EmailSegment.  # noqa: E501
        :type: str
        """

        self._thirdparty_provider_name = thirdparty_provider_name

    @property
    def used_by(self):
        """Gets the used_by of this EmailSegment.  # noqa: E501

        Details on the flows or campaigns that use this list.  # noqa: E501

        :return: The used_by of this EmailSegment.  # noqa: E501
        :rtype: list[EmailListSegmentUsedBy]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this EmailSegment.

        Details on the flows or campaigns that use this list.  # noqa: E501

        :param used_by: The used_by of this EmailSegment.  # noqa: E501
        :type: list[EmailListSegmentUsedBy]
        """

        self._used_by = used_by

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
        if issubclass(EmailSegment, dict):
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
        if not isinstance(other, EmailSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
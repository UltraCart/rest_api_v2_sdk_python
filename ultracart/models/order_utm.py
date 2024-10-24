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


class OrderUtm(object):
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
        'attribution_first_click_subtotal': 'float',
        'attribution_first_click_total': 'float',
        'attribution_last_click_subtotal': 'float',
        'attribution_last_click_total': 'float',
        'attribution_linear_subtotal': 'float',
        'attribution_linear_total': 'float',
        'attribution_position_based_subtotal': 'float',
        'attribution_position_based_total': 'float',
        'click_dts': 'str',
        'facebook_ad_id': 'str',
        'fbclid': 'str',
        'gbraid': 'str',
        'glcid': 'str',
        'itm_campaign': 'str',
        'itm_content': 'str',
        'itm_id': 'str',
        'itm_medium': 'str',
        'itm_source': 'str',
        'itm_term': 'str',
        'msclkid': 'str',
        'short_code': 'str',
        'short_code_backup': 'bool',
        'ttclid': 'str',
        'uc_message_id': 'str',
        'utm_campaign': 'str',
        'utm_content': 'str',
        'utm_id': 'str',
        'utm_medium': 'str',
        'utm_source': 'str',
        'utm_term': 'str',
        'vmcid': 'str',
        'wbraid': 'str'
    }

    attribute_map = {
        'attribution_first_click_subtotal': 'attribution_first_click_subtotal',
        'attribution_first_click_total': 'attribution_first_click_total',
        'attribution_last_click_subtotal': 'attribution_last_click_subtotal',
        'attribution_last_click_total': 'attribution_last_click_total',
        'attribution_linear_subtotal': 'attribution_linear_subtotal',
        'attribution_linear_total': 'attribution_linear_total',
        'attribution_position_based_subtotal': 'attribution_position_based_subtotal',
        'attribution_position_based_total': 'attribution_position_based_total',
        'click_dts': 'click_dts',
        'facebook_ad_id': 'facebook_ad_id',
        'fbclid': 'fbclid',
        'gbraid': 'gbraid',
        'glcid': 'glcid',
        'itm_campaign': 'itm_campaign',
        'itm_content': 'itm_content',
        'itm_id': 'itm_id',
        'itm_medium': 'itm_medium',
        'itm_source': 'itm_source',
        'itm_term': 'itm_term',
        'msclkid': 'msclkid',
        'short_code': 'short_code',
        'short_code_backup': 'short_code_backup',
        'ttclid': 'ttclid',
        'uc_message_id': 'uc_message_id',
        'utm_campaign': 'utm_campaign',
        'utm_content': 'utm_content',
        'utm_id': 'utm_id',
        'utm_medium': 'utm_medium',
        'utm_source': 'utm_source',
        'utm_term': 'utm_term',
        'vmcid': 'vmcid',
        'wbraid': 'wbraid'
    }

    def __init__(self, attribution_first_click_subtotal=None, attribution_first_click_total=None, attribution_last_click_subtotal=None, attribution_last_click_total=None, attribution_linear_subtotal=None, attribution_linear_total=None, attribution_position_based_subtotal=None, attribution_position_based_total=None, click_dts=None, facebook_ad_id=None, fbclid=None, gbraid=None, glcid=None, itm_campaign=None, itm_content=None, itm_id=None, itm_medium=None, itm_source=None, itm_term=None, msclkid=None, short_code=None, short_code_backup=None, ttclid=None, uc_message_id=None, utm_campaign=None, utm_content=None, utm_id=None, utm_medium=None, utm_source=None, utm_term=None, vmcid=None, wbraid=None):  # noqa: E501
        """OrderUtm - a model defined in Swagger"""  # noqa: E501

        self._attribution_first_click_subtotal = None
        self._attribution_first_click_total = None
        self._attribution_last_click_subtotal = None
        self._attribution_last_click_total = None
        self._attribution_linear_subtotal = None
        self._attribution_linear_total = None
        self._attribution_position_based_subtotal = None
        self._attribution_position_based_total = None
        self._click_dts = None
        self._facebook_ad_id = None
        self._fbclid = None
        self._gbraid = None
        self._glcid = None
        self._itm_campaign = None
        self._itm_content = None
        self._itm_id = None
        self._itm_medium = None
        self._itm_source = None
        self._itm_term = None
        self._msclkid = None
        self._short_code = None
        self._short_code_backup = None
        self._ttclid = None
        self._uc_message_id = None
        self._utm_campaign = None
        self._utm_content = None
        self._utm_id = None
        self._utm_medium = None
        self._utm_source = None
        self._utm_term = None
        self._vmcid = None
        self._wbraid = None
        self.discriminator = None

        if attribution_first_click_subtotal is not None:
            self.attribution_first_click_subtotal = attribution_first_click_subtotal
        if attribution_first_click_total is not None:
            self.attribution_first_click_total = attribution_first_click_total
        if attribution_last_click_subtotal is not None:
            self.attribution_last_click_subtotal = attribution_last_click_subtotal
        if attribution_last_click_total is not None:
            self.attribution_last_click_total = attribution_last_click_total
        if attribution_linear_subtotal is not None:
            self.attribution_linear_subtotal = attribution_linear_subtotal
        if attribution_linear_total is not None:
            self.attribution_linear_total = attribution_linear_total
        if attribution_position_based_subtotal is not None:
            self.attribution_position_based_subtotal = attribution_position_based_subtotal
        if attribution_position_based_total is not None:
            self.attribution_position_based_total = attribution_position_based_total
        if click_dts is not None:
            self.click_dts = click_dts
        if facebook_ad_id is not None:
            self.facebook_ad_id = facebook_ad_id
        if fbclid is not None:
            self.fbclid = fbclid
        if gbraid is not None:
            self.gbraid = gbraid
        if glcid is not None:
            self.glcid = glcid
        if itm_campaign is not None:
            self.itm_campaign = itm_campaign
        if itm_content is not None:
            self.itm_content = itm_content
        if itm_id is not None:
            self.itm_id = itm_id
        if itm_medium is not None:
            self.itm_medium = itm_medium
        if itm_source is not None:
            self.itm_source = itm_source
        if itm_term is not None:
            self.itm_term = itm_term
        if msclkid is not None:
            self.msclkid = msclkid
        if short_code is not None:
            self.short_code = short_code
        if short_code_backup is not None:
            self.short_code_backup = short_code_backup
        if ttclid is not None:
            self.ttclid = ttclid
        if uc_message_id is not None:
            self.uc_message_id = uc_message_id
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign
        if utm_content is not None:
            self.utm_content = utm_content
        if utm_id is not None:
            self.utm_id = utm_id
        if utm_medium is not None:
            self.utm_medium = utm_medium
        if utm_source is not None:
            self.utm_source = utm_source
        if utm_term is not None:
            self.utm_term = utm_term
        if vmcid is not None:
            self.vmcid = vmcid
        if wbraid is not None:
            self.wbraid = wbraid

    @property
    def attribution_first_click_subtotal(self):
        """Gets the attribution_first_click_subtotal of this OrderUtm.  # noqa: E501


        :return: The attribution_first_click_subtotal of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_first_click_subtotal

    @attribution_first_click_subtotal.setter
    def attribution_first_click_subtotal(self, attribution_first_click_subtotal):
        """Sets the attribution_first_click_subtotal of this OrderUtm.


        :param attribution_first_click_subtotal: The attribution_first_click_subtotal of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_first_click_subtotal = attribution_first_click_subtotal

    @property
    def attribution_first_click_total(self):
        """Gets the attribution_first_click_total of this OrderUtm.  # noqa: E501


        :return: The attribution_first_click_total of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_first_click_total

    @attribution_first_click_total.setter
    def attribution_first_click_total(self, attribution_first_click_total):
        """Sets the attribution_first_click_total of this OrderUtm.


        :param attribution_first_click_total: The attribution_first_click_total of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_first_click_total = attribution_first_click_total

    @property
    def attribution_last_click_subtotal(self):
        """Gets the attribution_last_click_subtotal of this OrderUtm.  # noqa: E501


        :return: The attribution_last_click_subtotal of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_last_click_subtotal

    @attribution_last_click_subtotal.setter
    def attribution_last_click_subtotal(self, attribution_last_click_subtotal):
        """Sets the attribution_last_click_subtotal of this OrderUtm.


        :param attribution_last_click_subtotal: The attribution_last_click_subtotal of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_last_click_subtotal = attribution_last_click_subtotal

    @property
    def attribution_last_click_total(self):
        """Gets the attribution_last_click_total of this OrderUtm.  # noqa: E501


        :return: The attribution_last_click_total of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_last_click_total

    @attribution_last_click_total.setter
    def attribution_last_click_total(self, attribution_last_click_total):
        """Sets the attribution_last_click_total of this OrderUtm.


        :param attribution_last_click_total: The attribution_last_click_total of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_last_click_total = attribution_last_click_total

    @property
    def attribution_linear_subtotal(self):
        """Gets the attribution_linear_subtotal of this OrderUtm.  # noqa: E501


        :return: The attribution_linear_subtotal of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_linear_subtotal

    @attribution_linear_subtotal.setter
    def attribution_linear_subtotal(self, attribution_linear_subtotal):
        """Sets the attribution_linear_subtotal of this OrderUtm.


        :param attribution_linear_subtotal: The attribution_linear_subtotal of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_linear_subtotal = attribution_linear_subtotal

    @property
    def attribution_linear_total(self):
        """Gets the attribution_linear_total of this OrderUtm.  # noqa: E501


        :return: The attribution_linear_total of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_linear_total

    @attribution_linear_total.setter
    def attribution_linear_total(self, attribution_linear_total):
        """Sets the attribution_linear_total of this OrderUtm.


        :param attribution_linear_total: The attribution_linear_total of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_linear_total = attribution_linear_total

    @property
    def attribution_position_based_subtotal(self):
        """Gets the attribution_position_based_subtotal of this OrderUtm.  # noqa: E501


        :return: The attribution_position_based_subtotal of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_position_based_subtotal

    @attribution_position_based_subtotal.setter
    def attribution_position_based_subtotal(self, attribution_position_based_subtotal):
        """Sets the attribution_position_based_subtotal of this OrderUtm.


        :param attribution_position_based_subtotal: The attribution_position_based_subtotal of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_position_based_subtotal = attribution_position_based_subtotal

    @property
    def attribution_position_based_total(self):
        """Gets the attribution_position_based_total of this OrderUtm.  # noqa: E501


        :return: The attribution_position_based_total of this OrderUtm.  # noqa: E501
        :rtype: float
        """
        return self._attribution_position_based_total

    @attribution_position_based_total.setter
    def attribution_position_based_total(self, attribution_position_based_total):
        """Sets the attribution_position_based_total of this OrderUtm.


        :param attribution_position_based_total: The attribution_position_based_total of this OrderUtm.  # noqa: E501
        :type: float
        """

        self._attribution_position_based_total = attribution_position_based_total

    @property
    def click_dts(self):
        """Gets the click_dts of this OrderUtm.  # noqa: E501

        Date/time that the click happened  # noqa: E501

        :return: The click_dts of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._click_dts

    @click_dts.setter
    def click_dts(self, click_dts):
        """Sets the click_dts of this OrderUtm.

        Date/time that the click happened  # noqa: E501

        :param click_dts: The click_dts of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._click_dts = click_dts

    @property
    def facebook_ad_id(self):
        """Gets the facebook_ad_id of this OrderUtm.  # noqa: E501


        :return: The facebook_ad_id of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._facebook_ad_id

    @facebook_ad_id.setter
    def facebook_ad_id(self, facebook_ad_id):
        """Sets the facebook_ad_id of this OrderUtm.


        :param facebook_ad_id: The facebook_ad_id of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._facebook_ad_id = facebook_ad_id

    @property
    def fbclid(self):
        """Gets the fbclid of this OrderUtm.  # noqa: E501


        :return: The fbclid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._fbclid

    @fbclid.setter
    def fbclid(self, fbclid):
        """Sets the fbclid of this OrderUtm.


        :param fbclid: The fbclid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._fbclid = fbclid

    @property
    def gbraid(self):
        """Gets the gbraid of this OrderUtm.  # noqa: E501


        :return: The gbraid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._gbraid

    @gbraid.setter
    def gbraid(self, gbraid):
        """Sets the gbraid of this OrderUtm.


        :param gbraid: The gbraid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._gbraid = gbraid

    @property
    def glcid(self):
        """Gets the glcid of this OrderUtm.  # noqa: E501


        :return: The glcid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._glcid

    @glcid.setter
    def glcid(self, glcid):
        """Sets the glcid of this OrderUtm.


        :param glcid: The glcid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._glcid = glcid

    @property
    def itm_campaign(self):
        """Gets the itm_campaign of this OrderUtm.  # noqa: E501


        :return: The itm_campaign of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_campaign

    @itm_campaign.setter
    def itm_campaign(self, itm_campaign):
        """Sets the itm_campaign of this OrderUtm.


        :param itm_campaign: The itm_campaign of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_campaign = itm_campaign

    @property
    def itm_content(self):
        """Gets the itm_content of this OrderUtm.  # noqa: E501


        :return: The itm_content of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_content

    @itm_content.setter
    def itm_content(self, itm_content):
        """Sets the itm_content of this OrderUtm.


        :param itm_content: The itm_content of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_content = itm_content

    @property
    def itm_id(self):
        """Gets the itm_id of this OrderUtm.  # noqa: E501


        :return: The itm_id of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_id

    @itm_id.setter
    def itm_id(self, itm_id):
        """Sets the itm_id of this OrderUtm.


        :param itm_id: The itm_id of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_id = itm_id

    @property
    def itm_medium(self):
        """Gets the itm_medium of this OrderUtm.  # noqa: E501


        :return: The itm_medium of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_medium

    @itm_medium.setter
    def itm_medium(self, itm_medium):
        """Sets the itm_medium of this OrderUtm.


        :param itm_medium: The itm_medium of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_medium = itm_medium

    @property
    def itm_source(self):
        """Gets the itm_source of this OrderUtm.  # noqa: E501


        :return: The itm_source of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_source

    @itm_source.setter
    def itm_source(self, itm_source):
        """Sets the itm_source of this OrderUtm.


        :param itm_source: The itm_source of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_source = itm_source

    @property
    def itm_term(self):
        """Gets the itm_term of this OrderUtm.  # noqa: E501


        :return: The itm_term of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._itm_term

    @itm_term.setter
    def itm_term(self, itm_term):
        """Sets the itm_term of this OrderUtm.


        :param itm_term: The itm_term of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._itm_term = itm_term

    @property
    def msclkid(self):
        """Gets the msclkid of this OrderUtm.  # noqa: E501


        :return: The msclkid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._msclkid

    @msclkid.setter
    def msclkid(self, msclkid):
        """Sets the msclkid of this OrderUtm.


        :param msclkid: The msclkid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._msclkid = msclkid

    @property
    def short_code(self):
        """Gets the short_code of this OrderUtm.  # noqa: E501


        :return: The short_code of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this OrderUtm.


        :param short_code: The short_code of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._short_code = short_code

    @property
    def short_code_backup(self):
        """Gets the short_code_backup of this OrderUtm.  # noqa: E501


        :return: The short_code_backup of this OrderUtm.  # noqa: E501
        :rtype: bool
        """
        return self._short_code_backup

    @short_code_backup.setter
    def short_code_backup(self, short_code_backup):
        """Sets the short_code_backup of this OrderUtm.


        :param short_code_backup: The short_code_backup of this OrderUtm.  # noqa: E501
        :type: bool
        """

        self._short_code_backup = short_code_backup

    @property
    def ttclid(self):
        """Gets the ttclid of this OrderUtm.  # noqa: E501


        :return: The ttclid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._ttclid

    @ttclid.setter
    def ttclid(self, ttclid):
        """Sets the ttclid of this OrderUtm.


        :param ttclid: The ttclid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._ttclid = ttclid

    @property
    def uc_message_id(self):
        """Gets the uc_message_id of this OrderUtm.  # noqa: E501


        :return: The uc_message_id of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._uc_message_id

    @uc_message_id.setter
    def uc_message_id(self, uc_message_id):
        """Sets the uc_message_id of this OrderUtm.


        :param uc_message_id: The uc_message_id of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._uc_message_id = uc_message_id

    @property
    def utm_campaign(self):
        """Gets the utm_campaign of this OrderUtm.  # noqa: E501


        :return: The utm_campaign of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        """Sets the utm_campaign of this OrderUtm.


        :param utm_campaign: The utm_campaign of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_campaign = utm_campaign

    @property
    def utm_content(self):
        """Gets the utm_content of this OrderUtm.  # noqa: E501


        :return: The utm_content of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_content

    @utm_content.setter
    def utm_content(self, utm_content):
        """Sets the utm_content of this OrderUtm.


        :param utm_content: The utm_content of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_content = utm_content

    @property
    def utm_id(self):
        """Gets the utm_id of this OrderUtm.  # noqa: E501


        :return: The utm_id of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_id

    @utm_id.setter
    def utm_id(self, utm_id):
        """Sets the utm_id of this OrderUtm.


        :param utm_id: The utm_id of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_id = utm_id

    @property
    def utm_medium(self):
        """Gets the utm_medium of this OrderUtm.  # noqa: E501


        :return: The utm_medium of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_medium

    @utm_medium.setter
    def utm_medium(self, utm_medium):
        """Sets the utm_medium of this OrderUtm.


        :param utm_medium: The utm_medium of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_medium = utm_medium

    @property
    def utm_source(self):
        """Gets the utm_source of this OrderUtm.  # noqa: E501


        :return: The utm_source of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_source

    @utm_source.setter
    def utm_source(self, utm_source):
        """Sets the utm_source of this OrderUtm.


        :param utm_source: The utm_source of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_source = utm_source

    @property
    def utm_term(self):
        """Gets the utm_term of this OrderUtm.  # noqa: E501


        :return: The utm_term of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._utm_term

    @utm_term.setter
    def utm_term(self, utm_term):
        """Sets the utm_term of this OrderUtm.


        :param utm_term: The utm_term of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._utm_term = utm_term

    @property
    def vmcid(self):
        """Gets the vmcid of this OrderUtm.  # noqa: E501


        :return: The vmcid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._vmcid

    @vmcid.setter
    def vmcid(self, vmcid):
        """Sets the vmcid of this OrderUtm.


        :param vmcid: The vmcid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._vmcid = vmcid

    @property
    def wbraid(self):
        """Gets the wbraid of this OrderUtm.  # noqa: E501


        :return: The wbraid of this OrderUtm.  # noqa: E501
        :rtype: str
        """
        return self._wbraid

    @wbraid.setter
    def wbraid(self, wbraid):
        """Sets the wbraid of this OrderUtm.


        :param wbraid: The wbraid of this OrderUtm.  # noqa: E501
        :type: str
        """

        self._wbraid = wbraid

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
        if issubclass(OrderUtm, dict):
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
        if not isinstance(other, OrderUtm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

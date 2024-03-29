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


class ItemDigitalItemPdfMeta(object):
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
        'assembly_allowed': 'bool',
        'copy_allowed': 'bool',
        'custom_footer': 'str',
        'custom_header': 'str',
        'degraded_printing_allowed': 'bool',
        'fillin_allowed': 'bool',
        'modify_annotations_allowed': 'bool',
        'modify_contents_allowed': 'bool',
        'printing_allowed': 'bool',
        'screen_readers_allowed': 'bool',
        'tagged': 'bool'
    }

    attribute_map = {
        'assembly_allowed': 'assembly_allowed',
        'copy_allowed': 'copy_allowed',
        'custom_footer': 'custom_footer',
        'custom_header': 'custom_header',
        'degraded_printing_allowed': 'degraded_printing_allowed',
        'fillin_allowed': 'fillin_allowed',
        'modify_annotations_allowed': 'modify_annotations_allowed',
        'modify_contents_allowed': 'modify_contents_allowed',
        'printing_allowed': 'printing_allowed',
        'screen_readers_allowed': 'screen_readers_allowed',
        'tagged': 'tagged'
    }

    def __init__(self, assembly_allowed=None, copy_allowed=None, custom_footer=None, custom_header=None, degraded_printing_allowed=None, fillin_allowed=None, modify_annotations_allowed=None, modify_contents_allowed=None, printing_allowed=None, screen_readers_allowed=None, tagged=None):  # noqa: E501
        """ItemDigitalItemPdfMeta - a model defined in Swagger"""  # noqa: E501

        self._assembly_allowed = None
        self._copy_allowed = None
        self._custom_footer = None
        self._custom_header = None
        self._degraded_printing_allowed = None
        self._fillin_allowed = None
        self._modify_annotations_allowed = None
        self._modify_contents_allowed = None
        self._printing_allowed = None
        self._screen_readers_allowed = None
        self._tagged = None
        self.discriminator = None

        if assembly_allowed is not None:
            self.assembly_allowed = assembly_allowed
        if copy_allowed is not None:
            self.copy_allowed = copy_allowed
        if custom_footer is not None:
            self.custom_footer = custom_footer
        if custom_header is not None:
            self.custom_header = custom_header
        if degraded_printing_allowed is not None:
            self.degraded_printing_allowed = degraded_printing_allowed
        if fillin_allowed is not None:
            self.fillin_allowed = fillin_allowed
        if modify_annotations_allowed is not None:
            self.modify_annotations_allowed = modify_annotations_allowed
        if modify_contents_allowed is not None:
            self.modify_contents_allowed = modify_contents_allowed
        if printing_allowed is not None:
            self.printing_allowed = printing_allowed
        if screen_readers_allowed is not None:
            self.screen_readers_allowed = screen_readers_allowed
        if tagged is not None:
            self.tagged = tagged

    @property
    def assembly_allowed(self):
        """Gets the assembly_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Assembly allowed  # noqa: E501

        :return: The assembly_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._assembly_allowed

    @assembly_allowed.setter
    def assembly_allowed(self, assembly_allowed):
        """Sets the assembly_allowed of this ItemDigitalItemPdfMeta.

        Assembly allowed  # noqa: E501

        :param assembly_allowed: The assembly_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._assembly_allowed = assembly_allowed

    @property
    def copy_allowed(self):
        """Gets the copy_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Copy/Paste is allowed  # noqa: E501

        :return: The copy_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._copy_allowed

    @copy_allowed.setter
    def copy_allowed(self, copy_allowed):
        """Sets the copy_allowed of this ItemDigitalItemPdfMeta.

        Copy/Paste is allowed  # noqa: E501

        :param copy_allowed: The copy_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._copy_allowed = copy_allowed

    @property
    def custom_footer(self):
        """Gets the custom_footer of this ItemDigitalItemPdfMeta.  # noqa: E501

        A custom footer for each pdf page  # noqa: E501

        :return: The custom_footer of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: str
        """
        return self._custom_footer

    @custom_footer.setter
    def custom_footer(self, custom_footer):
        """Sets the custom_footer of this ItemDigitalItemPdfMeta.

        A custom footer for each pdf page  # noqa: E501

        :param custom_footer: The custom_footer of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: str
        """
        if custom_footer is not None and len(custom_footer) > 8000:
            raise ValueError("Invalid value for `custom_footer`, length must be less than or equal to `8000`")  # noqa: E501

        self._custom_footer = custom_footer

    @property
    def custom_header(self):
        """Gets the custom_header of this ItemDigitalItemPdfMeta.  # noqa: E501

        A custom header for each pdf page  # noqa: E501

        :return: The custom_header of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: str
        """
        return self._custom_header

    @custom_header.setter
    def custom_header(self, custom_header):
        """Sets the custom_header of this ItemDigitalItemPdfMeta.

        A custom header for each pdf page  # noqa: E501

        :param custom_header: The custom_header of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: str
        """
        if custom_header is not None and len(custom_header) > 8000:
            raise ValueError("Invalid value for `custom_header`, length must be less than or equal to `8000`")  # noqa: E501

        self._custom_header = custom_header

    @property
    def degraded_printing_allowed(self):
        """Gets the degraded_printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Degraded printing allowed  # noqa: E501

        :return: The degraded_printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._degraded_printing_allowed

    @degraded_printing_allowed.setter
    def degraded_printing_allowed(self, degraded_printing_allowed):
        """Sets the degraded_printing_allowed of this ItemDigitalItemPdfMeta.

        Degraded printing allowed  # noqa: E501

        :param degraded_printing_allowed: The degraded_printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._degraded_printing_allowed = degraded_printing_allowed

    @property
    def fillin_allowed(self):
        """Gets the fillin_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Fillin is allowed  # noqa: E501

        :return: The fillin_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._fillin_allowed

    @fillin_allowed.setter
    def fillin_allowed(self, fillin_allowed):
        """Sets the fillin_allowed of this ItemDigitalItemPdfMeta.

        Fillin is allowed  # noqa: E501

        :param fillin_allowed: The fillin_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._fillin_allowed = fillin_allowed

    @property
    def modify_annotations_allowed(self):
        """Gets the modify_annotations_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Modifying annotations is allowed  # noqa: E501

        :return: The modify_annotations_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._modify_annotations_allowed

    @modify_annotations_allowed.setter
    def modify_annotations_allowed(self, modify_annotations_allowed):
        """Sets the modify_annotations_allowed of this ItemDigitalItemPdfMeta.

        Modifying annotations is allowed  # noqa: E501

        :param modify_annotations_allowed: The modify_annotations_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._modify_annotations_allowed = modify_annotations_allowed

    @property
    def modify_contents_allowed(self):
        """Gets the modify_contents_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Modifying contents is allowed  # noqa: E501

        :return: The modify_contents_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._modify_contents_allowed

    @modify_contents_allowed.setter
    def modify_contents_allowed(self, modify_contents_allowed):
        """Sets the modify_contents_allowed of this ItemDigitalItemPdfMeta.

        Modifying contents is allowed  # noqa: E501

        :param modify_contents_allowed: The modify_contents_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._modify_contents_allowed = modify_contents_allowed

    @property
    def printing_allowed(self):
        """Gets the printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Printing is allowed  # noqa: E501

        :return: The printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._printing_allowed

    @printing_allowed.setter
    def printing_allowed(self, printing_allowed):
        """Sets the printing_allowed of this ItemDigitalItemPdfMeta.

        Printing is allowed  # noqa: E501

        :param printing_allowed: The printing_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._printing_allowed = printing_allowed

    @property
    def screen_readers_allowed(self):
        """Gets the screen_readers_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501

        Screen readers are allowed  # noqa: E501

        :return: The screen_readers_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._screen_readers_allowed

    @screen_readers_allowed.setter
    def screen_readers_allowed(self, screen_readers_allowed):
        """Sets the screen_readers_allowed of this ItemDigitalItemPdfMeta.

        Screen readers are allowed  # noqa: E501

        :param screen_readers_allowed: The screen_readers_allowed of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._screen_readers_allowed = screen_readers_allowed

    @property
    def tagged(self):
        """Gets the tagged of this ItemDigitalItemPdfMeta.  # noqa: E501

        PDF is tagged  # noqa: E501

        :return: The tagged of this ItemDigitalItemPdfMeta.  # noqa: E501
        :rtype: bool
        """
        return self._tagged

    @tagged.setter
    def tagged(self, tagged):
        """Sets the tagged of this ItemDigitalItemPdfMeta.

        PDF is tagged  # noqa: E501

        :param tagged: The tagged of this ItemDigitalItemPdfMeta.  # noqa: E501
        :type: bool
        """

        self._tagged = tagged

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
        if issubclass(ItemDigitalItemPdfMeta, dict):
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
        if not isinstance(other, ItemDigitalItemPdfMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class EmailCampaignResponse(object):
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
        'campaign': 'EmailCampaign',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'success': 'bool'
    }

    attribute_map = {
        'campaign': 'campaign',
        'error': 'error',
        'metadata': 'metadata',
        'success': 'success'
    }

    def __init__(self, campaign=None, error=None, metadata=None, success=None):
        """
        EmailCampaignResponse - a model defined in Swagger
        """

        self._campaign = None
        self._error = None
        self._metadata = None
        self._success = None
        self.discriminator = None

        if campaign is not None:
          self.campaign = campaign
        if error is not None:
          self.error = error
        if metadata is not None:
          self.metadata = metadata
        if success is not None:
          self.success = success

    @property
    def campaign(self):
        """
        Gets the campaign of this EmailCampaignResponse.

        :return: The campaign of this EmailCampaignResponse.
        :rtype: EmailCampaign
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this EmailCampaignResponse.

        :param campaign: The campaign of this EmailCampaignResponse.
        :type: EmailCampaign
        """

        self._campaign = campaign

    @property
    def error(self):
        """
        Gets the error of this EmailCampaignResponse.

        :return: The error of this EmailCampaignResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this EmailCampaignResponse.

        :param error: The error of this EmailCampaignResponse.
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """
        Gets the metadata of this EmailCampaignResponse.

        :return: The metadata of this EmailCampaignResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this EmailCampaignResponse.

        :param metadata: The metadata of this EmailCampaignResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """
        Gets the success of this EmailCampaignResponse.
        Indicates if API call was successful

        :return: The success of this EmailCampaignResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this EmailCampaignResponse.
        Indicates if API call was successful

        :param success: The success of this EmailCampaignResponse.
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, EmailCampaignResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

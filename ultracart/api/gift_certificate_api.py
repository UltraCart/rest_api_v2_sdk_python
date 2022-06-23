# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ultracart.api_client import ApiClient
from ultracart.configuration import Configuration

class GiftCertificateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def fromApiKey(cls, apiKey, verify_ssl = True, debug = False):
        config = Configuration()
        config.api_key['x-ultracart-simple-key'] = apiKey
        config.debug = debug
        config.verify_ssl = verify_ssl

        api_client = ApiClient(configuration=config, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')
        return GiftCertificateApi(api_client)




    def add_gift_certificate_ledger_entry(self, gift_certificate_oid, gift_certificate_ledger_entry, **kwargs):  # noqa: E501
        """Add a gift certificate ledger entry  # noqa: E501

        Adds a ledger entry for this gift certificate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gift_certificate_ledger_entry(gift_certificate_oid, gift_certificate_ledger_entry, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :param GiftCertificateLedgerEntry gift_certificate_ledger_entry: Gift certificate ledger entry (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_gift_certificate_ledger_entry_with_http_info(gift_certificate_oid, gift_certificate_ledger_entry, **kwargs)  # noqa: E501
        else:
            (data) = self.add_gift_certificate_ledger_entry_with_http_info(gift_certificate_oid, gift_certificate_ledger_entry, **kwargs)  # noqa: E501
            return data

    def add_gift_certificate_ledger_entry_with_http_info(self, gift_certificate_oid, gift_certificate_ledger_entry, **kwargs):  # noqa: E501
        """Add a gift certificate ledger entry  # noqa: E501

        Adds a ledger entry for this gift certificate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_gift_certificate_ledger_entry_with_http_info(gift_certificate_oid, gift_certificate_ledger_entry, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :param GiftCertificateLedgerEntry gift_certificate_ledger_entry: Gift certificate ledger entry (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_oid', 'gift_certificate_ledger_entry']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_gift_certificate_ledger_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_oid' is set
        if ('gift_certificate_oid' not in params or
                params['gift_certificate_oid'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_oid` when calling `add_gift_certificate_ledger_entry`")  # noqa: E501
        # verify the required parameter 'gift_certificate_ledger_entry' is set
        if ('gift_certificate_ledger_entry' not in params or
                params['gift_certificate_ledger_entry'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_ledger_entry` when calling `add_gift_certificate_ledger_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gift_certificate_oid' in params:
            path_params['gift_certificate_oid'] = params['gift_certificate_oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gift_certificate_ledger_entry' in params:
            body_params = params['gift_certificate_ledger_entry']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/{gift_certificate_oid}/ledger_entry', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_gift_certificate(self, gift_certificate_create_request, **kwargs):  # noqa: E501
        """Create a gift certificate  # noqa: E501

        Creates a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gift_certificate(gift_certificate_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GiftCertificateCreateRequest gift_certificate_create_request: Gift certificate create request (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_gift_certificate_with_http_info(gift_certificate_create_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_gift_certificate_with_http_info(gift_certificate_create_request, **kwargs)  # noqa: E501
            return data

    def create_gift_certificate_with_http_info(self, gift_certificate_create_request, **kwargs):  # noqa: E501
        """Create a gift certificate  # noqa: E501

        Creates a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gift_certificate_with_http_info(gift_certificate_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GiftCertificateCreateRequest gift_certificate_create_request: Gift certificate create request (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_create_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_gift_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_create_request' is set
        if ('gift_certificate_create_request' not in params or
                params['gift_certificate_create_request'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_create_request` when calling `create_gift_certificate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gift_certificate_create_request' in params:
            body_params = params['gift_certificate_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_gift_certificate(self, gift_certificate_oid, **kwargs):  # noqa: E501
        """Delete a gift certificate  # noqa: E501

        Deletes a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_gift_certificate(gift_certificate_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_gift_certificate_with_http_info(gift_certificate_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_gift_certificate_with_http_info(gift_certificate_oid, **kwargs)  # noqa: E501
            return data

    def delete_gift_certificate_with_http_info(self, gift_certificate_oid, **kwargs):  # noqa: E501
        """Delete a gift certificate  # noqa: E501

        Deletes a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_gift_certificate_with_http_info(gift_certificate_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_gift_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_oid' is set
        if ('gift_certificate_oid' not in params or
                params['gift_certificate_oid'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_oid` when calling `delete_gift_certificate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gift_certificate_oid' in params:
            path_params['gift_certificate_oid'] = params['gift_certificate_oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/{gift_certificate_oid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gift_certificate_by_code(self, code, **kwargs):  # noqa: E501
        """Retrieve gift certificate by code  # noqa: E501

        Retrieves a gift certificate from the account based on the code (the value the customer enters at checkout time).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificate_by_code(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gift_certificate_by_code_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gift_certificate_by_code_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def get_gift_certificate_by_code_with_http_info(self, code, **kwargs):  # noqa: E501
        """Retrieve gift certificate by code  # noqa: E501

        Retrieves a gift certificate from the account based on the code (the value the customer enters at checkout time).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificate_by_code_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gift_certificate_by_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_gift_certificate_by_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/by_code/{code}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gift_certificate_by_oid(self, gift_certificate_oid, **kwargs):  # noqa: E501
        """Retrieve gift certificate by oid  # noqa: E501

        Retrieves a gift certificate from the account based on the internal primary key.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificate_by_oid(gift_certificate_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gift_certificate_by_oid_with_http_info(gift_certificate_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gift_certificate_by_oid_with_http_info(gift_certificate_oid, **kwargs)  # noqa: E501
            return data

    def get_gift_certificate_by_oid_with_http_info(self, gift_certificate_oid, **kwargs):  # noqa: E501
        """Retrieve gift certificate by oid  # noqa: E501

        Retrieves a gift certificate from the account based on the internal primary key.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificate_by_oid_with_http_info(gift_certificate_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gift_certificate_by_oid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_oid' is set
        if ('gift_certificate_oid' not in params or
                params['gift_certificate_oid'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_oid` when calling `get_gift_certificate_by_oid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gift_certificate_oid' in params:
            path_params['gift_certificate_oid'] = params['gift_certificate_oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/{gift_certificate_oid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gift_certificates_by_email(self, email, **kwargs):  # noqa: E501
        """Retrieve gift certificate by email  # noqa: E501

        Retrieves all gift certificates from the account based on customer email.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificates_by_email(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: (required)
        :return: GiftCertificatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gift_certificates_by_email_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gift_certificates_by_email_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def get_gift_certificates_by_email_with_http_info(self, email, **kwargs):  # noqa: E501
        """Retrieve gift certificate by email  # noqa: E501

        Retrieves all gift certificates from the account based on customer email.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificates_by_email_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: (required)
        :return: GiftCertificatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gift_certificates_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_gift_certificates_by_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/by_email/{email}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificatesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gift_certificates_by_query(self, gift_certificate_query, **kwargs):  # noqa: E501
        """Retrieve gift certificates by query  # noqa: E501

        Retrieves gift certificates from the account.  If no parameters are specified, all gift certificates will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificates_by_query(gift_certificate_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GiftCertificateQuery gift_certificate_query: Gift certificates query (required)
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch customers that have been created/modified since this date/time.
        :param str sort: The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: GiftCertificatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gift_certificates_by_query_with_http_info(gift_certificate_query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gift_certificates_by_query_with_http_info(gift_certificate_query, **kwargs)  # noqa: E501
            return data

    def get_gift_certificates_by_query_with_http_info(self, gift_certificate_query, **kwargs):  # noqa: E501
        """Retrieve gift certificates by query  # noqa: E501

        Retrieves gift certificates from the account.  If no parameters are specified, all gift certificates will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gift_certificates_by_query_with_http_info(gift_certificate_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GiftCertificateQuery gift_certificate_query: Gift certificates query (required)
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch customers that have been created/modified since this date/time.
        :param str sort: The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: GiftCertificatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_query', 'limit', 'offset', 'since', 'sort', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gift_certificates_by_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_query' is set
        if ('gift_certificate_query' not in params or
                params['gift_certificate_query'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_query` when calling `get_gift_certificates_by_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501
        if 'since' in params:
            query_params.append(('_since', params['since']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('_sort', params['sort']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gift_certificate_query' in params:
            body_params = params['gift_certificate_query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificatesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_gift_certificate(self, gift_certificate_oid, gift_certificate, **kwargs):  # noqa: E501
        """Update a gift certificate  # noqa: E501

        Update a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gift_certificate(gift_certificate_oid, gift_certificate, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :param GiftCertificate gift_certificate: Gift certificate (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_gift_certificate_with_http_info(gift_certificate_oid, gift_certificate, **kwargs)  # noqa: E501
        else:
            (data) = self.update_gift_certificate_with_http_info(gift_certificate_oid, gift_certificate, **kwargs)  # noqa: E501
            return data

    def update_gift_certificate_with_http_info(self, gift_certificate_oid, gift_certificate, **kwargs):  # noqa: E501
        """Update a gift certificate  # noqa: E501

        Update a gift certificate for this merchant account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gift_certificate_with_http_info(gift_certificate_oid, gift_certificate, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gift_certificate_oid: (required)
        :param GiftCertificate gift_certificate: Gift certificate (required)
        :return: GiftCertificateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gift_certificate_oid', 'gift_certificate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_gift_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gift_certificate_oid' is set
        if ('gift_certificate_oid' not in params or
                params['gift_certificate_oid'] is None):
            raise ValueError("Missing the required parameter `gift_certificate_oid` when calling `update_gift_certificate`")  # noqa: E501
        # verify the required parameter 'gift_certificate' is set
        if ('gift_certificate' not in params or
                params['gift_certificate'] is None):
            raise ValueError("Missing the required parameter `gift_certificate` when calling `update_gift_certificate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gift_certificate_oid' in params:
            path_params['gift_certificate_oid'] = params['gift_certificate_oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gift_certificate' in params:
            body_params = params['gift_certificate']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/gift_certificate/gift_certificates/{gift_certificate_oid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GiftCertificateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

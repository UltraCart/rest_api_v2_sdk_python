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

class IntegrationLogApi(object):
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
        return IntegrationLogApi(api_client)



    def get_integration_log(self, pk, sk, **kwargs):  # noqa: E501
        """Retrieve an integration log  # noqa: E501

        Retrieve an integration logs from the account based identifiers   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_log(pk, sk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pk: (required)
        :param str sk: (required)
        :return: IntegrationLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_log_with_http_info(pk, sk, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_log_with_http_info(pk, sk, **kwargs)  # noqa: E501
            return data

    def get_integration_log_with_http_info(self, pk, sk, **kwargs):  # noqa: E501
        """Retrieve an integration log  # noqa: E501

        Retrieve an integration logs from the account based identifiers   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_log_with_http_info(pk, sk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pk: (required)
        :param str sk: (required)
        :return: IntegrationLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk', 'sk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pk' is set
        if ('pk' not in params or
                params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `get_integration_log`")  # noqa: E501
        # verify the required parameter 'sk' is set
        if ('sk' not in params or
                params['sk'] is None):
            raise ValueError("Missing the required parameter `sk` when calling `get_integration_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']  # noqa: E501
        if 'sk' in params:
            path_params['sk'] = params['sk']  # noqa: E501

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
            '/integration_log/query/{pk}/{sk}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_logs_query(self, integration_log_query, **kwargs):  # noqa: E501
        """Retrieve integration logs  # noqa: E501

        Retrieves a set of integration logs from the account based on a query object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_logs_query(integration_log_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntegrationLogQueryRequest integration_log_query: Integration log query (required)
        :param int limit: The maximum number of records to return on this one API call. (Default 100, Max 500)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :return: IntegrationLogQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_logs_query_with_http_info(integration_log_query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_logs_query_with_http_info(integration_log_query, **kwargs)  # noqa: E501
            return data

    def get_integration_logs_query_with_http_info(self, integration_log_query, **kwargs):  # noqa: E501
        """Retrieve integration logs  # noqa: E501

        Retrieves a set of integration logs from the account based on a query object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_logs_query_with_http_info(integration_log_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntegrationLogQueryRequest integration_log_query: Integration log query (required)
        :param int limit: The maximum number of records to return on this one API call. (Default 100, Max 500)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :return: IntegrationLogQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_log_query', 'limit', 'offset', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_logs_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_log_query' is set
        if ('integration_log_query' not in params or
                params['integration_log_query'] is None):
            raise ValueError("Missing the required parameter `integration_log_query` when calling `get_integration_logs_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('_sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'integration_log_query' in params:
            body_params = params['integration_log_query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/integration_log/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationLogQueryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

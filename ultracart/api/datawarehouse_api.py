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

class DatawarehouseApi(object):
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
        return DatawarehouseApi(api_client)




    def delete_report(self, report_oid, **kwargs):  # noqa: E501
        """Delete a report  # noqa: E501

        Delete a report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report(report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int report_oid: The report oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_report_with_http_info(report_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_report_with_http_info(report_oid, **kwargs)  # noqa: E501
            return data

    def delete_report_with_http_info(self, report_oid, **kwargs):  # noqa: E501
        """Delete a report  # noqa: E501

        Delete a report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report_with_http_info(report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int report_oid: The report oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_oid' is set
        if ('report_oid' not in params or
                params['report_oid'] is None):
            raise ValueError("Missing the required parameter `report_oid` when calling `delete_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_oid' in params:
            path_params['report_oid'] = params['report_oid']  # noqa: E501

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
            '/datawarehouse/reports/{report_oid}', 'DELETE',
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

    def execute_report_queries(self, query_request, **kwargs):  # noqa: E501
        """Execute the report queries  # noqa: E501

        Execute the report queries   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_report_queries(query_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReportExecuteQueriesRequest query_request: Query request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execute_report_queries_with_http_info(query_request, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_report_queries_with_http_info(query_request, **kwargs)  # noqa: E501
            return data

    def execute_report_queries_with_http_info(self, query_request, **kwargs):  # noqa: E501
        """Execute the report queries  # noqa: E501

        Execute the report queries   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_report_queries_with_http_info(query_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReportExecuteQueriesRequest query_request: Query request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_report_queries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_request' is set
        if ('query_request' not in params or
                params['query_request'] is None):
            raise ValueError("Missing the required parameter `query_request` when calling `execute_report_queries`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_request' in params:
            body_params = params['query_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/datawarehouse/reports/execute', 'PUT',
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

    def get_report(self, report_oid, **kwargs):  # noqa: E501
        """Get a report  # noqa: E501

        Retrieve a report   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report(report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int report_oid: (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_with_http_info(report_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_with_http_info(report_oid, **kwargs)  # noqa: E501
            return data

    def get_report_with_http_info(self, report_oid, **kwargs):  # noqa: E501
        """Get a report  # noqa: E501

        Retrieve a report   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_with_http_info(report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int report_oid: (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_oid' is set
        if ('report_oid' not in params or
                params['report_oid'] is None):
            raise ValueError("Missing the required parameter `report_oid` when calling `get_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_oid' in params:
            path_params['report_oid'] = params['report_oid']  # noqa: E501

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
            '/datawarehouse/reports/{report_oid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_data_set(self, dataset_uuid, **kwargs):  # noqa: E501
        """Get a report data set  # noqa: E501

        Retrieve a report data set   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_data_set(dataset_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset_uuid: (required)
        :return: ReportDataSetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_data_set_with_http_info(dataset_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_data_set_with_http_info(dataset_uuid, **kwargs)  # noqa: E501
            return data

    def get_report_data_set_with_http_info(self, dataset_uuid, **kwargs):  # noqa: E501
        """Get a report data set  # noqa: E501

        Retrieve a report data set   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_data_set_with_http_info(dataset_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset_uuid: (required)
        :return: ReportDataSetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_data_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_uuid' is set
        if ('dataset_uuid' not in params or
                params['dataset_uuid'] is None):
            raise ValueError("Missing the required parameter `dataset_uuid` when calling `get_report_data_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_uuid' in params:
            path_params['dataset_uuid'] = params['dataset_uuid']  # noqa: E501

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
            '/datawarehouse/reports/dataset/{dataset_uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportDataSetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_data_set_page(self, dataset_uuid, page_number, **kwargs):  # noqa: E501
        """Get a report data set page  # noqa: E501

        Retrieve a report data set page   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_data_set_page(dataset_uuid, page_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset_uuid: (required)
        :param int page_number: (required)
        :return: ReportDataSetPageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_data_set_page_with_http_info(dataset_uuid, page_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_data_set_page_with_http_info(dataset_uuid, page_number, **kwargs)  # noqa: E501
            return data

    def get_report_data_set_page_with_http_info(self, dataset_uuid, page_number, **kwargs):  # noqa: E501
        """Get a report data set page  # noqa: E501

        Retrieve a report data set page   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_data_set_page_with_http_info(dataset_uuid, page_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset_uuid: (required)
        :param int page_number: (required)
        :return: ReportDataSetPageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_uuid', 'page_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_data_set_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_uuid' is set
        if ('dataset_uuid' not in params or
                params['dataset_uuid'] is None):
            raise ValueError("Missing the required parameter `dataset_uuid` when calling `get_report_data_set_page`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if ('page_number' not in params or
                params['page_number'] is None):
            raise ValueError("Missing the required parameter `page_number` when calling `get_report_data_set_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_uuid' in params:
            path_params['dataset_uuid'] = params['dataset_uuid']  # noqa: E501
        if 'page_number' in params:
            path_params['page_number'] = params['page_number']  # noqa: E501

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
            '/datawarehouse/reports/dataset/{dataset_uuid}/pages/{page_number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportDataSetPageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_websocket_authorization(self, **kwargs):  # noqa: E501
        """Get report websocket authorization  # noqa: E501

        Retrieve a JWT to authorize a report to make a websocket connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_websocket_authorization(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportAuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_websocket_authorization_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_report_websocket_authorization_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_report_websocket_authorization_with_http_info(self, **kwargs):  # noqa: E501
        """Get report websocket authorization  # noqa: E501

        Retrieve a JWT to authorize a report to make a websocket connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_websocket_authorization_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportAuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_websocket_authorization" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/datawarehouse/reports/auth', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportAuthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reports(self, **kwargs):  # noqa: E501
        """Get list of reports available  # noqa: E501

        Retrieve a list of reports available   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_reports_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_reports_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of reports available  # noqa: E501

        Retrieve a list of reports available   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reports" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/datawarehouse/reports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_report(self, report, **kwargs):  # noqa: E501
        """Create a report  # noqa: E501

        Create a new report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_report(report, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Report report: Report to create (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.insert_report_with_http_info(report, **kwargs)  # noqa: E501
        else:
            (data) = self.insert_report_with_http_info(report, **kwargs)  # noqa: E501
            return data

    def insert_report_with_http_info(self, report, **kwargs):  # noqa: E501
        """Create a report  # noqa: E501

        Create a new report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_report_with_http_info(report, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Report report: Report to create (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report' is set
        if ('report' not in params or
                params['report'] is None):
            raise ValueError("Missing the required parameter `report` when calling `insert_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'report' in params:
            body_params = params['report']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/datawarehouse/reports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_report(self, report, report_oid, **kwargs):  # noqa: E501
        """Update a report  # noqa: E501

        Update a report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_report(report, report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Report report: Report to update (required)
        :param int report_oid: The report oid to update. (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_report_with_http_info(report, report_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_report_with_http_info(report, report_oid, **kwargs)  # noqa: E501
            return data

    def update_report_with_http_info(self, report, report_oid, **kwargs):  # noqa: E501
        """Update a report  # noqa: E501

        Update a report on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_report_with_http_info(report, report_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Report report: Report to update (required)
        :param int report_oid: The report oid to update. (required)
        :return: ReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report', 'report_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report' is set
        if ('report' not in params or
                params['report'] is None):
            raise ValueError("Missing the required parameter `report` when calling `update_report`")  # noqa: E501
        # verify the required parameter 'report_oid' is set
        if ('report_oid' not in params or
                params['report_oid'] is None):
            raise ValueError("Missing the required parameter `report_oid` when calling `update_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_oid' in params:
            path_params['report_oid'] = params['report_oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'report' in params:
            body_params = params['report']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/datawarehouse/reports/{report_oid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

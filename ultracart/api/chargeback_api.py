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

class ChargebackApi(object):
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
        return ChargebackApi(api_client)



    def delete_chargeback(self, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Delete a chargeback  # noqa: E501

        Delete a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chargeback(chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chargeback_dispute_oid: The chargeback_dispute_oid to delete. (required)
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_chargeback_with_http_info(chargeback_dispute_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_chargeback_with_http_info(chargeback_dispute_oid, **kwargs)  # noqa: E501
            return data

    def delete_chargeback_with_http_info(self, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Delete a chargeback  # noqa: E501

        Delete a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chargeback_with_http_info(chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chargeback_dispute_oid: The chargeback_dispute_oid to delete. (required)
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chargeback_dispute_oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_chargeback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chargeback_dispute_oid' is set
        if ('chargeback_dispute_oid' not in params or
                params['chargeback_dispute_oid'] is None):
            raise ValueError("Missing the required parameter `chargeback_dispute_oid` when calling `delete_chargeback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chargeback_dispute_oid' in params:
            path_params['chargeback_dispute_oid'] = params['chargeback_dispute_oid']  # noqa: E501

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
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/chargeback/chargebacks/{chargeback_dispute_oid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargebackDisputeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chargeback_dispute(self, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Retrieve a chargeback  # noqa: E501

        Retrieves a single chargeback using the specified chargeback dispute oid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chargeback_dispute(chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chargeback_dispute_oid: The chargeback dispute oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chargeback_dispute_with_http_info(chargeback_dispute_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chargeback_dispute_with_http_info(chargeback_dispute_oid, **kwargs)  # noqa: E501
            return data

    def get_chargeback_dispute_with_http_info(self, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Retrieve a chargeback  # noqa: E501

        Retrieves a single chargeback using the specified chargeback dispute oid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chargeback_dispute_with_http_info(chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chargeback_dispute_oid: The chargeback dispute oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chargeback_dispute_oid', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chargeback_dispute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chargeback_dispute_oid' is set
        if ('chargeback_dispute_oid' not in params or
                params['chargeback_dispute_oid'] is None):
            raise ValueError("Missing the required parameter `chargeback_dispute_oid` when calling `get_chargeback_dispute`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chargeback_dispute_oid' in params:
            path_params['chargeback_dispute_oid'] = params['chargeback_dispute_oid']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))  # noqa: E501

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
            '/chargeback/chargebacks/{chargeback_dispute_oid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargebackDisputeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chargeback_disputes(self, **kwargs):  # noqa: E501
        """Retrieve chargebacks  # noqa: E501

        Retrieves chargebacks from the account.  If no parameters are specified, all chargebacks will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chargeback_disputes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Order Id
        :param str case_number: Case number
        :param str status: Status
        :param str expiration_dts_start: Expiration dts start
        :param str expiration_dts_end: Expiration dts end
        :param str chargeback_dts_start: Chargeback dts start
        :param str chargeback_dts_end: Chargeback dts end
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch chargebacks that have been created/modified since this date/time.
        :param str sort: The sort order of the chargebacks.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chargeback_disputes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_chargeback_disputes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_chargeback_disputes_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve chargebacks  # noqa: E501

        Retrieves chargebacks from the account.  If no parameters are specified, all chargebacks will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chargeback_disputes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Order Id
        :param str case_number: Case number
        :param str status: Status
        :param str expiration_dts_start: Expiration dts start
        :param str expiration_dts_end: Expiration dts end
        :param str chargeback_dts_start: Chargeback dts start
        :param str chargeback_dts_end: Chargeback dts end
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch chargebacks that have been created/modified since this date/time.
        :param str sort: The sort order of the chargebacks.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'case_number', 'status', 'expiration_dts_start', 'expiration_dts_end', 'chargeback_dts_start', 'chargeback_dts_end', 'limit', 'offset', 'since', 'sort', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chargeback_disputes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('order_id', params['order_id']))  # noqa: E501
        if 'case_number' in params:
            query_params.append(('case_number', params['case_number']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'expiration_dts_start' in params:
            query_params.append(('expiration_dts_start', params['expiration_dts_start']))  # noqa: E501
        if 'expiration_dts_end' in params:
            query_params.append(('expiration_dts_end', params['expiration_dts_end']))  # noqa: E501
        if 'chargeback_dts_start' in params:
            query_params.append(('chargeback_dts_start', params['chargeback_dts_start']))  # noqa: E501
        if 'chargeback_dts_end' in params:
            query_params.append(('chargeback_dts_end', params['chargeback_dts_end']))  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/chargeback/chargebacks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargebackDisputesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_chargeback(self, chargeback, **kwargs):  # noqa: E501
        """Insert a chargeback  # noqa: E501

        Insert a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_chargeback(chargeback, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChargebackDispute chargeback: Chargeback to insert (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.insert_chargeback_with_http_info(chargeback, **kwargs)  # noqa: E501
        else:
            (data) = self.insert_chargeback_with_http_info(chargeback, **kwargs)  # noqa: E501
            return data

    def insert_chargeback_with_http_info(self, chargeback, **kwargs):  # noqa: E501
        """Insert a chargeback  # noqa: E501

        Insert a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_chargeback_with_http_info(chargeback, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChargebackDispute chargeback: Chargeback to insert (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chargeback', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_chargeback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chargeback' is set
        if ('chargeback' not in params or
                params['chargeback'] is None):
            raise ValueError("Missing the required parameter `chargeback` when calling `insert_chargeback`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'chargeback' in params:
            body_params = params['chargeback']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/chargeback/chargebacks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargebackDisputeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_chargeback(self, chargeback, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Update a chargeback  # noqa: E501

        Update a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_chargeback(chargeback, chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChargebackDispute chargeback: Chargeback to update (required)
        :param int chargeback_dispute_oid: The chargeback_dispute_oid to update. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_chargeback_with_http_info(chargeback, chargeback_dispute_oid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_chargeback_with_http_info(chargeback, chargeback_dispute_oid, **kwargs)  # noqa: E501
            return data

    def update_chargeback_with_http_info(self, chargeback, chargeback_dispute_oid, **kwargs):  # noqa: E501
        """Update a chargeback  # noqa: E501

        Update a chargeback on the UltraCart account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_chargeback_with_http_info(chargeback, chargeback_dispute_oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChargebackDispute chargeback: Chargeback to update (required)
        :param int chargeback_dispute_oid: The chargeback_dispute_oid to update. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: ChargebackDisputeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chargeback', 'chargeback_dispute_oid', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_chargeback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chargeback' is set
        if ('chargeback' not in params or
                params['chargeback'] is None):
            raise ValueError("Missing the required parameter `chargeback` when calling `update_chargeback`")  # noqa: E501
        # verify the required parameter 'chargeback_dispute_oid' is set
        if ('chargeback_dispute_oid' not in params or
                params['chargeback_dispute_oid'] is None):
            raise ValueError("Missing the required parameter `chargeback_dispute_oid` when calling `update_chargeback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chargeback_dispute_oid' in params:
            path_params['chargeback_dispute_oid'] = params['chargeback_dispute_oid']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'chargeback' in params:
            body_params = params['chargeback']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/chargeback/chargebacks/{chargeback_dispute_oid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargebackDisputeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

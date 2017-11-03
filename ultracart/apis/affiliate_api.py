# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AffiliateApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_clicks_by_query(self, click_query, **kwargs):
        """
        Retrieve clicks
        Retrieves a group of clicks from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the clicks returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_clicks_by_query(click_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AffiliateClickQuery click_query: Click query (required)
        :param int limit: The maximum number of records to return on this one API call. (Maximum 10000)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str expand: The object expansion to perform on the result.  Only option is link.
        :return: AffiliateClicksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_clicks_by_query_with_http_info(click_query, **kwargs)
        else:
            (data) = self.get_clicks_by_query_with_http_info(click_query, **kwargs)
            return data

    def get_clicks_by_query_with_http_info(self, click_query, **kwargs):
        """
        Retrieve clicks
        Retrieves a group of clicks from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the clicks returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_clicks_by_query_with_http_info(click_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AffiliateClickQuery click_query: Click query (required)
        :param int limit: The maximum number of records to return on this one API call. (Maximum 10000)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str expand: The object expansion to perform on the result.  Only option is link.
        :return: AffiliateClicksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['click_query', 'limit', 'offset', 'expand']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clicks_by_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'click_query' is set
        if ('click_query' not in params) or (params['click_query'] is None):
            raise ValueError("Missing the required parameter `click_query` when calling `get_clicks_by_query`")

        resource_path = '/affiliate/clicks/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['_limit'] = params['limit']
        if 'offset' in params:
            query_params['_offset'] = params['offset']
        if 'expand' in params:
            query_params['_expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'click_query' in params:
            body_params = params['click_query']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AffiliateClicksResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_ledgers_by_query(self, ledger_query, **kwargs):
        """
        Retrieve ledger entries
        Retrieves a group of ledger entries from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the ledgers returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ledgers_by_query(ledger_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AffiliateLedgerQuery ledger_query: Ledger query (required)
        :param int limit: The maximum number of records to return on this one API call. (Maximum 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str expand: The object expansion to perform on the result.  Only option is link.
        :return: AffiliateLedgersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_ledgers_by_query_with_http_info(ledger_query, **kwargs)
        else:
            (data) = self.get_ledgers_by_query_with_http_info(ledger_query, **kwargs)
            return data

    def get_ledgers_by_query_with_http_info(self, ledger_query, **kwargs):
        """
        Retrieve ledger entries
        Retrieves a group of ledger entries from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the ledgers returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ledgers_by_query_with_http_info(ledger_query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AffiliateLedgerQuery ledger_query: Ledger query (required)
        :param int limit: The maximum number of records to return on this one API call. (Maximum 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str expand: The object expansion to perform on the result.  Only option is link.
        :return: AffiliateLedgersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ledger_query', 'limit', 'offset', 'expand']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ledgers_by_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ledger_query' is set
        if ('ledger_query' not in params) or (params['ledger_query'] is None):
            raise ValueError("Missing the required parameter `ledger_query` when calling `get_ledgers_by_query`")

        resource_path = '/affiliate/ledgers/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['_limit'] = params['limit']
        if 'offset' in params:
            query_params['_offset'] = params['offset']
        if 'expand' in params:
            query_params['_expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ledger_query' in params:
            body_params = params['ledger_query']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AffiliateLedgersResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

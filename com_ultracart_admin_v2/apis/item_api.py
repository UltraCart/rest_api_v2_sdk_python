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


class ItemApi(object):
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

    def item_items_get(self, **kwargs):
        """
        Retrieve items
        Retrieves a group of items from the account.  If no parameters are specified, all items will be returned. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int parent_category_id: The parent category to retrieve items for.  Unspecified means all items on the account.  0 = root
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch items that have been created/modified since this date/time.
        :param str sort: The sort order of the items.  See documentation for examples
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: ItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_items_get_with_http_info(**kwargs)
        else:
            (data) = self.item_items_get_with_http_info(**kwargs)
            return data

    def item_items_get_with_http_info(self, **kwargs):
        """
        Retrieve items
        Retrieves a group of items from the account.  If no parameters are specified, all items will be returned. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int parent_category_id: The parent category to retrieve items for.  Unspecified means all items on the account.  0 = root
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch items that have been created/modified since this date/time.
        :param str sort: The sort order of the items.  See documentation for examples
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: ItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parent_category_id', 'limit', 'offset', 'since', 'sort', 'expand', 'placeholders']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_items_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/item/items'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'parent_category_id' in params:
            query_params['parent_category_id'] = params['parent_category_id']
        if 'limit' in params:
            query_params['_limit'] = params['limit']
        if 'offset' in params:
            query_params['_offset'] = params['offset']
        if 'since' in params:
            query_params['_since'] = params['since']
        if 'sort' in params:
            query_params['_sort'] = params['sort']
        if 'expand' in params:
            query_params['_expand'] = params['expand']
        if 'placeholders' in params:
            query_params['_placeholders'] = params['placeholders']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ItemsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def item_items_merchant_item_oid_delete(self, merchant_item_oid, **kwargs):
        """
        Delete an item
        Delete an item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_delete(merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int merchant_item_oid: The item oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_items_merchant_item_oid_delete_with_http_info(merchant_item_oid, **kwargs)
        else:
            (data) = self.item_items_merchant_item_oid_delete_with_http_info(merchant_item_oid, **kwargs)
            return data

    def item_items_merchant_item_oid_delete_with_http_info(self, merchant_item_oid, **kwargs):
        """
        Delete an item
        Delete an item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_delete_with_http_info(merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int merchant_item_oid: The item oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_item_oid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_items_merchant_item_oid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_item_oid' is set
        if ('merchant_item_oid' not in params) or (params['merchant_item_oid'] is None):
            raise ValueError("Missing the required parameter `merchant_item_oid` when calling `item_items_merchant_item_oid_delete`")

        resource_path = '/item/items/{merchant_item_oid}'.replace('{format}', 'json')
        path_params = {}
        if 'merchant_item_oid' in params:
            path_params['merchant_item_oid'] = params['merchant_item_oid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

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

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def item_items_merchant_item_oid_get(self, merchant_item_oid, **kwargs):
        """
        Retrieve an item
        Retrieves a single item using the specified item oid. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_get(merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int merchant_item_oid: The item oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_items_merchant_item_oid_get_with_http_info(merchant_item_oid, **kwargs)
        else:
            (data) = self.item_items_merchant_item_oid_get_with_http_info(merchant_item_oid, **kwargs)
            return data

    def item_items_merchant_item_oid_get_with_http_info(self, merchant_item_oid, **kwargs):
        """
        Retrieve an item
        Retrieves a single item using the specified item oid. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_get_with_http_info(merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int merchant_item_oid: The item oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_item_oid', 'expand', 'placeholders']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_items_merchant_item_oid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_item_oid' is set
        if ('merchant_item_oid' not in params) or (params['merchant_item_oid'] is None):
            raise ValueError("Missing the required parameter `merchant_item_oid` when calling `item_items_merchant_item_oid_get`")

        resource_path = '/item/items/{merchant_item_oid}'.replace('{format}', 'json')
        path_params = {}
        if 'merchant_item_oid' in params:
            path_params['merchant_item_oid'] = params['merchant_item_oid']

        query_params = {}
        if 'expand' in params:
            query_params['_expand'] = params['expand']
        if 'placeholders' in params:
            query_params['_placeholders'] = params['placeholders']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def item_items_merchant_item_oid_put(self, item, merchant_item_oid, **kwargs):
        """
        Update an item
        Update a new item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_put(item, merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Item item: Item to create (required)
        :param int merchant_item_oid: The item oid to update. (required)
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_items_merchant_item_oid_put_with_http_info(item, merchant_item_oid, **kwargs)
        else:
            (data) = self.item_items_merchant_item_oid_put_with_http_info(item, merchant_item_oid, **kwargs)
            return data

    def item_items_merchant_item_oid_put_with_http_info(self, item, merchant_item_oid, **kwargs):
        """
        Update an item
        Update a new item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_merchant_item_oid_put_with_http_info(item, merchant_item_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Item item: Item to create (required)
        :param int merchant_item_oid: The item oid to update. (required)
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item', 'merchant_item_oid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_items_merchant_item_oid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item' is set
        if ('item' not in params) or (params['item'] is None):
            raise ValueError("Missing the required parameter `item` when calling `item_items_merchant_item_oid_put`")
        # verify the required parameter 'merchant_item_oid' is set
        if ('merchant_item_oid' not in params) or (params['merchant_item_oid'] is None):
            raise ValueError("Missing the required parameter `merchant_item_oid` when calling `item_items_merchant_item_oid_put`")

        resource_path = '/item/items/{merchant_item_oid}'.replace('{format}', 'json')
        path_params = {}
        if 'merchant_item_oid' in params:
            path_params['merchant_item_oid'] = params['merchant_item_oid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item' in params:
            body_params = params['item']

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

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def item_items_post(self, item, **kwargs):
        """
        Create an item
        Create a new item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_post(item, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Item item: Item to create (required)
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_items_post_with_http_info(item, **kwargs)
        else:
            (data) = self.item_items_post_with_http_info(item, **kwargs)
            return data

    def item_items_post_with_http_info(self, item, **kwargs):
        """
        Create an item
        Create a new item on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_items_post_with_http_info(item, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Item item: Item to create (required)
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_items_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item' is set
        if ('item' not in params) or (params['item'] is None):
            raise ValueError("Missing the required parameter `item` when calling `item_items_post`")

        resource_path = '/item/items'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item' in params:
            body_params = params['item']

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
                                            response_type='ItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def item_temp_multimedia_post(self, file, **kwargs):
        """
        Upload an image to the temporary multimedia.
        Uploads an image and returns back meta information about the image as well as the identifier needed for the item update. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_temp_multimedia_post(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :return: TempMultimediaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.item_temp_multimedia_post_with_http_info(file, **kwargs)
        else:
            (data) = self.item_temp_multimedia_post_with_http_info(file, **kwargs)
            return data

    def item_temp_multimedia_post_with_http_info(self, file, **kwargs):
        """
        Upload an image to the temporary multimedia.
        Uploads an image and returns back meta information about the image as well as the identifier needed for the item update. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.item_temp_multimedia_post_with_http_info(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :return: TempMultimediaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method item_temp_multimedia_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `item_temp_multimedia_post`")

        resource_path = '/item/temp_multimedia'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TempMultimediaResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

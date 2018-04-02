# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class WebhookApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_webhook(self, webhook_oid, **kwargs):
        """
        Delete a webhook
        Delete a webhook on the UltraCart account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_webhook(webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_webhook_with_http_info(webhook_oid, **kwargs)
        else:
            (data) = self.delete_webhook_with_http_info(webhook_oid, **kwargs)
            return data

    def delete_webhook_with_http_info(self, webhook_oid, **kwargs):
        """
        Delete a webhook
        Delete a webhook on the UltraCart account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_webhook_with_http_info(webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_oid']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_oid' is set
        if ('webhook_oid' not in params) or (params['webhook_oid'] is None):
            raise ValueError("Missing the required parameter `webhook_oid` when calling `delete_webhook`")


        collection_formats = {}

        path_params = {}
        if 'webhook_oid' in params:
            path_params['webhookOid'] = params['webhook_oid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks/{webhookOid}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_webhook_log(self, webhook_oid, request_id, **kwargs):
        """
        Retrieve an individual log
        Retrieves an individual log for a webhook given the webhook oid the request id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook_log(webhook_oid, request_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid that owns the log. (required)
        :param str request_id: The request id associated with the log to view. (required)
        :return: WebhookLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_webhook_log_with_http_info(webhook_oid, request_id, **kwargs)
        else:
            (data) = self.get_webhook_log_with_http_info(webhook_oid, request_id, **kwargs)
            return data

    def get_webhook_log_with_http_info(self, webhook_oid, request_id, **kwargs):
        """
        Retrieve an individual log
        Retrieves an individual log for a webhook given the webhook oid the request id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook_log_with_http_info(webhook_oid, request_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid that owns the log. (required)
        :param str request_id: The request id associated with the log to view. (required)
        :return: WebhookLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_oid', 'request_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_oid' is set
        if ('webhook_oid' not in params) or (params['webhook_oid'] is None):
            raise ValueError("Missing the required parameter `webhook_oid` when calling `get_webhook_log`")
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params) or (params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_webhook_log`")


        collection_formats = {}

        path_params = {}
        if 'webhook_oid' in params:
            path_params['webhookOid'] = params['webhook_oid']
        if 'request_id' in params:
            path_params['requestId'] = params['request_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks/{webhookOid}/logs/{requestId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookLogResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_webhook_log_summaries(self, webhook_oid, **kwargs):
        """
        Retrieve the log summaries
        Retrieves the log summary information for a given webhook.  This is useful for displaying all the various logs that can be viewed. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook_log_summaries(webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid to retrieve log summaries for. (required)
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch log summaries that have been delivered since this date/time.
        :return: WebhookLogSummariesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_webhook_log_summaries_with_http_info(webhook_oid, **kwargs)
        else:
            (data) = self.get_webhook_log_summaries_with_http_info(webhook_oid, **kwargs)
            return data

    def get_webhook_log_summaries_with_http_info(self, webhook_oid, **kwargs):
        """
        Retrieve the log summaries
        Retrieves the log summary information for a given webhook.  This is useful for displaying all the various logs that can be viewed. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook_log_summaries_with_http_info(webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid to retrieve log summaries for. (required)
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch log summaries that have been delivered since this date/time.
        :return: WebhookLogSummariesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_oid', 'limit', 'offset', 'since']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_log_summaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_oid' is set
        if ('webhook_oid' not in params) or (params['webhook_oid'] is None):
            raise ValueError("Missing the required parameter `webhook_oid` when calling `get_webhook_log_summaries`")


        collection_formats = {}

        path_params = {}
        if 'webhook_oid' in params:
            path_params['webhookOid'] = params['webhook_oid']

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))
        if 'since' in params:
            query_params.append(('_since', params['since']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks/{webhookOid}/logs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookLogSummariesResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_webhooks(self, **kwargs):
        """
        Retrieve webhooks
        Retrieves the webhooks associated with this application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhooks(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the webhooks.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhooksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_webhooks_with_http_info(**kwargs)
        else:
            (data) = self.get_webhooks_with_http_info(**kwargs)
            return data

    def get_webhooks_with_http_info(self, **kwargs):
        """
        Retrieve webhooks
        Retrieves the webhooks associated with this application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhooks_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of records to return on this one API call.
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the webhooks.  See documentation for examples
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhooksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'sort', 'placeholders']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhooks" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))
        if 'sort' in params:
            query_params.append(('_sort', params['sort']))
        if 'placeholders' in params:
            query_params.append(('_placeholders', params['placeholders']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhooksResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def insert_webhook(self, webhook, **kwargs):
        """
        Add a webhook
        Adds a new webhook on the account.  If you add a new webhook with the authentication_type set to basic, but do not specify the basic_username and basic_password, UltraCart will automatically generate random ones and return them.  This allows your application to have simpler logic on the setup of a secure webhook. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_webhook(webhook, async=True)
        >>> result = thread.get()

        :param async bool
        :param Webhook webhook: Webhook to create (required)
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.insert_webhook_with_http_info(webhook, **kwargs)
        else:
            (data) = self.insert_webhook_with_http_info(webhook, **kwargs)
            return data

    def insert_webhook_with_http_info(self, webhook, **kwargs):
        """
        Add a webhook
        Adds a new webhook on the account.  If you add a new webhook with the authentication_type set to basic, but do not specify the basic_username and basic_password, UltraCart will automatically generate random ones and return them.  This allows your application to have simpler logic on the setup of a secure webhook. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_webhook_with_http_info(webhook, async=True)
        >>> result = thread.get()

        :param async bool
        :param Webhook webhook: Webhook to create (required)
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook', 'placeholders']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook' is set
        if ('webhook' not in params) or (params['webhook'] is None):
            raise ValueError("Missing the required parameter `webhook` when calling `insert_webhook`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'placeholders' in params:
            query_params.append(('_placeholders', params['placeholders']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook' in params:
            body_params = params['webhook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json; charset=UTF-8'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def resend_event(self, webhook_oid, event_name, **kwargs):
        """
        Resend events to the webhook endpoint.
        This method will resend events to the webhook endpoint.  This method can be used for example to send all the existing items on an account to a webhook. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resend_event(webhook_oid, event_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid that is receiving the reflowed events. (required)
        :param str event_name: The event to reflow. (required)
        :return: WebhookSampleRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resend_event_with_http_info(webhook_oid, event_name, **kwargs)
        else:
            (data) = self.resend_event_with_http_info(webhook_oid, event_name, **kwargs)
            return data

    def resend_event_with_http_info(self, webhook_oid, event_name, **kwargs):
        """
        Resend events to the webhook endpoint.
        This method will resend events to the webhook endpoint.  This method can be used for example to send all the existing items on an account to a webhook. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resend_event_with_http_info(webhook_oid, event_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int webhook_oid: The webhook oid that is receiving the reflowed events. (required)
        :param str event_name: The event to reflow. (required)
        :return: WebhookSampleRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_oid', 'event_name']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resend_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_oid' is set
        if ('webhook_oid' not in params) or (params['webhook_oid'] is None):
            raise ValueError("Missing the required parameter `webhook_oid` when calling `resend_event`")
        # verify the required parameter 'event_name' is set
        if ('event_name' not in params) or (params['event_name'] is None):
            raise ValueError("Missing the required parameter `event_name` when calling `resend_event`")


        collection_formats = {}

        path_params = {}
        if 'webhook_oid' in params:
            path_params['webhookOid'] = params['webhook_oid']
        if 'event_name' in params:
            path_params['eventName'] = params['event_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json; charset=UTF-8'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks/{webhookOid}/reflow/{eventName}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookSampleRequestResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_webhook(self, webhook, webhook_oid, **kwargs):
        """
        Update a webhook
        Update a webhook on the account 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_webhook(webhook, webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param Webhook webhook: Webhook to update (required)
        :param int webhook_oid: The webhook oid to update. (required)
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_webhook_with_http_info(webhook, webhook_oid, **kwargs)
        else:
            (data) = self.update_webhook_with_http_info(webhook, webhook_oid, **kwargs)
            return data

    def update_webhook_with_http_info(self, webhook, webhook_oid, **kwargs):
        """
        Update a webhook
        Update a webhook on the account 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_webhook_with_http_info(webhook, webhook_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param Webhook webhook: Webhook to update (required)
        :param int webhook_oid: The webhook oid to update. (required)
        :param bool placeholders: Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook', 'webhook_oid', 'placeholders']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook' is set
        if ('webhook' not in params) or (params['webhook'] is None):
            raise ValueError("Missing the required parameter `webhook` when calling `update_webhook`")
        # verify the required parameter 'webhook_oid' is set
        if ('webhook_oid' not in params) or (params['webhook_oid'] is None):
            raise ValueError("Missing the required parameter `webhook_oid` when calling `update_webhook`")


        collection_formats = {}

        path_params = {}
        if 'webhook_oid' in params:
            path_params['webhookOid'] = params['webhook_oid']

        query_params = []
        if 'placeholders' in params:
            query_params.append(('_placeholders', params['placeholders']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook' in params:
            body_params = params['webhook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json; charset=UTF-8'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/webhook/webhooks/{webhookOid}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

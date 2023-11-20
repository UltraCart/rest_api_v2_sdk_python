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

class WorkflowApi(object):
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
        return WorkflowApi(api_client)




    def get_workflow_assignment_groups(self, **kwargs):  # noqa: E501
        """Retrieve a list of groups that workflow tasks can be assigned to  # noqa: E501

        Retrieve a list of groups that workflow tasks can be assigned to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_assignment_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :return: WorkflowGroupsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_assignment_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_assignment_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_workflow_assignment_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of groups that workflow tasks can be assigned to  # noqa: E501

        Retrieve a list of groups that workflow tasks can be assigned to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_assignment_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :return: WorkflowGroupsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_assignment_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501

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
            '/workflow/assignment_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowGroupsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workflow_assignment_users(self, **kwargs):  # noqa: E501
        """Retrieve a list of users that workflow tasks can be assigned to  # noqa: E501

        Retrieve a list of users that workflow tasks can be assigned to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_assignment_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :return: WorkflowUsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_assignment_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_assignment_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_workflow_assignment_users_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of users that workflow tasks can be assigned to  # noqa: E501

        Retrieve a list of users that workflow tasks can be assigned to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_assignment_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :return: WorkflowUsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_assignment_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501

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
            '/workflow/assignment_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowUsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workflow_task(self, task_uuid, **kwargs):  # noqa: E501
        """Retrieve a workflow task  # noqa: E501

        Retrieve a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task(task_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_uuid: (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_task_with_http_info(task_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_task_with_http_info(task_uuid, **kwargs)  # noqa: E501
            return data

    def get_workflow_task_with_http_info(self, task_uuid, **kwargs):  # noqa: E501
        """Retrieve a workflow task  # noqa: E501

        Retrieve a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task_with_http_info(task_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_uuid: (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_uuid' is set
        if ('task_uuid' not in params or
                params['task_uuid'] is None):
            raise ValueError("Missing the required parameter `task_uuid` when calling `get_workflow_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_uuid' in params:
            path_params['task_uuid'] = params['task_uuid']  # noqa: E501

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
            '/workflow/tasks/{task_uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowTaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workflow_task_attachment_upload_url(self, extension, **kwargs):  # noqa: E501
        """Get a presigned workflow task attachment upload URL  # noqa: E501

        Get a presigned workflow task attachment upload URL   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task_attachment_upload_url(extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension: (required)
        :return: WorkflowAttachmentUploadUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_task_attachment_upload_url_with_http_info(extension, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_task_attachment_upload_url_with_http_info(extension, **kwargs)  # noqa: E501
            return data

    def get_workflow_task_attachment_upload_url_with_http_info(self, extension, **kwargs):  # noqa: E501
        """Get a presigned workflow task attachment upload URL  # noqa: E501

        Get a presigned workflow task attachment upload URL   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task_attachment_upload_url_with_http_info(extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str extension: (required)
        :return: WorkflowAttachmentUploadUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['extension']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_task_attachment_upload_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extension' is set
        if ('extension' not in params or
                params['extension'] is None):
            raise ValueError("Missing the required parameter `extension` when calling `get_workflow_task_attachment_upload_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'extension' in params:
            path_params['extension'] = params['extension']  # noqa: E501

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
            '/workflow/tasks/attachments/{extension}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowAttachmentUploadUrlResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workflow_task_by_object_type(self, object_type, object_id, **kwargs):  # noqa: E501
        """Retrieve a workflow task by object type and id  # noqa: E501

        Retrieve a workflow task by object type and id   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task_by_object_type(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_type: (required)
        :param str object_id: (required)
        :return: WorkflowTasksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_task_by_object_type_with_http_info(object_type, object_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_task_by_object_type_with_http_info(object_type, object_id, **kwargs)  # noqa: E501
            return data

    def get_workflow_task_by_object_type_with_http_info(self, object_type, object_id, **kwargs):  # noqa: E501
        """Retrieve a workflow task by object type and id  # noqa: E501

        Retrieve a workflow task by object type and id   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_task_by_object_type_with_http_info(object_type, object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_type: (required)
        :param str object_id: (required)
        :return: WorkflowTasksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_type', 'object_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_task_by_object_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'object_type' is set
        if ('object_type' not in params or
                params['object_type'] is None):
            raise ValueError("Missing the required parameter `object_type` when calling `get_workflow_task_by_object_type`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if ('object_id' not in params or
                params['object_id'] is None):
            raise ValueError("Missing the required parameter `object_id` when calling `get_workflow_task_by_object_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in params:
            path_params['object_type'] = params['object_type']  # noqa: E501
        if 'object_id' in params:
            path_params['object_id'] = params['object_id']  # noqa: E501

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
            '/workflow/tasks/by/{object_type}/{object_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowTasksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workflow_tasks(self, workflow_tasks_query, **kwargs):  # noqa: E501
        """Search workflow tasks  # noqa: E501

        Retrieves a set of workflow tasks from the account based on a query object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_tasks(workflow_tasks_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkflowTasksRequest workflow_tasks_query: Workflow tasks query (required)
        :param int limit: The maximum number of records to return on this one API call. (Default 100, Max 500)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :return: WorkflowTasksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_tasks_with_http_info(workflow_tasks_query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_tasks_with_http_info(workflow_tasks_query, **kwargs)  # noqa: E501
            return data

    def get_workflow_tasks_with_http_info(self, workflow_tasks_query, **kwargs):  # noqa: E501
        """Search workflow tasks  # noqa: E501

        Retrieves a set of workflow tasks from the account based on a query object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_tasks_with_http_info(workflow_tasks_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkflowTasksRequest workflow_tasks_query: Workflow tasks query (required)
        :param int limit: The maximum number of records to return on this one API call. (Default 100, Max 500)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :return: WorkflowTasksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_tasks_query', 'limit', 'offset', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_tasks_query' is set
        if ('workflow_tasks_query' not in params or
                params['workflow_tasks_query'] is None):
            raise ValueError("Missing the required parameter `workflow_tasks_query` when calling `get_workflow_tasks`")  # noqa: E501

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
        if 'workflow_tasks_query' in params:
            body_params = params['workflow_tasks_query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/workflow/tasks/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowTasksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_workflow_task(self, workflow_task, **kwargs):  # noqa: E501
        """Insert a workflow task  # noqa: E501

        Insert a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_workflow_task(workflow_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkflowTask workflow_task: workflow task (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.insert_workflow_task_with_http_info(workflow_task, **kwargs)  # noqa: E501
        else:
            (data) = self.insert_workflow_task_with_http_info(workflow_task, **kwargs)  # noqa: E501
            return data

    def insert_workflow_task_with_http_info(self, workflow_task, **kwargs):  # noqa: E501
        """Insert a workflow task  # noqa: E501

        Insert a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_workflow_task_with_http_info(workflow_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkflowTask workflow_task: workflow task (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_task']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_workflow_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_task' is set
        if ('workflow_task' not in params or
                params['workflow_task'] is None):
            raise ValueError("Missing the required parameter `workflow_task` when calling `insert_workflow_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workflow_task' in params:
            body_params = params['workflow_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/workflow/tasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowTaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_workflow_task(self, task_uuid, workflow_task, **kwargs):  # noqa: E501
        """Update a workflow task  # noqa: E501

        Update a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_workflow_task(task_uuid, workflow_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_uuid: (required)
        :param WorkflowTask workflow_task: Workflow task (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_workflow_task_with_http_info(task_uuid, workflow_task, **kwargs)  # noqa: E501
        else:
            (data) = self.update_workflow_task_with_http_info(task_uuid, workflow_task, **kwargs)  # noqa: E501
            return data

    def update_workflow_task_with_http_info(self, task_uuid, workflow_task, **kwargs):  # noqa: E501
        """Update a workflow task  # noqa: E501

        Update a workflow task   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_workflow_task_with_http_info(task_uuid, workflow_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_uuid: (required)
        :param WorkflowTask workflow_task: Workflow task (required)
        :return: WorkflowTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_uuid', 'workflow_task']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_workflow_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_uuid' is set
        if ('task_uuid' not in params or
                params['task_uuid'] is None):
            raise ValueError("Missing the required parameter `task_uuid` when calling `update_workflow_task`")  # noqa: E501
        # verify the required parameter 'workflow_task' is set
        if ('workflow_task' not in params or
                params['workflow_task'] is None):
            raise ValueError("Missing the required parameter `workflow_task` when calling `update_workflow_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_uuid' in params:
            path_params['task_uuid'] = params['task_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workflow_task' in params:
            body_params = params['workflow_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/workflow/tasks/{task_uuid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowTaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

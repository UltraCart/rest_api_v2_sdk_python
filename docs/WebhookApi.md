# ultracart.WebhookApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /webhook/webhooks/{webhookOid} | Delete a webhook
[**delete_webhook_by_url**](WebhookApi.md#delete_webhook_by_url) | **DELETE** /webhook/webhooks | Delete a webhook by URL
[**get_webhook_log**](WebhookApi.md#get_webhook_log) | **GET** /webhook/webhooks/{webhookOid}/logs/{requestId} | Retrieve an individual log
[**get_webhook_log_summaries**](WebhookApi.md#get_webhook_log_summaries) | **GET** /webhook/webhooks/{webhookOid}/logs | Retrieve the log summaries
[**get_webhooks**](WebhookApi.md#get_webhooks) | **GET** /webhook/webhooks | Retrieve webhooks
[**insert_webhook**](WebhookApi.md#insert_webhook) | **POST** /webhook/webhooks | Add a webhook
[**resend_event**](WebhookApi.md#resend_event) | **POST** /webhook/webhooks/{webhookOid}/reflow/{eventName} | Resend events to the webhook endpoint.
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /webhook/webhooks/{webhookOid} | Update a webhook


# **delete_webhook**
> delete_webhook(webhook_oid)

Delete a webhook

Delete a webhook on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook_oid = 1 # int | The webhook oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook
        api_instance.delete_webhook(webhook_oid)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to delete. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_by_url**
> WebhookResponse delete_webhook_by_url(webhook)

Delete a webhook by URL

Delete a webhook based upon the URL on the webhook_url matching an existing webhook. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.webhook import Webhook
from ultracart.model.webhook_response import WebhookResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook = Webhook(
        api_user_oid=1,
        api_version="2017-03-01",
        application_profile=ApiUserApplicationProfile(
            api_application_logo_url="api_application_logo_url_example",
            application_description="application_description_example",
            application_name="application_name_example",
            developer_name="developer_name_example",
            developer_website="developer_website_example",
        ),
        authentication_type="none",
        basic_password="basic_password_example",
        basic_username="basic_username_example",
        compress_events=True,
        consecutive_failures=1,
        disabled=True,
        event_categories=[
            WebhookEventCategory(
                any_subscribed=True,
                available_expansions=[
                    "available_expansions_example",
                ],
                event_category="event_category_example",
                events=[
                    WebhookEventSubscription(
                        comments="comments_example",
                        deprecated_flag=True,
                        discontinued_flag=True,
                        event_description="event_description_example",
                        event_name="event_name_example",
                        event_ruler="event_ruler_example",
                        expansion="expansion_example",
                        subscribed=True,
                        supports_reflow=True,
                        webhook_event_oid=1,
                    ),
                ],
                subscribed=True,
            ),
        ],
        iam_access_key="iam_access_key_example",
        iam_secret_key="iam_secret_key_example",
        maximum_events=1,
        maximum_size=1,
        merchant_id="merchant_id_example",
        next_retry_after="next_retry_after_example",
        pending=1,
        webhook_oid=1,
        webhook_url="webhook_url_example",
    ) # Webhook | Webhook to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook by URL
        api_response = api_instance.delete_webhook_by_url(webhook)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->delete_webhook_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook to delete |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_log**
> WebhookLogResponse get_webhook_log(webhook_oid, request_id)

Retrieve an individual log

Retrieves an individual log for a webhook given the webhook oid the request id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.webhook_log_response import WebhookLogResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook_oid = 1 # int | The webhook oid that owns the log.
    request_id = "requestId_example" # str | The request id associated with the log to view.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an individual log
        api_response = api_instance.get_webhook_log(webhook_oid, request_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid that owns the log. |
 **request_id** | **str**| The request id associated with the log to view. |

### Return type

[**WebhookLogResponse**](WebhookLogResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_log_summaries**
> WebhookLogSummariesResponse get_webhook_log_summaries(webhook_oid)

Retrieve the log summaries

Retrieves the log summary information for a given webhook.  This is useful for displaying all the various logs that can be viewed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.webhook_log_summaries_response import WebhookLogSummariesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook_oid = 1 # int | The webhook oid to retrieve log summaries for.
    limit = 100 # int | The maximum number of records to return on this one API call. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch log summaries that have been delivered since this date/time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the log summaries
        api_response = api_instance.get_webhook_log_summaries(webhook_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_log_summaries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the log summaries
        api_response = api_instance.get_webhook_log_summaries(webhook_oid, limit=limit, offset=offset, since=since)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_log_summaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to retrieve log summaries for. |
 **limit** | **int**| The maximum number of records to return on this one API call. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch log summaries that have been delivered since this date/time. | [optional]

### Return type

[**WebhookLogSummariesResponse**](WebhookLogSummariesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhooksResponse get_webhooks()

Retrieve webhooks

Retrieves the webhooks associated with this application. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.webhooks_response import WebhooksResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the webhooks.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve webhooks
        api_response = api_instance.get_webhooks(limit=limit, offset=offset, sort=sort, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->get_webhooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the webhooks.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_webhook**
> WebhookResponse insert_webhook(webhook)

Add a webhook

Adds a new webhook on the account.  If you add a new webhook with the authentication_type set to basic, but do not specify the basic_username and basic_password, UltraCart will automatically generate random ones and return them.  This allows your application to have simpler logic on the setup of a secure webhook. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.webhook import Webhook
from ultracart.model.webhook_response import WebhookResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook = Webhook(
        api_user_oid=1,
        api_version="2017-03-01",
        application_profile=ApiUserApplicationProfile(
            api_application_logo_url="api_application_logo_url_example",
            application_description="application_description_example",
            application_name="application_name_example",
            developer_name="developer_name_example",
            developer_website="developer_website_example",
        ),
        authentication_type="none",
        basic_password="basic_password_example",
        basic_username="basic_username_example",
        compress_events=True,
        consecutive_failures=1,
        disabled=True,
        event_categories=[
            WebhookEventCategory(
                any_subscribed=True,
                available_expansions=[
                    "available_expansions_example",
                ],
                event_category="event_category_example",
                events=[
                    WebhookEventSubscription(
                        comments="comments_example",
                        deprecated_flag=True,
                        discontinued_flag=True,
                        event_description="event_description_example",
                        event_name="event_name_example",
                        event_ruler="event_ruler_example",
                        expansion="expansion_example",
                        subscribed=True,
                        supports_reflow=True,
                        webhook_event_oid=1,
                    ),
                ],
                subscribed=True,
            ),
        ],
        iam_access_key="iam_access_key_example",
        iam_secret_key="iam_secret_key_example",
        maximum_events=1,
        maximum_size=1,
        merchant_id="merchant_id_example",
        next_retry_after="next_retry_after_example",
        pending=1,
        webhook_oid=1,
        webhook_url="webhook_url_example",
    ) # Webhook | Webhook to create
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a webhook
        api_response = api_instance.insert_webhook(webhook)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->insert_webhook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a webhook
        api_response = api_instance.insert_webhook(webhook, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->insert_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook to create |
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_event**
> WebhookReflowResponse resend_event(webhook_oid, event_name)

Resend events to the webhook endpoint.

This method will resend events to the webhook endpoint.  This method can be used for example to send all the existing items on an account to a webhook. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.webhook_reflow_response import WebhookReflowResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook_oid = 1 # int | The webhook oid that is receiving the reflowed events.
    event_name = "eventName_example" # str | The event to reflow.

    # example passing only required values which don't have defaults set
    try:
        # Resend events to the webhook endpoint.
        api_response = api_instance.resend_event(webhook_oid, event_name)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->resend_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid that is receiving the reflowed events. |
 **event_name** | **str**| The event to reflow. |

### Return type

[**WebhookReflowResponse**](WebhookReflowResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookResponse update_webhook(webhook_oid, webhook)

Update a webhook

Update a webhook on the account 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import webhook_api
from ultracart.model.webhook import Webhook
from ultracart.model.webhook_response import WebhookResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    webhook_oid = 1 # int | The webhook oid to update.
    webhook = Webhook(
        api_user_oid=1,
        api_version="2017-03-01",
        application_profile=ApiUserApplicationProfile(
            api_application_logo_url="api_application_logo_url_example",
            application_description="application_description_example",
            application_name="application_name_example",
            developer_name="developer_name_example",
            developer_website="developer_website_example",
        ),
        authentication_type="none",
        basic_password="basic_password_example",
        basic_username="basic_username_example",
        compress_events=True,
        consecutive_failures=1,
        disabled=True,
        event_categories=[
            WebhookEventCategory(
                any_subscribed=True,
                available_expansions=[
                    "available_expansions_example",
                ],
                event_category="event_category_example",
                events=[
                    WebhookEventSubscription(
                        comments="comments_example",
                        deprecated_flag=True,
                        discontinued_flag=True,
                        event_description="event_description_example",
                        event_name="event_name_example",
                        event_ruler="event_ruler_example",
                        expansion="expansion_example",
                        subscribed=True,
                        supports_reflow=True,
                        webhook_event_oid=1,
                    ),
                ],
                subscribed=True,
            ),
        ],
        iam_access_key="iam_access_key_example",
        iam_secret_key="iam_secret_key_example",
        maximum_events=1,
        maximum_size=1,
        merchant_id="merchant_id_example",
        next_retry_after="next_retry_after_example",
        pending=1,
        webhook_oid=1,
        webhook_url="webhook_url_example",
    ) # Webhook | Webhook to update
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a webhook
        api_response = api_instance.update_webhook(webhook_oid, webhook)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a webhook
        api_response = api_instance.update_webhook(webhook_oid, webhook, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to update. |
 **webhook** | [**Webhook**](Webhook.md)| Webhook to update |
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


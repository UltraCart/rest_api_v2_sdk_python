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
"""
deletes a webhook

You will need the webhook_oid to call this method.  Call getWebhooks() if you don't know your oid.
Returns status code 204 (No Content) on success
"""

from ultracart.apis import WebhookApi
from samples import api_client

# Create Webhook API instance
webhook_api = WebhookApi(api_client())

# webhook_oid to delete (call getWebhooks if you don't know this)
webhook_oid = 123456789

# Delete the webhook
webhook_api.delete_webhook(webhook_oid=webhook_oid)
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
"""
This method can be confusing due to its payload.  The method does indeed delete a webhook by url, but you need to
pass a webhook object in as the payload.  However, only the url is used.  UltraCart does this to avoid any confusion
with the rest url versus the webhook url.

To use:
Get your webhook url.
Create a Webhook object.
Set the Webhook url property.
Pass the webhook to deleteWebhookByUrl()

Returns status code 204 (No Content) on success
"""

from ultracart.apis import WebhookApi
from ultracart.models import Webhook
from samples import api_client

# Create Webhook API instance
webhook_api = WebhookApi(api_client())

# Webhook URL to delete
webhook_url = "https://www.mywebiste.com/page/to/call/when/this/webhook/fires.php"

# Create Webhook object with the URL
webhook = Webhook(webhook_url=webhook_url)

# Delete webhook by URL
webhook_api.delete_webhook_by_url(webhook)
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
"""
getWebhookLog() provides a detail log of a webhook event.  It is used in tandem with getWebhookLogSummaries to audit
webhook events.  This method call will require the webhook_oid and the request_id.  The webhook_oid can be discerned
from the results of getWebhooks() and the request_id can be found from getWebhookLogSummaries().  see those examples
if needed.
"""

from ultracart.apis import WebhookApi
from samples import api_client

# Create Webhook API instance
webhook_api = WebhookApi(api_client())

# webhook_oid and request_id (call getWebhooks and getWebhookLogSummaries if you don't know these)
webhook_oid = 123456789
request_id = '987654321'

# Get webhook log
api_response = webhook_api.get_webhook_log(webhook_oid=webhook_oid, request_id=request_id)
webhook_log = api_response.webhook_log

# Check for errors
if api_response.error:
   print(f"Developer Message: {api_response.error.developer_message}")
   print(f"User Message: {api_response.error.user_message}")
else:
   # Print webhook log
   print(webhook_log)
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
"""
This example illustrates how to retrieve webhook log summaries.
"""

from datetime import datetime, timedelta
from ultracart.apis import WebhookApi
from ultracart.exceptions import ApiException
from samples import api_client


def get_summary_chunk(webhook_api, offset, limit):
    """Retrieve a chunk of webhook log summaries."""
    webhook_oid = 123456789  # Use getWebhooks to find your webhook's oid
    _since = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT00:00:00+00:00')

    api_response = webhook_api.get_webhook_log_summaries(webhook_oid=webhook_oid, limit=limit, offset=offset,
                                                         since=_since)
    return api_response.webhook_log_summaries or []


def retrieve_all_summaries():
    """Retrieve all webhook log summaries in chunks."""
    webhook_api = WebhookApi(api_client())

    summaries = []
    iteration = 1
    offset = 0
    limit = 200

    try:
        while True:
            print(f"executing iteration {iteration}")

            chunk_of_summaries = get_summary_chunk(webhook_api, offset, limit)
            summaries.extend(chunk_of_summaries)

            offset += limit
            if len(chunk_of_summaries) < limit:
                break

            iteration += 1

    except ApiException as e:
        print(f'ApiException occurred on iteration {iteration}')
        print(e)
        return None

    return summaries


# Retrieve and print summaries
all_summaries = retrieve_all_summaries()
if all_summaries is not None:
    print(all_summaries)
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
"""
This example illustrates how to retrieve all webhooks.
"""

from ultracart.apis import WebhookApi
from ultracart.exceptions import ApiException
from samples import api_client


def get_webhook_chunk(webhook_api, offset, limit):
    """Retrieve a chunk of webhooks."""
    _sort = None  # default sorting is webhook_url, disabled
    _placeholders = None  # useful for UI displays, but not needed here

    api_response = webhook_api.get_webhooks(limit=limit, offset=offset, sort=_sort, placeholders=_placeholders)
    return api_response.webhooks or []


def retrieve_all_webhooks():
    """Retrieve all webhooks in chunks."""
    webhook_api = WebhookApi(api_client())

    webhooks = []
    iteration = 1
    offset = 0
    limit = 200

    try:
        while True:
            print(f"executing iteration {iteration}")

            chunk_of_webhooks = get_webhook_chunk(webhook_api, offset, limit)
            webhooks.extend(chunk_of_webhooks)

            offset += limit
            if len(chunk_of_webhooks) < limit:
                break

            iteration += 1

    except ApiException as e:
        print(f'ApiException occurred on iteration {iteration}')
        print(e)
        return None

    return webhooks


# Retrieve and print webhooks
all_webhooks = retrieve_all_webhooks()
if all_webhooks is not None:
    print(all_webhooks)
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
"""
Adds a new webhook on the account with multiple event subscriptions.
"""

from ultracart.apis import WebhookApi
from ultracart.models import Webhook, WebhookEventCategory, WebhookEventSubscription
from samples import api_client

def create_webhook():
    webhook_api = WebhookApi(api_client())

    # Configure webhook
    webhook = Webhook(
        webhook_url="https://www.mywebiste.com/page/to/call/when/this/webhook/fires.php",
        authentication_type="basic",
        basic_username="george",
        basic_password="LlamaLlamaRedPajama",
        maximum_events=10,
        maximum_size=5242880,  # 5 MB
        api_version="2017-03-01",
        compress_events=True
    )

    # Define event subscriptions
    event_subs = [
        WebhookEventSubscription(
            event_name="order_create",
            event_description="when an order is placed",
            expansion="shipping,billing,item,coupon,summary",
            event_ruler=None,
            comments="Merchant specific comment about webhook"
        ),
        WebhookEventSubscription(
            event_name="order_update",
            event_description="when an order is modified",
            expansion="shipping,billing,item,coupon,summary",
            event_ruler=None,
            comments="Merchant specific comment about webhook"
        ),
        WebhookEventSubscription(
            event_name="order_delete",
            event_description="when an order is deleted",
            expansion="",
            event_ruler=None,
            comments="Merchant specific comment about webhook"
        )
    ]

    # Create event category
    event_category = WebhookEventCategory(
        event_category="order",
        events=event_subs
    )

    # Insert webhook
    api_response = webhook_api.insert_webhook(webhook, False)

    if api_response.error:
        print(f"Developer Message: {api_response.error.developer_message}")
        print(f"User Message: {api_response.error.user_message}")
        return None

    return api_response.webhook

# Execute webhook creation
created_webhook = create_webhook()
if created_webhook:
    print(created_webhook)
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
"""
Resend a specific event for a webhook to reflow all historical data.
Supports 'item_update' and 'order_create' events.
"""

from ultracart.apis import WebhookApi
from samples import api_client

def resend_webhook_event():
   webhook_api = WebhookApi(api_client())

   webhook_oid = 123456789  # Use getWebhooks to find your webhook's oid
   event_name = "item_update"  # or "order_create"

   api_response = webhook_api.resend_event(webhook_oid=webhook_oid, event_name=event_name)

   if api_response.error:
       print(f"Developer Message: {api_response.error.developer_message}")
       print(f"User Message: {api_response.error.user_message}")
       return None

   reflow = api_response.reflow
   success = reflow.queued

   return api_response

# Execute event resend
result = resend_webhook_event()
if result:
   print(result)
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
"""
Update a webhook's basic password by retrieving the existing webhook first.
"""

from ultracart.apis import WebhookApi
from samples import api_client

def update_webhook():
   webhook_api = WebhookApi(api_client())

   # Webhook OID to update
   webhook_oid = 123456789

   # Retrieve existing webhooks and find the target
   webhooks = webhook_api.get_webhooks(limit=100, offset=0).webhooks
   webhook_to_update = next((w for w in webhooks if w.webhook_oid == webhook_oid), None)

   if not webhook_to_update:
       print(f"Webhook with OID {webhook_oid} not found")
       return None

   # Update basic password
   webhook_to_update.basic_password = "new password here"

   # Perform update
   api_response = webhook_api.update_webhook(webhook_oid=webhook_oid, webhook=webhook_to_update)

   if api_response.error:
       print(f"Developer Message: {api_response.error.developer_message}")
       print(f"User Message: {api_response.error.user_message}")
       return None

   return api_response.webhook

# Execute webhook update
updated_webhook = update_webhook()
if updated_webhook:
   print(updated_webhook)
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


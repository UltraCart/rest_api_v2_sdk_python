# ultracart.WebhookApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_webhooks_get**](WebhookApi.md#webhook_webhooks_get) | **GET** /webhook/webhooks | Retrieve webhooks
[**webhook_webhooks_post**](WebhookApi.md#webhook_webhooks_post) | **POST** /webhook/webhooks | Add a webhook
[**webhook_webhooks_webhook_oid_delete**](WebhookApi.md#webhook_webhooks_webhook_oid_delete) | **DELETE** /webhook/webhooks/{webhookOid} | Delete a webhook
[**webhook_webhooks_webhook_oid_logs_get**](WebhookApi.md#webhook_webhooks_webhook_oid_logs_get) | **GET** /webhook/webhooks/{webhookOid}/logs | Retrieve the log summaries
[**webhook_webhooks_webhook_oid_logs_request_id_get**](WebhookApi.md#webhook_webhooks_webhook_oid_logs_request_id_get) | **GET** /webhook/webhooks/{webhookOid}/logs/{requestId} | Retrieve an individual log
[**webhook_webhooks_webhook_oid_put**](WebhookApi.md#webhook_webhooks_webhook_oid_put) | **PUT** /webhook/webhooks/{webhookOid} | Update a webhook
[**webhook_webhooks_webhook_oid_reflow_event_name_post**](WebhookApi.md#webhook_webhooks_webhook_oid_reflow_event_name_post) | **POST** /webhook/webhooks/{webhookOid}/reflow/{eventName} | Resend events to the webhook endpoint.


# **webhook_webhooks_get**
> WebhooksResponse webhook_webhooks_get(limit=limit, offset=offset, sort=sort, placeholders=placeholders)

Retrieve webhooks

Retrieves the webhooks associated with this application. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
limit = 100 # int | The maximum number of records to return on this one API call. (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the webhooks.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try: 
    # Retrieve webhooks
    api_response = api_instance.webhook_webhooks_get(limit=limit, offset=offset, sort=sort, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the webhooks.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_post**
> WebhookResponse webhook_webhooks_post(webhook, placeholders=placeholders)

Add a webhook

Adds a new webhook on the account.  If you add a new webhook with the authentication_type set to basic, but do not specify the basic_username and basic_password, UltraCart will automatically generate random ones and return them.  This allows your application to have simpler logic on the setup of a secure webhook. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook = ultracart.Webhook() # Webhook | Webhook to create
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try: 
    # Add a webhook
    api_response = api_instance.webhook_webhooks_post(webhook, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_post: %s\n" % e
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_delete**
> webhook_webhooks_webhook_oid_delete(webhook_oid)

Delete a webhook

Delete a webhook on the UltraCart account. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook_oid = 56 # int | The webhook oid to delete.

try: 
    # Delete a webhook
    api_instance.webhook_webhooks_webhook_oid_delete(webhook_oid)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_delete: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_logs_get**
> WebhookLogSummariesResponse webhook_webhooks_webhook_oid_logs_get(webhook_oid, limit=limit, offset=offset, since=since)

Retrieve the log summaries

Retrieves the log summary information for a given webhook.  This is useful for displaying all the various logs that can be viewed. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook_oid = 56 # int | The webhook oid to retrieve log summaries for.
limit = 100 # int | The maximum number of records to return on this one API call. (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch log summaries that have been delivered since this date/time. (optional)

try: 
    # Retrieve the log summaries
    api_response = api_instance.webhook_webhooks_webhook_oid_logs_get(webhook_oid, limit=limit, offset=offset, since=since)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_logs_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to retrieve log summaries for. | 
 **limit** | **int**| The maximum number of records to return on this one API call. | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch log summaries that have been delivered since this date/time. | [optional] 

### Return type

[**WebhookLogSummariesResponse**](WebhookLogSummariesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_logs_request_id_get**
> WebhookLogResponse webhook_webhooks_webhook_oid_logs_request_id_get(webhook_oid, request_id)

Retrieve an individual log

Retrieves an individual log for a webhook given the webhook oid the request id. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook_oid = 56 # int | The webhook oid that owns the log.
request_id = 'request_id_example' # str | The request id associated with the log to view.

try: 
    # Retrieve an individual log
    api_response = api_instance.webhook_webhooks_webhook_oid_logs_request_id_get(webhook_oid, request_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_logs_request_id_get: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_put**
> WebhookResponse webhook_webhooks_webhook_oid_put(webhook, webhook_oid, placeholders=placeholders)

Update a webhook

Update a webhook on the account 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook = ultracart.Webhook() # Webhook | Webhook to update
webhook_oid = 56 # int | The webhook oid to update.
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try: 
    # Update a webhook
    api_response = api_instance.webhook_webhooks_webhook_oid_put(webhook, webhook_oid, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook to update | 
 **webhook_oid** | **int**| The webhook oid to update. | 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_reflow_event_name_post**
> WebhookSampleRequestResponse webhook_webhooks_webhook_oid_reflow_event_name_post(webhook_oid, event_name)

Resend events to the webhook endpoint.

This method will resend events to the webhook endpoint.  This method can be used for example to send all the existing items on an account to a webhook. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.WebhookApi()
webhook_oid = 56 # int | The webhook oid that is receiving the reflowed events.
event_name = 'event_name_example' # str | The event to reflow.

try: 
    # Resend events to the webhook endpoint.
    api_response = api_instance.webhook_webhooks_webhook_oid_reflow_event_name_post(webhook_oid, event_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_reflow_event_name_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid that is receiving the reflowed events. | 
 **event_name** | **str**| The event to reflow. | 

### Return type

[**WebhookSampleRequestResponse**](WebhookSampleRequestResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


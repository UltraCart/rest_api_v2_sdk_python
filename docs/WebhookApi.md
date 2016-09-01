# com_ultracart_admin_v2.WebhookApi

All URIs are relative to *https://secure.ultracart.com/rest/admin/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_webhooks_get**](WebhookApi.md#webhook_webhooks_get) | **GET** /webhook/webhooks | Retrieve webhooks
[**webhook_webhooks_post**](WebhookApi.md#webhook_webhooks_post) | **POST** /webhook/webhooks | Add a webhook
[**webhook_webhooks_webhook_oid_delete**](WebhookApi.md#webhook_webhooks_webhook_oid_delete) | **DELETE** /webhook/webhooks/{webhookOid} | Delete a webhook
[**webhook_webhooks_webhook_oid_logs_get**](WebhookApi.md#webhook_webhooks_webhook_oid_logs_get) | **GET** /webhook/webhooks/{webhookOid}/logs | Retrieve the log summaries
[**webhook_webhooks_webhook_oid_logs_request_id_get**](WebhookApi.md#webhook_webhooks_webhook_oid_logs_request_id_get) | **GET** /webhook/webhooks/{webhookOid}/logs/{requestId} | Retrieve an individual log
[**webhook_webhooks_webhook_oid_put**](WebhookApi.md#webhook_webhooks_webhook_oid_put) | **PUT** /webhook/webhooks/{webhookOid} | Update a webhook
[**webhook_webhooks_webhook_oid_reflow_event_name_post**](WebhookApi.md#webhook_webhooks_webhook_oid_reflow_event_name_post) | **POST** /webhook/webhooks/{webhookOid}/reflow/{eventName} | Resend events to the webhook endpoint.
[**webhook_webhooks_webhook_oid_samples_get**](WebhookApi.md#webhook_webhooks_webhook_oid_samples_get) | **GET** /webhook/webhooks/{webhookOid}/samples | Retrieve a sample notification.
[**webhook_webhooks_webhook_oid_validate_post**](WebhookApi.md#webhook_webhooks_webhook_oid_validate_post) | **POST** /webhook/webhooks/{webhookOid}/validate | Send test message to an endpoint.


# **webhook_webhooks_get**
> WebhooksResponse webhook_webhooks_get()

Retrieve webhooks

Retrieves the webhooks associated with this application. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()

try: 
    # Retrieve webhooks
    api_response = api_instance.webhook_webhooks_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_post**
> WebhooksResponse webhook_webhooks_post(webhook)

Add a webhook

Adds a new webhook on the account 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
webhook = com_ultracart_admin_v2.Webhook() # Webhook | Webhook to create

try: 
    # Add a webhook
    api_response = api_instance.webhook_webhooks_post(webhook)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook to create | 

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_delete**
> webhook_webhooks_webhook_oid_delete(webhook_oid)

Delete a webhook

Delete a webhook on the UltraCart account. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
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
> WebhookLogSummariesResponse webhook_webhooks_webhook_oid_logs_get(webhook_oid)

Retrieve the log summaries

Retrieves the log summary information for a given webhook.  This is useful for displaying all the various logs that can be viewed. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
webhook_oid = 56 # int | The webhook oid to retrieve log summaries for.

try: 
    # Retrieve the log summaries
    api_response = api_instance.webhook_webhooks_webhook_oid_logs_get(webhook_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_logs_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to retrieve log summaries for. | 

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
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
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
> WebhooksResponse webhook_webhooks_webhook_oid_put(webhook, webhook_oid)

Update a webhook

Update a webhook on the account 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
webhook = com_ultracart_admin_v2.Webhook() # Webhook | Webhook to update
webhook_oid = 56 # int | The webhook oid to update.

try: 
    # Update a webhook
    api_response = api_instance.webhook_webhooks_webhook_oid_put(webhook, webhook_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook to update | 
 **webhook_oid** | **int**| The webhook oid to update. | 

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_reflow_event_name_post**
> WebhookSampleRequestResponse webhook_webhooks_webhook_oid_reflow_event_name_post(webhook_oid, event_name)

Resend events to the webhook endpoint.

This method will resend events to the webhook endpoint.  This method can be used for example to send all the existing items on an account to a webhook. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_samples_get**
> WebhookSampleRequestResponse webhook_webhooks_webhook_oid_samples_get(webhook_oid)

Retrieve a sample notification.

Retrieves a sample notification for the webhook.  This provides as example of what the notifications that can be delivered will look like. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
webhook_oid = 56 # int | The webhook oid to retrieve samples for.

try: 
    # Retrieve a sample notification.
    api_response = api_instance.webhook_webhooks_webhook_oid_samples_get(webhook_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_samples_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_oid** | **int**| The webhook oid to retrieve samples for. | 

### Return type

[**WebhookSampleRequestResponse**](WebhookSampleRequestResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_webhooks_webhook_oid_validate_post**
> WebhookLogResponse webhook_webhooks_webhook_oid_validate_post(samples, webhook_oid)

Send test message to an endpoint.

Performs a test of the webhook endpoint given the specified sample request and returns the log associated with the response. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.WebhookApi()
samples = com_ultracart_admin_v2.WebhookSampleRequest() # WebhookSampleRequest | Samples to send in the test
webhook_oid = 56 # int | The webhook oid that is being tested.

try: 
    # Send test message to an endpoint.
    api_response = api_instance.webhook_webhooks_webhook_oid_validate_post(samples, webhook_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookApi->webhook_webhooks_webhook_oid_validate_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **samples** | [**WebhookSampleRequest**](WebhookSampleRequest.md)| Samples to send in the test | 
 **webhook_oid** | **int**| The webhook oid that is being tested. | 

### Return type

[**WebhookLogResponse**](WebhookLogResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ultracart.ChargebackApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargeback_chargebacks_chargeback_dispute_oid_delete**](ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_delete) | **DELETE** /chargeback/chargebacks/{chargeback_dispute_oid} | Delete a chargeback
[**chargeback_chargebacks_chargeback_dispute_oid_get**](ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_get) | **GET** /chargeback/chargebacks/{chargeback_dispute_oid} | Retrieve a chargeback
[**chargeback_chargebacks_chargeback_dispute_oid_put**](ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_put) | **PUT** /chargeback/chargebacks/{chargeback_dispute_oid} | Update a chargeback
[**chargeback_chargebacks_get**](ChargebackApi.md#chargeback_chargebacks_get) | **GET** /chargeback/chargebacks | Retrieve chargebacks
[**chargeback_chargebacks_post**](ChargebackApi.md#chargeback_chargebacks_post) | **POST** /chargeback/chargebacks | Insert a chargeback


# **chargeback_chargebacks_chargeback_dispute_oid_delete**
> ChargebackDisputeResponse chargeback_chargebacks_chargeback_dispute_oid_delete(chargeback_dispute_oid)

Delete a chargeback

Delete a chargeback on the UltraCart account. 

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
api_instance = ultracart.ChargebackApi()
chargeback_dispute_oid = 56 # int | The chargeback_dispute_oid to delete.

try: 
    # Delete a chargeback
    api_response = api_instance.chargeback_chargebacks_chargeback_dispute_oid_delete(chargeback_dispute_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargebackApi->chargeback_chargebacks_chargeback_dispute_oid_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chargeback_dispute_oid** | **int**| The chargeback_dispute_oid to delete. | 

### Return type

[**ChargebackDisputeResponse**](ChargebackDisputeResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chargeback_chargebacks_chargeback_dispute_oid_get**
> ChargebackDisputeResponse chargeback_chargebacks_chargeback_dispute_oid_get(chargeback_dispute_oid, expand=expand)

Retrieve a chargeback

Retrieves a single chargeback using the specified chargeback dispute oid. 

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
api_instance = ultracart.ChargebackApi()
chargeback_dispute_oid = 56 # int | The chargeback dispute oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve a chargeback
    api_response = api_instance.chargeback_chargebacks_chargeback_dispute_oid_get(chargeback_dispute_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargebackApi->chargeback_chargebacks_chargeback_dispute_oid_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chargeback_dispute_oid** | **int**| The chargeback dispute oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**ChargebackDisputeResponse**](ChargebackDisputeResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chargeback_chargebacks_chargeback_dispute_oid_put**
> ChargebackDisputeResponse chargeback_chargebacks_chargeback_dispute_oid_put(chargeback, chargeback_dispute_oid)

Update a chargeback

Update a chargeback on the UltraCart account. 

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
api_instance = ultracart.ChargebackApi()
chargeback = ultracart.ChargebackDispute() # ChargebackDispute | Chargeback to update
chargeback_dispute_oid = 56 # int | The chargeback_dispute_oid to update.

try: 
    # Update a chargeback
    api_response = api_instance.chargeback_chargebacks_chargeback_dispute_oid_put(chargeback, chargeback_dispute_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargebackApi->chargeback_chargebacks_chargeback_dispute_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chargeback** | [**ChargebackDispute**](ChargebackDispute.md)| Chargeback to update | 
 **chargeback_dispute_oid** | **int**| The chargeback_dispute_oid to update. | 

### Return type

[**ChargebackDisputeResponse**](ChargebackDisputeResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chargeback_chargebacks_get**
> ChargebackDisputesResponse chargeback_chargebacks_get(order_id=order_id, case_number=case_number, status=status, expiration_dts_start=expiration_dts_start, expiration_dts_end=expiration_dts_end, chargeback_dts_start=chargeback_dts_start, chargeback_dts_end=chargeback_dts_end, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve chargebacks

Retrieves chargebacks from the account.  If no parameters are specified, all chargebacks will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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
api_instance = ultracart.ChargebackApi()
order_id = 'order_id_example' # str | Order Id (optional)
case_number = 'case_number_example' # str | Case number (optional)
status = 'status_example' # str | Status (optional)
expiration_dts_start = 'expiration_dts_start_example' # str | Expiration dts start (optional)
expiration_dts_end = 'expiration_dts_end_example' # str | Expiration dts end (optional)
chargeback_dts_start = 'chargeback_dts_start_example' # str | Chargeback dts start (optional)
chargeback_dts_end = 'chargeback_dts_end_example' # str | Chargeback dts end (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch chargebacks that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the chargebacks.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve chargebacks
    api_response = api_instance.chargeback_chargebacks_get(order_id=order_id, case_number=case_number, status=status, expiration_dts_start=expiration_dts_start, expiration_dts_end=expiration_dts_end, chargeback_dts_start=chargeback_dts_start, chargeback_dts_end=chargeback_dts_end, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargebackApi->chargeback_chargebacks_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order Id | [optional] 
 **case_number** | **str**| Case number | [optional] 
 **status** | **str**| Status | [optional] 
 **expiration_dts_start** | **str**| Expiration dts start | [optional] 
 **expiration_dts_end** | **str**| Expiration dts end | [optional] 
 **chargeback_dts_start** | **str**| Chargeback dts start | [optional] 
 **chargeback_dts_end** | **str**| Chargeback dts end | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch chargebacks that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the chargebacks.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**ChargebackDisputesResponse**](ChargebackDisputesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chargeback_chargebacks_post**
> ChargebackDisputeResponse chargeback_chargebacks_post(chargeback)

Insert a chargeback

Insert a chargeback on the UltraCart account. 

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
api_instance = ultracart.ChargebackApi()
chargeback = ultracart.ChargebackDispute() # ChargebackDispute | Chargeback to insert

try: 
    # Insert a chargeback
    api_response = api_instance.chargeback_chargebacks_post(chargeback)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargebackApi->chargeback_chargebacks_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chargeback** | [**ChargebackDispute**](ChargebackDispute.md)| Chargeback to insert | 

### Return type

[**ChargebackDisputeResponse**](ChargebackDisputeResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


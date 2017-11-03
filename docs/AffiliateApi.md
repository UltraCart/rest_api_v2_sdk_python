# ultracart.AffiliateApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clicks_by_query**](AffiliateApi.md#get_clicks_by_query) | **POST** /affiliate/clicks/query | Retrieve clicks
[**get_ledgers_by_query**](AffiliateApi.md#get_ledgers_by_query) | **POST** /affiliate/ledgers/query | Retrieve ledger entries


# **get_clicks_by_query**
> AffiliateClicksResponse get_clicks_by_query(click_query, limit=limit, offset=offset, expand=expand)

Retrieve clicks

Retrieves a group of clicks from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the clicks returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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
api_instance = ultracart.AffiliateApi()
click_query = ultracart.AffiliateClickQuery() # AffiliateClickQuery | Click query
limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) (default to 10000)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
expand = 'expand_example' # str | The object expansion to perform on the result.  Only option is link. (optional)

try: 
    # Retrieve clicks
    api_response = api_instance.get_clicks_by_query(click_query, limit=limit, offset=offset, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AffiliateApi->get_clicks_by_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_query** | [**AffiliateClickQuery**](AffiliateClickQuery.md)| Click query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] [default to 10000]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **expand** | **str**| The object expansion to perform on the result.  Only option is link. | [optional] 

### Return type

[**AffiliateClicksResponse**](AffiliateClicksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledgers_by_query**
> AffiliateLedgersResponse get_ledgers_by_query(ledger_query, limit=limit, offset=offset, expand=expand)

Retrieve ledger entries

Retrieves a group of ledger entries from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the ledgers returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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
api_instance = ultracart.AffiliateApi()
ledger_query = ultracart.AffiliateLedgerQuery() # AffiliateLedgerQuery | Ledger query
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
expand = 'expand_example' # str | The object expansion to perform on the result.  Only option is link. (optional)

try: 
    # Retrieve ledger entries
    api_response = api_instance.get_ledgers_by_query(ledger_query, limit=limit, offset=offset, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AffiliateApi->get_ledgers_by_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_query** | [**AffiliateLedgerQuery**](AffiliateLedgerQuery.md)| Ledger query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **expand** | **str**| The object expansion to perform on the result.  Only option is link. | [optional] 

### Return type

[**AffiliateLedgersResponse**](AffiliateLedgersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


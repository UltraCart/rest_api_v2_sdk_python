# com_ultracart_admin_v2.OauthApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_revoke_post**](OauthApi.md#oauth_revoke_post) | **POST** /oauth/revoke | Revoke this OAuth application.
[**oauth_token_post**](OauthApi.md#oauth_token_post) | **POST** /oauth/token | Exchange authorization code for access token.


# **oauth_revoke_post**
> OauthRevokeSuccessResponse oauth_revoke_post(client_id, token)

Revoke this OAuth application.

Revokes the OAuth application associated with the specified client_id and token. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.OauthApi()
client_id = 'client_id_example' # str | The OAuth application client_id.
token = 'token_example' # str | The OAuth access token that is to be revoked..

try: 
    # Revoke this OAuth application.
    api_response = api_instance.oauth_revoke_post(client_id, token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OauthApi->oauth_revoke_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The OAuth application client_id. | 
 **token** | **str**| The OAuth access token that is to be revoked.. | 

### Return type

[**OauthRevokeSuccessResponse**](OauthRevokeSuccessResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token_post**
> OauthTokenResponse oauth_token_post(client_id, grant_type, code=code, redirect_uri=redirect_uri, refresh_token=refresh_token)

Exchange authorization code for access token.

The final leg in the OAuth process which exchanges the specified access token for the access code needed to make API calls. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.OauthApi()
client_id = 'client_id_example' # str | The OAuth application client_id.
grant_type = 'grant_type_example' # str | Type of grant
code = 'code_example' # str | Authorization code received back from the browser redirect (optional)
redirect_uri = 'redirect_uri_example' # str | The URI that you redirect the browser to to start the authorization process (optional)
refresh_token = 'refresh_token_example' # str | The refresh token received during the original grant_type=authorization_code that can be used to return a new access token (optional)

try: 
    # Exchange authorization code for access token.
    api_response = api_instance.oauth_token_post(client_id, grant_type, code=code, redirect_uri=redirect_uri, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OauthApi->oauth_token_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The OAuth application client_id. | 
 **grant_type** | **str**| Type of grant | 
 **code** | **str**| Authorization code received back from the browser redirect | [optional] 
 **redirect_uri** | **str**| The URI that you redirect the browser to to start the authorization process | [optional] 
 **refresh_token** | **str**| The refresh token received during the original grant_type&#x3D;authorization_code that can be used to return a new access token | [optional] 

### Return type

[**OauthTokenResponse**](OauthTokenResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


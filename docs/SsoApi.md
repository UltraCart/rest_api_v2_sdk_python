# ultracart.SsoApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sso_session_user**](SsoApi.md#get_sso_session_user) | **GET** /sso/session/user | Get single sign on session user
[**sso_authorize**](SsoApi.md#sso_authorize) | **PUT** /sso/authorize | Authorize a single sign on session
[**sso_session_revoke**](SsoApi.md#sso_session_revoke) | **DELETE** /sso/session/revoke | Revoke single sign on session
[**sso_token**](SsoApi.md#sso_token) | **PUT** /sso/token | Exchange a single sign on code for a simple key token


# **get_sso_session_user**
> User get_sso_session_user()

Get single sign on session user

This is the equivalent of logging out of the single sign on session 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.SsoApi.fromApiKey(simple_key, False, True)


try:
    # Get single sign on session user
    api_response = api_instance.get_sso_session_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoApi->get_sso_session_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sso_authorize**
> SingleSignOnAuthorizeResponse sso_authorize(authorization_request)

Authorize a single sign on session

Starts the process of authorizing a single sign on session. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.SsoApi.fromApiKey(simple_key, False, True)

authorization_request = ultracart.SingleSignOnAuthorizeRequest() # SingleSignOnAuthorizeRequest | Authorization request

try:
    # Authorize a single sign on session
    api_response = api_instance.sso_authorize(authorization_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoApi->sso_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_request** | [**SingleSignOnAuthorizeRequest**](SingleSignOnAuthorizeRequest.md)| Authorization request | 

### Return type

[**SingleSignOnAuthorizeResponse**](SingleSignOnAuthorizeResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sso_session_revoke**
> sso_session_revoke()

Revoke single sign on session

This is the equivalent of logging out of the single sign on session 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.SsoApi.fromApiKey(simple_key, False, True)


try:
    # Revoke single sign on session
    api_instance.sso_session_revoke()
except ApiException as e:
    print("Exception when calling SsoApi->sso_session_revoke: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sso_token**
> SingleSignOnTokenResponse sso_token(token_request)

Exchange a single sign on code for a simple key token

Called by your application after receiving the code back on the redirect URI to obtain a simple key token to make API calls with 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.SsoApi.fromApiKey(simple_key, False, True)

token_request = ultracart.SingleSignOnTokenRequest() # SingleSignOnTokenRequest | Token request

try:
    # Exchange a single sign on code for a simple key token
    api_response = api_instance.sso_token(token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoApi->sso_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**SingleSignOnTokenRequest**](SingleSignOnTokenRequest.md)| Token request | 

### Return type

[**SingleSignOnTokenResponse**](SingleSignOnTokenResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ultracart.OauthApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_access_token**](OauthApi.md#oauth_access_token) | **POST** /oauth/token | Exchange authorization code for access token.
[**oauth_revoke**](OauthApi.md#oauth_revoke) | **POST** /oauth/revoke | Revoke this OAuth application.


# **oauth_access_token**
> OauthTokenResponse oauth_access_token(client_id, grant_type)

Exchange authorization code for access token.

The final leg in the OAuth process which exchanges the specified access token for the access code needed to make API calls. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import oauth_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.oauth_token_response import OauthTokenResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    client_id = "client_id_example" # str | The OAuth application client_id.
    grant_type = "grant_type_example" # str | Type of grant
    code = "code_example" # str | Authorization code received back from the browser redirect (optional)
    redirect_uri = "redirect_uri_example" # str | The URI that you redirect the browser to to start the authorization process (optional)
    refresh_token = "refresh_token_example" # str | The refresh token received during the original grant_type=authorization_code that can be used to return a new access token (optional)

    # example passing only required values which don't have defaults set
    try:
        # Exchange authorization code for access token.
        api_response = api_instance.oauth_access_token(client_id, grant_type)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OauthApi->oauth_access_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exchange authorization code for access token.
        api_response = api_instance.oauth_access_token(client_id, grant_type, code=code, redirect_uri=redirect_uri, refresh_token=refresh_token)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OauthApi->oauth_access_token: %s\n" % e)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_revoke**
> OauthRevokeSuccessResponse oauth_revoke(client_id, token)

Revoke this OAuth application.

Revokes the OAuth application associated with the specified client_id and token. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import oauth_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.oauth_revoke_success_response import OauthRevokeSuccessResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    client_id = "client_id_example" # str | The OAuth application client_id.
    token = "token_example" # str | The OAuth access token that is to be revoked..

    # example passing only required values which don't have defaults set
    try:
        # Revoke this OAuth application.
        api_response = api_instance.oauth_revoke(client_id, token)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OauthApi->oauth_revoke: %s\n" % e)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


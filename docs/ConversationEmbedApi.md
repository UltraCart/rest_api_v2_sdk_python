# ultracart.ConversationEmbedApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**embed_oauth_device_authorize**](ConversationEmbedApi.md#embed_oauth_device_authorize) | **POST** /conversation_embed/oauth/device/authorize | Initiate a device authorization flow for an embed widget.
[**embed_oauth_revoke**](ConversationEmbedApi.md#embed_oauth_revoke) | **POST** /conversation_embed/oauth/device/revoke | Revoke an embed widget access or refresh token.
[**embed_oauth_token**](ConversationEmbedApi.md#embed_oauth_token) | **POST** /conversation_embed/oauth/device/token | Exchange a device_code or refresh_token for an access token (embed widget).
[**get_embed_pbx_auth**](ConversationEmbedApi.md#get_embed_pbx_auth) | **PUT** /conversation_embed/pbx-auth | Get PBX authorization for the embedded softphone widget.


# **embed_oauth_device_authorize**
> embed_oauth_device_authorize(client_id, scope)

Initiate a device authorization flow for an embed widget.

RFC 8628 device authorization. Only the embed widget's client_id and the crm_embed scope are accepted. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The embed widget OAuth client_id. |
 **scope** | **str**| The application-level scope (must be &#39;crm_embed&#39;). |

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **embed_oauth_revoke**
> embed_oauth_revoke(client_id, token)

Revoke an embed widget access or refresh token.

RFC 7009 style â€” the token itself is proof of possession. Accepts either an access token or a refresh token in the 'token' parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The embed widget OAuth client_id. |
 **token** | **str**| The token to revoke (access token or refresh token). |

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **embed_oauth_token**
> embed_oauth_token(client_id, grant_type)

Exchange a device_code or refresh_token for an access token (embed widget).

Accepts grant_type=urn:ietf:params:oauth:grant-type:device_code or grant_type=refresh_token. Other grant types are rejected. Access tokens issued here expire in 60 minutes. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The embed widget OAuth client_id. |
 **grant_type** | **str**| Grant type. |
 **device_code** | **str**| The device code received from /oauth/device/authorize (required for device_code grant). | [optional]
 **refresh_token** | **str**| The refresh token (required for refresh_token grant). | [optional]

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embed_pbx_auth**
> ConversationEmbedPbxAuthResponse get_embed_pbx_auth()

Get PBX authorization for the embedded softphone widget.

Returns a narrow subset of agent auth fields â€” only what the softphone widget needs to connect to the PBX relay. Twilio tokens, conversation JWTs, and chat/customer permissions are intentionally excluded. 

### Example

* OAuth Authentication (ultraCartOauth):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationEmbedPbxAuthResponse**](ConversationEmbedPbxAuthResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth)

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


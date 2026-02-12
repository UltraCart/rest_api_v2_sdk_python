# OauthTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token to use in OAuth authenticated API call | [optional] 
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 
**error_uri** | **str** |  | [optional] 
**expires_in** | **str** | The number of seconds since issuance when the access token will expire and need to be refreshed using the refresh token | [optional] 
**refresh_token** | **str** | The refresh token that should be used to fetch a new access token when the expiration occurs | [optional] 
**scope** | **str** | The scope of permissions associated with teh access token | [optional] 
**token_type** | **str** | Type of token | [optional]  if omitted the server will use the default value of "bearer"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



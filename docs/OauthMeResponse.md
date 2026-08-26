# OauthMeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The name of your application as the merchant approved it. | [optional] 
**client_id** | **str** | Your application&#39;s client_id.  Null when authenticating with a simple key, which is not tied to an application. | [optional] 
**merchant_id** | **str** | The UltraCart merchant account that authorized your application.  Stable, and the value to key your own records on. | [optional] 
**merchant_name** | **str** | The account&#39;s company name, suitable for displaying to your user.  The merchant can change this, so display it rather than storing it as an identifier. | [optional] 
**scopes** | **[str]** | The permissions the merchant granted.  May be narrower than the permissions your application currently requests. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SfvbSmartAttributionPlatform


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assist_percent** | **float** | This platform&#39;s assist credit, 0 to 1.  Used only when platform_type_override is true. | [optional] 
**closer_percent** | **float** | This platform&#39;s closer credit, 0 to 1.  Used only when platform_type_override is true. | [optional] 
**fire_on_rebill** | **bool** | True when the platform also reports auto order rebills.  On a write, when left out, true for paid and owned and false for the affiliate types. | [optional] 
**integration_id** | **int** | The integration&#39;s id, such as an affiliate network pixel&#39;s oid.  Null for a platform matched by name.  On a write it must be an id from platforms or available_platforms. | [optional] 
**integration_name** | **str** | The platform, as Smart Attribution names it, up to 50 characters. | [optional] 
**non_participant_percent** | **float** | The credit this platform reports for an order it took no part in, 0 to 1.  0 when left out. | [optional] 
**originator_percent** | **float** | This platform&#39;s originator credit, 0 to 1.  Used only when platform_type_override is true. | [optional] 
**platform_type** | **str** | paid, owned, external affiliate, affiliate network pixel, or excluded. | [optional] 
**platform_type_override** | **bool** | True when this platform uses its own originator, assist and closer split instead of the global one.  On a write, when left out, true if all three of its percentages are sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



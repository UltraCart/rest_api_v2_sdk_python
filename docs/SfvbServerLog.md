# SfvbServerLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_error** | **bool** | True when the render itself failed and the page could not be produced. | [optional] 
**duration_ms** | **int** | How long the render took in milliseconds. | [optional] 
**error_count** | **int** | Error lines in the log, including Velocity problems such as a null | [optional] 
**line_count** | **int** | Lines in the full log text. | [optional] 
**log_id** | **str** | Opaque id of this log.  Pass it to the get endpoint.  Preview pages send the same id in the X-UltraCart-Storefront-Log-Id response header. | [optional] 
**request_template** | **str** | The template the page rendered with, when known. | [optional] 
**request_url** | **str** | The address that was rendered, as the server recorded it. | [optional] 
**start_date** | **str** | When the render started, ISO-8601 in UTC. | [optional] 
**status** | **str** | ERROR when the render logged any error line or failed, otherwise SUCCESS. | [optional] 
**stop_date** | **str** | When the render finished, ISO-8601 in UTC. | [optional] 
**warning_count** | **int** | Warning lines in the log. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CustomReportAccountConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_budget** | **float** |  | [optional] 
**ai_usage** | **float** | Current AI usage creating reports | [optional] 
**ai_usage_breakdowns** | [**[CustomReportUsageBreakdown]**](CustomReportUsageBreakdown.md) |  | [optional] 
**merchant_id** | **str** | Current BigQuery SQL usage running reports | [optional] 
**novice_sql_comments** | **bool** |  | [optional] 
**opt_in** | **bool** | True if they have opted into custom reports | [optional] 
**opt_in_by_user** | **str** | User that opted into custom reporting | [optional] 
**opt_in_date** | **str** | Date/time that custom reporting was opted in to | [optional] 
**read_only** | **bool** |  | [optional] 
**sql_budget** | **float** |  | [optional] 
**sql_usage** | **float** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



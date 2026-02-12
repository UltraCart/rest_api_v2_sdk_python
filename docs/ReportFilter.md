# ReportFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**[ReportFilterConnection]**](ReportFilterConnection.md) | How this filter connects to the data sources and columns | [optional] 
**name** | **str** |  | [optional] 
**timezone** | **str** | The timezone that the date range is querying on. | [optional] 
**type** | **str** | Type of filter | [optional] 
**uuid** | **str** | Unique UUID assigned to the filter.  Assists when returning values that the filter can use. | [optional] 
**values** | **[str]** | The selected values for the filter.  When used, some type conversion will need to occur. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



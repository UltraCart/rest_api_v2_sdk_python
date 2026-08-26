# SfvbCompileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The container JSON to compile. | [optional] 
**container_name** | **str** | Optional container name, used to derive the container id the same way a .cjson file name would.  Omit and the id on the document is kept. | [optional] 
**storefront_oid** | **int** | Optional storefront oid.  Required when theme_oid is supplied. | [optional] 
**theme_oid** | **int** | Optional theme oid.  Supplies the theme&#39;s inherit groups configuration so compilation matches what the theme would produce.  Omit to compile without inheritance. | [optional] 
**validate** | **bool** | Run validation before compiling and fail on errors.  Defaults to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



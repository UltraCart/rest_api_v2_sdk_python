# SfvbExperimentStartRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_days** | **int** | url - 3 to 90.  A url experiment always ends by itself after this many days. | [optional] 
**equal_weighting** | **bool** | url - true keeps the split fixed.  false shifts traffic toward the leader as the experiment runs.  Defaults to true. | [optional] 
**name** | **str** | url - experiment name. | [optional] 
**notes** | **str** | url - notes, such as the hypothesis being tested. | [optional] 
**objective** | **str** | url - one of the objectives from the objective list. | [optional] 
**objective_parameter** | **str** | url - the event name, when the objective is Events. | [optional] 
**optimization_type** | **str** | url - MAXIMUM or MINIMUM. | [optional] 
**path** | **str** | page - path of the page whose body holds the experiment element. | [optional] 
**slot** | **str** | page - the body file&#39;s name without .cjson.  Defaults to body. | [optional] 
**type** | **str** | page or url. | [optional] 
**variations** | [**[SfvbExperimentStartVariation]**](SfvbExperimentStartVariation.md) | url - 2 to 5 pages.  The first is the control. | [optional] 
**widget_id** | **str** | page - id of the experiment element in that body. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



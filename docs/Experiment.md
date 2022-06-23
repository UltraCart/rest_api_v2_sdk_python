# Experiment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | Contained ID where the experiment element was located | [optional] 
**duration_days** | **int** | Duration in days | [optional] 
**end_dts** | **str** | End date/time | [optional] 
**equal_weighting** | **bool** | Whether or not traffic is equally weighted or shifts over time during the experiment | [optional] 
**experiment_type** | **str** | The type of experiment | [optional] 
**id** | **str** | Experiment id | [optional] 
**name** | **str** | Experiment name | [optional] 
**notes** | **str** | Notes about the experiment | [optional] 
**objective** | **str** | Objective that is being optimized | [optional] 
**objective_parameter** | **str** | Objective parameter (such as event name) that is being optimized | [optional] 
**optimization_type** | **str** | Type of optimization | [optional] 
**session_count** | **int** | Total number of sessions in the experiment | [optional] 
**start_dts** | **str** | Start date/time | [optional] 
**status** | **str** | Status of the experiment | [optional] 
**storefront_experiment_oid** | **int** | Storefront Experiment Oid | [optional] 
**storefront_oid** | **int** | Storefront oid | [optional] 
**uri** | **str** | URI the experiment was started on | [optional] 
**variations** | [**[ExperimentVariation]**](ExperimentVariation.md) | Variations being tested in the experiment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



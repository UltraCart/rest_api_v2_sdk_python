# SfvbSequence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_sequence_uuid** | **str** | The sequence uuid. | [optional] 
**live** | **bool** | True when its emails and postcards reach customers now. | [optional] 
**notes** | **[str]** | Anything the read could not do, such as waiting counts that were unavailable. | [optional] 
**owner_name** | **str** | The campaign or flow name. | [optional] 
**owner_status** | **str** | The campaign or flow status. | [optional] 
**owner_type** | **str** | campaign or flow. | [optional] 
**owner_uuid** | **str** | The campaign or flow uuid. | [optional] 
**steps** | [**[SfvbSequenceStep]**](SfvbSequenceStep.md) | The steps from the start, in order.  A branching step holds its sides in branches. | [optional] 
**waiting_included** | **bool** | True when number_waiting was filled in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



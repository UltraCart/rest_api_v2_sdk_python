# CustomerEmailSuppressionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear_bounce** | **bool** | Clear bounce suppression for this address.  Bounce has no per-customer flag; it exists only on the suppression tables. | [optional] 
**clear_global_unsubscribe** | **bool** | Clear the global unsubscribe flag.  No-op if it is already clear. | [optional] 
**clear_spam_complaint** | **bool** | Clear the spam complaint flag.  Requires a reason.  No-op if it is already clear. | [optional] 
**consent_source** | **str** | How the customer communicated consent. | [optional] 
**reason** | **str** | Justification for the clear.  Required when clearing a spam complaint.  Retained on the audit record. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



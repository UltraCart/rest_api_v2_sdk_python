# SfvbCommsEmail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_last_modified_dts** | **str** | When the email container was last changed (ISO 8601, UTC). | [optional] 
**deleted** | **bool** | True when the email was deleted. | [optional] 
**email_uuid** | **str** | The email uuid.  Use it with the email container (owner type email) and with the email render endpoint. | [optional] 
**pending_review** | **bool** | True while a change waits for review. | [optional] 
**preview_text** | **str** | The preview text an inbox shows after the subject. | [optional] 
**rejected** | **bool** | True when review rejected the email.  Don&#39;t edit it without the merchant. | [optional] 
**requires_review** | **bool** | True when a change to this email must be reviewed before it sends. | [optional] 
**step_uuid** | **str** | The step that sends this email. | [optional] 
**subject** | **str** | The subject line. | [optional] 
**transactional** | **bool** | True for a transactional email, which skips the marketing footer rules. | [optional] 
**variant_name** | **str** | For an email in an experiment step, the variant name.  Absent otherwise. | [optional] 
**variant_percentage** | **float** | For an email in an experiment step, the share of customers it is sent to. | [optional] 
**variant_winner** | **bool** | For an email in an experiment step, true when the experiment chose it as the winner. | [optional] 
**version** | **int** | The email version. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



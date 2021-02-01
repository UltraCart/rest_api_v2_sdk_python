# EmailFlow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_concurrent_enrollments** | **bool** | True if a customer may be enrolled in this flow multiple times | [optional] 
**back_populating** | **bool** | True if the flow is currently performing a back population. | [optional] 
**click_rate_formatted** | **str** | Click rate of emails, formatted | [optional] 
**created_dts** | **str** | Created date | [optional] 
**deleted** | **bool** | True if this campaign was deleted | [optional] 
**email_communication_sequence_uuid** | **str** | Email communication sequence UUID | [optional] 
**email_flow_uuid** | **str** | Email flow UUID | [optional] 
**end_once_customer_purchases** | **bool** | True if the customer should end the flow once they purchase | [optional] 
**enrolled_customers** | **int** | Number of enrolled customers. | [optional] 
**esp_domain_user** | **str** | Username of sending email | [optional] 
**esp_domain_uuid** | **str** | UUID of sending domain | [optional] 
**esp_flow_folder_uuid** | **str** | Flow folder UUID.  Null for uncategorized | [optional] 
**esp_friendly_name** | **str** | Friendly name of the sending email | [optional] 
**filter_profile_equation_json** | **str** | File profile equation json | [optional] 
**library_item_oid** | **int** | If this item was ever added to the Code Library, this is the oid for that library item, or 0 if never added before.  This value is used to determine if a library item should be inserted or updated. | [optional] 
**merchant_id** | **str** | Merchant ID | [optional] 
**name** | **str** | Name of email flow | [optional] 
**open_rate_formatted** | **str** | Open rate of emails, formatted | [optional] 
**revenue_formatted** | **str** | Revenue, formatted | [optional] 
**revenue_per_customer_formatted** | **str** | Revenue per customer, formatted | [optional] 
**screenshot_large_full_url** | **str** | URL to a large full length screenshot | [optional] 
**status** | **str** | Status of the campaign of draft, archived, active, and inactive | [optional] 
**status_dts** | **str** | Timestamp when the last status change happened | [optional] 
**storefront_oid** | **int** | Storefront oid | [optional] 
**trigger_parameter** | **str** | Trigger parameter | [optional] 
**trigger_parameter_name** | **str** | Trigger parameter name | [optional] 
**trigger_type** | **str** | Trigger type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OrderPaymentCreditCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_auth_ticket** | **str** | Card authorization ticket | [optional] 
**card_authorization_amount** | **float** | Card authorization amount | [optional] 
**card_authorization_dts** | **str** | Card authorization date/time | [optional] 
**card_authorization_reference_number** | **str** | Card authorization reference number | [optional] 
**card_expiration_month** | **int** | Card expiration month (1-12) | [optional] 
**card_expiration_year** | **int** | Card expiration year (Four digit year) | [optional] 
**card_number** | **str** | Card number (masked to last 4) | [optional] 
**card_number_token** | **str** | Card number token from hosted fields used to update the card number | [optional] 
**card_number_truncated** | **bool** | True if the card has been truncated | [optional] 
**card_type** | **str** | Card type | [optional] 
**card_verification_number_token** | **str** | Card verification number token from hosted fields, only for import/insert of new orders, completely ignored for updates, and always null/empty for queries | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OrderPaymentHealthBenefitCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_benefit_card_expiration_month** | **int** | Health benefit card expiration month (1-12) | [optional] 
**health_benefit_card_expiration_year** | **int** | Health benefit card expiration year (Four digit year) | [optional] 
**health_benefit_card_number** | **str** | Health benefit card number (masked to last 4) | [optional] 
**health_benefit_card_number_token** | **str** | Health benefit card number token from hosted fields used to update the health benefit card number | [optional] 
**health_benefit_card_number_truncated** | **bool** | True if the health benefit card has been truncated | [optional] 
**health_benefit_card_verification_number_token** | **str** | Health benefit card verification number token from hosted fields, only for import/insert of new orders, completely ignored for updates, and always null/empty for queries | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



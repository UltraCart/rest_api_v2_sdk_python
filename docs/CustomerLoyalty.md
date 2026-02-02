# CustomerLoyalty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_points** | **int** | Current points | [optional] 
**internal_gift_certificate** | [**GiftCertificate**](GiftCertificate.md) |  | [optional] 
**internal_gift_certificate_balance** | **str** | Loyalty Cashback / Store credit balance (internal gift certificate balance) | [optional] 
**internal_gift_certificate_oid** | **int** | Internal gift certificate oid used to tracking loyalty cashback / store credit. | [optional] 
**ledger_entries** | [**[CustomerLoyaltyLedger]**](CustomerLoyaltyLedger.md) | Ledger entries | [optional] 
**loyalty_tier_expiration_dts** | **str** | Loyalty tier expiration date (read only because of SDK addition) | [optional] 
**loyalty_tier_name** | **str** | Loyalty tier name | [optional] 
**loyalty_tier_oid** | **int** | Loyalty tier oid (set to zero to remove the tier) | [optional] 
**pending_points** | **int** | Pending Points | [optional] 
**redemptions** | [**[CustomerLoyaltyRedemption]**](CustomerLoyaltyRedemption.md) | Redemptions | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



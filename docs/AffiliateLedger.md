# AffiliateLedger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_click_oid** | **int** | Unique object identifier for the click associated with this ledger entry | [optional] 
**affiliate_ledger_oid** | **int** | Affiliate ledger object ID associated with this ledger | [optional] 
**affiliate_link_oid** | **int** | Unique object identifier for the link that this click is associated with | [optional] 
**affiliate_oid** | **int** | Affiliate object ID associated with this transaction | [optional] 
**assigned_by_user** | **str** | User that assigned the transaction if it was done manually | [optional] 
**click** | [**AffiliateClick**](AffiliateClick.md) |  | [optional] 
**item_id** | **str** | Item ID associated with this transaction | [optional] 
**link** | [**AffiliateLink**](AffiliateLink.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**order_id** | **str** | Order ID associated with this transaction | [optional] 
**original_transaction_dts** | **str** | Date/time of the original transaction for reversals | [optional] 
**sub_id** | **str** | Sub ID associated with transaction (from the click) | [optional] 
**tier_number** | **int** | Tier number that this transaction earned | [optional] 
**transaction_amount** | **float** | Transaction amount | [optional] 
**transaction_amount_paid** | **float** | Amount of the transaction that has been paid out. | [optional] 
**transaction_dts** | **str** | Date/time that the transaction was made | [optional] 
**transaction_memo** | **str** | Memo explaining the transaction | [optional] 
**transaction_percentage** | **float** | Percentage associated with this transaction | [optional] 
**transaction_state** | **str** | Transaction state | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



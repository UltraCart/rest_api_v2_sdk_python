# AccountsReceivableRetryConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True if the retry should run daily.  False puts the retry service into an inactive state for this merchant. | [optional] 
**allow_process_linked_accounts** | **bool** | True if this account has linked accounts that it can process. | [optional] 
**cancel_auto_order** | **bool** | If true also cancel the auto order if the order is rejected at the end | [optional] 
**current_service_plan** | **str** | The current service plan that the account is on. | [optional] 
**daily_activity_list** | [**[AccountsReceivableRetryDayActivity]**](AccountsReceivableRetryDayActivity.md) | A list of days and what actions should take place on those days after an order reaches accounts receivable | [optional] 
**managed_by_linked_account_merchant_id** | **bool** | If not null, this account is managed by the specified parent merchant id. | [optional] 
**merchant_id** | **str** | UltraCart merchant ID | [optional] 
**notify_emails** | **[str]** | A list of email addresses to receive summary notifications from the retry service. | [optional] 
**notify_rejections** | **bool** | If true, email addresses are notified of rejections. | [optional] 
**notify_successes** | **bool** | If true, email addresses are notified of successful charges. | [optional] 
**process_linked_accounts** | **bool** | If true, all linked accounts are also processed using the same rules. | [optional] 
**processing_percentage** | **str** | The percentage rate charged for the service. | [optional] 
**reject_at_end** | **bool** | If true, the order is rejected the day after the last configured activity day | [optional] 
**transaction_rejects** | [**[AccountsReceivableRetryTransactionReject]**](AccountsReceivableRetryTransactionReject.md) | Array of key/value pairs that when found in the response cause the rejection of the transaction. | [optional] 
**trial_mode** | **bool** | True if the account is currently in trial mode.  Set to false to exit trial mode. | [optional] 
**trial_mode_expiration_dts** | **str** | The date when trial mode expires.  If this date is reached without exiting trial mode, the service will de-activate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



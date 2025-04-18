# EmailPerformance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_customers** | **int** | Active customers.  The value will be -1 if calculation is pending. | [optional] 
**actual_customers** | **int** | Actual customers that they have regardless of active state.  The value will be -1 if calculation is pending. | [optional] 
**bounce_count** | **int** | Bounce count | [optional] 
**bounce_percentage** | **float** | bounce percentage rate based upon our look back window.  This should be under five percent or the account will be paused for sending. | [optional] 
**bounce_percentage_formatted** | **str** | bounce percentage rate (formatted) based upon our look back window.  This should be under five percent or the account will be paused for sending. | [optional] 
**customer_histogram** | [**EmailPerformanceCustomerHistogram**](EmailPerformanceCustomerHistogram.md) |  | [optional] 
**daily_stats** | [**[EmailPerformanceDaily]**](EmailPerformanceDaily.md) | Daily statistics used for charting | [optional] 
**delivered_count** | **int** | Delivered count | [optional] 
**loyalty_program_type** | **str** | Loyalty Program Type | [optional] 
**max_active_customers** | **int** | Maximum active customers allowed under their billing plan | [optional] 
**max_emails_per_day** | **int** | Max emails per day | [optional] 
**max_emails_per_hour** | **int** | Max emails per hour | [optional] 
**max_emails_per_month** | **int** | Max emails per month | [optional] 
**paused_for_spam** | **bool** | True if campaign/flow emails are paused due to spam complaints. | [optional] 
**revenue** | **float** | Revenue | [optional] 
**sent_emails_per_day** | **int** | Sent emails last 24 hours | [optional] 
**sent_emails_per_hour** | **int** | Sent emails last hour | [optional] 
**sent_emails_per_month** | **int** | Sent emails last 31 days | [optional] 
**sequence_send_count** | **int** | Total sequence (campaign/flow) emails sent | [optional] 
**spam_count** | **int** | Spam complaints | [optional] 
**spam_percentage** | **float** | Spam percentage rate based upon our look back window.  This should be under one half a percent or the account will be paused for sending. | [optional] 
**spam_percentage_formatted** | **str** | Spam percentage rate (formatted) based upon our look back window.  This should be under one half a percent or the account will be paused for sending. | [optional] 
**transactional_send_count** | **int** | Total transactions emails sent | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



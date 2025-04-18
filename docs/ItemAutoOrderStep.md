# ItemAutoOrderStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_schedule_days** | **int** | If the schedule is arbitrary, then this is the number of days | [optional] 
**arbitrary_unit_cost** | **float** | Arbitrary unit cost used to override the regular item cost | [optional] 
**arbitrary_unit_cost_schedules** | [**[ItemAutoOrderStepArbitraryUnitCostSchedule]**](ItemAutoOrderStepArbitraryUnitCostSchedule.md) | Arbitrary unit costs schedules for more advanced discounting by rebill attempt | [optional] 
**grandfather_pricing** | [**[ItemAutoOrderStepGrandfatherPricing]**](ItemAutoOrderStepGrandfatherPricing.md) | Grand-father pricing configuration if the rebill schedule has changed over time | [optional] 
**managed_by** | **str** | Managed by (defaults to UltraCart) | [optional] 
**pause_days** | **int** | Number of days to pause | [optional] 
**pause_until_date** | **str** | Wait for this step to happen until the specified date | [optional] 
**pause_until_day_of_month** | **int** | Pause until a specific day of the month | [optional] 
**pause_until_minimum_delay_days** | **int** | Pause at least this many days between the last order and the calculated next day of month | [optional] 
**preshipment_notice_days** | **int** | If set, a pre-shipment notice is sent to the customer this many days in advance | [optional] 
**recurring_merchant_item_id** | **str** | Item id to rebill | [optional] 
**recurring_merchant_item_oid** | **int** | Item object identifier to rebill | [optional] 
**repeat_count** | **int** | Number of times to rebill.  Last step can be null for infinite | [optional] 
**schedule** | **str** | Frequency of the rebill | [optional] 
**subscribe_email_list_name** | **str** | Email list name to subscribe the customer to when the rebill occurs (decommissioned email engine) | [optional] 
**subscribe_email_list_oid** | **int** | Email list identifier to subscribe the customer to when this rebill occurs (decommissioned email engine) | [optional] 
**type** | **str** | Type of step (item, kit only, loop or pause) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AutoOrderItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_item_id** | **str** | Arbitrary item id that should be rebilled instead of the normal schedule | [optional] 
**arbitrary_percentage_discount** | **float** | An arbitrary percentage discount to provide on future rebills | [optional] 
**arbitrary_quantity** | **float** | Arbitrary quantity to rebill | [optional] 
**arbitrary_schedule_days** | **int** | The number of days to rebill if the frequency is set to an arbitrary number of days | [optional] 
**arbitrary_unit_cost** | **float** | Arbitrary unit cost that rebills of this item should occur at | [optional] 
**arbitrary_unit_cost_remaining_orders** | **int** | The number of rebills to give the arbitrary unit cost on before reverting to normal pricing. | [optional] 
**auto_order_item_oid** | **int** | Primary key of AutoOrderItem | [optional] 
**calculated_next_shipment_dts** | **str** | Calculated Date/time that this item is scheduled to rebill.  Will be null if no more shipments are going to occur on this item | [optional] 
**first_order_dts** | **str** | Date/time of the first order of this item.  Null if item added to auto order and has not been rebilled yet. | [optional] 
**frequency** | **str** | Frequency of the rebill if not a fixed schedule | [optional] 
**future_schedules** | [**[AutoOrderItemFutureSchedule]**](AutoOrderItemFutureSchedule.md) | The future rebill schedule for this item up to the next ten rebills | [optional] 
**last_order_dts** | **str** | Date/time of the last order of this item | [optional] 
**life_time_value** | **float** | The life time value of this item including the original purchase | [optional] 
**next_item_id** | **str** | Calculated next item id | [optional] 
**next_preshipment_notice_dts** | **str** | The date/time of when the next pre-shipment notice should be sent | [optional] 
**next_shipment_dts** | **str** | Date/time that this item is scheduled to rebill | [optional] 
**no_order_after_dts** | **str** | Date/time after which no additional rebills of this item should occur | [optional] 
**number_of_rebills** | **int** | The number of times this item has rebilled | [optional] 
**options** | [**[AutoOrderItemOption]**](AutoOrderItemOption.md) | Options associated with this item | [optional] 
**original_item_id** | **str** | The original item id purchased.  This item controls scheduling.  If you wish to modify a schedule, for example, from monthly to yearly, change this item from your monthly item to your yearly item, and then change the next_shipment_dts to your desired date. | [optional] 
**original_quantity** | **float** | The original quantity purchased | [optional] 
**paused** | **bool** | True if paused.  This field is an object instead of a primitive for backwards compatibility. | [optional] 
**paypal_payer_id** | **str** | The PayPal Payer ID tied to this item | [optional] 
**paypal_recurring_payment_profile_id** | **str** | The PayPal Profile ID tied to this item | [optional] 
**preshipment_notice_sent** | **bool** | True if the preshipment notice associated with the next rebill has been sent | [optional] 
**rebill_value** | **float** | The value of the rebills of this item | [optional] 
**remaining_repeat_count** | **int** | The number of rebills remaining before this item is complete | [optional] 
**simple_schedule** | [**AutoOrderItemSimpleSchedule**](AutoOrderItemSimpleSchedule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



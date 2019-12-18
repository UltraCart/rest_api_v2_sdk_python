# OrderShipping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**company** | **str** | Company | [optional] 
**country_code** | **str** | ISO-3166 two letter country code | [optional] 
**day_phone** | **str** | Day time phone | [optional] 
**day_phone_e164** | **str** | Day time phone (E164 format) | [optional] 
**delivery_date** | **str** | Date the customer is requesting delivery on.  Typically used for perishable product delivery. | [optional] 
**evening_phone** | **str** | Evening phone | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**least_cost_route** | **bool** | If true, instructs UltraCart to apply the cheapest shipping method to this order.  Used only for channel partner order inserts. | [optional] 
**least_cost_route_shipping_methods** | **list[str]** | List of shipping methods to consider if least_code_route is true. Used only for channel parter order inserts. | [optional] 
**lift_gate** | **bool** | Lift gate requested (LTL shipping methods only) | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**rma** | **str** | RMA number | [optional] 
**ship_on_date** | **str** | Date the customer is requesting that the order ship on.  Typically used for perishable product delivery. | [optional] 
**ship_to_residential** | **bool** | True if the shipping address is residential.  Effects the methods that are available to the customer as well as the price of the shipping method. | [optional] 
**shipping_3rd_party_account_number** | **str** | Shipping 3rd party account number | [optional] 
**shipping_date** | **str** | Date/time the order shipped on.  This date is set once the first shipment is sent to the customer. | [optional] 
**shipping_department_status** | **str** | Shipping department status | [optional] 
**shipping_method** | **str** | Shipping method | [optional] 
**shipping_method_accounting_code** | **str** | Shipping method accounting code | [optional] 
**special_instructions** | **str** | Special instructions from the customer regarding shipping | [optional] 
**state_region** | **str** | State | [optional] 
**title** | **str** | Title | [optional] 
**tracking_numbers** | **list[str]** | Tracking numbers | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



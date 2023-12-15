# CheckoutHandoffRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart** | [**Cart**](Cart.md) |  | [optional] 
**error_parameter_name** | **str** | If any error happen during the processing on the UltraCart side, the browser will be redirected to your error_return_url with the error passed in this parameter name. | [optional] 
**error_return_url** | **str** | The URL to return the browser to if there are processing errors on the UltraCart side. | [optional] 
**operation** | **str** | The type of handoff operation to perform | [optional] 
**paypal_maximum_upsell_revenue** | **float** | The maximum amount of revenue that you think the customer could add during a custom upsell after sequence on your checkout. | [optional] 
**paypal_return_url** | **str** | The URl to return the customers browser to after they have completed the PayPal process. | [optional] 
**secure_host_name** | **str** | The desired secure host name to perform the handoff on.  This should match the desired StoreFront. | [optional] 
**ucacid** | **str** | The UltraCart Analytics cookie value.  Populate this if you&#39;re handing off from a different domain than the checkout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



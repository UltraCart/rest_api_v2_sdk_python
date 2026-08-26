# ConversationPbxPayConnector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the connector | [optional] 
**environment** | **str** | Environment the connector points at.  Only live connectors are returned.  Sandbox and unconfigured connectors are ignored. | [optional]  if omitted the server will use the default value of "live"
**friendly_name** | **str** | Friendly name of the connector as shown in the Twilio console | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**processor** | **str** | Payment processor behind this connector | [optional] 
**processor_account_id** | **str** | The processor account this connector is bound to (Stripe connected account id or Braintree merchant id).  A payment captured with this connector can only be charged within this account. | [optional] 
**sid** | **str** | Twilio installed add-on SID for this connector | [optional] 
**unique_name** | **str** | Unique name of the connector.  This is the value used for the paymentConnector attribute of the Twilio Pay verb. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



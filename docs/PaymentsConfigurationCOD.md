# PaymentsConfigurationCOD

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_cod** | **bool** | Master flag indicating this merchant accepts COD | [optional] 
**approved_customers_only** | **bool** | If true, only approved customers may pay with COD | [optional] 
**restrictions** | [**PaymentsConfigurationRestrictions**](PaymentsConfigurationRestrictions.md) |  | [optional] 
**surcharge_accounting_code** | **str** | Optional field, if surcharge is set, this is the accounting code the surcharge is tagged with when sent to Quickbooks | [optional] 
**surcharge_fee** | **float** | Additional cost for using COD | [optional] 
**surcharge_percentage** | **float** | Additional percentage cost for using COD | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


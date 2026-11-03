# SfvbTrackingPrivacy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymize_ip** | **str** | Which shoppers have their IP address anonymized on the cart and order.  all, eea, non_us, or null for nobody. | [optional] 
**default_mailing_list_off** | **str** | Which shoppers start checkout with the mailing list sign-up unchecked.  all, eea, non_us, or null for nobody. | [optional] 
**disable_return_email** | **str** | Which shoppers are left out of the return email (the admin&#39;s Disable Return Email rule).  all, eea, non_us, or null for nobody. | [optional] 
**exclude_purchase_bubble_history** | **str** | Which shoppers&#39; purchases are left out of the purchase bubble history.  all, eea, non_us, or null for nobody. | [optional] 
**hash_sha256** | **str** | The hash of these five rules.  Send it as If-Match when changing them. | [optional] 
**show_cookie_notice** | **str** | Which shoppers see the privacy and cookie notice.  all, eea (shoppers in the European Economic Area), non_us, or null for nobody. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



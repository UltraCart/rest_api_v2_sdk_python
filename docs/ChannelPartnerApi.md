# ultracart.ChannelPartnerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order_by_channel_partner_order_id**](ChannelPartnerApi.md#cancel_order_by_channel_partner_order_id) | **DELETE** /channel_partner/cancel/by_channel_partner_order_id/{order_id} | Cancel channel partner order by channel partner order id
[**cancel_order_by_ultra_cart_order_id**](ChannelPartnerApi.md#cancel_order_by_ultra_cart_order_id) | **DELETE** /channel_partner/cancel/by_ultracart_order_id/{order_id} | Cancel channel partner order by UltraCart order id
[**delete_channel_partner_ship_to_preference**](ChannelPartnerApi.md#delete_channel_partner_ship_to_preference) | **DELETE** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Delete a ship to preference record for the channel partner.
[**estimate_shipping_for_channel_partner_order**](ChannelPartnerApi.md#estimate_shipping_for_channel_partner_order) | **POST** /channel_partner/estimate_shipping | Estimate shipping for channel partner order
[**estimate_tax_for_channel_partner_order**](ChannelPartnerApi.md#estimate_tax_for_channel_partner_order) | **POST** /channel_partner/estimate_tax | Estimate tax for channel partner order
[**get_channel_partner_order**](ChannelPartnerApi.md#get_channel_partner_order) | **GET** /channel_partner/orders/{order_id} | Retrieve a channel partner order
[**get_channel_partner_order_by_channel_partner_order_id**](ChannelPartnerApi.md#get_channel_partner_order_by_channel_partner_order_id) | **GET** /channel_partner/orders/by_channel_partner_order_id/{order_id} | Retrieve a channel partner order by the channel partner order id
[**get_channel_partner_ship_to_preference**](ChannelPartnerApi.md#get_channel_partner_ship_to_preference) | **GET** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Retrieve the ship to preference associated with the channel partner and the specific id.
[**get_channel_partner_ship_to_preferences**](ChannelPartnerApi.md#get_channel_partner_ship_to_preferences) | **GET** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences | Retrieve the ship to preferences associated with the channel partner.
[**get_channel_partners**](ChannelPartnerApi.md#get_channel_partners) | **GET** /channel_partner/channel_partners | Retrieve the channel partners configured on the account.
[**import_channel_partner_order**](ChannelPartnerApi.md#import_channel_partner_order) | **POST** /channel_partner/import | Insert channel partner order
[**insert_channel_partner_ship_to_preference**](ChannelPartnerApi.md#insert_channel_partner_ship_to_preference) | **POST** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences | Insert a ship to preference record for the channel partner.
[**refund_channel_partner_order**](ChannelPartnerApi.md#refund_channel_partner_order) | **PUT** /channel_partner/orders/{order_id}/refund | Refund a channel partner order
[**update_channel_partner_ship_to_preference**](ChannelPartnerApi.md#update_channel_partner_ship_to_preference) | **PUT** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Update a ship to preference record for the channel partner.


# **cancel_order_by_channel_partner_order_id**
> ChannelPartnerCancelResponse cancel_order_by_channel_partner_order_id(order_id)

Cancel channel partner order by channel partner order id

Cancel channel partner order by channel partner order id 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The channel partner order id to delete.

try:
    # Cancel channel partner order by channel partner order id
    api_response = api_instance.cancel_order_by_channel_partner_order_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->cancel_order_by_channel_partner_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The channel partner order id to delete. | 

### Return type

[**ChannelPartnerCancelResponse**](ChannelPartnerCancelResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order_by_ultra_cart_order_id**
> ChannelPartnerCancelResponse cancel_order_by_ultra_cart_order_id(order_id)

Cancel channel partner order by UltraCart order id

Cancel channel partner order by UltraCart order id 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The UltraCart order id to delete.

try:
    # Cancel channel partner order by UltraCart order id
    api_response = api_instance.cancel_order_by_ultra_cart_order_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->cancel_order_by_ultra_cart_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The UltraCart order id to delete. | 

### Return type

[**ChannelPartnerCancelResponse**](ChannelPartnerCancelResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel_partner_ship_to_preference**
> delete_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)

Delete a ship to preference record for the channel partner.

Delete a ship to preference record for the channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_oid = 56 # int | 
channel_partner_ship_to_preference_oid = 56 # int | 

try:
    # Delete a ship to preference record for the channel partner.
    api_instance.delete_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->delete_channel_partner_ship_to_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  | 
 **channel_partner_ship_to_preference_oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_shipping_for_channel_partner_order**
> ChannelPartnerEstimateShippingResponse estimate_shipping_for_channel_partner_order(channel_partner_order)

Estimate shipping for channel partner order

Estimate shipping for order from a channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_order = ultracart.ChannelPartnerOrder() # ChannelPartnerOrder | Order needing shipping estimate

try:
    # Estimate shipping for channel partner order
    api_response = api_instance.estimate_shipping_for_channel_partner_order(channel_partner_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->estimate_shipping_for_channel_partner_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order needing shipping estimate | 

### Return type

[**ChannelPartnerEstimateShippingResponse**](ChannelPartnerEstimateShippingResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_tax_for_channel_partner_order**
> ChannelPartnerEstimateTaxResponse estimate_tax_for_channel_partner_order(channel_partner_order)

Estimate tax for channel partner order

Estimate tax for order from a channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_order = ultracart.ChannelPartnerOrder() # ChannelPartnerOrder | Order needing tax estimate

try:
    # Estimate tax for channel partner order
    api_response = api_instance.estimate_tax_for_channel_partner_order(channel_partner_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->estimate_tax_for_channel_partner_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order needing tax estimate | 

### Return type

[**ChannelPartnerEstimateTaxResponse**](ChannelPartnerEstimateTaxResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_partner_order**
> OrderResponse get_channel_partner_order(order_id, expand=expand)

Retrieve a channel partner order

Retrieves a single order using the specified order id.  Only orders belonging to this channel partner may be retrieved. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples (optional)

try:
    # Retrieve a channel partner order
    api_response = api_instance.get_channel_partner_order(order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->get_channel_partner_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_partner_order_by_channel_partner_order_id**
> OrderResponse get_channel_partner_order_by_channel_partner_order_id(order_id, expand=expand)

Retrieve a channel partner order by the channel partner order id

Retrieves a single order using the channel partner order id, not the ultracart order id.  Only orders belonging to this channel partner may be retrieved. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The channel partner order id to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples (optional)

try:
    # Retrieve a channel partner order by the channel partner order id
    api_response = api_instance.get_channel_partner_order_by_channel_partner_order_id(order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->get_channel_partner_order_by_channel_partner_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The channel partner order id to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse get_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)

Retrieve the ship to preference associated with the channel partner and the specific id.

Retrieve the ship to preference associated with the channel partner and the specific id. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_oid = 56 # int | 
channel_partner_ship_to_preference_oid = 56 # int | 

try:
    # Retrieve the ship to preference associated with the channel partner and the specific id.
    api_response = api_instance.get_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->get_channel_partner_ship_to_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  | 
 **channel_partner_ship_to_preference_oid** | **int**|  | 

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_partner_ship_to_preferences**
> ChannelPartnerShipToPreferencesResponse get_channel_partner_ship_to_preferences(channel_partner_oid)

Retrieve the ship to preferences associated with the channel partner.

Retrieve the ship to preferences associated with the channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_oid = 56 # int | 

try:
    # Retrieve the ship to preferences associated with the channel partner.
    api_response = api_instance.get_channel_partner_ship_to_preferences(channel_partner_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->get_channel_partner_ship_to_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  | 

### Return type

[**ChannelPartnerShipToPreferencesResponse**](ChannelPartnerShipToPreferencesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_partners**
> ChannelPartnersResponse get_channel_partners()

Retrieve the channel partners configured on the account.

Retrieve the channel partners configured on the account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve the channel partners configured on the account.
    api_response = api_instance.get_channel_partners()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->get_channel_partners: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ChannelPartnersResponse**](ChannelPartnersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_channel_partner_order**
> ChannelPartnerImportResponse import_channel_partner_order(channel_partner_order)

Insert channel partner order

Insert order from a channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_order = ultracart.ChannelPartnerOrder() # ChannelPartnerOrder | Order to insert

try:
    # Insert channel partner order
    api_response = api_instance.import_channel_partner_order(channel_partner_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->import_channel_partner_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order to insert | 

### Return type

[**ChannelPartnerImportResponse**](ChannelPartnerImportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse insert_channel_partner_ship_to_preference(channel_partner_oid, ship_to_preference)

Insert a ship to preference record for the channel partner.

Insert a ship to preference record for the channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_oid = 56 # int | 
ship_to_preference = ultracart.ChannelPartnerShipToPreference() # ChannelPartnerShipToPreference | Ship to preference to create

try:
    # Insert a ship to preference record for the channel partner.
    api_response = api_instance.insert_channel_partner_ship_to_preference(channel_partner_oid, ship_to_preference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->insert_channel_partner_ship_to_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  | 
 **ship_to_preference** | [**ChannelPartnerShipToPreference**](ChannelPartnerShipToPreference.md)| Ship to preference to create | 

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_channel_partner_order**
> OrderResponse refund_channel_partner_order(order, order_id, reject_after_refund=reject_after_refund, skip_customer_notification=skip_customer_notification, auto_order_cancel=auto_order_cancel, manual_refund=manual_refund, reverse_affiliate_transactions=reverse_affiliate_transactions, issue_store_credit=issue_store_credit, auto_order_cancel_reason=auto_order_cancel_reason, expand=expand)

Refund a channel partner order

Perform a refund operation on a channel partner order and then update the order if successful.  All of the object properties ending in _refunded should be the TOTAL amount that should end up being refunded.  UltraCart will calculate the actual amount to refund based upon the prior refunds. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

order = ultracart.Order() # Order | Order to refund
order_id = 'order_id_example' # str | The order id to refund.
reject_after_refund = false # bool | Reject order after refund (optional) (default to false)
skip_customer_notification = false # bool | Skip customer email notification (optional) (default to false)
auto_order_cancel = false # bool | Cancel associated auto orders (optional) (default to false)
manual_refund = false # bool | Consider a manual refund done externally (optional) (default to false)
reverse_affiliate_transactions = true # bool | Reverse affiliate transactions (optional) (default to true)
issue_store_credit = false # bool | Issue a store credit instead of refunding the original payment method, loyalty must be configured on merchant account (optional) (default to false)
auto_order_cancel_reason = 'auto_order_cancel_reason_example' # str | Reason for auto orders cancellation (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See OrderApi.refundOrder documentation for examples (optional)

try:
    # Refund a channel partner order
    api_response = api_instance.refund_channel_partner_order(order, order_id, reject_after_refund=reject_after_refund, skip_customer_notification=skip_customer_notification, auto_order_cancel=auto_order_cancel, manual_refund=manual_refund, reverse_affiliate_transactions=reverse_affiliate_transactions, issue_store_credit=issue_store_credit, auto_order_cancel_reason=auto_order_cancel_reason, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->refund_channel_partner_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)| Order to refund | 
 **order_id** | **str**| The order id to refund. | 
 **reject_after_refund** | **bool**| Reject order after refund | [optional] [default to false]
 **skip_customer_notification** | **bool**| Skip customer email notification | [optional] [default to false]
 **auto_order_cancel** | **bool**| Cancel associated auto orders | [optional] [default to false]
 **manual_refund** | **bool**| Consider a manual refund done externally | [optional] [default to false]
 **reverse_affiliate_transactions** | **bool**| Reverse affiliate transactions | [optional] [default to true]
 **issue_store_credit** | **bool**| Issue a store credit instead of refunding the original payment method, loyalty must be configured on merchant account | [optional] [default to false]
 **auto_order_cancel_reason** | **str**| Reason for auto orders cancellation | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.refundOrder documentation for examples | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse update_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid, ship_to_preference)

Update a ship to preference record for the channel partner.

Update a ship to preference record for the channel partner. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ChannelPartnerApi.fromApiKey(simple_key, False, True)

channel_partner_oid = 56 # int | 
channel_partner_ship_to_preference_oid = 56 # int | 
ship_to_preference = ultracart.ChannelPartnerShipToPreference() # ChannelPartnerShipToPreference | Ship to preference to create

try:
    # Update a ship to preference record for the channel partner.
    api_response = api_instance.update_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid, ship_to_preference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelPartnerApi->update_channel_partner_ship_to_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  | 
 **channel_partner_ship_to_preference_oid** | **int**|  | 
 **ship_to_preference** | [**ChannelPartnerShipToPreference**](ChannelPartnerShipToPreference.md)| Ship to preference to create | 

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


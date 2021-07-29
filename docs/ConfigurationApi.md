# ultracart.ConfigurationApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delay_auto_orders**](ConfigurationApi.md#delay_auto_orders) | **POST** /configuration/checkout/payments/rtg/{rtg_oid}/delayAutoOrders | Delay auto order processing for a day for this rotating transaction gateway
[**delete_rotating_transaction_gateway**](ConfigurationApi.md#delete_rotating_transaction_gateway) | **DELETE** /configuration/checkout/payments/rtg/{rtg_oid} | Delete a rotating transaction gateway
[**get_payments_configuration**](ConfigurationApi.md#get_payments_configuration) | **GET** /configuration/checkout/payments | Retrieve payments configuration
[**get_payments_rotating_gateway**](ConfigurationApi.md#get_payments_rotating_gateway) | **GET** /configuration/checkout/payments/rtg/{rtg_oid} | Retrieve a rotating transaction gateway
[**get_payments_rotating_gateway_by_code**](ConfigurationApi.md#get_payments_rotating_gateway_by_code) | **GET** /configuration/checkout/payments/rtg/byCode/{code} | Retrieve a rotating transaction gateway by code
[**get_payments_rotating_transaction_gateways**](ConfigurationApi.md#get_payments_rotating_transaction_gateways) | **GET** /configuration/checkout/payments/rtg | Retrieve a list of rotating transaction gateways
[**get_payments_rtg_summaries**](ConfigurationApi.md#get_payments_rtg_summaries) | **GET** /configuration/checkout/payments/rtg/summaries | Retrieve a summary of rotating transaction gateways
[**get_payments_transaction_gateways**](ConfigurationApi.md#get_payments_transaction_gateways) | **GET** /configuration/checkout/payments/tg | Retrieve a list of transaction gateways
[**insert_rotating_transaction_gateway**](ConfigurationApi.md#insert_rotating_transaction_gateway) | **POST** /configuration/checkout/payments/rtg/ | Insert a rotating transaction gateway
[**migrate_to_rotating_transaction_gateway**](ConfigurationApi.md#migrate_to_rotating_transaction_gateway) | **POST** /configuration/checkout/payments/tg/migrateToRtgWithCodeOf/{code} | Migrate a normal transaction gateway to a rotating transaction gateway
[**stripe_connect**](ConfigurationApi.md#stripe_connect) | **POST** /configuration/checkout/payments/rtg/{rtg_oid}/stripeConnect | Begin the processing of connecting with Stripe
[**update_payments_configuration**](ConfigurationApi.md#update_payments_configuration) | **PUT** /configuration/checkout/payments | Updates payments configuration
[**update_payments_transaction_gateway**](ConfigurationApi.md#update_payments_transaction_gateway) | **PUT** /configuration/checkout/payments/tg | Updates payments transaction gateway
[**update_rotating_transaction_gateway**](ConfigurationApi.md#update_rotating_transaction_gateway) | **PUT** /configuration/checkout/payments/rtg/{rtg_oid} | Update a rotating transaction gateway
[**wepay_enroll**](ConfigurationApi.md#wepay_enroll) | **PUT** /configuration/checkout/wepayEnroll | Enroll with WePay


# **delay_auto_orders**
> DelayAutoOrdersResponse delay_auto_orders(rtg_oid)

Delay auto order processing for a day for this rotating transaction gateway

Delay auto order processing for a day for this rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rtg_oid = 56 # int | The rtg_oid to delay.

try:
    # Delay auto order processing for a day for this rotating transaction gateway
    api_response = api_instance.delay_auto_orders(rtg_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delay_auto_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rtg_oid** | **int**| The rtg_oid to delay. | 

### Return type

[**DelayAutoOrdersResponse**](DelayAutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rotating_transaction_gateway**
> BaseResponse delete_rotating_transaction_gateway(rtg_oid)

Delete a rotating transaction gateway

Delete a rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rtg_oid = 56 # int | The rtg_oid to delete.

try:
    # Delete a rotating transaction gateway
    api_response = api_instance.delete_rotating_transaction_gateway(rtg_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_rotating_transaction_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rtg_oid** | **int**| The rtg_oid to delete. | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_configuration**
> PaymentsConfiguration get_payments_configuration()

Retrieve payments configuration

Retrieves payments configuration for this account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve payments configuration
    api_response = api_instance.get_payments_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentsConfiguration**](PaymentsConfiguration.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_rotating_gateway**
> RotatingTransactionGateway get_payments_rotating_gateway(rtg_oid)

Retrieve a rotating transaction gateway

Retrieve a rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rtg_oid = 56 # int | The rtg_oid for the desired record.

try:
    # Retrieve a rotating transaction gateway
    api_response = api_instance.get_payments_rotating_gateway(rtg_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_rotating_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rtg_oid** | **int**| The rtg_oid for the desired record. | 

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_rotating_gateway_by_code**
> RotatingTransactionGateway get_payments_rotating_gateway_by_code(code)

Retrieve a rotating transaction gateway by code

Retrieve a rotating transaction gateway by code 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

code = 'code_example' # str | The code for the desired rotating transaction gateway.

try:
    # Retrieve a rotating transaction gateway by code
    api_response = api_instance.get_payments_rotating_gateway_by_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_rotating_gateway_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code for the desired rotating transaction gateway. | 

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_rotating_transaction_gateways**
> RotatingTransactionGateway get_payments_rotating_transaction_gateways()

Retrieve a list of rotating transaction gateways

Retrieve a list of rotating transaction gateways 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve a list of rotating transaction gateways
    api_response = api_instance.get_payments_rotating_transaction_gateways()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_rotating_transaction_gateways: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_rtg_summaries**
> RotatingTransactionGateway get_payments_rtg_summaries()

Retrieve a summary of rotating transaction gateways

Retrieve a summary of rotating transaction gateways 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve a summary of rotating transaction gateways
    api_response = api_instance.get_payments_rtg_summaries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_rtg_summaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_transaction_gateways**
> TransactionGatewaysResponse get_payments_transaction_gateways()

Retrieve a list of transaction gateways

Retrieve a list of transaction gateways 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve a list of transaction gateways
    api_response = api_instance.get_payments_transaction_gateways()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_payments_transaction_gateways: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionGatewaysResponse**](TransactionGatewaysResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_rotating_transaction_gateway**
> RotatingTransactionGateway insert_rotating_transaction_gateway(rotating_transaction_gateway)

Insert a rotating transaction gateway

Insert a rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rotating_transaction_gateway = ultracart.RotatingTransactionGateway() # RotatingTransactionGateway | Rotating transaction gateway

try:
    # Insert a rotating transaction gateway
    api_response = api_instance.insert_rotating_transaction_gateway(rotating_transaction_gateway)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->insert_rotating_transaction_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rotating_transaction_gateway** | [**RotatingTransactionGateway**](RotatingTransactionGateway.md)| Rotating transaction gateway | 

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_to_rotating_transaction_gateway**
> RotatingTransactionGateway migrate_to_rotating_transaction_gateway(code)

Migrate a normal transaction gateway to a rotating transaction gateway

Migrate a normal transaction gateway to a rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

code = 'code_example' # str | The short code for the new rotating transaction gateway

try:
    # Migrate a normal transaction gateway to a rotating transaction gateway
    api_response = api_instance.migrate_to_rotating_transaction_gateway(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->migrate_to_rotating_transaction_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The short code for the new rotating transaction gateway | 

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_connect**
> StripeConnectResponse stripe_connect(rtg_oid)

Begin the processing of connecting with Stripe

Begin the processing of connecting with Stripe. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rtg_oid = 56 # int | The rtg_oid to be connected to stripe.

try:
    # Begin the processing of connecting with Stripe
    api_response = api_instance.stripe_connect(rtg_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->stripe_connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rtg_oid** | **int**| The rtg_oid to be connected to stripe. | 

### Return type

[**StripeConnectResponse**](StripeConnectResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payments_configuration**
> PaymentsConfigurationResponse update_payments_configuration(payments_configuration)

Updates payments configuration

Updates payments configuration on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

payments_configuration = ultracart.PaymentsConfiguration() # PaymentsConfiguration | Payments configuration

try:
    # Updates payments configuration
    api_response = api_instance.update_payments_configuration(payments_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_payments_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payments_configuration** | [**PaymentsConfiguration**](PaymentsConfiguration.md)| Payments configuration | 

### Return type

[**PaymentsConfigurationResponse**](PaymentsConfigurationResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payments_transaction_gateway**
> TransactionGatewaysResponse update_payments_transaction_gateway(update_gateway_request)

Updates payments transaction gateway

Updates payments transaction gateway on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

update_gateway_request = ultracart.TransactionGatewaysRequest() # TransactionGatewaysRequest | Transaction gateways

try:
    # Updates payments transaction gateway
    api_response = api_instance.update_payments_transaction_gateway(update_gateway_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_payments_transaction_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_gateway_request** | [**TransactionGatewaysRequest**](TransactionGatewaysRequest.md)| Transaction gateways | 

### Return type

[**TransactionGatewaysResponse**](TransactionGatewaysResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rotating_transaction_gateway**
> RotatingTransactionGateway update_rotating_transaction_gateway(rtg_oid, rotating_transaction_gateway)

Update a rotating transaction gateway

Update a rotating transaction gateway 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

rtg_oid = 56 # int | The rtg_oid to update.
rotating_transaction_gateway = ultracart.RotatingTransactionGateway() # RotatingTransactionGateway | Rotating transaction gateway

try:
    # Update a rotating transaction gateway
    api_response = api_instance.update_rotating_transaction_gateway(rtg_oid, rotating_transaction_gateway)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_rotating_transaction_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rtg_oid** | **int**| The rtg_oid to update. | 
 **rotating_transaction_gateway** | [**RotatingTransactionGateway**](RotatingTransactionGateway.md)| Rotating transaction gateway | 

### Return type

[**RotatingTransactionGateway**](RotatingTransactionGateway.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wepay_enroll**
> PaymentsConfigurationResponse wepay_enroll(wepay_enroll)

Enroll with WePay

Enroll with WePay on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConfigurationApi.fromApiKey(simple_key, False, True)

wepay_enroll = ultracart.PaymentsWepayEnroll() # PaymentsWepayEnroll | Wepay enrollment information

try:
    # Enroll with WePay
    api_response = api_instance.wepay_enroll(wepay_enroll)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->wepay_enroll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wepay_enroll** | [**PaymentsWepayEnroll**](PaymentsWepayEnroll.md)| Wepay enrollment information | 

### Return type

[**PaymentsConfigurationResponse**](PaymentsConfigurationResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# com_ultracart_admin_v2.CheckoutApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_browser_key_put**](CheckoutApi.md#checkout_browser_key_put) | **PUT** /checkout/browser_key | Setup Browser Application
[**checkout_cart_cart_id_get**](CheckoutApi.md#checkout_cart_cart_id_get) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
[**checkout_cart_finalize_order_post**](CheckoutApi.md#checkout_cart_finalize_order_post) | **POST** /checkout/cart/finalizeOrder | Finalize Order
[**checkout_cart_get**](CheckoutApi.md#checkout_cart_get) | **GET** /checkout/cart | Get cart
[**checkout_cart_handoff_post**](CheckoutApi.md#checkout_cart_handoff_post) | **POST** /checkout/cart/handoff | Handoff cart
[**checkout_cart_profile_login_post**](CheckoutApi.md#checkout_cart_profile_login_post) | **POST** /checkout/cart/profile/login | Profile login
[**checkout_cart_profile_logout_post**](CheckoutApi.md#checkout_cart_profile_logout_post) | **POST** /checkout/cart/profile/logout | Profile logout
[**checkout_cart_profile_register_post**](CheckoutApi.md#checkout_cart_profile_register_post) | **POST** /checkout/cart/profile/register | Profile registration
[**checkout_cart_put**](CheckoutApi.md#checkout_cart_put) | **PUT** /checkout/cart | Update cart
[**checkout_cart_validate_post**](CheckoutApi.md#checkout_cart_validate_post) | **POST** /checkout/cart/validate | Validate
[**checkout_city_state_post**](CheckoutApi.md#checkout_city_state_post) | **POST** /checkout/city_state | City/State for Zip
[**checkout_related_items_item_id_post**](CheckoutApi.md#checkout_related_items_item_id_post) | **POST** /checkout/relatedItems/{item_id} | Related items (specific item)
[**checkout_related_items_post**](CheckoutApi.md#checkout_related_items_post) | **POST** /checkout/related_items | Related items
[**checkout_return_return_code_get**](CheckoutApi.md#checkout_return_return_code_get) | **GET** /checkout/return/{return_code} | Get cart (by return code)


# **checkout_browser_key_put**
> CheckoutSetupBrowserKeyResponse checkout_browser_key_put(browser_key_request)

Setup Browser Application

Setup a browser key authenticated application with checkout permissions.  This REST call must be made with an authentication scheme that is not browser key.  The new application will be linked to the application that makes this call.  If this application is disabled / deleted, then so will the application setup by this call.  The purpose of this call is to allow an OAuth applicaiton, such as the Wordpress plugin, to setup the proper browser based authentication for the REST checkout API to use. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
browser_key_request = com_ultracart_admin_v2.CheckoutSetupBrowserKeyRequest() # CheckoutSetupBrowserKeyRequest | Setup browser key request

try: 
    # Setup Browser Application
    api_response = api_instance.checkout_browser_key_put(browser_key_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_browser_key_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browser_key_request** | [**CheckoutSetupBrowserKeyRequest**](CheckoutSetupBrowserKeyRequest.md)| Setup browser key request | 

### Return type

[**CheckoutSetupBrowserKeyResponse**](CheckoutSetupBrowserKeyResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_cart_id_get**
> CartResponse checkout_cart_cart_id_get(cart_id, expand=expand)

Get cart (by cart id)

Get a cart specified by the cart_id parameter. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
cart_id = 'cart_id_example' # str | Cart ID to retrieve
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart (by cart id)
    api_response = api_instance.checkout_cart_cart_id_get(cart_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_cart_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Cart ID to retrieve | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_finalize_order_post**
> CartFinalizeOrderResponse checkout_cart_finalize_order_post(finalize_request)

Finalize Order

Finalize the cart into an order.  This method can not be called with browser key authentication.  It is ONLY meant for server side code to call. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
finalize_request = com_ultracart_admin_v2.CartFinalizeOrderRequest() # CartFinalizeOrderRequest | Finalize request

try: 
    # Finalize Order
    api_response = api_instance.checkout_cart_finalize_order_post(finalize_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_finalize_order_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finalize_request** | [**CartFinalizeOrderRequest**](CartFinalizeOrderRequest.md)| Finalize request | 

### Return type

[**CartFinalizeOrderResponse**](CartFinalizeOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_get**
> CartResponse checkout_cart_get(expand=expand)

Get cart

If the cookie is set on the browser making the request then it will return their active cart.  Otherwise it will create a new cart. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart
    api_response = api_instance.checkout_cart_get(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_handoff_post**
> CheckoutHandoffResponse checkout_cart_handoff_post(handoff_request, expand=expand)

Handoff cart

Handoff the browser to UltraCart for view cart on StoreFront, transfer to PayPal or finalization of the order (including upsell processing). 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
handoff_request = com_ultracart_admin_v2.CheckoutHandoffRequest() # CheckoutHandoffRequest | Handoff request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Handoff cart
    api_response = api_instance.checkout_cart_handoff_post(handoff_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_handoff_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handoff_request** | [**CheckoutHandoffRequest**](CheckoutHandoffRequest.md)| Handoff request | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CheckoutHandoffResponse**](CheckoutHandoffResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_profile_login_post**
> CartProfileLoginResponse checkout_cart_profile_login_post(login_request, expand=expand)

Profile login

Login in to the customer profile specified by cart.billing.email and password 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
login_request = com_ultracart_admin_v2.CartProfileLoginRequest() # CartProfileLoginRequest | Login request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile login
    api_response = api_instance.checkout_cart_profile_login_post(login_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_profile_login_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**CartProfileLoginRequest**](CartProfileLoginRequest.md)| Login request | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartProfileLoginResponse**](CartProfileLoginResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_profile_logout_post**
> CartResponse checkout_cart_profile_logout_post(cart, expand=expand)

Profile logout

Log the cart out of the current profile.  No error will occur if they are not logged in. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
cart = com_ultracart_admin_v2.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile logout
    api_response = api_instance.checkout_cart_profile_logout_post(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_profile_logout_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_profile_register_post**
> CartProfileRegisterResponse checkout_cart_profile_register_post(register_request, expand=expand)

Profile registration

Register a new customer profile.  Requires the cart.billing object to be populated along with the password. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
register_request = com_ultracart_admin_v2.CartProfileRegisterRequest() # CartProfileRegisterRequest | Register request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile registration
    api_response = api_instance.checkout_cart_profile_register_post(register_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_profile_register_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**CartProfileRegisterRequest**](CartProfileRegisterRequest.md)| Register request | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartProfileRegisterResponse**](CartProfileRegisterResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_put**
> CartResponse checkout_cart_put(cart, expand=expand)

Update cart

Update the cart. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
cart = com_ultracart_admin_v2.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Update cart
    api_response = api_instance.checkout_cart_put(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_cart_validate_post**
> CartValidationResponse checkout_cart_validate_post(validation_request, expand=expand)

Validate

Validate the cart for errors.  Specific checks can be passed and multiple validations can occur throughout your checkout flow. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
validation_request = com_ultracart_admin_v2.CartValidationRequest() # CartValidationRequest | Validation request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Validate
    api_response = api_instance.checkout_cart_validate_post(validation_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_cart_validate_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_request** | [**CartValidationRequest**](CartValidationRequest.md)| Validation request | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartValidationResponse**](CartValidationResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_city_state_post**
> ItemsResponse checkout_city_state_post(cart)

City/State for Zip

Look up the city and state for the shipping zip code.  Useful for building an auto complete for parts of the shipping address 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
cart = com_ultracart_admin_v2.Cart() # Cart | Cart

try: 
    # City/State for Zip
    api_response = api_instance.checkout_city_state_post(cart)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_city_state_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart | 

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_related_items_item_id_post**
> ItemsResponse checkout_related_items_item_id_post(item_id, cart, expand=expand)

Related items (specific item)

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
item_id = 'item_id_example' # str | Item ID to retrieve related items for
cart = com_ultracart_admin_v2.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

try: 
    # Related items (specific item)
    api_response = api_instance.checkout_related_items_item_id_post(item_id, cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_related_items_item_id_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item ID to retrieve related items for | 
 **cart** | [**Cart**](Cart.md)| Cart | 
 **expand** | **str**| The object expansion to perform on the result.  See item resource documentation for examples | [optional] 

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_related_items_post**
> ItemsResponse checkout_related_items_post(cart, expand=expand)

Related items

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
cart = com_ultracart_admin_v2.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

try: 
    # Related items
    api_response = api_instance.checkout_related_items_post(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_related_items_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart | 
 **expand** | **str**| The object expansion to perform on the result.  See item resource documentation for examples | [optional] 

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_return_return_code_get**
> CartResponse checkout_return_return_code_get(return_code, expand=expand)

Get cart (by return code)

Get a cart specified by the return code parameter. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.CheckoutApi()
return_code = 'return_code_example' # str | Return code to lookup cart ID by
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart (by return code)
    api_response = api_instance.checkout_return_return_code_get(return_code, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->checkout_return_return_code_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_code** | **str**| Return code to lookup cart ID by | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


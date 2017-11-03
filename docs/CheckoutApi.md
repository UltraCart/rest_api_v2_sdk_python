# ultracart.CheckoutApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**city_state**](CheckoutApi.md#city_state) | **POST** /checkout/city_state | City/State for Zip
[**finalize_order**](CheckoutApi.md#finalize_order) | **POST** /checkout/cart/finalizeOrder | Finalize Order
[**get_cart**](CheckoutApi.md#get_cart) | **GET** /checkout/cart | Get cart
[**get_cart_by_cart_id**](CheckoutApi.md#get_cart_by_cart_id) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
[**get_cart_by_return_code**](CheckoutApi.md#get_cart_by_return_code) | **GET** /checkout/return/{return_code} | Get cart (by return code)
[**handoff_cart**](CheckoutApi.md#handoff_cart) | **POST** /checkout/cart/handoff | Handoff cart
[**login**](CheckoutApi.md#login) | **POST** /checkout/cart/profile/login | Profile login
[**logout**](CheckoutApi.md#logout) | **POST** /checkout/cart/profile/logout | Profile logout
[**register**](CheckoutApi.md#register) | **POST** /checkout/cart/profile/register | Profile registration
[**related_items_for_cart**](CheckoutApi.md#related_items_for_cart) | **POST** /checkout/related_items | Related items
[**related_items_for_item**](CheckoutApi.md#related_items_for_item) | **POST** /checkout/relatedItems/{item_id} | Related items (specific item)
[**setup_browser_key**](CheckoutApi.md#setup_browser_key) | **PUT** /checkout/browser_key | Setup Browser Application
[**update_cart**](CheckoutApi.md#update_cart) | **PUT** /checkout/cart | Update cart
[**validate_cart**](CheckoutApi.md#validate_cart) | **POST** /checkout/cart/validate | Validate


# **city_state**
> CityStateZip city_state(cart)

City/State for Zip

Look up the city and state for the shipping zip code.  Useful for building an auto complete for parts of the shipping address 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
cart = ultracart.Cart() # Cart | Cart

try: 
    # City/State for Zip
    api_response = api_instance.city_state(cart)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->city_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart | 

### Return type

[**CityStateZip**](CityStateZip.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_order**
> CartFinalizeOrderResponse finalize_order(finalize_request)

Finalize Order

Finalize the cart into an order.  This method can not be called with browser key authentication.  It is ONLY meant for server side code to call. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
finalize_request = ultracart.CartFinalizeOrderRequest() # CartFinalizeOrderRequest | Finalize request

try: 
    # Finalize Order
    api_response = api_instance.finalize_order(finalize_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->finalize_order: %s\n" % e
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

# **get_cart**
> CartResponse get_cart(expand=expand)

Get cart

If the cookie is set on the browser making the request then it will return their active cart.  Otherwise it will create a new cart. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart
    api_response = api_instance.get_cart(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->get_cart: %s\n" % e
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

# **get_cart_by_cart_id**
> CartResponse get_cart_by_cart_id(cart_id, expand=expand)

Get cart (by cart id)

Get a cart specified by the cart_id parameter. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
cart_id = 'cart_id_example' # str | Cart ID to retrieve
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart (by cart id)
    api_response = api_instance.get_cart_by_cart_id(cart_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->get_cart_by_cart_id: %s\n" % e
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

# **get_cart_by_return_code**
> CartResponse get_cart_by_return_code(return_code, expand=expand)

Get cart (by return code)

Get a cart specified by the return code parameter. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
return_code = 'return_code_example' # str | Return code to lookup cart ID by
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Get cart (by return code)
    api_response = api_instance.get_cart_by_return_code(return_code, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->get_cart_by_return_code: %s\n" % e
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

# **handoff_cart**
> CheckoutHandoffResponse handoff_cart(handoff_request, expand=expand)

Handoff cart

Handoff the browser to UltraCart for view cart on StoreFront, transfer to PayPal, transfer to Affirm or finalization of the order (including upsell processing). 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
handoff_request = ultracart.CheckoutHandoffRequest() # CheckoutHandoffRequest | Handoff request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Handoff cart
    api_response = api_instance.handoff_cart(handoff_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->handoff_cart: %s\n" % e
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

# **login**
> CartProfileLoginResponse login(login_request, expand=expand)

Profile login

Login in to the customer profile specified by cart.billing.email and password 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
login_request = ultracart.CartProfileLoginRequest() # CartProfileLoginRequest | Login request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile login
    api_response = api_instance.login(login_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->login: %s\n" % e
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

# **logout**
> CartResponse logout(cart, expand=expand)

Profile logout

Log the cart out of the current profile.  No error will occur if they are not logged in. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
cart = ultracart.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile logout
    api_response = api_instance.logout(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->logout: %s\n" % e
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

# **register**
> CartProfileRegisterResponse register(register_request, expand=expand)

Profile registration

Register a new customer profile.  Requires the cart.billing object to be populated along with the password. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
register_request = ultracart.CartProfileRegisterRequest() # CartProfileRegisterRequest | Register request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Profile registration
    api_response = api_instance.register(register_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->register: %s\n" % e
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

# **related_items_for_cart**
> ItemsResponse related_items_for_cart(cart, expand=expand)

Related items

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
cart = ultracart.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

try: 
    # Related items
    api_response = api_instance.related_items_for_cart(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->related_items_for_cart: %s\n" % e
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

# **related_items_for_item**
> ItemsResponse related_items_for_item(item_id, cart, expand=expand)

Related items (specific item)

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
item_id = 'item_id_example' # str | Item ID to retrieve related items for
cart = ultracart.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

try: 
    # Related items (specific item)
    api_response = api_instance.related_items_for_item(item_id, cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->related_items_for_item: %s\n" % e
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

# **setup_browser_key**
> CheckoutSetupBrowserKeyResponse setup_browser_key(browser_key_request)

Setup Browser Application

Setup a browser key authenticated application with checkout permissions.  This REST call must be made with an authentication scheme that is not browser key.  The new application will be linked to the application that makes this call.  If this application is disabled / deleted, then so will the application setup by this call.  The purpose of this call is to allow an OAuth applicaiton, such as the Wordpress plugin, to setup the proper browser based authentication for the REST checkout API to use. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
browser_key_request = ultracart.CheckoutSetupBrowserKeyRequest() # CheckoutSetupBrowserKeyRequest | Setup browser key request

try: 
    # Setup Browser Application
    api_response = api_instance.setup_browser_key(browser_key_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->setup_browser_key: %s\n" % e
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

# **update_cart**
> CartResponse update_cart(cart, expand=expand)

Update cart

Update the cart. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
cart = ultracart.Cart() # Cart | Cart
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Update cart
    api_response = api_instance.update_cart(cart, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->update_cart: %s\n" % e
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

# **validate_cart**
> CartValidationResponse validate_cart(validation_request, expand=expand)

Validate

Validate the cart for errors.  Specific checks can be passed and multiple validations can occur throughout your checkout flow. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure API key authorization: ultraCartBrowserApiKey
ultracart.configuration.api_key['x-ultracart-browser-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-browser-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.CheckoutApi()
validation_request = ultracart.CartValidationRequest() # CartValidationRequest | Validation request
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Validate
    api_response = api_instance.validate_cart(validation_request, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CheckoutApi->validate_cart: %s\n" % e
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


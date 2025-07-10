# ultracart.CheckoutApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**city_state**](CheckoutApi.md#city_state) | **POST** /checkout/city_state | City/State for Zip
[**finalize_order**](CheckoutApi.md#finalize_order) | **POST** /checkout/cart/finalizeOrder | Finalize Order
[**get_affirm_checkout**](CheckoutApi.md#get_affirm_checkout) | **GET** /checkout/cart/{cart_id}/affirmCheckout | Get affirm checkout (by cart id)
[**get_allowed_countries**](CheckoutApi.md#get_allowed_countries) | **POST** /checkout/allowedCountries | Allowed countries
[**get_cart**](CheckoutApi.md#get_cart) | **GET** /checkout/cart | Get cart
[**get_cart_by_cart_id**](CheckoutApi.md#get_cart_by_cart_id) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
[**get_cart_by_return_code**](CheckoutApi.md#get_cart_by_return_code) | **GET** /checkout/return/{return_code} | Get cart (by return code)
[**get_cart_by_return_token**](CheckoutApi.md#get_cart_by_return_token) | **GET** /checkout/return_token | Get cart (by return token)
[**get_state_provinces_for_country**](CheckoutApi.md#get_state_provinces_for_country) | **POST** /checkout/stateProvincesForCountry/{country_code} | Get state/province list for a country code
[**handoff_cart**](CheckoutApi.md#handoff_cart) | **POST** /checkout/cart/handoff | Handoff cart
[**login**](CheckoutApi.md#login) | **POST** /checkout/cart/profile/login | Profile login
[**logout**](CheckoutApi.md#logout) | **POST** /checkout/cart/profile/logout | Profile logout
[**register**](CheckoutApi.md#register) | **POST** /checkout/cart/profile/register | Profile registration
[**register_affiliate_click**](CheckoutApi.md#register_affiliate_click) | **POST** /checkout/affiliateClick/register | Register affiliate click
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

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import Cart, CartShipping
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout
# Takes a postal code and returns back a city and state (US Only)

checkout_api = CheckoutApi(api_client())

cart_id = '123456789123456789123456789123456789'  # you should have the cart id from session or cookie
cart = Cart()
cart.cart_id = cart_id  # required
cart.shipping = CartShipping()
cart.shipping.postal_code = '44233'

api_response = checkout_api.city_state(cart)
print(f'City: {api_response.city}')
print(f'State: {api_response.state}')
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_order**
> CartFinalizeOrderResponse finalize_order(finalize_request)

Finalize Order

Finalize the cart into an order.  This method can not be called with browser key authentication.  It is ONLY meant for server side code to call. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CartFinalizeOrderRequest, CartFinalizeOrderRequestOptions
from samples import api_client
from flask import request, redirect

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# Note: You probably should NOT be using this method.  Use handoffCart() instead.
# This method is a server-side only (no browser key allowed) method for turning a cart into an order.
# It exists for merchants who wish to provide their own upsells, but again, a warning, using this method
# will exclude the customer checkout from a vast and powerful suite of functionality provided free by UltraCart.
# Still, some merchants need this functionality, so here it is.  If you're unsure, you don't need it.  Use handoff.

checkout_api = CheckoutApi(api_client())

expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate           items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

# Assuming you have a function to get cookies in your Python framework
cart_id = request.cookies.get('UltraCartShoppingCartID')  # Replace with your actual cookie handling

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)
cart = api_response.cart

# TODO - add some items, collect billing and shipping, use hosted fields to collect payment, etc.

finalize_request = CartFinalizeOrderRequest()
finalize_request.cart = cart
finalize_options = CartFinalizeOrderRequestOptions()  # Lots of options here. Contact support if you're unsure what you need.
finalize_request.options = finalize_options

api_response = checkout_api.finalize_order(finalize_request)
# Available properties:
# api_response.successful
# api_response.errors
# api_response.order_id
# api_response.order

print(api_response)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affirm_checkout**
> CartAffirmCheckoutResponse get_affirm_checkout(cart_id)

Get affirm checkout (by cart id)

Get a Affirm checkout object for the specified cart_id parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client
from flask import session, request

# Reference Implementation: https://github.com/UltraCart/responsive_checkout
# For a given cart id (the cart should be fully updated in UltraCart), returns back the json object
# needed to proceed with an Affirm checkout. See https://www.affirm.com/ for details about Affirm.
# This sample does not show the construction of the affirm checkout widgets. See the affirm api for those examples.

checkout_api = CheckoutApi(api_client())

# this should be retrieved from a session or cookie
cart_id = '123456789123456789123456789123456789'

api_response = checkout_api.get_affirm_checkout(cart_id)
if api_response.errors is not None and len(api_response.errors) > 0:
    # TODO: display errors to customer about the failure
    for error in api_response.errors:
        print(error)
else:
    print(api_response.checkout_json)  # this is the object to send to Affirm.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Cart ID to retrieve |

### Return type

[**CartAffirmCheckoutResponse**](CartAffirmCheckoutResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowed_countries**
> CheckoutAllowedCountriesResponse get_allowed_countries()

Allowed countries

Lookup the allowed countries for this merchant id 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout
# A simple method for populating the country list boxes with all the countries this merchant has configured to accept.

checkout_api = CheckoutApi(api_client())

api_response = checkout_api.get_allowed_countries()
allowed_countries = api_response.countries

for country in allowed_countries:
    print(country)  # contains both iso2code and name
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckoutAllowedCountriesResponse**](CheckoutAllowedCountriesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart**
> CartResponse get_cart()

Get cart

If the cookie is set on the browser making the request then it will return their active cart.  Otherwise it will create a new cart. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client
from flask import request, make_response

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# this example is the same for both getCart.php and getCartByCartId.php. They work as a pair and are called
# depending on the presence of an existing cart id or not. For new carts, getCart() is used. For existing
# carts, getCartByCartId(cart_id) is used.

checkout_api = CheckoutApi(api_client())

expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate           items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

inside_web_context = False
try:
    cart_id = request.cookies.get("UltraCartShoppingCartID")
    inside_web_context = True

except Exception as e:
    # Log the error if needed
    print(f"Error getting cart ID: {e}")
    # Set a default value or handle the error situation
    cart_id = None
    # Execution continues from here

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)

cart = api_response.cart

# TODO: set or re-set the cart cookie if this is part of a multi-page process. two weeks is a generous cart id time.
if inside_web_context:
    response = make_response(str(cart))
    response.set_cookie("UltraCartShoppingCartID", cart.cart_id, max_age=1209600, path="/")

print(cart)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_cart_id**
> CartResponse get_cart_by_cart_id(cart_id)

Get cart (by cart id)

Get a cart specified by the cart_id parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client
from flask import request, make_response

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# this example is the same for both getCart.php and getCartByCartId.php. They work as a pair and are called
# depending on the presence of an existing cart id or not. For new carts, getCart() is used. For existing
# carts, getCartByCartId(cart_id) is used.

checkout_api = CheckoutApi(api_client())

expand = "items"  # for this example, we're just getting a cart to insert some items into it.

cart_id = request.cookies.get("UltraCartShoppingCartID")

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)

cart = api_response.cart

# TODO: set or re-set the cart cookie if this is part of a multi-page process. two weeks is a generous cart id time.
response = make_response(str(cart))
response.set_cookie("UltraCartShoppingCartID", cart.cart_id, max_age=1209600, path="/")

print(cart)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_return_code**
> CartResponse get_cart_by_return_code(return_code)

Get cart (by return code)

Get a cart specified by the return code parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client
from flask import make_response

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# this example returns a shopping cart given a return_code. The return_code is generated by UltraCart
# and usually emailed to a customer. The email will provide a link to this script where you may use the
# return_code to retrieve the customer's cart.

checkout_api = CheckoutApi(api_client())

expand = "items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate           items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

return_code = '1234567890'  # usually retrieved from a query parameter
api_response = checkout_api.get_cart_by_return_code(return_code, expand=expand)
cart = api_response.cart

# TODO: set or re-set the cart cookie if this is part of a multi-page process. two weeks is a generous cart id time.
response = make_response(str(cart))
response.set_cookie("UltraCartShoppingCartID", cart.cart_id, max_age=1209600, path="/")

print(cart)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_return_token**
> CartResponse get_cart_by_return_token()

Get cart (by return token)

Get a cart specified by the encrypted return token parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client
from flask import make_response

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# this example returns a shopping cart given a return_token. The return token is generated by StoreFront Communications
# and usually emailed to a customer. The link within the email will (when you configure your storefront communications)
# provide a link to this script where you may use the token to retrieve the customer's cart.

checkout_api = CheckoutApi(api_client())

expand = "items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate           items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

cart_token = '1234567890'  # usually retrieved from a query parameter
api_response = checkout_api.get_cart_by_return_token(cart_token, expand=expand)
cart = api_response.cart

# TODO: set or re-set the cart cookie if this is part of a multi-page process. two weeks is a generous cart id time.
response = make_response(str(cart))
response.set_cookie("UltraCartShoppingCartID", cart.cart_id, max_age=1209600, path="/")

print(cart)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_token** | **str**| Return token provided by StoreFront Communications | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_provinces_for_country**
> CheckoutStateProvinceResponse get_state_provinces_for_country(country_code)

Get state/province list for a country code

Lookup a state/province list for a given country code 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout
# A simple method for populating the state_region list boxes with all the states/regions allowed for a country code.

checkout_api = CheckoutApi(api_client())

country_code = 'US'

api_response = checkout_api.get_state_provinces_for_country(country_code)
provinces = api_response.state_provinces

for province in provinces:
    print(province)  # contains both name and abbreviation
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter ISO country code |

### Return type

[**CheckoutStateProvinceResponse**](CheckoutStateProvinceResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handoff_cart**
> CheckoutHandoffResponse handoff_cart(handoff_request)

Handoff cart

Handoff the browser to UltraCart for view cart on StoreFront, transfer to PayPal, transfer to Affirm, transfer to Sezzle or finalization of the order (including upsell processing). 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import request, redirect
from ultracart.apis import CheckoutApi
from ultracart.models import CheckoutHandoffRequest
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# This example uses the getCart code as a starting point, because we must get a cart to handoff a cart.
# Here, we are handing off the cart to the ultracart engine with an operation of 'view', meaning that we
# simply added some items to the cart and wish for UltraCart to gather the remaining customer information
# as part of a normal checkout operation.
# Valid operations are: "view", "checkout", "paypal", "paypalcredit", "affirm", "sezzle"
# Besides "view", the other operations are finalizers.
# "checkout": finalize the transaction using a customer's personal credit card (traditional checkout)
# "paypal": finalize the transaction by sending the customer to PayPal

checkout_api = CheckoutApi(api_client())

expand = "items"  # for this example, we're just getting a cart to insert some items into it.

cart_id = request.cookies.get('UltraCartShoppingCartID')

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)
cart = api_response.cart

handoff_request = CheckoutHandoffRequest()
handoff_request.cart = cart
handoff_request.operation = "view"
handoff_request.error_return_url = "/some/page/on/this/python/server/that/can/handle/errors/if/ultracart/encounters/an/issue/with/this/cart"
handoff_request.error_parameter_name = "uc_error"  # name this whatever the script supplied in error_return_url will check for in request.args
handoff_request.secure_host_name = "mystorefront.com"  # set to desired storefront. some merchants have multiple storefronts
api_response = checkout_api.handoff_cart(handoff_request, expand=expand)

if api_response.errors:
    # TODO: handle errors that might happen before handoff and manage those
    pass
else:
    redirect_url = api_response.redirect_to_url
    # return redirect(redirect_url)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> CartProfileLoginResponse login(login_request)

Profile login

Login in to the customer profile specified by cart.billing.email and password 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CartBilling, CartProfileLoginRequest
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# This example logs a user into the UltraCart system.
# This example assumes you already have a shopping cart object created.
# For new carts, getCart() is used. For existing carts, getCartByCartId(cart_id) is used.

checkout_api = CheckoutApi(api_client())

# Note: customer_profile is a required expansion for login to work properly
expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html)

# create a new cart (change this to an existing if you have one)
api_response = checkout_api.get_cart(expand=expand)
cart = api_response.cart

email = 'test@test.com'  # collect this from user
password = 'ABC123'  # collect this from user

cart.billing = CartBilling()
cart.billing.email = email

login_request = CartProfileLoginRequest()
login_request.cart = cart  # will look for billing.email
login_request.password = password

api_response = checkout_api.login(login_request)
cart = api_response.cart

if api_response.success:
    # proceed with successful login.
    pass
else:
    # notify customer login failed.
    pass
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> CartResponse logout(cart)

Profile logout

Log the cart out of the current profile.  No error will occur if they are not logged in. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CartBilling, CartProfileLoginRequest
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# This example logs a user OUT of the UltraCart system.
# It assumes the shopping cart has already had a successful login.
# see login sdk_sample for logging in help.
# For new carts, getCart() is used. For existing carts, getCartByCartId(cart_id) is used.

checkout_api = CheckoutApi(api_client())

# Note: customer_profile is a required expansion for login to work properly
expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html)

# create a new cart (change this to an existing if you have one)
api_response = checkout_api.get_cart(expand=expand)
cart = api_response.cart

email = 'test@test.com'  # collect this from user
password = 'ABC123'  # collect this from user

cart.billing = CartBilling()
cart.billing.email = email

login_request = CartProfileLoginRequest()
login_request.cart = cart  # will look for billing.email
login_request.password = password

api_response = checkout_api.login(login_request)
cart = api_response.cart

if api_response.success:
    checkout_api.logout(cart, expand=expand)  # <-- Here is the logout call.
else:
    # notify customer login failed. Until they login, you can't logout.
    pass
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> CartProfileRegisterResponse register(register_request)

Profile registration

Register a new customer profile.  Requires the cart.billing object to be populated along with the password. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CartBilling, CartProfileRegisterRequest
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# Registers a user in your merchant system. This will create a customer profile.
# For new carts, getCart() is used. For existing carts, getCartByCartId(cart_id) is used.

checkout_api = CheckoutApi(api_client())

# Note: customer_profile is a required expansion for login to work properly
expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html)

# create a new cart (change this to an existing if you have one)
api_response = checkout_api.get_cart(expand=expand)
cart = api_response.cart

email = 'test@test.com'  # collect this from user
password = 'ABC123'  # collect this from user

cart.billing = CartBilling()
cart.billing.email = email  # this is the username

register_request = CartProfileRegisterRequest()
register_request.cart = cart  # will look for billing.email
register_request.password = password

api_response = checkout_api.register(register_request)
cart = api_response.cart  # Important! Get the cart from the response.

if api_response.success:
    print('Successfully registered new customer profile!')
else:
    for error in api_response.errors:
        print(error)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_affiliate_click**
> RegisterAffiliateClickResponse register_affiliate_click(register_affiliate_click_request)

Register affiliate click

Register an affiliate click.  Used by custom checkouts that are completely API based and do not perform checkout handoff. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import request
from ultracart.apis import CheckoutApi
from ultracart.models import RegisterAffiliateClickRequest
from samples import api_client

# Initialize the checkout API
checkout_api = CheckoutApi(api_client())

# Create affiliate click request
click_request = RegisterAffiliateClickRequest(
    ip_address=request.headers.get('X-Forwarded-For', request.remote_addr),
    user_agent=request.headers.get('User-Agent', ''),
    referrer_url=request.referrer or '',
    affid=123456789,  # you should know this from your UltraCart affiliate system
    subid='TODO:SupplyThisValue'
    # landing_page_url=None  # if you have landing page url
)

# Register the affiliate click
api_response = checkout_api.register_affiliate_click(click_request)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_affiliate_click_request** | [**RegisterAffiliateClickRequest**](RegisterAffiliateClickRequest.md)| Register affiliate click request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**RegisterAffiliateClickResponse**](RegisterAffiliateClickResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_items_for_cart**
> ItemsResponse related_items_for_cart(cart)

Related items

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import request
from ultracart.apis import CheckoutApi
from ultracart.models import CartItem
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# Retrieves items related to the items within the cart. Item relations are configured in the UltraCart backend.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377171/Related+Items

# Note: The returned items have a fixed expansion (only so many item properties are returned). The item expansion is:
# content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers

checkout_api = CheckoutApi(api_client())

expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate            items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

cart_id = request.cookies.get('UltraCartShoppingCartID')

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)
cart = api_response.cart

# TODO - add some items to the cart and update.

items = []
cart_item = CartItem()
cart_item.item_id = 'ITEM_ABC'
cart_item.quantity = 1
items.append(cart_item)
cart.items = items

# update the cart and assign it back to our variable
cart = checkout_api.update_cart(cart, expand=expand).cart

api_response = checkout_api.related_items_for_cart(cart)
related_items = api_response.items

print(related_items)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_items_for_item**
> ItemsResponse related_items_for_item(item_id, cart)

Related items (specific item)

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import request
from ultracart.apis import CheckoutApi
from ultracart.models import CartItem
from samples import api_client

# Reference Implementation: https://github.com/UltraCart/responsive_checkout

# Retrieves items related to the items within the cart, in addition to another item id you supply.
# Item relations are configured in the UltraCart backend.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377171/Related+Items

# Note: The returned items have a fixed expansion (only so many item properties are returned). The item expansion is:
# content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers

checkout_api = CheckoutApi(api_client())

expand = "customer_profile,items,billing,shipping,coupons,checkout,payment,summary,taxes"
# Possible Expansion Variables: (see https://www.ultracart.com/api/#resource_checkout.html
"""
affiliate                   checkout                            customer_profile
billing                     coupons                             gift
gift_certificate            items.attributes                   items.multimedia
items                       items.multimedia.thumbnails         items.physical
marketing                   payment                                settings.gift
settings.billing.provinces  settings.shipping.deliver_on_date   settings.shipping.estimates
settings.shipping.provinces settings.shipping.ship_on_date     settings.taxes
settings.terms              shipping                           taxes
summary                     upsell_after
"""

cart_id = request.cookies.get('UltraCartShoppingCartID')

if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)
cart = api_response.cart

# TODO - add some items to the cart and update.

items = []
cart_item = CartItem()
cart_item.item_id = 'ITEM_ABC'
cart_item.quantity = 1
items.append(cart_item)
cart.items = items

# update the cart and assign it back to our variable
cart = checkout_api.update_cart(cart, expand=expand).cart

another_item_id = 'ITEM_ZZZ'

api_response = checkout_api.related_items_for_item(another_item_id, cart, expand=expand)
related_items = api_response.items

print(related_items)
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_browser_key**
> CheckoutSetupBrowserKeyResponse setup_browser_key(browser_key_request)

Setup Browser Application

Setup a browser key authenticated application with checkout permissions.  This REST call must be made with an authentication scheme that is not browser key.  The new application will be linked to the application that makes this call.  If this application is disabled / deleted, then so will the application setup by this call.  The purpose of this call is to allow an OAuth application, such as the Wordpress plugin, to setup the proper browser based authentication for the REST checkout API to use. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CheckoutSetupBrowserKeyRequest
from samples import api_client

# Initialize the checkout API
checkout_api = CheckoutApi(api_client())

# Create browser key request
key_request = CheckoutSetupBrowserKeyRequest(allowed_referrers=["https://www.mywebsite.com"])

# Get browser key
browser_key = checkout_api.setup_browser_key(key_request).browser_key
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart**
> CartResponse update_cart(cart)

Update cart

Update the cart. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import request
from ultracart.apis import CheckoutApi
from ultracart.models import CartItem
from samples import api_client

# Initialize the checkout API
checkout_api = CheckoutApi(api_client())

# Set expansion to retrieve items
expand = "items"

# Check for existing cart ID in cookies
# cart_id = request.cookies.get("UltraCartShoppingCartID")
cart_id = '48E2F76C5BD1BB0196476FAACF800100'

# Get cart based on whether we have an existing cart ID
inside_web_context = False
if cart_id is None:
    api_response = checkout_api.get_cart(expand=expand)
    inside_web_context = True

else:
    api_response = checkout_api.get_cart_by_cart_id(cart_id, expand=expand)

cart = api_response.cart

# Get items array from cart, initialize if needed
items = cart.items or []

# Create new item
item = CartItem(
    item_id="BASEBALL",  # TODO: Adjust the item id
    quantity=1.0,          # TODO: Adjust the quantity
    options=[]          # TODO: If item has options, create CartItemOption objects and add to this list
)

# Add item to items array
items.append(item)

# Update cart with new items
cart.items = items

# Save updated cart
cart_response = checkout_api.update_cart(cart, expand=expand)
cart = cart_response.cart


# if inside_web_context:
#     # Create response with updated cart
#     response = {'cart': cart}
#
#     # Set cookie for cart ID - Using Flask's response object
#     @app.after_request
#     def add_cart_cookie(response):
#         response.set_cookie(
#             "UltraCartShoppingCartID",
#             cart.cart_id,
#             max_age=1209600,  # Two weeks in seconds
#             path="/"
#         )
#         return response
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cart**
> CartValidationResponse validate_cart(validation_request)

Validate

Validate the cart for errors.  Specific checks can be passed and multiple validations can occur throughout your checkout flow. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CheckoutApi
from ultracart.models import CartValidationRequest
from samples import api_client

# Initialize the checkout API
checkout_api = CheckoutApi(api_client())

# Cart ID would normally come from session or cookie
cart_id = '123456789123456789123456789123456789'

# Define expansion string for detailed cart information
expand = "items,billing,shipping,coupons,checkout,payment,summary,taxes"

# Get the cart
cart = checkout_api.get_cart_by_cart_id(cart_id, expand=expand).cart

# Create validation request
validation_request = CartValidationRequest(cart=cart)
# validation_request.checks = None  # leave as None for all validations

# Possible checks:
"""
All, Advertising Source Provided, Billing Address Provided,
Billing Destination Restriction, Billing Phone Numbers Provided, Billing State Abbreviation Valid, Billing Validate City State Zip,
Coupon Zip Code Restriction, Credit Card Shipping Method Conflict, Customer Profile Does Not Exist., CVV2 Not Required,
Electronic Check Confirm Account Number, Email confirmed, Email provided if required, Gift Message Length, Item Quantity Valid,
Item Restrictions, Items Present, Merchant Specific Item Relationships, One per customer violations, Options Provided,
Payment Information Validate, Payment Method Provided, Payment Method Restriction, Pricing Tier Limits, Quantity requirements met,
Referral Code Provided, Shipping Address Provided, Shipping Destination Restriction, Shipping Method Provided,
Shipping Needs Recalculation, Shipping State Abbreviation Valid, Shipping Validate City State Zip, Special Instructions Length,
Tax County Specified, Valid Delivery Date, Valid Ship On Date, Auth Test Credit Card
"""

# Validate cart and get updated cart in response
api_response = checkout_api.validate_cart(validation_request, expand=expand)
cart = api_response.cart

# Handle validation errors
validation_errors = api_response.errors
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


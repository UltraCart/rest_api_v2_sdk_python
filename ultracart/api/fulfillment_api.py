"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ultracart.api_client import ApiClient, Endpoint as _Endpoint
from ultracart.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ultracart.model.distribution_centers_response import DistributionCentersResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.fulfillment_inventory import FulfillmentInventory
from ultracart.model.fulfillment_shipment import FulfillmentShipment
from ultracart.model.order_packing_slip_response import OrderPackingSlipResponse
from ultracart.model.orders_response import OrdersResponse


class FulfillmentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    def fromApiKey(cls, apiKey, verify_ssl = True, debug = False):
        config = Configuration()
        config.api_key['x-ultracart-simple-key'] = apiKey
        config.debug = debug
        config.verify_ssl = verify_ssl

        api_client = ApiClient(configuration=config, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')
        return FulfillmentApi(api_client)


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.acknowledge_orders_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers/{distribution_center_code}/acknowledgements',
                'operation_id': 'acknowledge_orders',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'distribution_center_code',
                    'order_ids',
                ],
                'required': [
                    'distribution_center_code',
                    'order_ids',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'distribution_center_code':
                        (str,),
                    'order_ids':
                        ([str],),
                },
                'attribute_map': {
                    'distribution_center_code': 'distribution_center_code',
                },
                'location_map': {
                    'distribution_center_code': 'path',
                    'order_ids': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.generate_packing_slip_endpoint = _Endpoint(
            settings={
                'response_type': (OrderPackingSlipResponse,),
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers/{distribution_center_code}/orders/{order_id}',
                'operation_id': 'generate_packing_slip',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'distribution_center_code',
                    'order_id',
                ],
                'required': [
                    'distribution_center_code',
                    'order_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'distribution_center_code':
                        (str,),
                    'order_id':
                        (str,),
                },
                'attribute_map': {
                    'distribution_center_code': 'distribution_center_code',
                    'order_id': 'order_id',
                },
                'location_map': {
                    'distribution_center_code': 'path',
                    'order_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_distribution_center_orders_endpoint = _Endpoint(
            settings={
                'response_type': (OrdersResponse,),
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers/{distribution_center_code}/orders',
                'operation_id': 'get_distribution_center_orders',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'distribution_center_code',
                ],
                'required': [
                    'distribution_center_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'distribution_center_code':
                        (str,),
                },
                'attribute_map': {
                    'distribution_center_code': 'distribution_center_code',
                },
                'location_map': {
                    'distribution_center_code': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_distribution_centers_endpoint = _Endpoint(
            settings={
                'response_type': (DistributionCentersResponse,),
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers',
                'operation_id': 'get_distribution_centers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.ship_orders_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers/{distribution_center_code}/shipments',
                'operation_id': 'ship_orders',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'distribution_center_code',
                    'shipments',
                ],
                'required': [
                    'distribution_center_code',
                    'shipments',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'distribution_center_code':
                        (str,),
                    'shipments':
                        ([FulfillmentShipment],),
                },
                'attribute_map': {
                    'distribution_center_code': 'distribution_center_code',
                },
                'location_map': {
                    'distribution_center_code': 'path',
                    'shipments': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_inventory_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ultraCartOauth',
                    'ultraCartSimpleApiKey'
                ],
                'endpoint_path': '/fulfillment/distribution_centers/{distribution_center_code}/inventory',
                'operation_id': 'update_inventory',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'distribution_center_code',
                    'inventories',
                ],
                'required': [
                    'distribution_center_code',
                    'inventories',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'distribution_center_code':
                        (str,),
                    'inventories':
                        ([FulfillmentInventory],),
                },
                'attribute_map': {
                    'distribution_center_code': 'distribution_center_code',
                },
                'location_map': {
                    'distribution_center_code': 'path',
                    'inventories': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def acknowledge_orders(
        self,
        distribution_center_code,
        order_ids,
        **kwargs
    ):
        """Acknowledge receipt of orders.  # noqa: E501

        Acknowledge receipt of orders so that they are removed from the fulfillment queue.  This method must be called after receiving and order (via webhook) or retrieving (via retrieve orders method).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.acknowledge_orders(distribution_center_code, order_ids, async_req=True)
        >>> result = thread.get()

        Args:
            distribution_center_code (str): Distribution center code
            order_ids ([str]): Orders to acknowledge receipt of (limit 100)

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['distribution_center_code'] = \
            distribution_center_code
        kwargs['order_ids'] = \
            order_ids
        return self.acknowledge_orders_endpoint.call_with_http_info(**kwargs)

    def generate_packing_slip(
        self,
        distribution_center_code,
        order_id,
        **kwargs
    ):
        """Generate a packing slip for this order for the given distribution center.  # noqa: E501

        The packing slip PDF that is returned is base 64 encoded   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_packing_slip(distribution_center_code, order_id, async_req=True)
        >>> result = thread.get()

        Args:
            distribution_center_code (str): Distribution center code
            order_id (str): Order ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            OrderPackingSlipResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['distribution_center_code'] = \
            distribution_center_code
        kwargs['order_id'] = \
            order_id
        return self.generate_packing_slip_endpoint.call_with_http_info(**kwargs)

    def get_distribution_center_orders(
        self,
        distribution_center_code,
        **kwargs
    ):
        """Retrieve orders queued up for this distribution center.  # noqa: E501

        Retrieves up to 100 orders that are queued up in this distribution center.  You must acknowledge them before additional new orders will be returned.  There is NO record chunking.  You'll get the same 100 records again and again until you acknowledge orders.  The orders that are returned contain only items for this distribution center and are by default completely expanded with billing, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal, items, payment, shipping, summary, taxes.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_distribution_center_orders(distribution_center_code, async_req=True)
        >>> result = thread.get()

        Args:
            distribution_center_code (str): Distribution center code

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            OrdersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['distribution_center_code'] = \
            distribution_center_code
        return self.get_distribution_center_orders_endpoint.call_with_http_info(**kwargs)

    def get_distribution_centers(
        self,
        **kwargs
    ):
        """Retrieve distribution centers  # noqa: E501

        Retrieves the distribution centers that this user has access to.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_distribution_centers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DistributionCentersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_distribution_centers_endpoint.call_with_http_info(**kwargs)

    def ship_orders(
        self,
        distribution_center_code,
        shipments,
        **kwargs
    ):
        """Mark orders as shipped  # noqa: E501

        Store the tracking information and mark the order shipped for this distribution center.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ship_orders(distribution_center_code, shipments, async_req=True)
        >>> result = thread.get()

        Args:
            distribution_center_code (str): Distribution center code
            shipments ([FulfillmentShipment]): Orders to mark shipped

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['distribution_center_code'] = \
            distribution_center_code
        kwargs['shipments'] = \
            shipments
        return self.ship_orders_endpoint.call_with_http_info(**kwargs)

    def update_inventory(
        self,
        distribution_center_code,
        inventories,
        **kwargs
    ):
        """Update inventory  # noqa: E501

        Update the inventory for items associated with this distribution center   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_inventory(distribution_center_code, inventories, async_req=True)
        >>> result = thread.get()

        Args:
            distribution_center_code (str): Distribution center code
            inventories ([FulfillmentInventory]): Inventory updates (limit 500)

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['distribution_center_code'] = \
            distribution_center_code
        kwargs['inventories'] = \
            inventories
        return self.update_inventory_endpoint.call_with_http_info(**kwargs)


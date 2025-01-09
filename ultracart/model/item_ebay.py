"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ultracart.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ultracart.exceptions import ApiAttributeError


def lazy_import():
    from ultracart.model.item_ebay_category_specific import ItemEbayCategorySpecific
    from ultracart.model.item_ebay_market_place_analysis import ItemEbayMarketPlaceAnalysis
    globals()['ItemEbayCategorySpecific'] = ItemEbayCategorySpecific
    globals()['ItemEbayMarketPlaceAnalysis'] = ItemEbayMarketPlaceAnalysis


class ItemEbay(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'active': (bool,),  # noqa: E501
            'category_id': (int,),  # noqa: E501
            'category_specifics': ([ItemEbayCategorySpecific],),  # noqa: E501
            'condition_description': (str,),  # noqa: E501
            'condition_id': (int,),  # noqa: E501
            'consecutive_failures': (int,),  # noqa: E501
            'custom_category1': (int,),  # noqa: E501
            'custom_category2': (int,),  # noqa: E501
            'dispatch_time_max': (int,),  # noqa: E501
            'domestic_1_additional_cost': (float,),  # noqa: E501
            'domestic_1_first_cost': (float,),  # noqa: E501
            'domestic_2_additional_cost': (float,),  # noqa: E501
            'domestic_2_first_cost': (float,),  # noqa: E501
            'domestic_3_additional_cost': (float,),  # noqa: E501
            'domestic_3_first_cost': (float,),  # noqa: E501
            'domestic_4_additional_cost': (float,),  # noqa: E501
            'domestic_4_first_cost': (float,),  # noqa: E501
            'ebay_auction_id': (str,),  # noqa: E501
            'ebay_specific_inventory': (int,),  # noqa: E501
            'ebay_template_name': (str,),  # noqa: E501
            'ebay_template_oid': (int,),  # noqa: E501
            'end_time': (str,),  # noqa: E501
            'free_shipping': (bool,),  # noqa: E501
            'free_shipping_method': (str,),  # noqa: E501
            'international_1_additional_cost': (float,),  # noqa: E501
            'international_1_first_cost': (float,),  # noqa: E501
            'international_2_additional_cost': (float,),  # noqa: E501
            'international_2_first_cost': (float,),  # noqa: E501
            'international_3_additional_cost': (float,),  # noqa: E501
            'international_3_first_cost': (float,),  # noqa: E501
            'international_4_additional_cost': (float,),  # noqa: E501
            'international_4_first_cost': (float,),  # noqa: E501
            'last_status_dts': (str,),  # noqa: E501
            'listed_dispatch_time_max': (int,),  # noqa: E501
            'listed_ebay_template_oid': (int,),  # noqa: E501
            'listing_dts': (str,),  # noqa: E501
            'listing_duration': (str,),  # noqa: E501
            'listing_price': (float,),  # noqa: E501
            'listing_price_override': (float,),  # noqa: E501
            'listing_type': (str,),  # noqa: E501
            'marketplace_analysis': (ItemEbayMarketPlaceAnalysis,),  # noqa: E501
            'marketplace_analysis_perform': (bool,),  # noqa: E501
            'marketplace_final_value_fee_percentage': (float,),  # noqa: E501
            'marketplace_last_check_dts': (str,),  # noqa: E501
            'marketplace_lowest': (bool,),  # noqa: E501
            'marketplace_map_violation': (bool,),  # noqa: E501
            'marketplace_multiplier': (float,),  # noqa: E501
            'marketplace_other_price': (float,),  # noqa: E501
            'marketplace_other_seller': (str,),  # noqa: E501
            'marketplace_other_shipping': (float,),  # noqa: E501
            'marketplace_other_total': (float,),  # noqa: E501
            'marketplace_our_additional_profit_potential': (float,),  # noqa: E501
            'marketplace_our_price': (float,),  # noqa: E501
            'marketplace_our_profit': (float,),  # noqa: E501
            'marketplace_our_shipping': (float,),  # noqa: E501
            'marketplace_our_total': (float,),  # noqa: E501
            'marketplace_overhead': (float,),  # noqa: E501
            'marketplace_profitable': (bool,),  # noqa: E501
            'next_attempt_dts': (str,),  # noqa: E501
            'next_listing_duration': (str,),  # noqa: E501
            'no_promotional_shipping': (bool,),  # noqa: E501
            'packaging_handling_costs': (float,),  # noqa: E501
            'previous_ebay_auction_id': (str,),  # noqa: E501
            'quantity': (int,),  # noqa: E501
            'reserve_price': (float,),  # noqa: E501
            'send_dimensions_and_weight': (str,),  # noqa: E501
            'start_time': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'target_dispatch_time_max': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active': 'active',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'category_specifics': 'category_specifics',  # noqa: E501
        'condition_description': 'condition_description',  # noqa: E501
        'condition_id': 'condition_id',  # noqa: E501
        'consecutive_failures': 'consecutive_failures',  # noqa: E501
        'custom_category1': 'custom_category1',  # noqa: E501
        'custom_category2': 'custom_category2',  # noqa: E501
        'dispatch_time_max': 'dispatch_time_max',  # noqa: E501
        'domestic_1_additional_cost': 'domestic_1_additional_cost',  # noqa: E501
        'domestic_1_first_cost': 'domestic_1_first_cost',  # noqa: E501
        'domestic_2_additional_cost': 'domestic_2_additional_cost',  # noqa: E501
        'domestic_2_first_cost': 'domestic_2_first_cost',  # noqa: E501
        'domestic_3_additional_cost': 'domestic_3_additional_cost',  # noqa: E501
        'domestic_3_first_cost': 'domestic_3_first_cost',  # noqa: E501
        'domestic_4_additional_cost': 'domestic_4_additional_cost',  # noqa: E501
        'domestic_4_first_cost': 'domestic_4_first_cost',  # noqa: E501
        'ebay_auction_id': 'ebay_auction_id',  # noqa: E501
        'ebay_specific_inventory': 'ebay_specific_inventory',  # noqa: E501
        'ebay_template_name': 'ebay_template_name',  # noqa: E501
        'ebay_template_oid': 'ebay_template_oid',  # noqa: E501
        'end_time': 'end_time',  # noqa: E501
        'free_shipping': 'free_shipping',  # noqa: E501
        'free_shipping_method': 'free_shipping_method',  # noqa: E501
        'international_1_additional_cost': 'international_1_additional_cost',  # noqa: E501
        'international_1_first_cost': 'international_1_first_cost',  # noqa: E501
        'international_2_additional_cost': 'international_2_additional_cost',  # noqa: E501
        'international_2_first_cost': 'international_2_first_cost',  # noqa: E501
        'international_3_additional_cost': 'international_3_additional_cost',  # noqa: E501
        'international_3_first_cost': 'international_3_first_cost',  # noqa: E501
        'international_4_additional_cost': 'international_4_additional_cost',  # noqa: E501
        'international_4_first_cost': 'international_4_first_cost',  # noqa: E501
        'last_status_dts': 'last_status_dts',  # noqa: E501
        'listed_dispatch_time_max': 'listed_dispatch_time_max',  # noqa: E501
        'listed_ebay_template_oid': 'listed_ebay_template_oid',  # noqa: E501
        'listing_dts': 'listing_dts',  # noqa: E501
        'listing_duration': 'listing_duration',  # noqa: E501
        'listing_price': 'listing_price',  # noqa: E501
        'listing_price_override': 'listing_price_override',  # noqa: E501
        'listing_type': 'listing_type',  # noqa: E501
        'marketplace_analysis': 'marketplace_analysis',  # noqa: E501
        'marketplace_analysis_perform': 'marketplace_analysis_perform',  # noqa: E501
        'marketplace_final_value_fee_percentage': 'marketplace_final_value_fee_percentage',  # noqa: E501
        'marketplace_last_check_dts': 'marketplace_last_check_dts',  # noqa: E501
        'marketplace_lowest': 'marketplace_lowest',  # noqa: E501
        'marketplace_map_violation': 'marketplace_map_violation',  # noqa: E501
        'marketplace_multiplier': 'marketplace_multiplier',  # noqa: E501
        'marketplace_other_price': 'marketplace_other_price',  # noqa: E501
        'marketplace_other_seller': 'marketplace_other_seller',  # noqa: E501
        'marketplace_other_shipping': 'marketplace_other_shipping',  # noqa: E501
        'marketplace_other_total': 'marketplace_other_total',  # noqa: E501
        'marketplace_our_additional_profit_potential': 'marketplace_our_additional_profit_potential',  # noqa: E501
        'marketplace_our_price': 'marketplace_our_price',  # noqa: E501
        'marketplace_our_profit': 'marketplace_our_profit',  # noqa: E501
        'marketplace_our_shipping': 'marketplace_our_shipping',  # noqa: E501
        'marketplace_our_total': 'marketplace_our_total',  # noqa: E501
        'marketplace_overhead': 'marketplace_overhead',  # noqa: E501
        'marketplace_profitable': 'marketplace_profitable',  # noqa: E501
        'next_attempt_dts': 'next_attempt_dts',  # noqa: E501
        'next_listing_duration': 'next_listing_duration',  # noqa: E501
        'no_promotional_shipping': 'no_promotional_shipping',  # noqa: E501
        'packaging_handling_costs': 'packaging_handling_costs',  # noqa: E501
        'previous_ebay_auction_id': 'previous_ebay_auction_id',  # noqa: E501
        'quantity': 'quantity',  # noqa: E501
        'reserve_price': 'reserve_price',  # noqa: E501
        'send_dimensions_and_weight': 'send_dimensions_and_weight',  # noqa: E501
        'start_time': 'start_time',  # noqa: E501
        'status': 'status',  # noqa: E501
        'target_dispatch_time_max': 'target_dispatch_time_max',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ItemEbay - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active (bool): True if the item is active for listing. [optional]  # noqa: E501
            category_id (int): e-Bay category ID. [optional]  # noqa: E501
            category_specifics ([ItemEbayCategorySpecific]): Answers to category specific questions. [optional]  # noqa: E501
            condition_description (str): Description of the condition (e-Bay constant). [optional]  # noqa: E501
            condition_id (int): Numerical ID of the condition (e-Bay constant). [optional]  # noqa: E501
            consecutive_failures (int): Number of consecutive failures trying to list this item. [optional]  # noqa: E501
            custom_category1 (int): e-Bay Store category 1. [optional]  # noqa: E501
            custom_category2 (int): e-Bay Store category 2. [optional]  # noqa: E501
            dispatch_time_max (int): Maximum number of days it will take to ship the item. [optional]  # noqa: E501
            domestic_1_additional_cost (float): Domestic 1 method additional item cost. [optional]  # noqa: E501
            domestic_1_first_cost (float): Domestic 1 method first item cost. [optional]  # noqa: E501
            domestic_2_additional_cost (float): Domestic 2 method additional item cost. [optional]  # noqa: E501
            domestic_2_first_cost (float): Domestic 2 method first item cost. [optional]  # noqa: E501
            domestic_3_additional_cost (float): Domestic 3 method additional item cost. [optional]  # noqa: E501
            domestic_3_first_cost (float): Domestic 3 method first item cost. [optional]  # noqa: E501
            domestic_4_additional_cost (float): Domestic 4 method additional item cost. [optional]  # noqa: E501
            domestic_4_first_cost (float): Domestic 4 method first item cost. [optional]  # noqa: E501
            ebay_auction_id (str): If listed, this is the e-Bay auction id. [optional]  # noqa: E501
            ebay_specific_inventory (int): e-Bay specific inventory. [optional]  # noqa: E501
            ebay_template_name (str): The template name to use hwen rendering the e-Bay listing. [optional]  # noqa: E501
            ebay_template_oid (int): The template object identifier to use when rendering the e-Bay listing. [optional]  # noqa: E501
            end_time (str): Date/time of the auction end. [optional]  # noqa: E501
            free_shipping (bool): True if item receives free shipping. [optional]  # noqa: E501
            free_shipping_method (str): The method that is free for free shipping. [optional]  # noqa: E501
            international_1_additional_cost (float): International 1 method additional item cost. [optional]  # noqa: E501
            international_1_first_cost (float): International 1 method first item cost. [optional]  # noqa: E501
            international_2_additional_cost (float): International 2 method additional item cost. [optional]  # noqa: E501
            international_2_first_cost (float): International 2 method first item cost. [optional]  # noqa: E501
            international_3_additional_cost (float): International 3 method additional item cost. [optional]  # noqa: E501
            international_3_first_cost (float): International 3 method first item cost. [optional]  # noqa: E501
            international_4_additional_cost (float): International 4 method additional item cost. [optional]  # noqa: E501
            international_4_first_cost (float): International 4 method first item cost. [optional]  # noqa: E501
            last_status_dts (str): Date/time of the last status check. [optional]  # noqa: E501
            listed_dispatch_time_max (int): Current listing dispatch time maximum. [optional]  # noqa: E501
            listed_ebay_template_oid (int): The template object identifier used for the listing. [optional]  # noqa: E501
            listing_dts (str): Date/time of the listing. [optional]  # noqa: E501
            listing_duration (str): The duration of the listing. [optional]  # noqa: E501
            listing_price (float): Price to list the item at. [optional]  # noqa: E501
            listing_price_override (float): The price to list the item at if different than the regular UltraCart item price. [optional]  # noqa: E501
            listing_type (str): The type of e-Bay listing. [optional]  # noqa: E501
            marketplace_analysis (ItemEbayMarketPlaceAnalysis): [optional]  # noqa: E501
            marketplace_analysis_perform (bool): True if marketplace analysis should be performed. [optional]  # noqa: E501
            marketplace_final_value_fee_percentage (float): Marketplace FVF percentage. [optional]  # noqa: E501
            marketplace_last_check_dts (str): Date/time of the marketplace analysis last check. [optional]  # noqa: E501
            marketplace_lowest (bool): True if we are the lowest offer in the marketplace. [optional]  # noqa: E501
            marketplace_map_violation (bool): True if another seller is violating MAP. [optional]  # noqa: E501
            marketplace_multiplier (float): Marketplace multiplier. [optional]  # noqa: E501
            marketplace_other_price (float): Marketplace other price. [optional]  # noqa: E501
            marketplace_other_seller (str): Marketplace other seller. [optional]  # noqa: E501
            marketplace_other_shipping (float): Marketplace other shipping. [optional]  # noqa: E501
            marketplace_other_total (float): Marketplace other total. [optional]  # noqa: E501
            marketplace_our_additional_profit_potential (float): Marketplace our additional profit potential. [optional]  # noqa: E501
            marketplace_our_price (float): Marketplace our price. [optional]  # noqa: E501
            marketplace_our_profit (float): Marketplace our profit. [optional]  # noqa: E501
            marketplace_our_shipping (float): Marketplace our shipping. [optional]  # noqa: E501
            marketplace_our_total (float): Marketplace our total. [optional]  # noqa: E501
            marketplace_overhead (float): Marketplace overhead. [optional]  # noqa: E501
            marketplace_profitable (bool): True if our listing is profitable to sell. [optional]  # noqa: E501
            next_attempt_dts (str): Date/time for the next attempt to list. [optional]  # noqa: E501
            next_listing_duration (str): The next listing duration to use when the current listing ends.. [optional]  # noqa: E501
            no_promotional_shipping (bool): True if the item should not qualify for promotional shipping. [optional]  # noqa: E501
            packaging_handling_costs (float): Packaging and handling costs. [optional]  # noqa: E501
            previous_ebay_auction_id (str): Previous e-Bay auction id. [optional]  # noqa: E501
            quantity (int): Quantity available of the item. [optional]  # noqa: E501
            reserve_price (float): Reserve price. [optional]  # noqa: E501
            send_dimensions_and_weight (str): How to send the item dimensions and weights to e-Bay. [optional]  # noqa: E501
            start_time (str): Date/time of the auction start. [optional]  # noqa: E501
            status (str): Status of the item's listing. [optional]  # noqa: E501
            target_dispatch_time_max (int): Typical number of days it will take to ship the item. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ItemEbay - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active (bool): True if the item is active for listing. [optional]  # noqa: E501
            category_id (int): e-Bay category ID. [optional]  # noqa: E501
            category_specifics ([ItemEbayCategorySpecific]): Answers to category specific questions. [optional]  # noqa: E501
            condition_description (str): Description of the condition (e-Bay constant). [optional]  # noqa: E501
            condition_id (int): Numerical ID of the condition (e-Bay constant). [optional]  # noqa: E501
            consecutive_failures (int): Number of consecutive failures trying to list this item. [optional]  # noqa: E501
            custom_category1 (int): e-Bay Store category 1. [optional]  # noqa: E501
            custom_category2 (int): e-Bay Store category 2. [optional]  # noqa: E501
            dispatch_time_max (int): Maximum number of days it will take to ship the item. [optional]  # noqa: E501
            domestic_1_additional_cost (float): Domestic 1 method additional item cost. [optional]  # noqa: E501
            domestic_1_first_cost (float): Domestic 1 method first item cost. [optional]  # noqa: E501
            domestic_2_additional_cost (float): Domestic 2 method additional item cost. [optional]  # noqa: E501
            domestic_2_first_cost (float): Domestic 2 method first item cost. [optional]  # noqa: E501
            domestic_3_additional_cost (float): Domestic 3 method additional item cost. [optional]  # noqa: E501
            domestic_3_first_cost (float): Domestic 3 method first item cost. [optional]  # noqa: E501
            domestic_4_additional_cost (float): Domestic 4 method additional item cost. [optional]  # noqa: E501
            domestic_4_first_cost (float): Domestic 4 method first item cost. [optional]  # noqa: E501
            ebay_auction_id (str): If listed, this is the e-Bay auction id. [optional]  # noqa: E501
            ebay_specific_inventory (int): e-Bay specific inventory. [optional]  # noqa: E501
            ebay_template_name (str): The template name to use hwen rendering the e-Bay listing. [optional]  # noqa: E501
            ebay_template_oid (int): The template object identifier to use when rendering the e-Bay listing. [optional]  # noqa: E501
            end_time (str): Date/time of the auction end. [optional]  # noqa: E501
            free_shipping (bool): True if item receives free shipping. [optional]  # noqa: E501
            free_shipping_method (str): The method that is free for free shipping. [optional]  # noqa: E501
            international_1_additional_cost (float): International 1 method additional item cost. [optional]  # noqa: E501
            international_1_first_cost (float): International 1 method first item cost. [optional]  # noqa: E501
            international_2_additional_cost (float): International 2 method additional item cost. [optional]  # noqa: E501
            international_2_first_cost (float): International 2 method first item cost. [optional]  # noqa: E501
            international_3_additional_cost (float): International 3 method additional item cost. [optional]  # noqa: E501
            international_3_first_cost (float): International 3 method first item cost. [optional]  # noqa: E501
            international_4_additional_cost (float): International 4 method additional item cost. [optional]  # noqa: E501
            international_4_first_cost (float): International 4 method first item cost. [optional]  # noqa: E501
            last_status_dts (str): Date/time of the last status check. [optional]  # noqa: E501
            listed_dispatch_time_max (int): Current listing dispatch time maximum. [optional]  # noqa: E501
            listed_ebay_template_oid (int): The template object identifier used for the listing. [optional]  # noqa: E501
            listing_dts (str): Date/time of the listing. [optional]  # noqa: E501
            listing_duration (str): The duration of the listing. [optional]  # noqa: E501
            listing_price (float): Price to list the item at. [optional]  # noqa: E501
            listing_price_override (float): The price to list the item at if different than the regular UltraCart item price. [optional]  # noqa: E501
            listing_type (str): The type of e-Bay listing. [optional]  # noqa: E501
            marketplace_analysis (ItemEbayMarketPlaceAnalysis): [optional]  # noqa: E501
            marketplace_analysis_perform (bool): True if marketplace analysis should be performed. [optional]  # noqa: E501
            marketplace_final_value_fee_percentage (float): Marketplace FVF percentage. [optional]  # noqa: E501
            marketplace_last_check_dts (str): Date/time of the marketplace analysis last check. [optional]  # noqa: E501
            marketplace_lowest (bool): True if we are the lowest offer in the marketplace. [optional]  # noqa: E501
            marketplace_map_violation (bool): True if another seller is violating MAP. [optional]  # noqa: E501
            marketplace_multiplier (float): Marketplace multiplier. [optional]  # noqa: E501
            marketplace_other_price (float): Marketplace other price. [optional]  # noqa: E501
            marketplace_other_seller (str): Marketplace other seller. [optional]  # noqa: E501
            marketplace_other_shipping (float): Marketplace other shipping. [optional]  # noqa: E501
            marketplace_other_total (float): Marketplace other total. [optional]  # noqa: E501
            marketplace_our_additional_profit_potential (float): Marketplace our additional profit potential. [optional]  # noqa: E501
            marketplace_our_price (float): Marketplace our price. [optional]  # noqa: E501
            marketplace_our_profit (float): Marketplace our profit. [optional]  # noqa: E501
            marketplace_our_shipping (float): Marketplace our shipping. [optional]  # noqa: E501
            marketplace_our_total (float): Marketplace our total. [optional]  # noqa: E501
            marketplace_overhead (float): Marketplace overhead. [optional]  # noqa: E501
            marketplace_profitable (bool): True if our listing is profitable to sell. [optional]  # noqa: E501
            next_attempt_dts (str): Date/time for the next attempt to list. [optional]  # noqa: E501
            next_listing_duration (str): The next listing duration to use when the current listing ends.. [optional]  # noqa: E501
            no_promotional_shipping (bool): True if the item should not qualify for promotional shipping. [optional]  # noqa: E501
            packaging_handling_costs (float): Packaging and handling costs. [optional]  # noqa: E501
            previous_ebay_auction_id (str): Previous e-Bay auction id. [optional]  # noqa: E501
            quantity (int): Quantity available of the item. [optional]  # noqa: E501
            reserve_price (float): Reserve price. [optional]  # noqa: E501
            send_dimensions_and_weight (str): How to send the item dimensions and weights to e-Bay. [optional]  # noqa: E501
            start_time (str): Date/time of the auction start. [optional]  # noqa: E501
            status (str): Status of the item's listing. [optional]  # noqa: E501
            target_dispatch_time_max (int): Typical number of days it will take to ship the item. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

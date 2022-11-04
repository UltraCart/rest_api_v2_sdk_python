# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ItemReview(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer_profile_oid': 'int',
        'featured': 'bool',
        'helperful_no_votes': 'int',
        'helpful_yes_votes': 'int',
        'order_id': 'str',
        'overall': 'float',
        'rating_name1': 'str',
        'rating_name10': 'str',
        'rating_name2': 'str',
        'rating_name3': 'str',
        'rating_name4': 'str',
        'rating_name5': 'str',
        'rating_name6': 'str',
        'rating_name7': 'str',
        'rating_name8': 'str',
        'rating_name9': 'str',
        'rating_score1': 'float',
        'rating_score10': 'float',
        'rating_score2': 'float',
        'rating_score3': 'float',
        'rating_score4': 'float',
        'rating_score5': 'float',
        'rating_score6': 'float',
        'rating_score7': 'float',
        'rating_score8': 'float',
        'rating_score9': 'float',
        'recommend_store_to_friend': 'int',
        'recommend_to_friend': 'bool',
        'review': 'str',
        'review_oid': 'int',
        'reviewed_nickname': 'str',
        'reviewer_email': 'str',
        'reviewer_location': 'str',
        'status': 'str',
        'store_feedback': 'str',
        'submitted_dts': 'str',
        'title': 'str'
    }

    attribute_map = {
        'customer_profile_oid': 'customer_profile_oid',
        'featured': 'featured',
        'helperful_no_votes': 'helperful_no_votes',
        'helpful_yes_votes': 'helpful_yes_votes',
        'order_id': 'order_id',
        'overall': 'overall',
        'rating_name1': 'rating_name1',
        'rating_name10': 'rating_name10',
        'rating_name2': 'rating_name2',
        'rating_name3': 'rating_name3',
        'rating_name4': 'rating_name4',
        'rating_name5': 'rating_name5',
        'rating_name6': 'rating_name6',
        'rating_name7': 'rating_name7',
        'rating_name8': 'rating_name8',
        'rating_name9': 'rating_name9',
        'rating_score1': 'rating_score1',
        'rating_score10': 'rating_score10',
        'rating_score2': 'rating_score2',
        'rating_score3': 'rating_score3',
        'rating_score4': 'rating_score4',
        'rating_score5': 'rating_score5',
        'rating_score6': 'rating_score6',
        'rating_score7': 'rating_score7',
        'rating_score8': 'rating_score8',
        'rating_score9': 'rating_score9',
        'recommend_store_to_friend': 'recommend_store_to_friend',
        'recommend_to_friend': 'recommend_to_friend',
        'review': 'review',
        'review_oid': 'review_oid',
        'reviewed_nickname': 'reviewed_nickname',
        'reviewer_email': 'reviewer_email',
        'reviewer_location': 'reviewer_location',
        'status': 'status',
        'store_feedback': 'store_feedback',
        'submitted_dts': 'submitted_dts',
        'title': 'title'
    }

    def __init__(self, customer_profile_oid=None, featured=None, helperful_no_votes=None, helpful_yes_votes=None, order_id=None, overall=None, rating_name1=None, rating_name10=None, rating_name2=None, rating_name3=None, rating_name4=None, rating_name5=None, rating_name6=None, rating_name7=None, rating_name8=None, rating_name9=None, rating_score1=None, rating_score10=None, rating_score2=None, rating_score3=None, rating_score4=None, rating_score5=None, rating_score6=None, rating_score7=None, rating_score8=None, rating_score9=None, recommend_store_to_friend=None, recommend_to_friend=None, review=None, review_oid=None, reviewed_nickname=None, reviewer_email=None, reviewer_location=None, status=None, store_feedback=None, submitted_dts=None, title=None):  # noqa: E501
        """ItemReview - a model defined in Swagger"""  # noqa: E501

        self._customer_profile_oid = None
        self._featured = None
        self._helperful_no_votes = None
        self._helpful_yes_votes = None
        self._order_id = None
        self._overall = None
        self._rating_name1 = None
        self._rating_name10 = None
        self._rating_name2 = None
        self._rating_name3 = None
        self._rating_name4 = None
        self._rating_name5 = None
        self._rating_name6 = None
        self._rating_name7 = None
        self._rating_name8 = None
        self._rating_name9 = None
        self._rating_score1 = None
        self._rating_score10 = None
        self._rating_score2 = None
        self._rating_score3 = None
        self._rating_score4 = None
        self._rating_score5 = None
        self._rating_score6 = None
        self._rating_score7 = None
        self._rating_score8 = None
        self._rating_score9 = None
        self._recommend_store_to_friend = None
        self._recommend_to_friend = None
        self._review = None
        self._review_oid = None
        self._reviewed_nickname = None
        self._reviewer_email = None
        self._reviewer_location = None
        self._status = None
        self._store_feedback = None
        self._submitted_dts = None
        self._title = None
        self.discriminator = None

        if customer_profile_oid is not None:
            self.customer_profile_oid = customer_profile_oid
        if featured is not None:
            self.featured = featured
        if helperful_no_votes is not None:
            self.helperful_no_votes = helperful_no_votes
        if helpful_yes_votes is not None:
            self.helpful_yes_votes = helpful_yes_votes
        if order_id is not None:
            self.order_id = order_id
        if overall is not None:
            self.overall = overall
        if rating_name1 is not None:
            self.rating_name1 = rating_name1
        if rating_name10 is not None:
            self.rating_name10 = rating_name10
        if rating_name2 is not None:
            self.rating_name2 = rating_name2
        if rating_name3 is not None:
            self.rating_name3 = rating_name3
        if rating_name4 is not None:
            self.rating_name4 = rating_name4
        if rating_name5 is not None:
            self.rating_name5 = rating_name5
        if rating_name6 is not None:
            self.rating_name6 = rating_name6
        if rating_name7 is not None:
            self.rating_name7 = rating_name7
        if rating_name8 is not None:
            self.rating_name8 = rating_name8
        if rating_name9 is not None:
            self.rating_name9 = rating_name9
        if rating_score1 is not None:
            self.rating_score1 = rating_score1
        if rating_score10 is not None:
            self.rating_score10 = rating_score10
        if rating_score2 is not None:
            self.rating_score2 = rating_score2
        if rating_score3 is not None:
            self.rating_score3 = rating_score3
        if rating_score4 is not None:
            self.rating_score4 = rating_score4
        if rating_score5 is not None:
            self.rating_score5 = rating_score5
        if rating_score6 is not None:
            self.rating_score6 = rating_score6
        if rating_score7 is not None:
            self.rating_score7 = rating_score7
        if rating_score8 is not None:
            self.rating_score8 = rating_score8
        if rating_score9 is not None:
            self.rating_score9 = rating_score9
        if recommend_store_to_friend is not None:
            self.recommend_store_to_friend = recommend_store_to_friend
        if recommend_to_friend is not None:
            self.recommend_to_friend = recommend_to_friend
        if review is not None:
            self.review = review
        if review_oid is not None:
            self.review_oid = review_oid
        if reviewed_nickname is not None:
            self.reviewed_nickname = reviewed_nickname
        if reviewer_email is not None:
            self.reviewer_email = reviewer_email
        if reviewer_location is not None:
            self.reviewer_location = reviewer_location
        if status is not None:
            self.status = status
        if store_feedback is not None:
            self.store_feedback = store_feedback
        if submitted_dts is not None:
            self.submitted_dts = submitted_dts
        if title is not None:
            self.title = title

    @property
    def customer_profile_oid(self):
        """Gets the customer_profile_oid of this ItemReview.  # noqa: E501

        Customer profile object identifier  # noqa: E501

        :return: The customer_profile_oid of this ItemReview.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_oid

    @customer_profile_oid.setter
    def customer_profile_oid(self, customer_profile_oid):
        """Sets the customer_profile_oid of this ItemReview.

        Customer profile object identifier  # noqa: E501

        :param customer_profile_oid: The customer_profile_oid of this ItemReview.  # noqa: E501
        :type: int
        """

        self._customer_profile_oid = customer_profile_oid

    @property
    def featured(self):
        """Gets the featured of this ItemReview.  # noqa: E501


        :return: The featured of this ItemReview.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this ItemReview.


        :param featured: The featured of this ItemReview.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def helperful_no_votes(self):
        """Gets the helperful_no_votes of this ItemReview.  # noqa: E501


        :return: The helperful_no_votes of this ItemReview.  # noqa: E501
        :rtype: int
        """
        return self._helperful_no_votes

    @helperful_no_votes.setter
    def helperful_no_votes(self, helperful_no_votes):
        """Sets the helperful_no_votes of this ItemReview.


        :param helperful_no_votes: The helperful_no_votes of this ItemReview.  # noqa: E501
        :type: int
        """

        self._helperful_no_votes = helperful_no_votes

    @property
    def helpful_yes_votes(self):
        """Gets the helpful_yes_votes of this ItemReview.  # noqa: E501


        :return: The helpful_yes_votes of this ItemReview.  # noqa: E501
        :rtype: int
        """
        return self._helpful_yes_votes

    @helpful_yes_votes.setter
    def helpful_yes_votes(self, helpful_yes_votes):
        """Sets the helpful_yes_votes of this ItemReview.


        :param helpful_yes_votes: The helpful_yes_votes of this ItemReview.  # noqa: E501
        :type: int
        """

        self._helpful_yes_votes = helpful_yes_votes

    @property
    def order_id(self):
        """Gets the order_id of this ItemReview.  # noqa: E501


        :return: The order_id of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ItemReview.


        :param order_id: The order_id of this ItemReview.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def overall(self):
        """Gets the overall of this ItemReview.  # noqa: E501


        :return: The overall of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this ItemReview.


        :param overall: The overall of this ItemReview.  # noqa: E501
        :type: float
        """

        self._overall = overall

    @property
    def rating_name1(self):
        """Gets the rating_name1 of this ItemReview.  # noqa: E501


        :return: The rating_name1 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name1

    @rating_name1.setter
    def rating_name1(self, rating_name1):
        """Sets the rating_name1 of this ItemReview.


        :param rating_name1: The rating_name1 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name1 = rating_name1

    @property
    def rating_name10(self):
        """Gets the rating_name10 of this ItemReview.  # noqa: E501


        :return: The rating_name10 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name10

    @rating_name10.setter
    def rating_name10(self, rating_name10):
        """Sets the rating_name10 of this ItemReview.


        :param rating_name10: The rating_name10 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name10 = rating_name10

    @property
    def rating_name2(self):
        """Gets the rating_name2 of this ItemReview.  # noqa: E501


        :return: The rating_name2 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name2

    @rating_name2.setter
    def rating_name2(self, rating_name2):
        """Sets the rating_name2 of this ItemReview.


        :param rating_name2: The rating_name2 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name2 = rating_name2

    @property
    def rating_name3(self):
        """Gets the rating_name3 of this ItemReview.  # noqa: E501


        :return: The rating_name3 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name3

    @rating_name3.setter
    def rating_name3(self, rating_name3):
        """Sets the rating_name3 of this ItemReview.


        :param rating_name3: The rating_name3 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name3 = rating_name3

    @property
    def rating_name4(self):
        """Gets the rating_name4 of this ItemReview.  # noqa: E501


        :return: The rating_name4 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name4

    @rating_name4.setter
    def rating_name4(self, rating_name4):
        """Sets the rating_name4 of this ItemReview.


        :param rating_name4: The rating_name4 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name4 = rating_name4

    @property
    def rating_name5(self):
        """Gets the rating_name5 of this ItemReview.  # noqa: E501


        :return: The rating_name5 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name5

    @rating_name5.setter
    def rating_name5(self, rating_name5):
        """Sets the rating_name5 of this ItemReview.


        :param rating_name5: The rating_name5 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name5 = rating_name5

    @property
    def rating_name6(self):
        """Gets the rating_name6 of this ItemReview.  # noqa: E501


        :return: The rating_name6 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name6

    @rating_name6.setter
    def rating_name6(self, rating_name6):
        """Sets the rating_name6 of this ItemReview.


        :param rating_name6: The rating_name6 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name6 = rating_name6

    @property
    def rating_name7(self):
        """Gets the rating_name7 of this ItemReview.  # noqa: E501


        :return: The rating_name7 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name7

    @rating_name7.setter
    def rating_name7(self, rating_name7):
        """Sets the rating_name7 of this ItemReview.


        :param rating_name7: The rating_name7 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name7 = rating_name7

    @property
    def rating_name8(self):
        """Gets the rating_name8 of this ItemReview.  # noqa: E501


        :return: The rating_name8 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name8

    @rating_name8.setter
    def rating_name8(self, rating_name8):
        """Sets the rating_name8 of this ItemReview.


        :param rating_name8: The rating_name8 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name8 = rating_name8

    @property
    def rating_name9(self):
        """Gets the rating_name9 of this ItemReview.  # noqa: E501


        :return: The rating_name9 of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._rating_name9

    @rating_name9.setter
    def rating_name9(self, rating_name9):
        """Sets the rating_name9 of this ItemReview.


        :param rating_name9: The rating_name9 of this ItemReview.  # noqa: E501
        :type: str
        """

        self._rating_name9 = rating_name9

    @property
    def rating_score1(self):
        """Gets the rating_score1 of this ItemReview.  # noqa: E501


        :return: The rating_score1 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score1

    @rating_score1.setter
    def rating_score1(self, rating_score1):
        """Sets the rating_score1 of this ItemReview.


        :param rating_score1: The rating_score1 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score1 = rating_score1

    @property
    def rating_score10(self):
        """Gets the rating_score10 of this ItemReview.  # noqa: E501


        :return: The rating_score10 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score10

    @rating_score10.setter
    def rating_score10(self, rating_score10):
        """Sets the rating_score10 of this ItemReview.


        :param rating_score10: The rating_score10 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score10 = rating_score10

    @property
    def rating_score2(self):
        """Gets the rating_score2 of this ItemReview.  # noqa: E501


        :return: The rating_score2 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score2

    @rating_score2.setter
    def rating_score2(self, rating_score2):
        """Sets the rating_score2 of this ItemReview.


        :param rating_score2: The rating_score2 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score2 = rating_score2

    @property
    def rating_score3(self):
        """Gets the rating_score3 of this ItemReview.  # noqa: E501


        :return: The rating_score3 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score3

    @rating_score3.setter
    def rating_score3(self, rating_score3):
        """Sets the rating_score3 of this ItemReview.


        :param rating_score3: The rating_score3 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score3 = rating_score3

    @property
    def rating_score4(self):
        """Gets the rating_score4 of this ItemReview.  # noqa: E501


        :return: The rating_score4 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score4

    @rating_score4.setter
    def rating_score4(self, rating_score4):
        """Sets the rating_score4 of this ItemReview.


        :param rating_score4: The rating_score4 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score4 = rating_score4

    @property
    def rating_score5(self):
        """Gets the rating_score5 of this ItemReview.  # noqa: E501


        :return: The rating_score5 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score5

    @rating_score5.setter
    def rating_score5(self, rating_score5):
        """Sets the rating_score5 of this ItemReview.


        :param rating_score5: The rating_score5 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score5 = rating_score5

    @property
    def rating_score6(self):
        """Gets the rating_score6 of this ItemReview.  # noqa: E501


        :return: The rating_score6 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score6

    @rating_score6.setter
    def rating_score6(self, rating_score6):
        """Sets the rating_score6 of this ItemReview.


        :param rating_score6: The rating_score6 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score6 = rating_score6

    @property
    def rating_score7(self):
        """Gets the rating_score7 of this ItemReview.  # noqa: E501


        :return: The rating_score7 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score7

    @rating_score7.setter
    def rating_score7(self, rating_score7):
        """Sets the rating_score7 of this ItemReview.


        :param rating_score7: The rating_score7 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score7 = rating_score7

    @property
    def rating_score8(self):
        """Gets the rating_score8 of this ItemReview.  # noqa: E501


        :return: The rating_score8 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score8

    @rating_score8.setter
    def rating_score8(self, rating_score8):
        """Sets the rating_score8 of this ItemReview.


        :param rating_score8: The rating_score8 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score8 = rating_score8

    @property
    def rating_score9(self):
        """Gets the rating_score9 of this ItemReview.  # noqa: E501


        :return: The rating_score9 of this ItemReview.  # noqa: E501
        :rtype: float
        """
        return self._rating_score9

    @rating_score9.setter
    def rating_score9(self, rating_score9):
        """Sets the rating_score9 of this ItemReview.


        :param rating_score9: The rating_score9 of this ItemReview.  # noqa: E501
        :type: float
        """

        self._rating_score9 = rating_score9

    @property
    def recommend_store_to_friend(self):
        """Gets the recommend_store_to_friend of this ItemReview.  # noqa: E501


        :return: The recommend_store_to_friend of this ItemReview.  # noqa: E501
        :rtype: int
        """
        return self._recommend_store_to_friend

    @recommend_store_to_friend.setter
    def recommend_store_to_friend(self, recommend_store_to_friend):
        """Sets the recommend_store_to_friend of this ItemReview.


        :param recommend_store_to_friend: The recommend_store_to_friend of this ItemReview.  # noqa: E501
        :type: int
        """

        self._recommend_store_to_friend = recommend_store_to_friend

    @property
    def recommend_to_friend(self):
        """Gets the recommend_to_friend of this ItemReview.  # noqa: E501


        :return: The recommend_to_friend of this ItemReview.  # noqa: E501
        :rtype: bool
        """
        return self._recommend_to_friend

    @recommend_to_friend.setter
    def recommend_to_friend(self, recommend_to_friend):
        """Sets the recommend_to_friend of this ItemReview.


        :param recommend_to_friend: The recommend_to_friend of this ItemReview.  # noqa: E501
        :type: bool
        """

        self._recommend_to_friend = recommend_to_friend

    @property
    def review(self):
        """Gets the review of this ItemReview.  # noqa: E501


        :return: The review of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this ItemReview.


        :param review: The review of this ItemReview.  # noqa: E501
        :type: str
        """

        self._review = review

    @property
    def review_oid(self):
        """Gets the review_oid of this ItemReview.  # noqa: E501


        :return: The review_oid of this ItemReview.  # noqa: E501
        :rtype: int
        """
        return self._review_oid

    @review_oid.setter
    def review_oid(self, review_oid):
        """Sets the review_oid of this ItemReview.


        :param review_oid: The review_oid of this ItemReview.  # noqa: E501
        :type: int
        """

        self._review_oid = review_oid

    @property
    def reviewed_nickname(self):
        """Gets the reviewed_nickname of this ItemReview.  # noqa: E501


        :return: The reviewed_nickname of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._reviewed_nickname

    @reviewed_nickname.setter
    def reviewed_nickname(self, reviewed_nickname):
        """Sets the reviewed_nickname of this ItemReview.


        :param reviewed_nickname: The reviewed_nickname of this ItemReview.  # noqa: E501
        :type: str
        """

        self._reviewed_nickname = reviewed_nickname

    @property
    def reviewer_email(self):
        """Gets the reviewer_email of this ItemReview.  # noqa: E501


        :return: The reviewer_email of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._reviewer_email

    @reviewer_email.setter
    def reviewer_email(self, reviewer_email):
        """Sets the reviewer_email of this ItemReview.


        :param reviewer_email: The reviewer_email of this ItemReview.  # noqa: E501
        :type: str
        """

        self._reviewer_email = reviewer_email

    @property
    def reviewer_location(self):
        """Gets the reviewer_location of this ItemReview.  # noqa: E501


        :return: The reviewer_location of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._reviewer_location

    @reviewer_location.setter
    def reviewer_location(self, reviewer_location):
        """Sets the reviewer_location of this ItemReview.


        :param reviewer_location: The reviewer_location of this ItemReview.  # noqa: E501
        :type: str
        """

        self._reviewer_location = reviewer_location

    @property
    def status(self):
        """Gets the status of this ItemReview.  # noqa: E501


        :return: The status of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemReview.


        :param status: The status of this ItemReview.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def store_feedback(self):
        """Gets the store_feedback of this ItemReview.  # noqa: E501


        :return: The store_feedback of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._store_feedback

    @store_feedback.setter
    def store_feedback(self, store_feedback):
        """Sets the store_feedback of this ItemReview.


        :param store_feedback: The store_feedback of this ItemReview.  # noqa: E501
        :type: str
        """

        self._store_feedback = store_feedback

    @property
    def submitted_dts(self):
        """Gets the submitted_dts of this ItemReview.  # noqa: E501

        Date/time of review submission  # noqa: E501

        :return: The submitted_dts of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._submitted_dts

    @submitted_dts.setter
    def submitted_dts(self, submitted_dts):
        """Sets the submitted_dts of this ItemReview.

        Date/time of review submission  # noqa: E501

        :param submitted_dts: The submitted_dts of this ItemReview.  # noqa: E501
        :type: str
        """

        self._submitted_dts = submitted_dts

    @property
    def title(self):
        """Gets the title of this ItemReview.  # noqa: E501


        :return: The title of this ItemReview.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ItemReview.


        :param title: The title of this ItemReview.  # noqa: E501
        :type: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ItemReview, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ItemReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
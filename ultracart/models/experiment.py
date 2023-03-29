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


class Experiment(object):
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
        'container_id': 'str',
        'duration_days': 'int',
        'end_dts': 'str',
        'equal_weighting': 'bool',
        'experiment_type': 'str',
        'id': 'str',
        'name': 'str',
        'notes': 'str',
        'objective': 'str',
        'objective_parameter': 'str',
        'openai_current_iteration': 'int',
        'openai_element_type': 'str',
        'openai_model': 'str',
        'openai_total_iterations': 'int',
        'optimization_type': 'str',
        'p_value': 'float',
        'session_count': 'int',
        'start_dts': 'str',
        'status': 'str',
        'storefront_experiment_oid': 'int',
        'storefront_oid': 'int',
        'uri': 'str',
        'variations': 'list[ExperimentVariation]'
    }

    attribute_map = {
        'container_id': 'container_id',
        'duration_days': 'duration_days',
        'end_dts': 'end_dts',
        'equal_weighting': 'equal_weighting',
        'experiment_type': 'experiment_type',
        'id': 'id',
        'name': 'name',
        'notes': 'notes',
        'objective': 'objective',
        'objective_parameter': 'objective_parameter',
        'openai_current_iteration': 'openai_current_iteration',
        'openai_element_type': 'openai_element_type',
        'openai_model': 'openai_model',
        'openai_total_iterations': 'openai_total_iterations',
        'optimization_type': 'optimization_type',
        'p_value': 'p_value',
        'session_count': 'session_count',
        'start_dts': 'start_dts',
        'status': 'status',
        'storefront_experiment_oid': 'storefront_experiment_oid',
        'storefront_oid': 'storefront_oid',
        'uri': 'uri',
        'variations': 'variations'
    }

    def __init__(self, container_id=None, duration_days=None, end_dts=None, equal_weighting=None, experiment_type=None, id=None, name=None, notes=None, objective=None, objective_parameter=None, openai_current_iteration=None, openai_element_type=None, openai_model=None, openai_total_iterations=None, optimization_type=None, p_value=None, session_count=None, start_dts=None, status=None, storefront_experiment_oid=None, storefront_oid=None, uri=None, variations=None):  # noqa: E501
        """Experiment - a model defined in Swagger"""  # noqa: E501

        self._container_id = None
        self._duration_days = None
        self._end_dts = None
        self._equal_weighting = None
        self._experiment_type = None
        self._id = None
        self._name = None
        self._notes = None
        self._objective = None
        self._objective_parameter = None
        self._openai_current_iteration = None
        self._openai_element_type = None
        self._openai_model = None
        self._openai_total_iterations = None
        self._optimization_type = None
        self._p_value = None
        self._session_count = None
        self._start_dts = None
        self._status = None
        self._storefront_experiment_oid = None
        self._storefront_oid = None
        self._uri = None
        self._variations = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if duration_days is not None:
            self.duration_days = duration_days
        if end_dts is not None:
            self.end_dts = end_dts
        if equal_weighting is not None:
            self.equal_weighting = equal_weighting
        if experiment_type is not None:
            self.experiment_type = experiment_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if objective is not None:
            self.objective = objective
        if objective_parameter is not None:
            self.objective_parameter = objective_parameter
        if openai_current_iteration is not None:
            self.openai_current_iteration = openai_current_iteration
        if openai_element_type is not None:
            self.openai_element_type = openai_element_type
        if openai_model is not None:
            self.openai_model = openai_model
        if openai_total_iterations is not None:
            self.openai_total_iterations = openai_total_iterations
        if optimization_type is not None:
            self.optimization_type = optimization_type
        if p_value is not None:
            self.p_value = p_value
        if session_count is not None:
            self.session_count = session_count
        if start_dts is not None:
            self.start_dts = start_dts
        if status is not None:
            self.status = status
        if storefront_experiment_oid is not None:
            self.storefront_experiment_oid = storefront_experiment_oid
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if uri is not None:
            self.uri = uri
        if variations is not None:
            self.variations = variations

    @property
    def container_id(self):
        """Gets the container_id of this Experiment.  # noqa: E501

        Contained ID where the experiment element was located  # noqa: E501

        :return: The container_id of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this Experiment.

        Contained ID where the experiment element was located  # noqa: E501

        :param container_id: The container_id of this Experiment.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def duration_days(self):
        """Gets the duration_days of this Experiment.  # noqa: E501

        Duration in days  # noqa: E501

        :return: The duration_days of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._duration_days

    @duration_days.setter
    def duration_days(self, duration_days):
        """Sets the duration_days of this Experiment.

        Duration in days  # noqa: E501

        :param duration_days: The duration_days of this Experiment.  # noqa: E501
        :type: int
        """

        self._duration_days = duration_days

    @property
    def end_dts(self):
        """Gets the end_dts of this Experiment.  # noqa: E501

        End date/time  # noqa: E501

        :return: The end_dts of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._end_dts

    @end_dts.setter
    def end_dts(self, end_dts):
        """Sets the end_dts of this Experiment.

        End date/time  # noqa: E501

        :param end_dts: The end_dts of this Experiment.  # noqa: E501
        :type: str
        """

        self._end_dts = end_dts

    @property
    def equal_weighting(self):
        """Gets the equal_weighting of this Experiment.  # noqa: E501

        Whether or not traffic is equally weighted or shifts over time during the experiment  # noqa: E501

        :return: The equal_weighting of this Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._equal_weighting

    @equal_weighting.setter
    def equal_weighting(self, equal_weighting):
        """Sets the equal_weighting of this Experiment.

        Whether or not traffic is equally weighted or shifts over time during the experiment  # noqa: E501

        :param equal_weighting: The equal_weighting of this Experiment.  # noqa: E501
        :type: bool
        """

        self._equal_weighting = equal_weighting

    @property
    def experiment_type(self):
        """Gets the experiment_type of this Experiment.  # noqa: E501

        The type of experiment  # noqa: E501

        :return: The experiment_type of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._experiment_type

    @experiment_type.setter
    def experiment_type(self, experiment_type):
        """Sets the experiment_type of this Experiment.

        The type of experiment  # noqa: E501

        :param experiment_type: The experiment_type of this Experiment.  # noqa: E501
        :type: str
        """

        self._experiment_type = experiment_type

    @property
    def id(self):
        """Gets the id of this Experiment.  # noqa: E501

        Experiment id  # noqa: E501

        :return: The id of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Experiment.

        Experiment id  # noqa: E501

        :param id: The id of this Experiment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Experiment.  # noqa: E501

        Experiment name  # noqa: E501

        :return: The name of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Experiment.

        Experiment name  # noqa: E501

        :param name: The name of this Experiment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this Experiment.  # noqa: E501

        Notes about the experiment  # noqa: E501

        :return: The notes of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Experiment.

        Notes about the experiment  # noqa: E501

        :param notes: The notes of this Experiment.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def objective(self):
        """Gets the objective of this Experiment.  # noqa: E501

        Objective that is being optimized  # noqa: E501

        :return: The objective of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this Experiment.

        Objective that is being optimized  # noqa: E501

        :param objective: The objective of this Experiment.  # noqa: E501
        :type: str
        """

        self._objective = objective

    @property
    def objective_parameter(self):
        """Gets the objective_parameter of this Experiment.  # noqa: E501

        Objective parameter (such as event name) that is being optimized  # noqa: E501

        :return: The objective_parameter of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._objective_parameter

    @objective_parameter.setter
    def objective_parameter(self, objective_parameter):
        """Sets the objective_parameter of this Experiment.

        Objective parameter (such as event name) that is being optimized  # noqa: E501

        :param objective_parameter: The objective_parameter of this Experiment.  # noqa: E501
        :type: str
        """

        self._objective_parameter = objective_parameter

    @property
    def openai_current_iteration(self):
        """Gets the openai_current_iteration of this Experiment.  # noqa: E501

        The current iteration of the OpenAI related experiment  # noqa: E501

        :return: The openai_current_iteration of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._openai_current_iteration

    @openai_current_iteration.setter
    def openai_current_iteration(self, openai_current_iteration):
        """Sets the openai_current_iteration of this Experiment.

        The current iteration of the OpenAI related experiment  # noqa: E501

        :param openai_current_iteration: The openai_current_iteration of this Experiment.  # noqa: E501
        :type: int
        """

        self._openai_current_iteration = openai_current_iteration

    @property
    def openai_element_type(self):
        """Gets the openai_element_type of this Experiment.  # noqa: E501

        The type of OpenAI element being experimented on  # noqa: E501

        :return: The openai_element_type of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._openai_element_type

    @openai_element_type.setter
    def openai_element_type(self, openai_element_type):
        """Sets the openai_element_type of this Experiment.

        The type of OpenAI element being experimented on  # noqa: E501

        :param openai_element_type: The openai_element_type of this Experiment.  # noqa: E501
        :type: str
        """
        allowed_values = ["headline", "text", "textblock"]  # noqa: E501
        if openai_element_type not in allowed_values:
            raise ValueError(
                "Invalid value for `openai_element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(openai_element_type, allowed_values)
            )

        self._openai_element_type = openai_element_type

    @property
    def openai_model(self):
        """Gets the openai_model of this Experiment.  # noqa: E501

        The type of OpenAI model used  # noqa: E501

        :return: The openai_model of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._openai_model

    @openai_model.setter
    def openai_model(self, openai_model):
        """Sets the openai_model of this Experiment.

        The type of OpenAI model used  # noqa: E501

        :param openai_model: The openai_model of this Experiment.  # noqa: E501
        :type: str
        """

        self._openai_model = openai_model

    @property
    def openai_total_iterations(self):
        """Gets the openai_total_iterations of this Experiment.  # noqa: E501

        The total number of iterations to perform on the experiment  # noqa: E501

        :return: The openai_total_iterations of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._openai_total_iterations

    @openai_total_iterations.setter
    def openai_total_iterations(self, openai_total_iterations):
        """Sets the openai_total_iterations of this Experiment.

        The total number of iterations to perform on the experiment  # noqa: E501

        :param openai_total_iterations: The openai_total_iterations of this Experiment.  # noqa: E501
        :type: int
        """

        self._openai_total_iterations = openai_total_iterations

    @property
    def optimization_type(self):
        """Gets the optimization_type of this Experiment.  # noqa: E501

        Type of optimization  # noqa: E501

        :return: The optimization_type of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._optimization_type

    @optimization_type.setter
    def optimization_type(self, optimization_type):
        """Sets the optimization_type of this Experiment.

        Type of optimization  # noqa: E501

        :param optimization_type: The optimization_type of this Experiment.  # noqa: E501
        :type: str
        """

        self._optimization_type = optimization_type

    @property
    def p_value(self):
        """Gets the p_value of this Experiment.  # noqa: E501

        Statistics p-value for the experiment  # noqa: E501

        :return: The p_value of this Experiment.  # noqa: E501
        :rtype: float
        """
        return self._p_value

    @p_value.setter
    def p_value(self, p_value):
        """Sets the p_value of this Experiment.

        Statistics p-value for the experiment  # noqa: E501

        :param p_value: The p_value of this Experiment.  # noqa: E501
        :type: float
        """

        self._p_value = p_value

    @property
    def session_count(self):
        """Gets the session_count of this Experiment.  # noqa: E501

        Total number of sessions in the experiment  # noqa: E501

        :return: The session_count of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this Experiment.

        Total number of sessions in the experiment  # noqa: E501

        :param session_count: The session_count of this Experiment.  # noqa: E501
        :type: int
        """

        self._session_count = session_count

    @property
    def start_dts(self):
        """Gets the start_dts of this Experiment.  # noqa: E501

        Start date/time  # noqa: E501

        :return: The start_dts of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._start_dts

    @start_dts.setter
    def start_dts(self, start_dts):
        """Sets the start_dts of this Experiment.

        Start date/time  # noqa: E501

        :param start_dts: The start_dts of this Experiment.  # noqa: E501
        :type: str
        """

        self._start_dts = start_dts

    @property
    def status(self):
        """Gets the status of this Experiment.  # noqa: E501

        Status of the experiment  # noqa: E501

        :return: The status of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Experiment.

        Status of the experiment  # noqa: E501

        :param status: The status of this Experiment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "Ended", "Deleted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def storefront_experiment_oid(self):
        """Gets the storefront_experiment_oid of this Experiment.  # noqa: E501

        Storefront Experiment Oid  # noqa: E501

        :return: The storefront_experiment_oid of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._storefront_experiment_oid

    @storefront_experiment_oid.setter
    def storefront_experiment_oid(self, storefront_experiment_oid):
        """Sets the storefront_experiment_oid of this Experiment.

        Storefront Experiment Oid  # noqa: E501

        :param storefront_experiment_oid: The storefront_experiment_oid of this Experiment.  # noqa: E501
        :type: int
        """

        self._storefront_experiment_oid = storefront_experiment_oid

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this Experiment.  # noqa: E501

        Storefront oid  # noqa: E501

        :return: The storefront_oid of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this Experiment.

        Storefront oid  # noqa: E501

        :param storefront_oid: The storefront_oid of this Experiment.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def uri(self):
        """Gets the uri of this Experiment.  # noqa: E501

        URI the experiment was started on  # noqa: E501

        :return: The uri of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Experiment.

        URI the experiment was started on  # noqa: E501

        :param uri: The uri of this Experiment.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def variations(self):
        """Gets the variations of this Experiment.  # noqa: E501

        Variations being tested in the experiment  # noqa: E501

        :return: The variations of this Experiment.  # noqa: E501
        :rtype: list[ExperimentVariation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this Experiment.

        Variations being tested in the experiment  # noqa: E501

        :param variations: The variations of this Experiment.  # noqa: E501
        :type: list[ExperimentVariation]
        """

        self._variations = variations

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
        if issubclass(Experiment, dict):
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
        if not isinstance(other, Experiment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

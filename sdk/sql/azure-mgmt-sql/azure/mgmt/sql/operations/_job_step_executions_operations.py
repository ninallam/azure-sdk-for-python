# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_job_execution_request(
    resource_group_name: str,
    server_name: str,
    job_agent_name: str,
    job_name: str,
    job_execution_id: str,
    subscription_id: str,
    *,
    create_time_min: Optional[datetime.datetime] = None,
    create_time_max: Optional[datetime.datetime] = None,
    end_time_min: Optional[datetime.datetime] = None,
    end_time_max: Optional[datetime.datetime] = None,
    is_active: Optional[bool] = None,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "jobAgentName": _SERIALIZER.url("job_agent_name", job_agent_name, 'str'),
        "jobName": _SERIALIZER.url("job_name", job_name, 'str'),
        "jobExecutionId": _SERIALIZER.url("job_execution_id", job_execution_id, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if create_time_min is not None:
        _params['createTimeMin'] = _SERIALIZER.query("create_time_min", create_time_min, 'iso-8601')
    if create_time_max is not None:
        _params['createTimeMax'] = _SERIALIZER.query("create_time_max", create_time_max, 'iso-8601')
    if end_time_min is not None:
        _params['endTimeMin'] = _SERIALIZER.query("end_time_min", end_time_min, 'iso-8601')
    if end_time_max is not None:
        _params['endTimeMax'] = _SERIALIZER.query("end_time_max", end_time_max, 'iso-8601')
    if is_active is not None:
        _params['isActive'] = _SERIALIZER.query("is_active", is_active, 'bool')
    if skip is not None:
        _params['$skip'] = _SERIALIZER.query("skip", skip, 'int')
    if top is not None:
        _params['$top'] = _SERIALIZER.query("top", top, 'int')
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    server_name: str,
    job_agent_name: str,
    job_name: str,
    job_execution_id: str,
    step_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "jobAgentName": _SERIALIZER.url("job_agent_name", job_agent_name, 'str'),
        "jobName": _SERIALIZER.url("job_name", job_name, 'str'),
        "jobExecutionId": _SERIALIZER.url("job_execution_id", job_execution_id, 'str'),
        "stepName": _SERIALIZER.url("step_name", step_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class JobStepExecutionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.SqlManagementClient`'s
        :attr:`job_step_executions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_by_job_execution(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable[_models.JobExecutionListResult]:
        """Lists the step executions of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param job_execution_id: The id of the job execution.
        :type job_execution_id: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included. Default value is None.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included. Default value is None.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included. Default value is None.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included. Default value is None.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
         Default value is None.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip. Default value is None.
        :type skip: int
        :param top: The number of elements to return from the collection. Default value is None.
        :type top: int
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecutionListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.JobExecutionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecutionListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_job_execution_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    job_execution_id=job_execution_id,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=self.list_by_job_execution.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_job_execution_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    job_execution_id=job_execution_id,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("JobExecutionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_job_execution.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        step_name: str,
        **kwargs: Any
    ) -> _models.JobExecution:
        """Gets a step execution of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param job_execution_id: The unique id of the job execution.
        :type job_execution_id: str
        :param step_name: The name of the step.
        :type step_name: str
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobExecution, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.JobExecution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecution]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            job_execution_id=job_execution_id,
            step_name=step_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JobExecution', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName}"}  # type: ignore


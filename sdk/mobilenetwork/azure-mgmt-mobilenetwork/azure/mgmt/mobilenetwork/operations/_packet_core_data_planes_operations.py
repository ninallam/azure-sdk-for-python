# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union, cast

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_delete_request_initial(
    resource_group_name: str,
    packet_core_control_plane_name: str,
    packet_core_data_plane_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "packetCoreControlPlaneName": _SERIALIZER.url("packet_core_control_plane_name", packet_core_control_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "packetCoreDataPlaneName": _SERIALIZER.url("packet_core_data_plane_name", packet_core_data_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    packet_core_control_plane_name: str,
    packet_core_data_plane_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "packetCoreControlPlaneName": _SERIALIZER.url("packet_core_control_plane_name", packet_core_control_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "packetCoreDataPlaneName": _SERIALIZER.url("packet_core_data_plane_name", packet_core_data_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
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


def build_create_or_update_request_initial(
    resource_group_name: str,
    packet_core_control_plane_name: str,
    packet_core_data_plane_name: str,
    subscription_id: str,
    *,
    json: Optional[_models.PacketCoreDataPlane] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "packetCoreControlPlaneName": _SERIALIZER.url("packet_core_control_plane_name", packet_core_control_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "packetCoreDataPlaneName": _SERIALIZER.url("packet_core_data_plane_name", packet_core_data_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )


def build_update_tags_request(
    resource_group_name: str,
    packet_core_control_plane_name: str,
    packet_core_data_plane_name: str,
    subscription_id: str,
    *,
    json: Optional[_models.TagsObject] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "packetCoreControlPlaneName": _SERIALIZER.url("packet_core_control_plane_name", packet_core_control_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "packetCoreDataPlaneName": _SERIALIZER.url("packet_core_data_plane_name", packet_core_data_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )


def build_list_by_packet_core_control_plane_request(
    resource_group_name: str,
    packet_core_control_plane_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "packetCoreControlPlaneName": _SERIALIZER.url("packet_core_control_plane_name", packet_core_control_plane_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
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

class PacketCoreDataPlanesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.mobilenetwork.MobileNetworkManagementClient`'s
        :attr:`packet_core_data_planes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request_initial(
            resource_group_name=resource_group_name,
            packet_core_control_plane_name=packet_core_control_plane_name,
            packet_core_data_plane_name=packet_core_data_plane_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
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

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore


    @distributed_trace
    def begin_delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        **kwargs: Any
    ) -> LROPoller[None]:
        """Deletes the specified packet core data plane.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param packet_core_control_plane_name: The name of the packet core control plane.
        :type packet_core_control_plane_name: str
        :param packet_core_data_plane_name: The name of the packet core data plane.
        :type packet_core_data_plane_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                packet_core_control_plane_name=packet_core_control_plane_name,
                packet_core_data_plane_name=packet_core_data_plane_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True:
            polling_method = cast(PollingMethod, ARMPolling(
                lro_delay,
                lro_options={'final-state-via': 'location'},
                
                **kwargs
        ))  # type: PollingMethod
        elif polling is False: polling_method = cast(PollingMethod, NoPolling())
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        **kwargs: Any
    ) -> _models.PacketCoreDataPlane:
        """Gets information about the specified packet core data plane.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param packet_core_control_plane_name: The name of the packet core control plane.
        :type packet_core_control_plane_name: str
        :param packet_core_data_plane_name: The name of the packet core data plane.
        :type packet_core_data_plane_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PacketCoreDataPlane, or the result of cls(response)
        :rtype: ~azure.mgmt.mobilenetwork.models.PacketCoreDataPlane
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PacketCoreDataPlane]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            packet_core_control_plane_name=packet_core_control_plane_name,
            packet_core_data_plane_name=packet_core_data_plane_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PacketCoreDataPlane', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore


    def _create_or_update_initial(
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        parameters: _models.PacketCoreDataPlane,
        **kwargs: Any
    ) -> _models.PacketCoreDataPlane:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PacketCoreDataPlane]

        _json = self._serialize.body(parameters, 'PacketCoreDataPlane')

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            packet_core_control_plane_name=packet_core_control_plane_name,
            packet_core_data_plane_name=packet_core_data_plane_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('PacketCoreDataPlane', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PacketCoreDataPlane', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore


    @distributed_trace
    def begin_create_or_update(
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        parameters: _models.PacketCoreDataPlane,
        **kwargs: Any
    ) -> LROPoller[_models.PacketCoreDataPlane]:
        """Creates or updates a packet core data plane.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param packet_core_control_plane_name: The name of the packet core control plane.
        :type packet_core_control_plane_name: str
        :param packet_core_data_plane_name: The name of the packet core data plane.
        :type packet_core_data_plane_name: str
        :param parameters: Parameters supplied to the create or update packet core data plane
         operation.
        :type parameters: ~azure.mgmt.mobilenetwork.models.PacketCoreDataPlane
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either PacketCoreDataPlane or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.mobilenetwork.models.PacketCoreDataPlane]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PacketCoreDataPlane]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                packet_core_control_plane_name=packet_core_control_plane_name,
                packet_core_data_plane_name=packet_core_data_plane_name,
                parameters=parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('PacketCoreDataPlane', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(PollingMethod, ARMPolling(
                lro_delay,
                lro_options={'final-state-via': 'azure-async-operation'},
                
                **kwargs
        ))  # type: PollingMethod
        elif polling is False: polling_method = cast(PollingMethod, NoPolling())
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore

    @distributed_trace
    def update_tags(
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        packet_core_data_plane_name: str,
        parameters: _models.TagsObject,
        **kwargs: Any
    ) -> _models.PacketCoreDataPlane:
        """Updates packet core data planes tags.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param packet_core_control_plane_name: The name of the packet core control plane.
        :type packet_core_control_plane_name: str
        :param packet_core_data_plane_name: The name of the packet core data plane.
        :type packet_core_data_plane_name: str
        :param parameters: Parameters supplied to update packet core data plane tags.
        :type parameters: ~azure.mgmt.mobilenetwork.models.TagsObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PacketCoreDataPlane, or the result of cls(response)
        :rtype: ~azure.mgmt.mobilenetwork.models.PacketCoreDataPlane
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PacketCoreDataPlane]

        _json = self._serialize.body(parameters, 'TagsObject')

        request = build_update_tags_request(
            resource_group_name=resource_group_name,
            packet_core_control_plane_name=packet_core_control_plane_name,
            packet_core_data_plane_name=packet_core_data_plane_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update_tags.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PacketCoreDataPlane', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_tags.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}"}  # type: ignore


    @distributed_trace
    def list_by_packet_core_control_plane(
        self,
        resource_group_name: str,
        packet_core_control_plane_name: str,
        **kwargs: Any
    ) -> Iterable[_models.PacketCoreDataPlaneListResult]:
        """Lists all the packet core data planes associated with a packet core control plane.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param packet_core_control_plane_name: The name of the packet core control plane.
        :type packet_core_control_plane_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PacketCoreDataPlaneListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.mobilenetwork.models.PacketCoreDataPlaneListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PacketCoreDataPlaneListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_packet_core_control_plane_request(
                    resource_group_name=resource_group_name,
                    packet_core_control_plane_name=packet_core_control_plane_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_packet_core_control_plane.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_packet_core_control_plane_request(
                    resource_group_name=resource_group_name,
                    packet_core_control_plane_name=packet_core_control_plane_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PacketCoreDataPlaneListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_packet_core_control_plane.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes"}  # type: ignore

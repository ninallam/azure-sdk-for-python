# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._feature_client_enums import *


class AuthorizationProfile(msrest.serialization.Model):
    """Authorization Profile.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar requested_time: The requested time.
    :vartype requested_time: ~datetime.datetime
    :ivar requester: The requester.
    :vartype requester: str
    :ivar requester_object_id: The requester object id.
    :vartype requester_object_id: str
    :ivar approved_time: The approved time.
    :vartype approved_time: ~datetime.datetime
    :ivar approver: The approver.
    :vartype approver: str
    """

    _validation = {
        'requested_time': {'readonly': True},
        'requester': {'readonly': True},
        'requester_object_id': {'readonly': True},
        'approved_time': {'readonly': True},
        'approver': {'readonly': True},
    }

    _attribute_map = {
        'requested_time': {'key': 'requestedTime', 'type': 'iso-8601'},
        'requester': {'key': 'requester', 'type': 'str'},
        'requester_object_id': {'key': 'requesterObjectId', 'type': 'str'},
        'approved_time': {'key': 'approvedTime', 'type': 'iso-8601'},
        'approver': {'key': 'approver', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AuthorizationProfile, self).__init__(**kwargs)
        self.requested_time = None
        self.requester = None
        self.requester_object_id = None
        self.approved_time = None
        self.approver = None


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :param details: Internal error details.
    :type details: list[~azure.mgmt.resource.features.v2021_07_01.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        *,
        details: Optional[List["ErrorDefinition"]] = None,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = details


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates that the service is not able to process the incoming request.

    :param error: The error details.
    :type error: ~azure.mgmt.resource.features.v2021_07_01.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinition"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class FeatureOperationsListResult(msrest.serialization.Model):
    """List of previewed features.

    :param value: The array of features.
    :type value: list[~azure.mgmt.resource.features.v2021_07_01.models.FeatureResult]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[FeatureResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["FeatureResult"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(FeatureOperationsListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class FeatureProperties(msrest.serialization.Model):
    """Information about feature.

    :param state: The registration state of the feature for the subscription.
    :type state: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        state: Optional[str] = None,
        **kwargs
    ):
        super(FeatureProperties, self).__init__(**kwargs)
        self.state = state


class FeatureResult(msrest.serialization.Model):
    """Previewed feature information.

    :param name: The name of the feature.
    :type name: str
    :param properties: Properties of the previewed feature.
    :type properties: ~azure.mgmt.resource.features.v2021_07_01.models.FeatureProperties
    :param id: The resource ID of the feature.
    :type id: str
    :param type: The resource type of the feature.
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'FeatureProperties'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        properties: Optional["FeatureProperties"] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        super(FeatureResult, self).__init__(**kwargs)
        self.name = name
        self.properties = properties
        self.id = id
        self.type = type


class Operation(msrest.serialization.Model):
    """Microsoft.Features operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.resource.features.v2021_07_01.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Features.
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile, endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Microsoft.Features operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Microsoft.Features operations.
    :type value: list[~azure.mgmt.resource.features.v2021_07_01.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ProxyResource(msrest.serialization.Model):
    """An Azure proxy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class SubscriptionFeatureRegistration(ProxyResource):
    """Subscription feature registration details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param properties:
    :type properties:
     ~azure.mgmt.resource.features.v2021_07_01.models.SubscriptionFeatureRegistrationProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SubscriptionFeatureRegistrationProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["SubscriptionFeatureRegistrationProperties"] = None,
        **kwargs
    ):
        super(SubscriptionFeatureRegistration, self).__init__(**kwargs)
        self.properties = properties


class SubscriptionFeatureRegistrationList(msrest.serialization.Model):
    """The list of subscription feature registrations.

    :param next_link: The link used to get the next page of subscription feature registrations
     list.
    :type next_link: str
    :param value: The list of subscription feature registrations.
    :type value:
     list[~azure.mgmt.resource.features.v2021_07_01.models.SubscriptionFeatureRegistration]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[SubscriptionFeatureRegistration]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["SubscriptionFeatureRegistration"]] = None,
        **kwargs
    ):
        super(SubscriptionFeatureRegistrationList, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class SubscriptionFeatureRegistrationProperties(msrest.serialization.Model):
    """SubscriptionFeatureRegistrationProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar tenant_id: The tenantId.
    :vartype tenant_id: str
    :ivar subscription_id: The subscriptionId.
    :vartype subscription_id: str
    :ivar feature_name: The featureName.
    :vartype feature_name: str
    :ivar display_name: The featureDisplayName.
    :vartype display_name: str
    :ivar provider_namespace: The providerNamespace.
    :vartype provider_namespace: str
    :param state: The state. Possible values include: "NotSpecified", "NotRegistered", "Pending",
     "Registering", "Registered", "Unregistering", "Unregistered".
    :type state: str or
     ~azure.mgmt.resource.features.v2021_07_01.models.SubscriptionFeatureRegistrationState
    :param authorization_profile: Authorization Profile.
    :type authorization_profile:
     ~azure.mgmt.resource.features.v2021_07_01.models.AuthorizationProfile
    :param metadata: Key-value pairs for meta data.
    :type metadata: dict[str, str]
    :ivar release_date: The feature release date.
    :vartype release_date: ~datetime.datetime
    :ivar registration_date: The feature registration date.
    :vartype registration_date: ~datetime.datetime
    :ivar documentation_link: The feature documentation link.
    :vartype documentation_link: str
    :ivar approval_type: The feature approval type. Possible values include: "NotSpecified",
     "ApprovalRequired", "AutoApproval".
    :vartype approval_type: str or
     ~azure.mgmt.resource.features.v2021_07_01.models.SubscriptionFeatureRegistrationApprovalType
    :param should_feature_display_in_portal: Indicates whether feature should be displayed in
     Portal.
    :type should_feature_display_in_portal: bool
    :param description: The feature description.
    :type description: str
    """

    _validation = {
        'tenant_id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'feature_name': {'readonly': True},
        'display_name': {'readonly': True},
        'provider_namespace': {'readonly': True},
        'release_date': {'readonly': True},
        'registration_date': {'readonly': True},
        'documentation_link': {'readonly': True, 'max_length': 1000, 'min_length': 0},
        'approval_type': {'readonly': True},
        'description': {'max_length': 1000, 'min_length': 0},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'feature_name': {'key': 'featureName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'provider_namespace': {'key': 'providerNamespace', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'authorization_profile': {'key': 'authorizationProfile', 'type': 'AuthorizationProfile'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
        'release_date': {'key': 'releaseDate', 'type': 'iso-8601'},
        'registration_date': {'key': 'registrationDate', 'type': 'iso-8601'},
        'documentation_link': {'key': 'documentationLink', 'type': 'str'},
        'approval_type': {'key': 'approvalType', 'type': 'str'},
        'should_feature_display_in_portal': {'key': 'shouldFeatureDisplayInPortal', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        state: Optional[Union[str, "SubscriptionFeatureRegistrationState"]] = None,
        authorization_profile: Optional["AuthorizationProfile"] = None,
        metadata: Optional[Dict[str, str]] = None,
        should_feature_display_in_portal: Optional[bool] = False,
        description: Optional[str] = None,
        **kwargs
    ):
        super(SubscriptionFeatureRegistrationProperties, self).__init__(**kwargs)
        self.tenant_id = None
        self.subscription_id = None
        self.feature_name = None
        self.display_name = None
        self.provider_namespace = None
        self.state = state
        self.authorization_profile = authorization_profile
        self.metadata = metadata
        self.release_date = None
        self.registration_date = None
        self.documentation_link = None
        self.approval_type = None
        self.should_feature_display_in_portal = should_feature_display_in_portal
        self.description = description

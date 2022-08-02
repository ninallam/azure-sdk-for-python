# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, TYPE_CHECKING

from azure.core.exceptions import HttpResponseError
import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    import __init__ as _models


class ActionGroupList(msrest.serialization.Model):
    """A list of action groups.

    :ivar value: The list of action groups.
    :vartype value: list[~$(python-base-namespace).v2018_09_01.models.ActionGroupResource]
    :ivar next_link: Provides the link to retrieve the next set of elements.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActionGroupResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.ActionGroupResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: The list of action groups.
        :paramtype value: list[~$(python-base-namespace).v2018_09_01.models.ActionGroupResource]
        :keyword next_link: Provides the link to retrieve the next set of elements.
        :paramtype next_link: str
        """
        super(ActionGroupList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ActionGroupPatchBody(msrest.serialization.Model):
    """An action group object for the body of patch operations.

    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its actions will be activated.
    :vartype enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[bool] = True,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword enabled: Indicates whether this action group is enabled. If an action group is not
         enabled, then none of its actions will be activated.
        :paramtype enabled: bool
        """
        super(ActionGroupPatchBody, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Required. Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword location: Required. Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Required. Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar group_short_name: The short name of the action group. This will be used in SMS messages.
    :vartype group_short_name: str
    :ivar enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its receivers will receive communications.
    :vartype enabled: bool
    :ivar email_receivers: The list of email receivers that are part of this action group.
    :vartype email_receivers: list[~$(python-base-namespace).v2018_09_01.models.EmailReceiver]
    :ivar sms_receivers: The list of SMS receivers that are part of this action group.
    :vartype sms_receivers: list[~$(python-base-namespace).v2018_09_01.models.SmsReceiver]
    :ivar webhook_receivers: The list of webhook receivers that are part of this action group.
    :vartype webhook_receivers: list[~$(python-base-namespace).v2018_09_01.models.WebhookReceiver]
    :ivar itsm_receivers: The list of ITSM receivers that are part of this action group.
    :vartype itsm_receivers: list[~$(python-base-namespace).v2018_09_01.models.ItsmReceiver]
    :ivar azure_app_push_receivers: The list of AzureAppPush receivers that are part of this action
     group.
    :vartype azure_app_push_receivers:
     list[~$(python-base-namespace).v2018_09_01.models.AzureAppPushReceiver]
    :ivar automation_runbook_receivers: The list of AutomationRunbook receivers that are part of
     this action group.
    :vartype automation_runbook_receivers:
     list[~$(python-base-namespace).v2018_09_01.models.AutomationRunbookReceiver]
    :ivar voice_receivers: The list of voice receivers that are part of this action group.
    :vartype voice_receivers: list[~$(python-base-namespace).v2018_09_01.models.VoiceReceiver]
    :ivar logic_app_receivers: The list of logic app receivers that are part of this action group.
    :vartype logic_app_receivers:
     list[~$(python-base-namespace).v2018_09_01.models.LogicAppReceiver]
    :ivar azure_function_receivers: The list of azure function receivers that are part of this
     action group.
    :vartype azure_function_receivers:
     list[~$(python-base-namespace).v2018_09_01.models.AzureFunctionReceiver]
    :ivar arm_role_receivers: The list of ARM role receivers that are part of this action group.
     Roles are Azure RBAC roles and only built-in roles are supported.
    :vartype arm_role_receivers: list[~$(python-base-namespace).v2018_09_01.models.ArmRoleReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'max_length': 12, 'min_length': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
        'itsm_receivers': {'key': 'properties.itsmReceivers', 'type': '[ItsmReceiver]'},
        'azure_app_push_receivers': {'key': 'properties.azureAppPushReceivers', 'type': '[AzureAppPushReceiver]'},
        'automation_runbook_receivers': {'key': 'properties.automationRunbookReceivers', 'type': '[AutomationRunbookReceiver]'},
        'voice_receivers': {'key': 'properties.voiceReceivers', 'type': '[VoiceReceiver]'},
        'logic_app_receivers': {'key': 'properties.logicAppReceivers', 'type': '[LogicAppReceiver]'},
        'azure_function_receivers': {'key': 'properties.azureFunctionReceivers', 'type': '[AzureFunctionReceiver]'},
        'arm_role_receivers': {'key': 'properties.armRoleReceivers', 'type': '[ArmRoleReceiver]'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        group_short_name: Optional[str] = None,
        enabled: Optional[bool] = True,
        email_receivers: Optional[List["_models.EmailReceiver"]] = None,
        sms_receivers: Optional[List["_models.SmsReceiver"]] = None,
        webhook_receivers: Optional[List["_models.WebhookReceiver"]] = None,
        itsm_receivers: Optional[List["_models.ItsmReceiver"]] = None,
        azure_app_push_receivers: Optional[List["_models.AzureAppPushReceiver"]] = None,
        automation_runbook_receivers: Optional[List["_models.AutomationRunbookReceiver"]] = None,
        voice_receivers: Optional[List["_models.VoiceReceiver"]] = None,
        logic_app_receivers: Optional[List["_models.LogicAppReceiver"]] = None,
        azure_function_receivers: Optional[List["_models.AzureFunctionReceiver"]] = None,
        arm_role_receivers: Optional[List["_models.ArmRoleReceiver"]] = None,
        **kwargs
    ):
        """
        :keyword location: Required. Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword group_short_name: The short name of the action group. This will be used in SMS
         messages.
        :paramtype group_short_name: str
        :keyword enabled: Indicates whether this action group is enabled. If an action group is not
         enabled, then none of its receivers will receive communications.
        :paramtype enabled: bool
        :keyword email_receivers: The list of email receivers that are part of this action group.
        :paramtype email_receivers: list[~$(python-base-namespace).v2018_09_01.models.EmailReceiver]
        :keyword sms_receivers: The list of SMS receivers that are part of this action group.
        :paramtype sms_receivers: list[~$(python-base-namespace).v2018_09_01.models.SmsReceiver]
        :keyword webhook_receivers: The list of webhook receivers that are part of this action group.
        :paramtype webhook_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.WebhookReceiver]
        :keyword itsm_receivers: The list of ITSM receivers that are part of this action group.
        :paramtype itsm_receivers: list[~$(python-base-namespace).v2018_09_01.models.ItsmReceiver]
        :keyword azure_app_push_receivers: The list of AzureAppPush receivers that are part of this
         action group.
        :paramtype azure_app_push_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.AzureAppPushReceiver]
        :keyword automation_runbook_receivers: The list of AutomationRunbook receivers that are part of
         this action group.
        :paramtype automation_runbook_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.AutomationRunbookReceiver]
        :keyword voice_receivers: The list of voice receivers that are part of this action group.
        :paramtype voice_receivers: list[~$(python-base-namespace).v2018_09_01.models.VoiceReceiver]
        :keyword logic_app_receivers: The list of logic app receivers that are part of this action
         group.
        :paramtype logic_app_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.LogicAppReceiver]
        :keyword azure_function_receivers: The list of azure function receivers that are part of this
         action group.
        :paramtype azure_function_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.AzureFunctionReceiver]
        :keyword arm_role_receivers: The list of ARM role receivers that are part of this action group.
         Roles are Azure RBAC roles and only built-in roles are supported.
        :paramtype arm_role_receivers:
         list[~$(python-base-namespace).v2018_09_01.models.ArmRoleReceiver]
        """
        super(ActionGroupResource, self).__init__(location=location, tags=tags, **kwargs)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
        self.itsm_receivers = itsm_receivers
        self.azure_app_push_receivers = azure_app_push_receivers
        self.automation_runbook_receivers = automation_runbook_receivers
        self.voice_receivers = voice_receivers
        self.logic_app_receivers = logic_app_receivers
        self.azure_function_receivers = azure_function_receivers
        self.arm_role_receivers = arm_role_receivers


class ArmRoleReceiver(msrest.serialization.Model):
    """An arm role receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the arm role receiver. Names must be unique across all
     receivers within an action group.
    :vartype name: str
    :ivar role_id: Required. The arm role id.
    :vartype role_id: str
    """

    _validation = {
        'name': {'required': True},
        'role_id': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        role_id: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the arm role receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword role_id: Required. The arm role id.
        :paramtype role_id: str
        """
        super(ArmRoleReceiver, self).__init__(**kwargs)
        self.name = name
        self.role_id = role_id


class AutomationRunbookReceiver(msrest.serialization.Model):
    """The Azure Automation Runbook notification receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar automation_account_id: Required. The Azure automation account Id which holds this runbook
     and authenticate to Azure resource.
    :vartype automation_account_id: str
    :ivar runbook_name: Required. The name for this runbook.
    :vartype runbook_name: str
    :ivar webhook_resource_id: Required. The resource id for webhook linked to this runbook.
    :vartype webhook_resource_id: str
    :ivar is_global_runbook: Required. Indicates whether this instance is global runbook.
    :vartype is_global_runbook: bool
    :ivar name: Indicates name of the webhook.
    :vartype name: str
    :ivar service_uri: The URI where webhooks should be sent.
    :vartype service_uri: str
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        automation_account_id: str,
        runbook_name: str,
        webhook_resource_id: str,
        is_global_runbook: bool,
        name: Optional[str] = None,
        service_uri: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword automation_account_id: Required. The Azure automation account Id which holds this
         runbook and authenticate to Azure resource.
        :paramtype automation_account_id: str
        :keyword runbook_name: Required. The name for this runbook.
        :paramtype runbook_name: str
        :keyword webhook_resource_id: Required. The resource id for webhook linked to this runbook.
        :paramtype webhook_resource_id: str
        :keyword is_global_runbook: Required. Indicates whether this instance is global runbook.
        :paramtype is_global_runbook: bool
        :keyword name: Indicates name of the webhook.
        :paramtype name: str
        :keyword service_uri: The URI where webhooks should be sent.
        :paramtype service_uri: str
        """
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = automation_account_id
        self.runbook_name = runbook_name
        self.webhook_resource_id = webhook_resource_id
        self.is_global_runbook = is_global_runbook
        self.name = name
        self.service_uri = service_uri


class AzureAppPushReceiver(msrest.serialization.Model):
    """The Azure mobile App push notification receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the Azure mobile app push receiver. Names must be unique
     across all receivers within an action group.
    :vartype name: str
    :ivar email_address: Required. The email address registered for the Azure mobile app.
    :vartype email_address: str
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the Azure mobile app push receiver. Names must be unique
         across all receivers within an action group.
        :paramtype name: str
        :keyword email_address: Required. The email address registered for the Azure mobile app.
        :paramtype email_address: str
        """
        super(AzureAppPushReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address


class AzureFunctionReceiver(msrest.serialization.Model):
    """An azure function receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the azure function receiver. Names must be unique across all
     receivers within an action group.
    :vartype name: str
    :ivar function_app_resource_id: Required. The azure resource id of the function app.
    :vartype function_app_resource_id: str
    :ivar function_name: Required. The function name in the function app.
    :vartype function_name: str
    :ivar http_trigger_url: Required. The http trigger url where http request sent to.
    :vartype http_trigger_url: str
    """

    _validation = {
        'name': {'required': True},
        'function_app_resource_id': {'required': True},
        'function_name': {'required': True},
        'http_trigger_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'function_app_resource_id': {'key': 'functionAppResourceId', 'type': 'str'},
        'function_name': {'key': 'functionName', 'type': 'str'},
        'http_trigger_url': {'key': 'httpTriggerUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        function_app_resource_id: str,
        function_name: str,
        http_trigger_url: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the azure function receiver. Names must be unique across
         all receivers within an action group.
        :paramtype name: str
        :keyword function_app_resource_id: Required. The azure resource id of the function app.
        :paramtype function_app_resource_id: str
        :keyword function_name: Required. The function name in the function app.
        :paramtype function_name: str
        :keyword http_trigger_url: Required. The http trigger url where http request sent to.
        :paramtype http_trigger_url: str
        """
        super(AzureFunctionReceiver, self).__init__(**kwargs)
        self.name = name
        self.function_app_resource_id = function_app_resource_id
        self.function_name = function_name
        self.http_trigger_url = http_trigger_url


class EmailReceiver(msrest.serialization.Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the email receiver. Names must be unique across all receivers
     within an action group.
    :vartype name: str
    :ivar email_address: Required. The email address of this receiver.
    :vartype email_address: str
    :ivar status: The receiver status of the e-mail. Known values are: "NotSpecified", "Enabled",
     "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the email receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword email_address: Required. The email address of this receiver.
        :paramtype email_address: str
        """
        super(EmailReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.status = None


class EnableRequest(msrest.serialization.Model):
    """Describes a receiver that should be resubscribed.

    All required parameters must be populated in order to send to Azure.

    :ivar receiver_name: Required. The name of the receiver to resubscribe.
    :vartype receiver_name: str
    """

    _validation = {
        'receiver_name': {'required': True},
    }

    _attribute_map = {
        'receiver_name': {'key': 'receiverName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        receiver_name: str,
        **kwargs
    ):
        """
        :keyword receiver_name: Required. The name of the receiver to resubscribe.
        :paramtype receiver_name: str
        """
        super(EnableRequest, self).__init__(**kwargs)
        self.receiver_name = receiver_name


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ItsmReceiver(msrest.serialization.Model):
    """An Itsm receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the Itsm receiver. Names must be unique across all receivers
     within an action group.
    :vartype name: str
    :ivar workspace_id: Required. OMS LA instance identifier.
    :vartype workspace_id: str
    :ivar connection_id: Required. Unique identification of ITSM connection among multiple defined
     in above workspace.
    :vartype connection_id: str
    :ivar ticket_configuration: Required. JSON blob for the configurations of the ITSM action.
     CreateMultipleWorkItems option will be part of this blob as well.
    :vartype ticket_configuration: str
    :ivar region: Required. Region in which workspace resides. Supported
     values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'.
    :vartype region: str
    """

    _validation = {
        'name': {'required': True},
        'workspace_id': {'required': True},
        'connection_id': {'required': True},
        'ticket_configuration': {'required': True},
        'region': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'ticket_configuration': {'key': 'ticketConfiguration', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        workspace_id: str,
        connection_id: str,
        ticket_configuration: str,
        region: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the Itsm receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword workspace_id: Required. OMS LA instance identifier.
        :paramtype workspace_id: str
        :keyword connection_id: Required. Unique identification of ITSM connection among multiple
         defined in above workspace.
        :paramtype connection_id: str
        :keyword ticket_configuration: Required. JSON blob for the configurations of the ITSM action.
         CreateMultipleWorkItems option will be part of this blob as well.
        :paramtype ticket_configuration: str
        :keyword region: Required. Region in which workspace resides. Supported
         values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'.
        :paramtype region: str
        """
        super(ItsmReceiver, self).__init__(**kwargs)
        self.name = name
        self.workspace_id = workspace_id
        self.connection_id = connection_id
        self.ticket_configuration = ticket_configuration
        self.region = region


class LogicAppReceiver(msrest.serialization.Model):
    """A logic app receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the logic app receiver. Names must be unique across all
     receivers within an action group.
    :vartype name: str
    :ivar resource_id: Required. The azure resource id of the logic app receiver.
    :vartype resource_id: str
    :ivar callback_url: Required. The callback url where http request sent to.
    :vartype callback_url: str
    """

    _validation = {
        'name': {'required': True},
        'resource_id': {'required': True},
        'callback_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'callback_url': {'key': 'callbackUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        resource_id: str,
        callback_url: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the logic app receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword resource_id: Required. The azure resource id of the logic app receiver.
        :paramtype resource_id: str
        :keyword callback_url: Required. The callback url where http request sent to.
        :paramtype callback_url: str
        """
        super(LogicAppReceiver, self).__init__(**kwargs)
        self.name = name
        self.resource_id = resource_id
        self.callback_url = callback_url


class SmsReceiver(msrest.serialization.Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the SMS receiver. Names must be unique across all receivers
     within an action group.
    :vartype name: str
    :ivar country_code: Required. The country code of the SMS receiver.
    :vartype country_code: str
    :ivar phone_number: Required. The phone number of the SMS receiver.
    :vartype phone_number: str
    :ivar status: The status of the receiver. Known values are: "NotSpecified", "Enabled",
     "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        phone_number: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the SMS receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword country_code: Required. The country code of the SMS receiver.
        :paramtype country_code: str
        :keyword phone_number: Required. The phone number of the SMS receiver.
        :paramtype phone_number: str
        """
        super(SmsReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None


class VoiceReceiver(msrest.serialization.Model):
    """A voice receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the voice receiver. Names must be unique across all receivers
     within an action group.
    :vartype name: str
    :ivar country_code: Required. The country code of the voice receiver.
    :vartype country_code: str
    :ivar phone_number: Required. The phone number of the voice receiver.
    :vartype phone_number: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        phone_number: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the voice receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword country_code: Required. The country code of the voice receiver.
        :paramtype country_code: str
        :keyword phone_number: Required. The phone number of the voice receiver.
        :paramtype phone_number: str
        """
        super(VoiceReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number


class WebhookReceiver(msrest.serialization.Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the webhook receiver. Names must be unique across all
     receivers within an action group.
    :vartype name: str
    :ivar service_uri: Required. The URI where webhooks should be sent.
    :vartype service_uri: str
    """

    _validation = {
        'name': {'required': True},
        'service_uri': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        service_uri: str,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the webhook receiver. Names must be unique across all
         receivers within an action group.
        :paramtype name: str
        :keyword service_uri: Required. The URI where webhooks should be sent.
        :paramtype service_uri: str
        """
        super(WebhookReceiver, self).__init__(**kwargs)
        self.name = name
        self.service_uri = service_uri

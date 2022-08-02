# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DataStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of VM Insights data from the resource. When reported as ``present`` the data array
    will contain information about the data containers to which data for the specified resource is
    being routed.
    """

    PRESENT = "present"
    NOT_PRESENT = "notPresent"

class OnboardingStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The onboarding status for the resource. Note that, a higher level scope, e.g., resource group
    or subscription, is considered onboarded if at least one resource under it is onboarded.
    """

    ONBOARDED = "onboarded"
    NOT_ONBOARDED = "notOnboarded"
    UNKNOWN = "unknown"

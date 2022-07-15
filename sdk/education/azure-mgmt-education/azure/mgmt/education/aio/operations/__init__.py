# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._grants_operations import GrantsOperations
from ._labs_operations import LabsOperations
from ._join_requests_operations import JoinRequestsOperations
from ._education_management_client_operations import EducationManagementClientOperationsMixin
from ._students_operations import StudentsOperations
from ._student_labs_operations import StudentLabsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'Operations',
    'GrantsOperations',
    'LabsOperations',
    'JoinRequestsOperations',
    'EducationManagementClientOperationsMixin',
    'StudentsOperations',
    'StudentLabsOperations',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
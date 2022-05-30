# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AllocationState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Allocation state of the compute. Possible values are: steady - Indicates that the compute is
    not resizing. There are no changes to the number of compute nodes in the compute in progress. A
    compute enters this state when it is created and when no operations are being performed on the
    compute to change the number of compute nodes. resizing - Indicates that the compute is
    resizing; that is, compute nodes are being added to or removed from the compute.
    """

    STEADY = "Steady"
    RESIZING = "Resizing"

class ApplicationSharingPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Policy for sharing applications on this compute instance among users of parent workspace. If
    Personal, only the creator can access applications on this compute instance. When Shared, any
    workspace user can access applications on this instance depending on his/her assigned role.
    """

    PERSONAL = "Personal"
    SHARED = "Shared"

class Autosave(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Auto save settings.
    """

    NONE = "None"
    LOCAL = "Local"
    REMOTE = "Remote"

class BatchLoggingLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Log verbosity for batch inferencing.
    Increasing verbosity order for logging is : Warning, Info and Debug.
    The default value is Info.
    """

    INFO = "Info"
    WARNING = "Warning"
    DEBUG = "Debug"

class BatchOutputAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine how batch inferencing will handle output
    """

    SUMMARY_ONLY = "SummaryOnly"
    APPEND_ROW = "AppendRow"

class BillingCurrency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Three lettered code specifying the currency of the VM price. Example: USD
    """

    USD = "USD"

class Caching(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Caching type of Data Disk.
    """

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class ClusterPurpose(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Intended usage of the cluster
    """

    FAST_PROD = "FastProd"
    DENSE_PROD = "DenseProd"
    DEV_TEST = "DevTest"

class ComputeInstanceAuthorizationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Compute Instance Authorization type. Available values are personal (default).
    """

    PERSONAL = "personal"

class ComputeInstanceState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current state of an ComputeInstance.
    """

    CREATING = "Creating"
    CREATE_FAILED = "CreateFailed"
    DELETING = "Deleting"
    RUNNING = "Running"
    RESTARTING = "Restarting"
    JOB_RUNNING = "JobRunning"
    SETTING_UP = "SettingUp"
    SETUP_FAILED = "SetupFailed"
    STARTING = "Starting"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    USER_SETTING_UP = "UserSettingUp"
    USER_SETUP_FAILED = "UserSetupFailed"
    UNKNOWN = "Unknown"
    UNUSABLE = "Unusable"

class ComputePowerAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The compute power action.
    """

    START = "Start"
    STOP = "Stop"

class ComputeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of compute
    """

    AKS = "AKS"
    KUBERNETES = "Kubernetes"
    AML_COMPUTE = "AmlCompute"
    COMPUTE_INSTANCE = "ComputeInstance"
    DATA_FACTORY = "DataFactory"
    VIRTUAL_MACHINE = "VirtualMachine"
    HD_INSIGHT = "HDInsight"
    DATABRICKS = "Databricks"
    DATA_LAKE_ANALYTICS = "DataLakeAnalytics"
    SYNAPSE_SPARK = "SynapseSpark"

class ConnectionAuthType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Authentication type of the connection target
    """

    PAT = "PAT"
    MANAGED_IDENTITY = "ManagedIdentity"
    USERNAME_PASSWORD = "UsernamePassword"
    NONE = "None"
    SAS = "SAS"

class ConnectionCategory(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Category of the connection
    """

    PYTHON_FEED = "PythonFeed"
    CONTAINER_REGISTRY = "ContainerRegistry"
    GIT = "Git"

class ContainerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    STORAGE_INITIALIZER = "StorageInitializer"
    INFERENCE_SERVER = "InferenceServer"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CredentialsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the datastore credentials type.
    """

    ACCOUNT_KEY = "AccountKey"
    CERTIFICATE = "Certificate"
    NONE = "None"
    SAS = "Sas"
    SERVICE_PRINCIPAL = "ServicePrincipal"

class DatastoreType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the datastore contents type.
    """

    AZURE_BLOB = "AzureBlob"
    AZURE_DATA_LAKE_GEN1 = "AzureDataLakeGen1"
    AZURE_DATA_LAKE_GEN2 = "AzureDataLakeGen2"
    AZURE_FILE = "AzureFile"

class DataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the type of data.
    """

    URI_FILE = "uri_file"
    URI_FOLDER = "uri_folder"
    MLTABLE = "mltable"

class DeploymentProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Possible values for DeploymentProvisioningState.
    """

    CREATING = "Creating"
    DELETING = "Deleting"
    SCALING = "Scaling"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class DiagnoseResultLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Level of workspace setup error
    """

    WARNING = "Warning"
    ERROR = "Error"
    INFORMATION = "Information"

class DistributionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the job distribution type.
    """

    PY_TORCH = "PyTorch"
    TENSOR_FLOW = "TensorFlow"
    MPI = "Mpi"

class EarlyTerminationPolicyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    BANDIT = "Bandit"
    MEDIAN_STOPPING = "MedianStopping"
    TRUNCATION_SELECTION = "TruncationSelection"

class EncryptionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether or not the encryption is enabled for the workspace.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class EndpointAuthMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine endpoint authentication mode.
    """

    AML_TOKEN = "AMLToken"
    KEY = "Key"
    AAD_TOKEN = "AADToken"

class EndpointComputeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine endpoint compute type.
    """

    MANAGED = "Managed"
    KUBERNETES = "Kubernetes"
    AZURE_ML_COMPUTE = "AzureMLCompute"

class EndpointProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of endpoint provisioning.
    """

    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UPDATING = "Updating"
    CANCELED = "Canceled"

class EnvironmentType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Environment type is either user created or curated by Azure ML service
    """

    CURATED = "Curated"
    USER_CREATED = "UserCreated"

class Goal(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Defines supported metric goals for hyperparameter tuning
    """

    MINIMIZE = "Minimize"
    MAXIMIZE = "Maximize"

class IdentityConfigurationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine identity framework.
    """

    MANAGED = "Managed"
    AML_TOKEN = "AMLToken"
    USER_IDENTITY = "UserIdentity"

class InputDeliveryMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the input data delivery mode.
    """

    READ_ONLY_MOUNT = "ReadOnlyMount"
    READ_WRITE_MOUNT = "ReadWriteMount"
    DOWNLOAD = "Download"
    DIRECT = "Direct"
    EVAL_MOUNT = "EvalMount"
    EVAL_DOWNLOAD = "EvalDownload"

class JobInputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the Job Input Type.
    """

    LITERAL = "literal"
    URI_FILE = "uri_file"
    URI_FOLDER = "uri_folder"
    MLTABLE = "mltable"
    CUSTOM_MODEL = "custom_model"
    MLFLOW_MODEL = "mlflow_model"
    TRITON_MODEL = "triton_model"

class JobLimitsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    COMMAND = "Command"
    SWEEP = "Sweep"

class JobOutputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the Job Output Type.
    """

    URI_FILE = "uri_file"
    URI_FOLDER = "uri_folder"
    MLTABLE = "mltable"
    CUSTOM_MODEL = "custom_model"
    MLFLOW_MODEL = "mlflow_model"
    TRITON_MODEL = "triton_model"

class JobStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of a job.
    """

    #: Run hasn't started yet.
    NOT_STARTED = "NotStarted"
    #: Run has started. The user has a run ID.
    STARTING = "Starting"
    #: (Not used currently) It will be used if ES is creating the compute target.
    PROVISIONING = "Provisioning"
    #: The run environment is being prepared.
    PREPARING = "Preparing"
    #: The job is queued in the compute target. For example, in BatchAI the job is in queued state,
    #: while waiting for all required nodes to be ready.
    QUEUED = "Queued"
    #: The job started to run in the compute target.
    RUNNING = "Running"
    #: Job is completed in the target. It is in output collection state now.
    FINALIZING = "Finalizing"
    #: Cancellation has been requested for the job.
    CANCEL_REQUESTED = "CancelRequested"
    #: Job completed successfully. This reflects that both the job itself and output collection states
    #: completed successfully.
    COMPLETED = "Completed"
    #: Job failed.
    FAILED = "Failed"
    #: Following cancellation request, the job is now successfully canceled.
    CANCELED = "Canceled"
    #: When heartbeat is enabled, if the run isn't updating any information to RunHistory then the run
    #: goes to NotResponding state.
    #: NotResponding is the only state that is exempt from strict transition orders. A run can go from
    #: NotResponding to any of the previous states.
    NOT_RESPONDING = "NotResponding"
    #: The job is paused by users. Some adjustment to labeling jobs can be made only in paused state.
    PAUSED = "Paused"
    #: Default job status if not mapped to all other statuses.
    UNKNOWN = "Unknown"

class JobType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the type of job.
    """

    COMMAND = "Command"
    SWEEP = "Sweep"
    PIPELINE = "Pipeline"

class KeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class ListViewType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVE_ONLY = "ActiveOnly"
    ARCHIVED_ONLY = "ArchivedOnly"
    ALL = "All"

class LoadBalancerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Load Balancer Type
    """

    PUBLIC_IP = "PublicIp"
    INTERNAL_LOAD_BALANCER = "InternalLoadBalancer"

class ManagedServiceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class MountAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Mount Action.
    """

    MOUNT = "Mount"
    UNMOUNT = "Unmount"

class MountState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Mount state.
    """

    MOUNT_REQUESTED = "MountRequested"
    MOUNTED = "Mounted"
    MOUNT_FAILED = "MountFailed"
    UNMOUNT_REQUESTED = "UnmountRequested"
    UNMOUNT_FAILED = "UnmountFailed"
    UNMOUNTED = "Unmounted"

class Network(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """network of this container.
    """

    BRIDGE = "Bridge"
    HOST = "Host"

class NodeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the compute node. Values are idle, running, preparing, unusable, leaving and
    preempted.
    """

    IDLE = "idle"
    RUNNING = "running"
    PREPARING = "preparing"
    UNUSABLE = "unusable"
    LEAVING = "leaving"
    PREEMPTED = "preempted"

class OperatingSystemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of operating system.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class OperationName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the last operation.
    """

    CREATE = "Create"
    START = "Start"
    STOP = "Stop"
    RESTART = "Restart"
    REIMAGE = "Reimage"
    DELETE = "Delete"

class OperationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operation status.
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    CREATE_FAILED = "CreateFailed"
    START_FAILED = "StartFailed"
    STOP_FAILED = "StopFailed"
    RESTART_FAILED = "RestartFailed"
    REIMAGE_FAILED = "ReimageFailed"
    DELETE_FAILED = "DeleteFailed"

class OperationTrigger(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Trigger of operation.
    """

    USER = "User"
    SCHEDULE = "Schedule"
    IDLE_SHUTDOWN = "IdleShutdown"

class OrderString(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CREATED_AT_DESC = "CreatedAtDesc"
    CREATED_AT_ASC = "CreatedAtAsc"
    UPDATED_AT_DESC = "UpdatedAtDesc"
    UPDATED_AT_ASC = "UpdatedAtAsc"

class OsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Compute OS Type
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class OutputDeliveryMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Output data delivery mode enums.
    """

    READ_WRITE_MOUNT = "ReadWriteMount"
    UPLOAD = "Upload"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current deployment state of workspace resource. The provisioningState is to indicate states
    for resource provisioning.
    """

    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class ProvisioningStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current deployment state of schedule.
    """

    COMPLETED = "Completed"
    PROVISIONING = "Provisioning"
    FAILED = "Failed"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether requests from Public Network are allowed.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QuotaUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of quota measurement.
    """

    COUNT = "Count"

class RandomSamplingAlgorithmRule(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The specific type of random algorithm
    """

    RANDOM = "Random"
    SOBOL = "Sobol"

class RecurrenceFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to describe the frequency of a recurrence schedule
    """

    #: Minute frequency.
    MINUTE = "Minute"
    #: Hour frequency.
    HOUR = "Hour"
    #: Day frequency.
    DAY = "Day"
    #: Week frequency.
    WEEK = "Week"
    #: Month frequency.
    MONTH = "Month"

class ReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine which reference method to use for an asset.
    """

    ID = "Id"
    DATA_PATH = "DataPath"
    OUTPUT_PATH = "OutputPath"

class RemoteLoginPortPublicAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is
    open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed
    on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be
    default only during cluster creation time, after creation it will be either enabled or
    disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOT_SPECIFIED = "NotSpecified"

class SamplingAlgorithmType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    GRID = "Grid"
    RANDOM = "Random"
    BAYESIAN = "Bayesian"

class ScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    TARGET_UTILIZATION = "TargetUtilization"

class ScheduleStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to describe status of schedule
    """

    #: Schedule is enabled.
    ENABLED = "Enabled"
    #: Schedule is disabled.
    DISABLED = "Disabled"

class ScheduleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to describe type of schedule
    """

    #: Cron schedule type.
    CRON = "Cron"
    #: Recurrence schedule type.
    RECURRENCE = "Recurrence"

class SecretsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the datastore secrets type.
    """

    ACCOUNT_KEY = "AccountKey"
    CERTIFICATE = "Certificate"
    SAS = "Sas"
    SERVICE_PRINCIPAL = "ServicePrincipal"

class ServiceDataAccessAuthIdentity(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    #: Do not use any identity for service data access.
    NONE = "None"
    #: Use the system assigned managed identity of the Workspace to authenticate service data access.
    WORKSPACE_SYSTEM_ASSIGNED_IDENTITY = "WorkspaceSystemAssignedIdentity"
    #: Use the user assigned managed identity of the Workspace to authenticate service data access.
    WORKSPACE_USER_ASSIGNED_IDENTITY = "WorkspaceUserAssignedIdentity"

class SkuScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """TODO - SKU scale type
    """

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"

class SkuTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class SourceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Data source type.
    """

    DATASET = "Dataset"
    DATASTORE = "Datastore"
    URI = "URI"

class SshPublicAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on this instance. Enabled - Indicates that the public ssh port is open and
    accessible according to the VNet/subnet policy if applicable.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class SslConfigurationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enable or disable ssl for scoring
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"
    AUTO = "Auto"

class Status(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of update workspace quota.
    """

    UNDEFINED = "Undefined"
    SUCCESS = "Success"
    FAILURE = "Failure"
    INVALID_QUOTA_BELOW_CLUSTER_MINIMUM = "InvalidQuotaBelowClusterMinimum"
    INVALID_QUOTA_EXCEEDS_SUBSCRIPTION_LIMIT = "InvalidQuotaExceedsSubscriptionLimit"
    INVALID_VM_FAMILY_NAME = "InvalidVMFamilyName"
    OPERATION_NOT_SUPPORTED_FOR_SKU = "OperationNotSupportedForSku"
    OPERATION_NOT_ENABLED_FOR_REGION = "OperationNotEnabledForRegion"

class StorageAccountType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """type of this storage account.
    """

    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"

class UnderlyingResourceAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DELETE = "Delete"
    DETACH = "Detach"

class UnitOfMeasure(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of time measurement for the specified VM price. Example: OneHour
    """

    ONE_HOUR = "OneHour"

class UsageUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of usage measurement.
    """

    COUNT = "Count"

class ValueFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """format for the workspace connection value
    """

    JSON = "JSON"

class VMPriceOSType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operating system type used by the VM.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class VmPriority(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Virtual Machine priority
    """

    DEDICATED = "Dedicated"
    LOW_PRIORITY = "LowPriority"

class VMTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the VM.
    """

    STANDARD = "Standard"
    LOW_PRIORITY = "LowPriority"
    SPOT = "Spot"

class Weekday(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum of weekdays
    """

    #: Monday weekday.
    MONDAY = "Monday"
    #: Tuesday weekday.
    TUESDAY = "Tuesday"
    #: Wednesday weekday.
    WEDNESDAY = "Wednesday"
    #: Thursday weekday.
    THURSDAY = "Thursday"
    #: Friday weekday.
    FRIDAY = "Friday"
    #: Saturday weekday.
    SATURDAY = "Saturday"
    #: Sunday weekday.
    SUNDAY = "Sunday"

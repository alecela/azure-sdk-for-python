# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.policy_assignments_operations import PolicyAssignmentsOperations
from .operations.policy_definitions_operations import PolicyDefinitionsOperations
from .operations.policy_set_definitions_operations import PolicySetDefinitionsOperations
from . import models


class PolicyClientConfiguration(AzureConfiguration):
    """Configuration for PolicyClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(PolicyClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-resource/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class PolicyClient(SDKClient):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    :ivar config: Configuration for client.
    :vartype config: PolicyClientConfiguration

    :ivar policy_assignments: PolicyAssignments operations
    :vartype policy_assignments: azure.mgmt.resource.policy.v2018_03_01.operations.PolicyAssignmentsOperations
    :ivar policy_definitions: PolicyDefinitions operations
    :vartype policy_definitions: azure.mgmt.resource.policy.v2018_03_01.operations.PolicyDefinitionsOperations
    :ivar policy_set_definitions: PolicySetDefinitions operations
    :vartype policy_set_definitions: azure.mgmt.resource.policy.v2018_03_01.operations.PolicySetDefinitionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = PolicyClientConfiguration(credentials, subscription_id, base_url)
        super(PolicyClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-03-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.policy_assignments = PolicyAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_definitions = PolicyDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_set_definitions = PolicySetDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)

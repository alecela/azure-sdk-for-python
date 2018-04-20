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

from .proxy_resource import ProxyResource


class Experiment(ProxyResource):
    """Contains information about the experiment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar creation_time: Time when the Experiment was created.
    :vartype creation_time: datetime
    :ivar provisioning_state: The provisioned state of the experiment.
     Possible values include: 'creating', 'succeeded', 'failed', 'deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.batchai.models.ProvisioningState
    :ivar provisioning_state_transition_time: The time at which the experiment
     entered its current provisioning state. The time at which the experiment
     entered its current provisioning state.
    :vartype provisioning_state_transition_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(Experiment, self).__init__(**kwargs)
        self.creation_time = None
        self.provisioning_state = None
        self.provisioning_state_transition_time = None

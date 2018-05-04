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

from msrest.serialization import Model


class SourceControlSyncJob(Model):
    """Definition of the source control sync job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar id: Resource id.
    :vartype id: str
    :param sync_job_id: Gets the source control sync job id.
    :type sync_job_id: str
    :ivar creation_time: Gets the creation time of the job.
    :vartype creation_time: datetime
    :param provisioning_state: Gets the provisioning state of the job.
     Possible values include: 'Completed', 'Failed', 'Running'
    :type provisioning_state: str or
     ~azure.mgmt.automation.models.ProvisioningState
    :ivar start_time: Gets the start time of the job.
    :vartype start_time: datetime
    :ivar end_time: Gets the end time of the job.
    :vartype end_time: datetime
    :param start_type: Gets the type of start for the sync job. Possible
     values include: 'AutoSync', 'ManualSync'
    :type start_type: str or ~azure.mgmt.automation.models.StartType
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'id': {'readonly': True},
        'creation_time': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'sync_job_id': {'key': 'properties.syncJobId', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'start_type': {'key': 'properties.startType', 'type': 'str'},
    }

    def __init__(self, sync_job_id=None, provisioning_state=None, start_type=None):
        super(SourceControlSyncJob, self).__init__()
        self.name = None
        self.type = None
        self.id = None
        self.sync_job_id = sync_job_id
        self.creation_time = None
        self.provisioning_state = provisioning_state
        self.start_time = None
        self.end_time = None
        self.start_type = start_type

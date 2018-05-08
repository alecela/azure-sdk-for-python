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


class NamespacePatchParameters(Model):
    """Parameters supplied to the Patch Namespace operation.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param kind: The kind of namespace
    :type kind: ~azure.mgmt.notificationhubs.models.Kind
    :param sku: The sku of the created namespace
    :type sku: ~azure.mgmt.notificationhubs.models.Sku
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'Kind'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(NamespacePatchParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.kind = kwargs.get('kind', None)
        self.sku = kwargs.get('sku', None)

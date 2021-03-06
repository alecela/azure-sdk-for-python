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

from .audio import Audio


class AacAudio(Audio):
    """Describes Advanced Audio Codec (AAC) audio encoding settings.

    All required parameters must be populated in order to send to Azure.

    :param label: An optional label for the codec. The label can be used to
     control muxing behavior.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param channels: The number of channels in the audio.
    :type channels: int
    :param sampling_rate: The sampling rate to use for encoding in hertz.
    :type sampling_rate: int
    :param bitrate: The bitrate, in bits per second, of the output encoded
     audio.
    :type bitrate: int
    :param profile: The encoding profile to be used when encoding audio with
     AAC. Possible values include: 'AacLc', 'HeAacV1', 'HeAacV2'
    :type profile: str or ~azure.mgmt.media.models.AacAudioProfile
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'channels': {'key': 'channels', 'type': 'int'},
        'sampling_rate': {'key': 'samplingRate', 'type': 'int'},
        'bitrate': {'key': 'bitrate', 'type': 'int'},
        'profile': {'key': 'profile', 'type': 'AacAudioProfile'},
    }

    def __init__(self, *, label: str=None, channels: int=None, sampling_rate: int=None, bitrate: int=None, profile=None, **kwargs) -> None:
        super(AacAudio, self).__init__(label=label, channels=channels, sampling_rate=sampling_rate, bitrate=bitrate, **kwargs)
        self.profile = profile
        self.odatatype = '#Microsoft.Media.AacAudio'

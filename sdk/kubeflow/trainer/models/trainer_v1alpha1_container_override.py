# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.trainer.configuration import Configuration


class TrainerV1alpha1ContainerOverride(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'args': 'list[str]',
        'command': 'list[str]',
        'env': 'list[V1EnvVar]',
        'env_from': 'list[V1EnvFromSource]',
        'name': 'str',
        'volume_mounts': 'list[V1VolumeMount]'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'env': 'env',
        'env_from': 'envFrom',
        'name': 'name',
        'volume_mounts': 'volumeMounts'
    }

    def __init__(self, args=None, command=None, env=None, env_from=None, name='', volume_mounts=None, local_vars_configuration=None):  # noqa: E501
        """TrainerV1alpha1ContainerOverride - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._command = None
        self._env = None
        self._env_from = None
        self._name = None
        self._volume_mounts = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if env_from is not None:
            self.env_from = env_from
        self.name = name
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts

    @property
    def args(self):
        """Gets the args of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        Arguments to the entrypoint for the training container.  # noqa: E501

        :return: The args of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this TrainerV1alpha1ContainerOverride.

        Arguments to the entrypoint for the training container.  # noqa: E501

        :param args: The args of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        Entrypoint commands for the training container.  # noqa: E501

        :return: The command of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this TrainerV1alpha1ContainerOverride.

        Entrypoint commands for the training container.  # noqa: E501

        :param command: The command of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        List of environment variables to set in the container. These values will be merged with the TrainingRuntime's environments.  # noqa: E501

        :return: The env of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this TrainerV1alpha1ContainerOverride.

        List of environment variables to set in the container. These values will be merged with the TrainingRuntime's environments.  # noqa: E501

        :param env: The env of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def env_from(self):
        """Gets the env_from of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        List of sources to populate environment variables in the container. These   values will be merged with the TrainingRuntime's environments.  # noqa: E501

        :return: The env_from of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: list[V1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from):
        """Sets the env_from of this TrainerV1alpha1ContainerOverride.

        List of sources to populate environment variables in the container. These   values will be merged with the TrainingRuntime's environments.  # noqa: E501

        :param env_from: The env_from of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: list[V1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def name(self):
        """Gets the name of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        Name for the container. TrainingRuntime must have this container.  # noqa: E501

        :return: The name of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrainerV1alpha1ContainerOverride.

        Name for the container. TrainingRuntime must have this container.  # noqa: E501

        :param name: The name of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this TrainerV1alpha1ContainerOverride.  # noqa: E501

        Pod volumes to mount into the container's filesystem.  # noqa: E501

        :return: The volume_mounts of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this TrainerV1alpha1ContainerOverride.

        Pod volumes to mount into the container's filesystem.  # noqa: E501

        :param volume_mounts: The volume_mounts of this TrainerV1alpha1ContainerOverride.  # noqa: E501
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrainerV1alpha1ContainerOverride):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrainerV1alpha1ContainerOverride):
            return True

        return self.to_dict() != other.to_dict()

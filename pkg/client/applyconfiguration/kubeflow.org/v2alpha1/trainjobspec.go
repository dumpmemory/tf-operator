// Copyright 2024 The Kubeflow Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by applyconfiguration-gen. DO NOT EDIT.

package v2alpha1

// TrainJobSpecApplyConfiguration represents an declarative configuration of the TrainJobSpec type for use
// with apply.
type TrainJobSpecApplyConfiguration struct {
	RuntimeRef       *RuntimeRefApplyConfiguration       `json:"runtimeRef,omitempty"`
	Trainer          *TrainerApplyConfiguration          `json:"trainer,omitempty"`
	DatasetConfig    *DatasetConfigApplyConfiguration    `json:"datasetConfig,omitempty"`
	ModelConfig      *ModelConfigApplyConfiguration      `json:"modelConfig,omitempty"`
	Labels           map[string]string                   `json:"labels,omitempty"`
	Annotations      map[string]string                   `json:"annotations,omitempty"`
	PodSpecOverrides []PodSpecOverrideApplyConfiguration `json:"podSpecOverrides,omitempty"`
	Suspend          *bool                               `json:"suspend,omitempty"`
	ManagedBy        *string                             `json:"managedBy,omitempty"`
}

// TrainJobSpecApplyConfiguration constructs an declarative configuration of the TrainJobSpec type for use with
// apply.
func TrainJobSpec() *TrainJobSpecApplyConfiguration {
	return &TrainJobSpecApplyConfiguration{}
}

// WithRuntimeRef sets the RuntimeRef field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the RuntimeRef field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithRuntimeRef(value *RuntimeRefApplyConfiguration) *TrainJobSpecApplyConfiguration {
	b.RuntimeRef = value
	return b
}

// WithTrainer sets the Trainer field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the Trainer field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithTrainer(value *TrainerApplyConfiguration) *TrainJobSpecApplyConfiguration {
	b.Trainer = value
	return b
}

// WithDatasetConfig sets the DatasetConfig field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the DatasetConfig field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithDatasetConfig(value *DatasetConfigApplyConfiguration) *TrainJobSpecApplyConfiguration {
	b.DatasetConfig = value
	return b
}

// WithModelConfig sets the ModelConfig field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the ModelConfig field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithModelConfig(value *ModelConfigApplyConfiguration) *TrainJobSpecApplyConfiguration {
	b.ModelConfig = value
	return b
}

// WithLabels puts the entries into the Labels field in the declarative configuration
// and returns the receiver, so that objects can be build by chaining "With" function invocations.
// If called multiple times, the entries provided by each call will be put on the Labels field,
// overwriting an existing map entries in Labels field with the same key.
func (b *TrainJobSpecApplyConfiguration) WithLabels(entries map[string]string) *TrainJobSpecApplyConfiguration {
	if b.Labels == nil && len(entries) > 0 {
		b.Labels = make(map[string]string, len(entries))
	}
	for k, v := range entries {
		b.Labels[k] = v
	}
	return b
}

// WithAnnotations puts the entries into the Annotations field in the declarative configuration
// and returns the receiver, so that objects can be build by chaining "With" function invocations.
// If called multiple times, the entries provided by each call will be put on the Annotations field,
// overwriting an existing map entries in Annotations field with the same key.
func (b *TrainJobSpecApplyConfiguration) WithAnnotations(entries map[string]string) *TrainJobSpecApplyConfiguration {
	if b.Annotations == nil && len(entries) > 0 {
		b.Annotations = make(map[string]string, len(entries))
	}
	for k, v := range entries {
		b.Annotations[k] = v
	}
	return b
}

// WithPodSpecOverrides adds the given value to the PodSpecOverrides field in the declarative configuration
// and returns the receiver, so that objects can be build by chaining "With" function invocations.
// If called multiple times, values provided by each call will be appended to the PodSpecOverrides field.
func (b *TrainJobSpecApplyConfiguration) WithPodSpecOverrides(values ...*PodSpecOverrideApplyConfiguration) *TrainJobSpecApplyConfiguration {
	for i := range values {
		if values[i] == nil {
			panic("nil value passed to WithPodSpecOverrides")
		}
		b.PodSpecOverrides = append(b.PodSpecOverrides, *values[i])
	}
	return b
}

// WithSuspend sets the Suspend field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the Suspend field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithSuspend(value bool) *TrainJobSpecApplyConfiguration {
	b.Suspend = &value
	return b
}

// WithManagedBy sets the ManagedBy field in the declarative configuration to the given value
// and returns the receiver, so that objects can be built by chaining "With" function invocations.
// If called multiple times, the ManagedBy field is set to the value of the last call.
func (b *TrainJobSpecApplyConfiguration) WithManagedBy(value string) *TrainJobSpecApplyConfiguration {
	b.ManagedBy = &value
	return b
}

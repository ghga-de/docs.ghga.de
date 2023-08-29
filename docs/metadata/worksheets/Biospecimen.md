# Biospecimen

## Description

A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

## Fields


**name** : The name for an entity.
**alias** : name
**data type** : string
**required** : False


**type** : The type of Biospecimen.
**alias** : type
**data type** : string
**required** : False


**description** : Description of an entity.
**alias** : description
**data type** : string
**required** : False


**isolation** : Method or device employed for collecting/isolating a biospecimen or a sample.
**alias** : isolation
**data type** : string
**required** : False


**storage** : Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
**alias** : storage
**data type** : string
**required** : False


**individual** : The Individual entity from which this Biospecimen was derived.
**alias** : individual
**data type** : Individual
**required** : True


**age_at_sampling** : Age of an individual.
**alias** : age_at_sampling
**data type** : AgeRangeEnum
**required** : True


**vital_status_at_sampling** : Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
**alias** : vital_status_at_sampling
**data type** : VitalStatusEnum
**required** : False


**tissue** : None
**alias** : tissue
**data type** : string
**required** : True


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

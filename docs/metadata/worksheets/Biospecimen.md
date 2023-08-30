# Biospecimen

## Description

A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

## Fields


**name** : The name for an entity.
**data type** : string
**required** : False

**type** : The type of Biospecimen.
**data type** : string
**required** : False

**description** : Description of an entity.
**data type** : string
**required** : False

**isolation** : Method or device employed for collecting/isolating a biospecimen or a sample.
**data type** : string
**required** : False

**storage** : Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
**data type** : string
**required** : False

**individual** : The Individual entity from which this Biospecimen was derived.
**data type** : Individual
**required** : True

**age_at_sampling** : Age of an individual.
**data type** : Controlled Vocabulary
**required** : True

**vital_status_at_sampling** : Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
**data type** : Controlled Vocabulary
**required** : False

**tissue** : None
**data type** : string
**required** : True

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

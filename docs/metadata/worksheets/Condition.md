# Condition

## Description

An condition that is linked to comparable samples.

## Fields


**title** : The title that describes an entity.
**data type** : string
**required** : None

**description** : Description of an entity.
**data type** : string
**required** : True

**name** : The name for an entity.
**data type** : string
**required** : True

**disease_or_healthy** : Whether a condition corresponds to a disease or a healthy state.
**data type** : Controlled Vocabulary
**required** : True

**case_control_status** : Whether a condition corresponds to a treatment or a control.
**data type** : Controlled Vocabulary
**required** : True

**mutant_or_wildtype** : Whether a condition corresponds to a mutant or a wildtype.
**data type** : Controlled Vocabulary
**required** : True

**study** : The study associated with an entity.
**data type** : Study
**required** : True

**attributes** : Key/value pairs corresponding to an entity.
**data type** : Attribute
**required** : False

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

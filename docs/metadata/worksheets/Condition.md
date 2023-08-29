# Condition

## Description

An condition that is linked to comparable samples.

## Fields


**title** : The title that describes an entity.
**alias** : title
**data type** : string
**required** : None


**description** : Description of an entity.
**alias** : description
**data type** : string
**required** : True


**name** : The name for an entity.
**alias** : name
**data type** : string
**required** : True


**disease_or_healthy** : Whether a condition corresponds to a disease or a healthy state.
**alias** : disease_or_healthy
**data type** : DiseaseOrHealthyEnum
**required** : True


**case_control_status** : Whether a condition corresponds to a treatment or a control.
**alias** : case_control_status
**data type** : CaseControlStatusEnum
**required** : True


**mutant_or_wildtype** : Whether a condition corresponds to a mutant or a wildtype.
**alias** : mutant_or_wildtype
**data type** : MutantOrWildtypeEnum
**required** : True


**study** : The study associated with an entity.
**alias** : study
**data type** : Study
**required** : True


**attributes** : Key/value pairs corresponding to an entity.
**alias** : attributes
**data type** : Attribute
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

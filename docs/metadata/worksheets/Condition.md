# Condition

## Description

An condition that is linked to comparable samples.

## Fields

**title** : The title that describes an entity.<br>
**required** : None<br>
**data type** : string <br>


**description** : Description of an entity.<br>
**required** : True<br>
**data type** : string <br>


**name** : The name for an entity.<br>
**required** : True<br>
**data type** : string <br>


**disease_or_healthy** : Whether a condition corresponds to a disease or a healthy state.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `DISEASE` | `Disease state.` |
| `HEALTHY` | `Healthy state.` |
| `NOT_APPLICABLE` | `The distinction is not applicaple.` |



**case_control_status** : Whether a condition corresponds to a treatment or a control.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `NEITHER_CASE_OR_CONTROL_STATUS` | `None` |
| `PROBABLE_CASE_STATUS` | `None` |
| `PROBABLE_CONTROL_STATUS` | `None` |
| `TRUE_CASE_STATUS` | `None` |
| `TRUE_CONTROL_STATUS` | `None` |
| `UNABLE_TO_ASSESS_CASE_OR_CONTROL_STATUS` | `None` |



**mutant_or_wildtype** : Whether a condition corresponds to a mutant or a wildtype.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `MUTANT` | `Mutant state.` |
| `WILDTYPE` | `Wildtype state.` |
| `NOT_APPLICABLE` | `The distinction is not applicaple.` |



**study** : The study associated with an entity.<br>
**required** : True<br>
**data type** : Study <br>


**attributes** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

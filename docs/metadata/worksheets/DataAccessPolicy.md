# DataAccessPolicy

## Description

A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

## Fields

### ***name***<br>
**description** : A name for the Data Access Policy.<br>
**required** : True<br>
**data type** : string <br>
### ***description***<br>
**description** : A short description for the Data Access Policy.<br>
**required** : True<br>
**data type** : string <br>
### ***policy_text***<br>
**description** : The terms of data use and policy verbiage should be captured here.<br>
**required** : True<br>
**data type** : string <br>
### ***policy_url***<br>
**description** : URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.<br>
**required** : False<br>
**data type** : string <br>
### ***data_access_committee***<br>
**description** : The Data Access Committee linked to this policy.<br>
**required** : True<br>
**data type** : DataAccessCommittee <br>
### ***data_use_permission***<br>
**description** : Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `general research use` | `None` |
| `health or medical or biomedical research` | `None` |
| `disease specific research` | `None` |
| `no restriction` | `None` |
| `population origins or ancestry research only` | `None` |


</details>

### ***data_use_modifiers***<br>
**description** : Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `clinical care use` | `None` |
| `return to database or resource` | `None` |
| `institution specific restriction` | `None` |
| `project specific restriction` | `None` |
| `user specific restriction` | `None` |
| `time limit on use` | `None` |
| `publication moratorium` | `None` |
| `geographical restriction` | `None` |
| `ethics approval required` | `None` |
| `collaboration required` | `None` |
| `publication required` | `None` |
| `not for profit, non commercial use only` | `None` |
| `non-commercial use only` | `None` |
| `not for profit organisation use only` | `None` |
| `genetic studies only` | `None` |
| `no general methods research` | `None` |
| `research specific restrictions` | `None` |
| `population origins or ancestry research prohibited` | `None` |


</details>

### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

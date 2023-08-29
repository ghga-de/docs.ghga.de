# DataAccessPolicy

## Description

A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

## Fields


**name** : A name for the Data Access Policy.
**alias** : name
**data type** : string
**required** : True


**description** : A short description for the Data Access Policy.
**alias** : description
**data type** : string
**required** : True


**policy_text** : The terms of data use and policy verbiage should be captured here.
**alias** : policy_text
**data type** : string
**required** : True


**policy_url** : URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
**alias** : policy_url
**data type** : string
**required** : False


**data_access_committee** : The Data Access Committee linked to this policy.
**alias** : data_access_committee
**data type** : DataAccessCommittee
**required** : True


**data_use_permission** : Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
**alias** : data_use_permission
**data type** : DataUsePermissionEnum
**required** : True


**data_use_modifiers** : Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
**alias** : data_use_modifiers
**data type** : DataUseModifierEnum
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

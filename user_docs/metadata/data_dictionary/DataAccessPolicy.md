# DataAccessPolicy

## Description
A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

## Fields
### ***name***
**description** : A name for this Data Access Policy.<br>
**required** : True<br>
**significance** : required<br>
**data type** : string <br>
### ***description***
**description** : A short description for this Data Access Policy.<br>
**required** : True<br>
**significance** : required<br>
**data type** : string <br>
### ***policy_text***
**description** : The complete text for the Data Access Policy.<br>
**required** : True<br>
**significance** : required<br>
**data type** : string <br>
### ***policy_url***
**description** : An alternative to the Data Access Policy text is to provide the URL for the policy. This is useful if the terms of the policy are available online at a resolvable URL.<br>
**required** : False<br>
**significance** : recommended<br>
**data type** : string <br>
### ***data_use_permission_term***
**description** : The Data Use Permission associated with this Data Use Policy. The used term should be a descendant of 'DUO:0000001: data use permission' (e.g., no restriction).<br>
**required** : True<br>
**significance** : required<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `GENERAL_RESEARCH_USE` | `This data use permission indicates that use is allowed for general research use for any research purpose.` |
| `HEALTH_OR_MEDICAL_OR_BIOMEDICAL_RESEARCH` | `This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.` |
| `DISEASE_SPECIFIC_RESEARCH` | `This data use permission indicates that use is allowed provided it is related to the specified disease.` |
| `NO_RESTRICTION` | `This data use permission indicates there is no restriction on use.` |
| `POPULATION_ORIGINS_OR_ANCESTRY_RESEARCH_ONLY` | `This data use permission indicates that use of the data is limited to the study of population origins or ancestry.` |
///

### ***data_use_permission_id***
**description** : The DUO ID corresponding to the Data Use Permission term (e.g., DUO:0000004).<br>
**required** : True<br>
**significance** : required<br>
**data type** : string <br>
### ***data_use_modifier_terms***
**description** : One or more Data Use Modifiers for the Data Use Permission associated with this Data Use Policy. The used terms should be descendants of 'DUO:0000017: data use modifier' (e.g., clinical care use). Please use 'USER_SPECIFIC_RESTRICTION' if no other modifier applies.<br>
**required** : False<br>
**significance** : recommended<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `CLINICAL_CARE_USE` | `This data use modifier indicates that use is allowed for clinical use and care.  Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making.` |
| `RETURN_TO_DATABASE_OR_RESOURCE` | `This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.` |
| `INSTITUTION_SPECIFIC_RESTRICTION` | `This data use modifier indicates that use is limited to use within an approved institution.` |
| `PROJECT_SPECIFIC_RESTRICTION` | `This data use modifier indicates that use is limited to use within an approved project.` |
| `USER_SPECIFIC_RESTRICTION` | `This data use modifier indicates that use is limited to use by approved users.` |
| `TIME_LIMIT_ON_USE` | `This data use modifier indicates that use is approved for a specific number of months. This should be coupled with an integer value indicating the number of months.` |
| `PUBLICATION_MORATORIUM` | `This data use modifier indicates that requestor agrees not to publish results of studies until a specific date. This should be coupled with a date specified as ISO8601.` |
| `GEOGRAPHICAL_RESTRICTION` | `This data use modifier indicates that use is limited to within a specific geographic region. This should be coupled with an ontology term describing the geographical location the restriction applies to.` |
| `ETHICS_APPROVAL_REQUIRED` | `This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.` |
| `COLLABORATION_REQUIRED` | `This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s). This could be coupled with a string describing the primary study investigator(s).` |
| `PUBLICATION_REQUIRED` | `This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.` |
| `NOT_FOR_PROFIT_NON_COMMERCIAL_USE_ONLY` | `This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.` |
| `NON_COMMERCIAL_USE_ONLY` | `This data use modifier indicates that use of the data is limited to not-for-profit use. This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes.` |
| `NOT_FOR_PROFIT_ORGANISATION_USE_ONLY` | `This data use modifier indicates that use of the data is limited to not-for-profit organizations.` |
| `GENETIC_STUDIES_ONLY` | `This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively).` |
| `NO_GENERAL_METHODS_RESEARCH` | `This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).` |
| `RESEARCH_SPECIFIC_RESTRICTIONS` | `This data use modifier indicates that use is limited to studies of a certain research type.` |
| `POPULATION_ORIGINS_OR_ANCESTRY_RESEARCH_PROHIBITED` | `This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.` |
///

### ***data_use_modifier_ids***
**description** : The DUO IDs corresponding to the Data Use Modifier terms (e.g., DUO:0000043).<br>
**required** : False<br>
**significance** : recommended<br>
**data type** : string <br>
### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**required** : False<br>
**significance** : optional<br>
**data type** : string <br>
### ***data_access_committee***
**description** : The Data Access Committee linked to this Data Use Policy.<br>
**required** : True<br>
**significance** : required<br>
**data type** : DataAccessCommittee <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**significance** : required<br>
**data type** : string <br>

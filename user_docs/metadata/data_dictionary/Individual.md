# Individual

## Description
An Individual is a Person who is participating in a Study.

## Fields
### ***phenotypic_features_terms***
**description** : The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology (e.g., Lymph node hypoplasia, Cough, Hypotension).<br>
**required** : False<br>
**data type** : string <br>
### ***phenotypic_features_ids***
**description** : The corresponding ID to the HPO vocabulary (e.g., HP:0002732, HP:0012735, HP:0002615).<br>
**required** : False<br>
**data type** : string <br>
### ***diagnosis_ids***
**description** : One or more diagnoses that the entity is associated with at the time of retrieval from the organism. The diagnosis is captured using a code from ICD-10 (WHO version). Please restrict the ICD code to the chapter letter and two digits for the main diagnosis (e.g., E10, C01).<br>
**required** : False<br>
**data type** : string <br>
### ***diagnosis_terms***
**description** : The ICD-10 terms corresponding to the ICD-10 codes (e.g., Type 1 diabetes mellitus, Malignant neoplasm of base of tongue).<br>
**required** : False<br>
**data type** : string <br>
### ***sex***
**description** : The biological sex of the Individual (e.g., female).<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `FEMALE` | `A sex for clinical use value in which stereotypically or statistically "female" values apply to an individual in a given medical context, such as for a procedure, process, algorithm, hormone level, genetic composition, organ inventory.` |
| `MALE` | `A sex for clinical use value in which stereotypically or statistically "male" values apply to an individual in a given medical context, such as for a procedure, process, algorithm, hormone level, genetic composition, organ inventory.` |
| `UNKNOWN` | `A sex for clinical use value in which the stereotypical or statistical known values do not apply, cannot be determined, or are not sufficient for determination of a another value.` |
| `OTHER` | `A sex not captured by the controlled vocabulary.` |
///

### ***geographical_region_term***
**description** : The Individual's geographical region. The used terms should be descendants of 'NCIT:C25464: country' (e.g., Austria, Germany, Italy).<br>
**required** : False<br>
**data type** : string <br>
### ***geographical_region_id***
**description** : The corresponding ID to the NCIT vocabulary (e.g., NCIT:C16312, NCIT:C16636, NCIT:C16761).<br>
**required** : False<br>
**data type** : string <br>
### ***ancestry_terms***
**description** : A person's descent or lineage from a population. The used terms should be descendants of 'HANCESTRO:0004: ancestry category' (e.g., African, European, Oceanian).<br>
**required** : False<br>
**data type** : string <br>
### ***ancestry_ids***
**description** : The corresponding ID to the HANCESTRO vocabulary (e.g., HANCESTRO:0010, HANCESTRO:0005, HANCESTRO:0017).<br>
**required** : False<br>
**data type** : string <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

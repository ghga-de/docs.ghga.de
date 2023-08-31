# Individual

## Description

An Individual is a Person who is participating in a Study.

## Fields

**sex** : The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `FEMALE_SEX_FOR_CLINICAL_USE` | `None` |
| `IMAGING_SEX` | `None` |
| `MALE_SEX_FOR_CLINICAL_USE` | `None` |
| `SPECIFIED_SEX_FOR_CLINICAL_USE` | `None` |
| `UNKNOWN_SEX_FOR_CLINICAL_USE` | `None` |



**karyotype** : The karyotype of an individual if defined.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `46_XY` | `None` |
| `46_XX` | `None` |
| `OTHER` | `None` |



**geographical_region** : The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.<br>
**required** : False<br>
**data type** : string <br>


**ancestries** : A person's descent or lineage, from a person or from a population.<br>
**required** : False<br>
**data type** : string <br>


**phenotypic_features** : The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.<br>
**required** : False<br>
**data type** : string <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

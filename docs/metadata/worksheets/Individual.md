# Individual

## Description

An Individual is a Person who is participating in a Study.

## Fields


**sex** : The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
**alias** : sex
**data type** : IndividualSexEnum
**required** : True


**karyotype** : The karyotype of an individual if defined.
**alias** : karyotype
**data type** : KaryotypeEnum
**required** : False


**geographical_region** : The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
**alias** : geographical_region
**data type** : string
**required** : False


**ancestries** : A person's descent or lineage, from a person or from a population.
**alias** : ancestries
**data type** : string
**required** : False


**phenotypic_features** : The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
**alias** : phenotypic_features
**data type** : string
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

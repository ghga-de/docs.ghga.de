# Publication

## Description

The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

## Fields


**title** : The title for the Publication.
**alias** : title
**data type** : string
**required** : False


**abstract** : The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
**alias** : abstract
**data type** : string
**required** : False


**author** : The individual who is responsible for the content of a document version.
**alias** : author
**data type** : string
**required** : False


**year** : Year in which the paper was published.
**alias** : year
**data type** : integer
**required** : False


**journal** : Name of the journal.
**alias** : journal
**data type** : string
**required** : False


**doi** : DOI identifier of the Publication.
**alias** : doi
**data type** : string
**required** : True


**study** : The Study entity associated with this Publication.
**alias** : study
**data type** : Study
**required** : True


**xref** : One or more cross-references for this Publication.
**alias** : xref
**data type** : string
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

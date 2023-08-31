# Publication

## Description

The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

## Fields

**title** : The title for the Publication.<br>
**required** : False<br>
**data type** : string <br>


**abstract** : The study abstract that describes the goals. Can also hold abstract from a publication related to this study.<br>
**required** : False<br>
**data type** : string <br>


**author** : The individual who is responsible for the content of a document version.<br>
**required** : False<br>
**data type** : string <br>


**year** : Year in which the paper was published.<br>
**required** : False<br>
**data type** : integer <br>


**journal** : Name of the journal.<br>
**required** : False<br>
**data type** : string <br>


**doi** : DOI identifier of the Publication.<br>
**required** : True<br>
**data type** : string <br>


**study** : The Study entity associated with this Publication.<br>
**required** : True<br>
**data type** : Study <br>


**xref** : One or more cross-references for this Publication.<br>
**required** : False<br>
**data type** : string <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

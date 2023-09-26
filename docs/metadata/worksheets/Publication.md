# Publication

## Description

The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

## Fields

### ***title***<br>
**description** : The title for the Publication.<br>
**required** : False<br>
**data type** : string <br>
### ***abstract***<br>
**description** : The study abstract that describes the goals. Can also hold abstract from a publication related to this study.<br>
**required** : False<br>
**data type** : string <br>
### ***author***<br>
**description** : The individual who is responsible for the content of a document version.<br>
**required** : False<br>
**data type** : string <br>
### ***year***<br>
**description** : Year in which the paper was published.<br>
**required** : False<br>
**data type** : integer <br>
### ***journal***<br>
**description** : Name of the journal.<br>
**required** : False<br>
**data type** : string <br>
### ***doi***<br>
**description** : DOI identifier of the Publication.<br>
**required** : True<br>
**data type** : string <br>
### ***study***<br>
**description** : The Study entity associated with this Publication.<br>
**required** : True<br>
**data type** : Study <br>
### ***xref***<br>
**description** : One or more cross-references for this Publication.<br>
**required** : False<br>
**data type** : string <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

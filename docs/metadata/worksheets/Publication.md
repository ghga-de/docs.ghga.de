# Publication

## Description

A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.

## Fields

### ***study***<br>
**description** : The Study entity associated with this Publication.<br>
**required** : True<br>
**data type** : Study <br>
### ***title***<br>
**description** : The title for this Publication.<br>
**required** : False<br>
**data type** : string <br>
### ***abstract***<br>
**description** : The study abstract that describes the goals. Can also hold abstract from a publication related to this Study.<br>
**required** : False<br>
**data type** : string <br>
### ***author***<br>
**description** : Author(s) of this Publication.<br>
**required** : False<br>
**data type** : string <br>
### ***year***<br>
**description** : The year in which the paper was published.<br>
**required** : False<br>
**data type** : integer <br>
### ***journal***<br>
**description** : The name of the journal.<br>
**required** : False<br>
**data type** : string <br>
### ***doi***<br>
**description** : DOI identifier of a publication.<br>
**required** : True<br>
**data type** : string <br>
### ***xref***<br>
**description** : One or more cross-references for this Publication.<br>
**required** : False<br>
**data type** : string <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

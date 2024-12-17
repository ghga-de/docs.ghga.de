# Publication

## Description
A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.

$\color{green}{test}$

## Fields
### ***study***
**description** : The Study entity associated with this Publication.<br>
**requirement**:  $\color{red}{required}$
**data type** : Study <br>
### ***title***
**description** : The title for this Publication.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***abstract***
**description** : The study abstract that describes the goals. Can also hold abstract from a publication related to this Study.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***author***
**description** : Author(s) of this Publication.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***year***
**description** : The year in which the paper was published.<br>
**requirement**:  $\color{green}{optional}$
**data type** : integer <br>
### ***journal***
**description** : The name of the journal.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***doi***
**description** : DOI identifier of a publication.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>
### ***xref***
**description** : One or more cross-references for this Publication.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>

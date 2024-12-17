# Dataset

## Description
A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

$\color{green}{test}$

## Fields
### ***title***
**description** : A title for this Dataset.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>
### ***description***
**description** : A description summarizing this Dataset.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>
### ***types***
**description** : The type of this Dataset.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>
### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**requirement**:  $\color{green}{optional}$
**data type** : string <br>
### ***data_access_policy***
**description** : The Data Access Policy that applies to this Dataset.<br>
**requirement**:  $\color{red}{required}$
**data type** : DataAccessPolicy <br>
### ***study***
**description** : The Study associated with this Dataset.<br>
**requirement**:  $\color{red}{required}$
**data type** : Study <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**:  $\color{red}{required}$
**data type** : string <br>

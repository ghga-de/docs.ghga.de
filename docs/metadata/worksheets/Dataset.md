# Dataset

## Description

A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

## Fields

### ***title***<br>
**description** : A title for this Dataset.<br>
**required** : True<br>
**data type** : string <br>
### ***description***<br>
**description** : A description summarizing this Dataset.<br>
**required** : True<br>
**data type** : string <br>
### ***types***<br>
**description** : The type of this Dataset.<br>
**required** : True<br>
**data type** : string <br>
### ***ega_accession***<br>
**description** : The EGA accession ID of an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***data_access_policy***<br>
**description** : The Data Access Policy that applies to this Dataset.<br>
**required** : True<br>
**data type** : DataAccessPolicy <br>
### ***study***<br>
**description** : The Study associated with this Dataset.<br>
**required** : True<br>
**data type** : Study <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

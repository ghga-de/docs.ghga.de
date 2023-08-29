# Study

## Description

Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Fields


**title** : A comprehensive title for the study.
**alias** : title
**data type** : string
**required** : True


**description** : A detailed description (abstract) that describes the goals of this Study.
**alias** : description
**data type** : string
**required** : True


**type** : The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
**alias** : type
**data type** : StudyTypeEnum
**required** : True


**affiliations** : The Institution(s) associated with an entity.
**alias** : affiliations
**data type** : string
**required** : True


**attributes** : Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell,_bulk_etc)
**alias** : attributes
**data type** : Attribute
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

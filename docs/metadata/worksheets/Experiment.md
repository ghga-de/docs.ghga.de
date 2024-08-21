# Experiment

## Description

An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

## Fields

### ***experiment_method***<br>
**description** : The alias of one or more Experiment Methods that are associated with this Experiment.<br>
**required** : True<br>
**data type** : ExperimentMethod <br>
### ***title***<br>
**description** : The title for this Experiment (e.g., GHGAE_PBMC_RNAseq).<br>
**required** : True<br>
**data type** : string <br>
### ***description***<br>
**description** : A detailed description of this Experiment.<br>
**required** : True<br>
**data type** : string <br>
### ***type***<br>
**description** : The type of this Experiment.<br>
**required** : False<br>
**data type** : string <br>
### ***ega_accession***<br>
**description** : The EGA accession of the 'Run' entity (EGAR).<br>
**required** : False<br>
**data type** : string <br>
### ***sample***<br>
**description** : The alias of one or more Samples that are associated with this Experiment.<br>
**required** : True<br>
**data type** : Sample <br>
### ***attributes***<br>
**description** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

# SequencingExperiment

## Description

An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

## Fields

### ***title***<br>
**description** : Name for the experiment (eg: GHGAE_PBMC_RNAseq).<br>
**required** : None<br>
**data type** : string <br>
### ***description***<br>
**description** : A detailed description of the Experiment.<br>
**required** : True<br>
**data type** : string <br>
### ***type***<br>
**description** : The type of sequencing experiment.<br>
**required** : False<br>
**data type** : string <br>
### ***sequencing_protocol***<br>
**description** : The sequencing protocol associated with an entity.<br>
**required** : True<br>
**data type** : SequencingProtocol <br>
### ***library_preparation_protocol***<br>
**description** : The library_preparation Protocol associated with an entity.<br>
**required** : True<br>
**data type** : LibraryPreparationProtocol <br>
### ***attributes***<br>
**description** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

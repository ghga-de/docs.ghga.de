# SequencingExperiment

## Description

An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

## Fields

**title** : Name for the experiment (eg: GHGAE_PBMC_RNAseq).<br>
**required** : None<br>
**data type** : string <br>


**description** : A detailed description of the Experiment.<br>
**required** : True<br>
**data type** : string <br>


**type** : The type of sequencing experiment.<br>
**required** : False<br>
**data type** : string <br>


**sequencing_protocol** : The sequencing protocol associated with an entity.<br>
**required** : True<br>
**data type** : SequencingProtocol <br>


**library_preparation_protocol** : The library_preparation Protocol associated with an entity.<br>
**required** : True<br>
**data type** : LibraryPreparationProtocol <br>


**attributes** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

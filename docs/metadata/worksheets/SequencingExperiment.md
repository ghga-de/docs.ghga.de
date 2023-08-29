# SequencingExperiment

## Description

An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

## Fields


**title** : Name for the experiment (eg: GHGAE_PBMC_RNAseq).
**alias** : title
**data type** : string
**required** : None


**description** : A detailed description of the Experiment.
**alias** : description
**data type** : string
**required** : True


**type** : The type of sequencing experiment.
**alias** : type
**data type** : string
**required** : False


**sequencing_protocol** : The sequencing protocol associated with an entity.
**alias** : sequencing_protocol
**data type** : SequencingProtocol
**required** : True


**library_preparation_protocol** : The library_preparation Protocol associated with an entity.
**alias** : library_preparation_protocol
**data type** : LibraryPreparationProtocol
**required** : True


**attributes** : Key/value pairs corresponding to an entity.
**alias** : attributes
**data type** : Attribute
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

# Experiment

## Description
An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

## Fields
### ***experiment_method***
**description** : The alias of one or more Experiment Methods that are associated with this Experiment.<br>
**required** : True<br>
**importance** : required<br>
**data_type** : ExperimentMethod<br>

### ***title***
**description** : The title for this Experiment (e.g., GHGAE_PBMC_RNAseq).<br>
**required** : True<br>
**importance** : required<br>
**data_type** : string<br>

### ***description***
**description** : A detailed description of this Experiment.<br>
**required** : True<br>
**importance** : required<br>
**data_type** : string<br>

### ***type***
**description** : The type of this Experiment.<br>
**required** : False<br>
**importance** : optional<br>
**data_type** : string<br>

### ***ega_accession***
**description** : The EGA accession of the 'Run' entity (EGAR).<br>
**required** : False<br>
**importance** : optional<br>
**data_type** : string<br>

### ***sample***
**description** : The alias of one or more Samples that are associated with this Experiment.<br>
**required** : True<br>
**importance** : required<br>
**data_type** : Sample<br>

### ***attributes***
**description** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**importance** : optional<br>
**data_type** : Attribute<br>

### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**importance** : required<br>
**data_type** : string<br>


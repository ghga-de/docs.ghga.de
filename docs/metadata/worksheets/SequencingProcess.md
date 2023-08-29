# SequencingProcess

## Description

A sequencing process linking a sample to sequencing output.

## Fields


**title** : The title that describes an entity.
**alias** : title
**data type** : string
**required** : None


**description** : Description of an entity.
**alias** : description
**data type** : string
**required** : True


**name** : The name for an entity.
**alias** : name
**data type** : string
**required** : True


**sequencing_run_id** : Identifier of the sequencing run. Used for batch correction.
**alias** : sequencing_run_id
**data type** : string
**required** : False


**sequencing_lane_id** : Identifier of the sequencing lane. Used for batch correction.
**alias** : sequencing_lane_id
**data type** : string
**required** : False


**sequencing_machine_id** : Identifier of the sequencing machine. Used for batch correction.
**alias** : sequencing_machine_id
**data type** : string
**required** : False


**sequencing_experiment** : The sequencing experiment associated with an entity.
**alias** : sequencing_experiment
**data type** : SequencingExperiment
**required** : True


**index_sequence** : A unique nucleotide sequence that is added to a sample during library_preparation to serve as a unique identifier for the sample.
**alias** : index_sequence
**data type** : string
**required** : False


**lane_number** : The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
**alias** : lane_number
**data type** : string
**required** : False


**sample** : The sample associated with an entity.
**alias** : sample
**data type** : Sample
**required** : True


**attributes** : Key/value pairs corresponding to an entity.
**alias** : attributes
**data type** : Attribute
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

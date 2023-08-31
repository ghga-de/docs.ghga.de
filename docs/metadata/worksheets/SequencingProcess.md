# SequencingProcess

## Description

A sequencing process linking a sample to sequencing output.

## Fields

**title** : The title that describes an entity.<br>
**required** : None<br>
**data type** : string <br>


**description** : Description of an entity.<br>
**required** : True<br>
**data type** : string <br>


**name** : The name for an entity.<br>
**required** : True<br>
**data type** : string <br>


**sequencing_run_id** : Identifier of the sequencing run. Used for batch correction.<br>
**required** : False<br>
**data type** : string <br>


**sequencing_lane_id** : Identifier of the sequencing lane. Used for batch correction.<br>
**required** : False<br>
**data type** : string <br>


**sequencing_machine_id** : Identifier of the sequencing machine. Used for batch correction.<br>
**required** : False<br>
**data type** : string <br>


**sequencing_experiment** : The sequencing experiment associated with an entity.<br>
**required** : True<br>
**data type** : SequencingExperiment <br>


**index_sequence** : A unique nucleotide sequence that is added to a sample during library_preparation to serve as a unique identifier for the sample.<br>
**required** : False<br>
**data type** : string <br>


**lane_number** : The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.<br>
**required** : False<br>
**data type** : string <br>


**sample** : The sample associated with an entity.<br>
**required** : True<br>
**data type** : Sample <br>


**attributes** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

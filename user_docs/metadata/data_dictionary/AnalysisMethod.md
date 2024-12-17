# AnalysisMethod

## Description
An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.

## Fields
### ***name***
**description** : A name identifying this Analysis Method.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***description***
**description** : Description of an entity.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***type***
**description** : The type of an entity. Note: Not to be confused with rdf:type.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***workflow_name***
**description** : The workflow name.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***workflow_version***
**description** : The workflow version.<br>
**requirement**: <span style="color: blue;">recommended</span>

**data type** : string <br>
### ***workflow_repository***
**description** : The workflow repository (e.g., the URL).<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***workflow_doi***
**description** : A digital object identifier for the workflow. Can be a publication or the workflow commit that was used for the Analysis.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***workflow_tasks***
**description** : Tasks performed by the workflow<br>
**requirement**: <span style="color: blue;">recommended</span>

**data type** : string <br>
### ***parameters***
**description** : Key/value pairs where key corresponds to a parameter name and value corresponds to a parameter value (e.g., 'aligner' = 'star_salmon',  'hisat2_build_memory' = '200.GB', 'split_fastq' = 50000000).<br>
**requirement**: <span style="color: blue;">recommended</span>

**data type** : Attribute <br>
### ***software_versions***
**description** : key/value pairs where key corresponds to a software name and value corresponds to a version descriptor (e.g., `salmon` = '1.3.0', `trim-galore` = '0.6.6', `bedtools` = '2.29.2').<br>
**requirement**: <span style="color: blue;">recommended</span>

**data type** : Attribute <br>
### ***attributes***
**description** : One or more attributes that further characterize this Analysis Method.<br>
**requirement**: <span style="color: green;">optional</span>

**data type** : Attribute <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>

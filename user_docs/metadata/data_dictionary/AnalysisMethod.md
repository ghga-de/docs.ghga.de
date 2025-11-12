# AnalysisMethod

## Description
An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.

## Fields
### ***name***
**description** : A name identifying this Analysis Method.<br>
**required** : True<br>
**data type** : string <br>
### ***description***
**description** : Description of an entity.<br>
**required** : True<br>
**data type** : string <br>
### ***type***
**description** : The type of an entity. Note: Not to be confused with rdf:type.<br>
**required** : True<br>
**data type** : string <br>
### ***workflow_name***
**description** : The workflow name.<br>
**required** : True<br>
**data type** : string <br>
### ***workflow_version***
**description** : The workflow version.<br>
**required** : False<br>
**data type** : string <br>
### ***workflow_repository***
**description** : The workflow repository (e.g., the URL).<br>
**required** : True<br>
**data type** : string <br>
### ***workflow_doi***
**description** : A digital object identifier for the workflow. Can be a publication or the workflow commit that was used for the Analysis.<br>
**required** : True<br>
**data type** : string <br>
### ***workflow_tasks***
**description** : Tasks performed by the workflow<br>
**required** : False<br>
**data type** : string <br>
### ***parameters***
**description** : Key/value pairs where key corresponds to a parameter name and value corresponds to a parameter value (e.g., 'aligner' = 'star_salmon',  'hisat2_build_memory' = '200.GB', 'split_fastq' = 50000000).<br>
**required** : False<br>
**data type** : Attribute <br>
### ***software_versions***
**description** : key/value pairs where key corresponds to a software name and value corresponds to a version descriptor (e.g., `salmon` = '1.3.0', `trim-galore` = '0.6.6', `bedtools` = '2.29.2').<br>
**required** : False<br>
**data type** : Attribute <br>
### ***reference_name***
**description** : Name or identifier of the reference, e.g., "hg38", "dbSNP"<br>
**required** : False<br>
**data type** : string <br>
### ***reference_type***
**description** : Type of reference data used<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `GENOME` | `Reference genome sequence` |
| `SNP` | `SNP reference database` |
| `INDEL` | `Indel reference set` |
| `TRANSCRIPTOME` | `Transcript sequences` |
| `HAPLOTYPE` | `Haplotype panels` |
| `VCF` | `Variant call format reference` |
| `BED` | `BED-formatted genomic regions` |
| `REPEATMASKER` | `RepeatMasker annotations` |
| `OTHER` | `Other types of references` |
///

### ***reference_source***
**description** : Source or provider of the reference, e.g., "UCSC", "Ensembl"<br>
**required** : False<br>
**data type** : string <br>
### ***reference_link***
**description** : URL to the reference<br>
**required** : False<br>
**data type** : string <br>
### ***reference_version***
**description** : Version or release identifier of the reference data<br>
**required** : False<br>
**data type** : string <br>
### ***attributes***
**description** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

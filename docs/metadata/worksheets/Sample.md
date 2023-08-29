# Sample

## Description

A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

## Fields


**name** : Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
**alias** : name
**data type** : string
**required** : True


**type** : The type of sample.
**alias** : type
**data type** : SampleTypeEnum
**required** : False


**description** : Short textual description of the sample (How the sample was collected, sample source, Protocol followed for processing the sample etc).
**alias** : description
**data type** : string
**required** : True


**isolation** : Method or device employed for collecting/isolating a biospecimen or a sample.
**alias** : isolation
**data type** : string
**required** : False


**storage** : Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
**alias** : storage
**data type** : string
**required** : False


**biospecimen** : The Biospecimen from which this Sample was prepared from.
**alias** : biospecimen
**data type** : Biospecimen
**required** : False


**condition** : The condition associated with an entity.
**alias** : condition
**data type** : Condition
**required** : True


**xref** : One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
**alias** : xref
**data type** : string
**required** : False


**attributes** : Key/value pairs corresponding to an entity.
**alias** : attributes
**data type** : Attribute
**required** : False


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

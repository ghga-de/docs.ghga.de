# Sample

## Description

A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

## Fields

### ***name***<br>
**description** : Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).<br>
**required** : True<br>
**data type** : string <br>
### ***type***<br>
**description** : The type of sample.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `CF_DNA` | `None` |
| `DEPLETED_RNA` | `None` |
| `DS_DNA_CH_IP` | `None` |
| `FFPE_DNA` | `None` |
| `FFPE_TOTAL_RNA` | `None` |
| `GENOMIC_DNA` | `None` |
| `PCR_PRODUCTS` | `None` |
| `POLY_A_RNA` | `None` |
| `SINGLE_CELL_DNA` | `None` |
| `SINGLE_CELL_RNA` | `None` |
| `SMALL_RNA` | `None` |
| `TOTAL_RNA` | `None` |


</details>

### ***description***<br>
**description** : Short textual description of the sample (How the sample was collected, sample source, Protocol followed for processing the sample etc).<br>
**required** : True<br>
**data type** : string <br>
### ***isolation***<br>
**description** : Method or device employed for collecting/isolating a biospecimen or a sample.<br>
**required** : False<br>
**data type** : string <br>
### ***storage***<br>
**description** : Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).<br>
**required** : False<br>
**data type** : string <br>
### ***biospecimen***<br>
**description** : The Biospecimen from which this Sample was prepared from.<br>
**required** : False<br>
**data type** : Biospecimen <br>
### ***condition***<br>
**description** : The condition associated with an entity.<br>
**required** : True<br>
**data type** : Condition <br>
### ***xref***<br>
**description** : One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.<br>
**required** : False<br>
**data type** : string <br>
### ***attributes***<br>
**description** : Key/value pairs corresponding to an entity.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

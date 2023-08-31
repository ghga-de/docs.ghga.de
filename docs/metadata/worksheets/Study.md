# Study

## Description

Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Fields

**title** : A comprehensive title for the study.<br>
**required** : True<br>
**data type** : string <br>


**description** : A detailed description (abstract) that describes the goals of this Study.<br>
**required** : True<br>
**data type** : string <br>


**type** : The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `CANCER_GENOMICS` | `None` |
| `EPIGENETICS` | `None` |
| `EXOME_SEQUENCING` | `None` |
| `FORENSIC_GENETICS` | `None` |
| `PALEO_GENOMICS` | `None` |
| `GENE_REGULATION_STUDY` | `None` |
| `METAGENOMICS` | `None` |
| `OTHER` | `None` |
| `POOLED_CLONE_SEQUENCING` | `None` |
| `POPULATION_GENOMICS` | `None` |
| `RNASEQ` | `None` |
| `RESEQUENCING` | `None` |
| `SYNTHETIC_GENOMICS` | `None` |
| `TRANSCRIPTOME_ANALYSIS` | `None` |
| `WHOLE_GENOME_SEQUENCING` | `None` |
| `GWAS` | `None` |



**affiliations** : The Institution(s) associated with an entity.<br>
**required** : True<br>
**data type** : string <br>


**attributes** : Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell,_bulk_etc)<br>
**required** : False<br>
**data type** : Attribute <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

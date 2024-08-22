# Study

## Description
A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Fields
### ***title***
**description** : A comprehensive title for this Study.<br>
**required** : True<br>
**data type** : string <br>
### ***description***
**description** : A detailed description (abstract) that describes the goals of this Study.<br>
**required** : True<br>
**data type** : string <br>
### ***types***
**description** : One or more types of this Study (e.g., Cancer Genomics, Epigenetics, Exome Sequencing).<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `CANCER_GENOMICS` | `Cancer genomics` |
| `EPIGENETICS` | `Epigenetics` |
| `EXOME_SEQUENCING` | `Exome sequencing` |
| `FORENSIC_GENETICS` | `Forensic genetics` |
| `PALEO_GENOMICS` | `Paleo genomics` |
| `GENE_REGULATION_STUDY` | `Gene regulation study` |
| `METAGENOMICS` | `Metagenomics` |
| `POOLED_CLONE_SEQUENCING` | `Pooled clone sequencing` |
| `POPULATION_GENOMICS` | `Population genomics` |
| `RNASEQ` | `RNA sequencing` |
| `RESEQUENCING` | `Resequencing` |
| `SYNTHETIC_GENOMICS` | `Synthetic genomics` |
| `TRANSCRIPTOME_ANALYSIS` | `Transcriptome analysis` |
| `WHOLE_GENOME_SEQUENCING` | `Whole genome sequencing` |
| `GWAS` | `Genome Wide Association Study` |
| `RARE_DISEASE` | `Rare disease study` |
| `CANCER` | `Cancer study` |
| `COMMON_DISEASE` | `Common disease study` |
| `NEURODEGENERATIVE_DISEASE` | `Neurodegenerative disease study` |
| `CASE_CONTROL` | `Case-control study` |
| `FAMILY` | `Family study` |
| `HEREDITARY_DISEASE` | `Hereditary disease study` |
| `GENOMICS` | `Genomics study` |
| `EPIGENOMICS` | `Epigenomics study` |
| `TRANSCRIPTOMICS` | `Transcriptomics study` |
| `SINGLE_CELL_SEQUENCING` | `Single-cell sequencing study` |
| `SINGLE_CENTER` | `Single-center study` |
| `MULTI_CENTER` | `Multi-center study` |
| `COHORT` | `Cohort study` |
| `LONGITUDINAL` | `Longitudinal study` |
| `TIME_SERIES` | `Time series study` |
| `INTERVENTIONAL` | `Interventional study` |
| `NON_INTERVENTIONAL` | `Non-interventional study` |
| `COMMUNITY_BASED` | `Community-based study` |
| `OTHER` | `A study type not captured by the above mentioned.` |
///

### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***affiliations***
**description** : The affiliations associated with this Study.<br>
**required** : True<br>
**data type** : string <br>
### ***attributes***
**description** : One or more attributes that further characterize this Study.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

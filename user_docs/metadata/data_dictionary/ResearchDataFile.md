# ResearchDataFile

## Description
A Research Data File is a File that contains raw data originating from an Experiment.

## Fields
### ***format***
**description** : The file format of the Research Data File (e.g., FASTQ, uBAM, FASTA).<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `FASTA` | `FASTA format including NCBI-style IDs.` |
| `FASTQ` | `FASTQ short read format ignoring quality scores.` |
| `UBAM` | `Unaligned BAM file.` |
| `FAST5` | `FAST5 data format for Nanopore.` |
| `RAW` | `Raw file format for mass spectrometry proteomics data.` |
| `D` | `Raw .d files for mass spectrometry proteomics data.` |
| `MZML` | `mzML format for mass spectrometry proteomics data.` |
| `MZDATA` | `mzData for mass spectrometry proteomics data.` |
| `OTHER` | `A file format not captured by the controlled vocabulary.` |
///

### ***technical_replicate***
**description** : An integer to indicate the technical replicate of this File.<br>
**required** : True<br>
**data type** : integer <br>
### ***sequencing_lane_id***
**description** : The identifier of a sequencing lane.<br>
**required** : False<br>
**data type** : string <br>
### ***experiments***
**description** : The aliases of the Experiments that produced this Research Data File.<br>
**required** : True<br>
**data type** : Experiment <br>
### ***name***
**description** : The given filename.<br>
**required** : True<br>
**data type** : string <br>
### ***dataset***
**description** : The Dataset alias associated with this File.<br>
**required** : True<br>
**data type** : Dataset <br>
### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***included_in_submission***
**description** : Whether a File is included in the Submission or not.<br>
**required** : True<br>
**data type** : boolean <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

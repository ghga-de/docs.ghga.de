# SequencingProcessFile

## Description

A SequencingProcessFile is a File that is associated with a SequencingProcess.

## Fields

**sequencing_process** : The SequencingProcess associated with an entity.<br>
**required** : True<br>
**data type** : SequencingProcess <br>


**name** : The given filename.<br>
**required** : True<br>
**data type** : string <br>


**format** : The format of the file: BAM, SAM, CRAM, BAI, etc.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `AGP` | `None` |
| `BAI` | `None` |
| `BAM` | `None` |
| `BCF` | `None` |
| `BED` | `None` |
| `CRAI` | `None` |
| `CRAM` | `None` |
| `CSV` | `None` |
| `FASTA` | `None` |
| `FASTQ` | `None` |
| `GFF` | `None` |
| `HDF5` | `None` |
| `INFO` | `None` |
| `JSON` | `None` |
| `MD` | `None` |
| `OTHER` | `None` |
| `PED` | `None` |
| `SAM` | `None` |
| `SFF` | `None` |
| `SRF` | `None` |
| `TAB` | `None` |
| `TABIX` | `None` |
| `TSV` | `None` |
| `TXT` | `None` |
| `VCF` | `None` |
| `WIG` | `None` |



**size** : The size of a file in bytes.<br>
**required** : True<br>
**data type** : integer <br>


**checksum** : A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.<br>
**required** : True<br>
**data type** : string <br>


**forward_or_reverse** : Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `FORWARD` | `The reads are forward (R1) reads` |
| `REVERSE` | `The reads are reverse (R2) reads` |



**checksum_type** : The type of algorithm used to generate the checksum of a file.<br>
**required** : True<br>
**data type** : string <br>


**dataset** : The Dataset associated with an entity.<br>
**required** : True<br>
**data type** : Dataset <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

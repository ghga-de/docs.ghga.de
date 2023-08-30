# SampleFile

## Description

A SampleFile is a File that is associated with a Sample.

## Fields


**sample** : The sample associated with an entity.
**data type** : Sample
**required** : True

**name** : The given filename.
**data type** : string
**required** : True

**format** : The format of the file: BAM, SAM, CRAM, BAI, etc.
**data type** : Controlled Vocabulary
**required** : True

**size** : The size of a file in bytes.
**data type** : integer
**required** : True

**checksum** : A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
**data type** : string
**required** : True

**forward_or_reverse** : Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
**data type** : Controlled Vocabulary
**required** : False

**checksum_type** : The type of algorithm used to generate the checksum of a file.
**data type** : string
**required** : True

**dataset** : The Dataset associated with an entity.
**data type** : Dataset
**required** : True

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

# AnalysisProcessOutputFile

## Description

A AnalysisProcessOutputFile is a File that is associated as an output file with an AnalysisProcess.

## Fields


**analysis_process** : The AnalysisProcess associated with an entity.
**alias** : analysis_process
**data type** : AnalysisProcess
**required** : True


**name** : The given filename.
**alias** : name
**data type** : string
**required** : True


**format** : The format of the file: BAM, SAM, CRAM, BAI, etc.
**alias** : format
**data type** : FileFormatEnum
**required** : True


**size** : The size of a file in bytes.
**alias** : size
**data type** : integer
**required** : True


**checksum** : A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
**alias** : checksum
**data type** : string
**required** : True


**forward_or_reverse** : Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
**alias** : forward_or_reverse
**data type** : ForwardOrReverseEnum
**required** : False


**checksum_type** : The type of algorithm used to generate the checksum of a file.
**alias** : checksum_type
**data type** : string
**required** : True


**dataset** : The Dataset associated with an entity.
**alias** : dataset
**data type** : Dataset
**required** : True


**alias** : The alias for an entity at the time of submission.
**alias** : alias
**data type** : string
**required** : True

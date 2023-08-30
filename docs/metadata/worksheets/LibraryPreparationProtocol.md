# LibraryPreparationProtocol

## Description

Information about the library_preparation of an sequencing experiment.

## Fields


**description** : Description about how a sequencing library was prepared (eg: Library construction method).
**data type** : string
**required** : True

**library_name** : A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
**data type** : string
**required** : True

**library_layout** : Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
**data type** : Controlled Vocabulary
**required** : True

**library_type** : Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
**data type** : Controlled Vocabulary
**required** : True

**library_selection** : Whether any method was used to select for or against, enrich, or screen the material being sequenced. library_selection method (e.g. random, PCA, cDNA, etc )
**data type** : Controlled Vocabulary
**required** : True

**library_preparation** : The general method for sequencing library_preparation (e.g. KAPA PCR-free).
**data type** : string
**required** : True

**library_preparation_kit_retail_name** : A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
**data type** : Controlled Vocabulary
**required** : False

**library_preparation_kit_manufacturer** : Manufacturer of library_preparation kit
**data type** : string
**required** : False

**primer** : The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
**data type** : Controlled Vocabulary
**required** : False

**end_bias** : The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
**data type** : Controlled Vocabulary
**required** : False

**target_regions** : Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
**data type** : string
**required** : False

**rnaseq_strandedness** : The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
**data type** : Controlled Vocabulary
**required** : False

**attributes** : One or more attributes that further characterizes this library_preparation Protocol.
**data type** : Attribute
**required** : False

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

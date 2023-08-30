# SequencingProtocol

## Description

Information about the sequencing of a sample.

## Fields


**description** : Description about the sequencing Protocol (eg: mRNA-seq, Whole exome long-read sequencing etc).
**data type** : string
**required** : True

**type** : Type of the sequencing Protocol (eg: mRNA-seq, Whole exome long-read sequencing etc).
**data type** : string
**required** : None

**instrument_model** : The name and model of the technology platform used to perform sequencing.
**data type** : Controlled Vocabulary
**required** : True

**sequencing_center** : Center where sample was sequenced.
**data type** : string
**required** : False

**sequencing_read_length** : Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
**data type** : string
**required** : False

**target_coverage** : Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
**data type** : string
**required** : False

**flow_cell_id** : Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
**data type** : string
**required** : False

**flow_cell_type** : Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
**data type** : Controlled Vocabulary
**required** : False

**umi_barcode_read** : The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
**data type** : Controlled Vocabulary
**required** : False

**umi_barcode_offset** : The offset in sequence of the UMI identifying barcode. (E.g. '16').
**data type** : string
**required** : False

**umi_barcode_size** : The size of the UMI identifying barcode (Eg. '10').
**data type** : string
**required** : False

**cell_barcode_read** : The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
**data type** : Controlled Vocabulary
**required** : False

**cell_barcode_offset** : The offset in sequence of the cell identifying barcode. (Eg. '0').
**data type** : string
**required** : False

**cell_barcode_size** : The size of the cell identifying barcode (E.g. '16').
**data type** : string
**required** : False

**sample_barcode_read** : The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
**data type** : Controlled Vocabulary
**required** : False

**attributes** : One or more attributes that further characterizes this Sequencing Protocol.
**data type** : Attribute
**required** : False

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

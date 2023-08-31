# SequencingProtocol

## Description

Information about the sequencing of a sample.

## Fields

### ***description***<br>
**description** : Description about the sequencing Protocol (eg: mRNA-seq, Whole exome long-read sequencing etc).<br>
**required** : True<br>
**data type** : string <br>
### ***type***<br>
**description** : Type of the sequencing Protocol (eg: mRNA-seq, Whole exome long-read sequencing etc).<br>
**required** : None<br>
**data type** : string <br>
### ***instrument_model***<br>
**description** : The name and model of the technology platform used to perform sequencing.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `ILLUMINA_HI_SCAN` | `None` |
| `ILLUMINA_HI_SEQ_1000` | `None` |
| `ILLUMINA_HI_SEQ_1500` | `None` |
| `ILLUMINA_HI_SEQ_2000` | `None` |
| `ILLUMINA_HI_SEQ_2500` | `None` |
| `ILLUMINA_HI_SEQ_3000` | `None` |
| `ILLUMINA_HI_SEQ_4000` | `None` |
| `ILLUMINA_HI_SEQ_X_FIVE` | `None` |
| `ILLUMINA_HI_SEQ_X_TEN` | `None` |
| `ILLUMINA_HI_SEQ_X` | `None` |
| `ILLUMINA_I_SCAN` | `None` |
| `ILLUMINA_I_SEQ_100` | `None` |
| `ILLUMINA_MINI_SEQ` | `None` |
| `ILLUMINA_MI_SEQ` | `None` |
| `ILLUMINA_MI_SEQ_DX` | `None` |
| `ILLUMINA_MI_SEQ_DX_RESEARCH_MODE` | `None` |
| `ILLUMINA_NEXT_SEQ_500` | `None` |
| `ILLUMINA_NEXT_SEQ_550` | `None` |
| `ILLUMINA_NEXT_SEQ_550_DX` | `None` |
| `ILLUMINA_NEXT_SEQ_550_DX_RESEARCH_MODE` | `None` |
| `ILLUMINA_NEXT_SEQ_1000` | `None` |
| `ILLUMINA_NEXT_SEQ_2000` | `None` |
| `ILLUMINA_NOVA_SEQ_6000` | `None` |
| `ILLUMINA_GENOME_ANALYZER` | `None` |
| `ILLUMINA_GENOME_ANALYZER_II` | `None` |
| `ILLUMINA_GENOME_ANALYZER_IIX` | `None` |
| `ILLUMINA_HI_SCAN_SQ` | `None` |
| `PAC_BIO_REVIO` | `None` |
| `PAC_BIO_ONSO` | `None` |
| `PAC_BIO_SEQUEL_IIE` | `None` |
| `PAC_BIO_SEQUEL_II` | `None` |
| `PAC_BIO_SEQUEL` | `None` |
| `PAC_BIO_RS` | `None` |
| `PAC_BIO_RS_II` | `None` |
| `ONT_MIN_ION` | `None` |
| `ONT_GRID_ION` | `None` |
| `ONT_PROMETH_ION` | `None` |
| `DNBSEQ_G50` | `None` |
| `DNBSEQ_T7` | `None` |
| `DNBSEQ_G400` | `None` |
| `DNBSEQ_G400_FAST` | `None` |
| `ULTIMA_UG_100` | `None` |
| `OTHER` | `None` |


</details>

### ***sequencing_center***<br>
**description** : Center where sample was sequenced.<br>
**required** : False<br>
**data type** : string <br>
### ***sequencing_read_length***<br>
**description** : Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process<br>
**required** : False<br>
**data type** : string <br>
### ***target_coverage***<br>
**description** : Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.<br>
**required** : False<br>
**data type** : string <br>
### ***flow_cell_id***<br>
**description** : Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.<br>
**required** : False<br>
**data type** : string <br>
### ***flow_cell_type***<br>
**description** : Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `ILLUMINA_NOVA_SEQ_S2` | `None` |
| `ILLUMINA_NOVA_SEQ_S4` | `None` |
| `PROMETH_ION` | `None` |
| `FLONGLE` | `None` |
| `MIN_ION` | `None` |
| `GRID_ION` | `None` |
| `OTHER` | `None` |


</details>

### ***umi_barcode_read***<br>
**description** : The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `INDEX1` | `None` |
| `INDEX2` | `None` |
| `READ1` | `None` |
| `READ2` | `None` |


</details>

### ***umi_barcode_offset***<br>
**description** : The offset in sequence of the UMI identifying barcode. (E.g. '16').<br>
**required** : False<br>
**data type** : string <br>
### ***umi_barcode_size***<br>
**description** : The size of the UMI identifying barcode (Eg. '10').<br>
**required** : False<br>
**data type** : string <br>
### ***cell_barcode_read***<br>
**description** : The type of read that contains the cell barcode (eg: index1/index2/read1/read2).<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `INDEX1` | `None` |
| `INDEX2` | `None` |
| `READ1` | `None` |
| `READ2` | `None` |


</details>

### ***cell_barcode_offset***<br>
**description** : The offset in sequence of the cell identifying barcode. (Eg. '0').<br>
**required** : False<br>
**data type** : string <br>
### ***cell_barcode_size***<br>
**description** : The size of the cell identifying barcode (E.g. '16').<br>
**required** : False<br>
**data type** : string <br>
### ***sample_barcode_read***<br>
**description** : The type of read that contains the sample barcode (eg: index1/index2/read1/read2).<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `INDEX1` | `None` |
| `INDEX1_AND_INDEX2` | `None` |
| `OTHER` | `None` |


</details>

### ***attributes***<br>
**description** : One or more attributes that further characterizes this Sequencing Protocol.<br>
**required** : False<br>
**data type** : Attribute <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

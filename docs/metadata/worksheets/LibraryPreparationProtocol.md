# LibraryPreparationProtocol

## Description

Information about the library_preparation of an sequencing experiment.

## Fields

**description** : Description about how a sequencing library was prepared (eg: Library construction method).<br>
**required** : True<br>
**data type** : string <br>


**library_name** : A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.<br>
**required** : True<br>
**data type** : string <br>


**library_layout** : Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `SE` | `None` |
| `PE` | `None` |



**library_type** : Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `WGS` | `None` |
| `WXS` | `None` |
| `WCS` | `None` |
| `TOTAL_RNA` | `None` |
| `M_RNA` | `None` |
| `MI_RNA` | `None` |
| `NC_RNA` | `None` |
| `ATAC` | `None` |
| `METHYLATION` | `None` |
| `CHROMOSOME_CONFORMATION_CAPTURE` | `None` |



**library_selection** : Whether any method was used to select for or against, enrich, or screen the material being sequenced. library_selection method (e.g. random, PCA, cDNA, etc )<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `5_METHYLCYTIDINE_ANTIBODY_METHOD` | `None` |
| `CAGE_METHOD` | `None` |
| `C_DNA_METHOD` | `None` |
| `CF_H_METHOD` | `None` |
| `CF_M_METHOD` | `None` |
| `CF_S_METHOD` | `None` |
| `CF_T_METHOD` | `None` |
| `CH_IP_SEQ_METHOD` | `None` |
| `D_NASE_METHOD` | `None` |
| `HMPR_METHOD` | `None` |
| `HYBRID_SELECTION_METHOD` | `None` |
| `INVERSE_R_RNA` | `None` |
| `MBD2_PROTEIN_METHYL_CP_G_BINDING_DOMAIN_METHOD` | `None` |
| `MDA` | `None` |
| `MF_METHOD` | `None` |
| `M_NASE_METHOD` | `None` |
| `MSLL_METHOD` | `None` |
| `OLIGO_D_T` | `None` |
| `PADLOCK_PROBES_CAPTURE_METHOD` | `None` |
| `PCR_METHOD` | `None` |
| `POLY_A` | `None` |
| `RACE_METHOD` | `None` |
| `RANDOM_PCR_METHOD` | `None` |
| `RANDOM_METHOD` | `None` |
| `RT_PCR_METHOD` | `None` |
| `REDUCED_REPRESENTATION_METHOD` | `None` |
| `REPEAT_FRACTIONATION` | `None` |
| `RESTRICTION_DIGEST_METHOD` | `None` |
| `SIZE_FRACTIONATION_METHOD` | `None` |
| `UNSPECIFIED` | `None` |
| `OTHER` | `None` |



**library_preparation** : The general method for sequencing library_preparation (e.g. KAPA PCR-free).<br>
**required** : True<br>
**data type** : string <br>


**library_preparation_kit_retail_name** : A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `10X_GENOMICS_CHROMIUM_SINGLE_CELL_3_V2` | `None` |
| `10X_GENOMICS_CHROMIUM_SINGLE_CELL_3_V3` | `None` |
| `ACCEL_NGS_2_S_PLUS_DNA_LIBRARY_KIT` | `None` |
| `ACCEL_NGS_METHYL_SEQ_DNA` | `None` |
| `AGILENT_STRAND_SPECIFIC_RNA` | `None` |
| `AGILENT_SURE_SELECT_CUSTOM_ENRICHMENT_KIT` | `None` |
| `AGILENT_SURE_SELECT_V3` | `None` |
| `AGILENT_SURE_SELECT_V4` | `None` |
| `AGILENT_SURE_SELECT_V4_UT_RS` | `None` |
| `AGILENT_SURE_SELECT_V5` | `None` |
| `AGILENT_SURE_SELECT_V5_UT_RS` | `None` |
| `AGILENT_SURE_SELECT_V6` | `None` |
| `AGILENT_SURE_SELECT_V6_ONE` | `None` |
| `AGILENT_SURE_SELECT_V6_UT_RS` | `None` |
| `AGILENT_SURE_SELECT_V7` | `None` |
| `AGILENT_SURE_SELECT_WGS` | `None` |
| `AGILENT_SURE_SELECT_XT_HS_HUMAN_ALL_EXON_V7` | `None` |
| `AGILENT_SURE_SELECT_XT_MOUSE_ALL_EXON` | `None` |
| `AGILENT_XT_HS_SURE_SELECT_CLINICAL_RESEARCH_EXOME_V2` | `None` |
| `AVENIO_CT_DNA_KIT` | `None` |
| `IDT_X_GEN_EXOME_RESEARCH_PANEL` | `None` |
| `ILLUMINA_DNA_PCR_FREE` | `None` |
| `ILLUMINA_NEXTERA_DNA_FLEX` | `None` |
| `ILLUMINA_NEXTERA_EXOME_ENRICHMENT_KIT` | `None` |
| `ILLUMINA_STRANDED_M_RNA_PREP_LIGATION` | `None` |
| `ILLUMINA_TRU_SEQ_CH_IP_SAMPLE_PREPARATION_KIT` | `None` |
| `ILLUMINA_TRU_SEQ_CUSTOM_AMPLICON` | `None` |
| `ILLUMINA_TRU_SEQ_DNA` | `None` |
| `ILLUMINA_TRU_SEQ_NANO_DNA` | `None` |
| `ILLUMINA_TRU_SEQ_NANO_DNA_HT` | `None` |
| `ILLUMINA_TRU_SEQ_NANO_DNA_LT` | `None` |
| `ILLUMINA_TRU_SEQ_NANO_FFPE_DNA` | `None` |
| `ILLUMINA_TRU_SEQ_PCR_FREE` | `None` |
| `ILLUMINA_TRU_SEQ_PCR_FREE_DNA` | `None` |
| `ILLUMINA_TRUSEQ_PCR_FREE_METHYL` | `None` |
| `ILLUMINA_TRU_SEQ_RNA` | `None` |
| `ILLUMINA_TRU_SEQ_SMALL_RNA_KIT` | `None` |
| `ILLUMINA_TRU_SEQ_STRANDED_TOTAL_RNA_KIT` | `None` |
| `ILLUMINA_TRU_SEQ_STRANDED_TOTAL_RNA_LIBRARY_PREP_GLOBIN` | `None` |
| `ILLUMINA_TRU_SEQ_STRANDED_TOTAL_RNA_RIBO_MINUS_GOLD` | `None` |
| `ILLUMINA_VAHTS_TOTAL_RNA` | `None` |
| `INFORM_ONCO_PANEL_HG19` | `None` |
| `ION_AMPLI_SEQ_EXOME_KIT` | `None` |
| `KAPA_HIFI_HOT_START_READYMIX` | `None` |
| `KAPA_HYPER_PREP_KIT` | `None` |
| `KAPA_HYPER_PLUS_KIT` | `None` |
| `KAPA_M_RNA_HYPER_PREP_KIT` | `None` |
| `MAGNETIC_METHYLATED_DNA_IMMUNOPRECIPITATION_DIAGNODE` | `None` |
| `NEB_NEXT_CH_IP_SEQ_LIBRARY_PREP_KIT_FOR_ILLUMINA` | `None` |
| `NEB_NEXT_GLOBIN_R_RNA_DEPLETION_KIT_HUMAN_MOUSE_RAT_WITH_BEADS` | `None` |
| `NEB_NEXT_POLY_A_M_RNA_MAGNETIC_ISOLATION_MODULE` | `None` |
| `NEB_NEXT_RNA_ULTRA_II_STRANDED` | `None` |
| `NEBNEXT_ULTRA_DIRECTIONAL_RNA` | `None` |
| `NEB_NEXT_ULTRA_DNA` | `None` |
| `NEB_NEXT_ULTRA_DNA_LIBRARY_PREP_KIT_FOR_ILLUMINA` | `None` |
| `NEB_NEXT_ULTRA_II_DIRECTIONAL_RNA` | `None` |
| `NEB_NEXT_ULTRA_II_DNA_LIBRARY_PREP_KIT_FOR_ILLUMINA` | `None` |
| `NEXTERA_XT_DNA` | `None` |
| `OLIGO_D_T` | `None` |
| `PICO_METHYL_SEQ` | `None` |
| `SMART_SEQ_V4_ULTRA_LOW_INPUT_RNA_KIT` | `None` |
| `SMAR_TER_STRANDED_TOTAL_RNA_SEQ_KIT` | `None` |
| `SMAR_TER_ULTRA_LOW_INPUT_RNA_AND_NEB_NEXT_CH_IP_SEQ` | `None` |
| `SMAR_TER_ULTRA_LOW_INPUT_RNA_V4_AND_NEB_NEXT_CH_IP_SEQ` | `None` |
| `SMAR_TSEQ2_TAG` | `None` |
| `SUPER_SCRIPT_II_RT_BULK` | `None` |
| `SURE_CELL_ATAC_SEQ_LIBRARY_PREP_KIT` | `None` |
| `SURE_SELECT_EUROFINS_ENRICHMENT_CUSTOM_01` | `None` |
| `TAKARA_CLONTECH_SMAR_TER_STRANDED_TOTAL_RNA` | `None` |
| `TAKARA_SMAR_TER_PREP_X_DNA_LIBRARY_KIT_ACTIVE_MOTIF_CUSTOM_INDICES_01` | `None` |
| `TEMPLATE_SWITCHING_RT_ENZYME_MIX_BULK` | `None` |
| `TWIST_HUMAN_CORE_EXOME_PLUS_KIT` | `None` |
| `ULTRALOW_METHYL_SEQ_WITH_TRUE_METHYL_OX_BS_MODULE` | `None` |



**library_preparation_kit_manufacturer** : Manufacturer of library_preparation kit<br>
**required** : False<br>
**data type** : string <br>


**primer** : The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `OLIGO_D_T` | `None` |
| `RANDOM` | `None` |
| `GENE_SPECIFIC` | `None` |
| `OTHER` | `None` |



**end_bias** : The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `3_PRIME_END` | `None` |
| `5_PRIME_END` | `None` |
| `FULL_LENGTH` | `None` |



**target_regions** : Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.<br>
**required** : False<br>
**data type** : string <br>


**rnaseq_strandedness** : The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

| Permissible Values | Description |
| --- | --- |
| `SENSE` | `None` |
| `ANTISENSE` | `None` |
| `BOTH` | `None` |



**attributes** : One or more attributes that further characterizes this library_preparation Protocol.<br>
**required** : False<br>
**data type** : Attribute <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

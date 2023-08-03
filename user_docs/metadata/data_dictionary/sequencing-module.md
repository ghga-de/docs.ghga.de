# **Sequencing Module**

The **Sequencing Module** captures the following entities and properties:

- Sequencing Experiment
    - title
    - type
    - description

- Sequencing Process
    - title
    - name
    - description
    - index sequence
    - lane number
    - sequencing run id
    - sequencing machine id
    - sequencing lane id

- Library Preparation Protocol
    - description
    - library name
    - library preparation kit retail name
    - library preparation kit manufacturer
    - [library layout](#library-layout)
    - [library type](#library-type)
    - [library selection](#library-selection)
    - [library preparation](#library-preparation)
    - [rna strandedness](#library-rna-strandedness)
    - [primer](#library-primer)
    - [end bias](#library-end-bias)
    - rnaseq strandedness
    - target regions

- Sequencing Protocol
    - type
    - description
    - [instrument model](#instrument-model)
    - [flow cell type](#flow-cell-type)
    - flow cell id
    - sequencing center
    - sequencing read length
    - target coverage
    - [umi barcode read](#umi-barcode-read)
    - umi barcode offset
    - umi barcode size
    - [cell barcode read](#cell-barcode-read)
    - cell barcode offset
    - cell barcode size
    - [sample barcode read](#sample-barcode-read)

## **Library Preparation Protocol**

### **library layout**

| Controlled Vocabulary | Ontology Term | Description                                                                                                                                          |
| :-------------------- | :-----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| SE                    | [OBI:0002481] | A cDNA library that is a collection of short tags from only one end of DNA fragments.                                                                |
| PE                    | [OBI:0000722] | A paired-end library is a collection of short paired tags from the two ends of DNA fragments are extracted and covalently linked as ditag constructs |

### **library type**

| Controlled Vocabulary           | Ontology Term  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :------------------------------ | :------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WGS                             | [NCIT:C101294] | A procedure that can determine the DNA sequence for nearly the entire genome of an individual. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| WXS                             | [NCIT:C101295] | A procedure that can determine the DNA sequence for all of the exons in an individual. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| WCS                             | [NCIT:C19653]  | A DNA sequencing method, which involves random sequencing of tiny cloned pieces of the genome, with no foreknowledge of where on a chromosome the piece originally came from. The sequences obtained have a considerable overlap and by using appropriate computer software it is possible to compare sequences and align them to build larger units of genetic information. This sequencing strategy can be automated and leads to rapid sequencing information. [ NCI ]                                                                                                                                                     |
| Total RNA                       | [NCIT:C124261] | A procedure that can determine the nucleotide sequence for all of the RNA transcripts in an individual. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| mRNA                            | [NCIT:C129432] | A procedure that can determine the RNA sequences for all or part of the poly-A tail-containing messenger RNA transcripts in an individual. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| miRNA                           | [NCIT:C156057] | A next-generation or massively parallel high-throughput DNA sequencing-based procedure that can identify and quantify the microRNA sequences present in a biological sample. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ncRNA                           | [NCIT:C172858] | A molecular genetic technique that can determine the RNA sequences for all or part of the population of small and large non-protein coding RNA transcripts in a sample. [ NCI ]                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ATAC                            | [NCIT:C156056] | A molecular genetic technique that isolates and sequences chromosomal regions that are rich in open chromatin. First, nuclei are harvested from a cellular sample. Then a hyperactive Tn5 transposase is added to the nuclei where it excises non-nucleosomal DNA strands and ligates co-administered high-throughput sequencing adapters (tagmentation). The tagged DNA fragments are isolated, amplified by PCR and sequenced. The number of reads for specific region of DNA correlate with increased chromatin accessibility and this method can identify regions of transcription factor and nucleosome binding. [ NCI ] |
| Methylation                     |  [topic:3674]  | Laboratory technique to sequence the methylated regions in DNA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Chromosome conformation capture |  [topic:3940]  | Molecular biology methods used to analyze the spatial organization of chromatin in a cell.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### **library selection**

| Controlled Vocabulary                         |   Ontology Term   | Description                                                                                                                                             |
| :-------------------------------------------- | :---------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5-methylcytidine antibody method              | [GENEPIO:0001941] | Selection of methylated DNA fragments using an antibody raised against 5-methylcytosine or 5-methylcytidine (m5C).                                      |
| CAGE method                                   | [GENEPIO:0001942] | Cap-analysis gene expression.                                                                                                                           |
| cDNA method                                   | [GENEPIO:0001962] | PolyA selection or enrichment for messenger RNA (mRNA) complementary DNA.                                                                               |
| CF-H method                                   | [GENEPIO:0001943] | Cot-filtered highly repetitive genomic DNA                                                                                                              |
| CF-M method                                   | [GENEPIO:0001944] | Cot-filtered moderately repetitive genomic DNA                                                                                                          |
| CF-S method                                   | [GENEPIO:0001945] | Cot-filtered single/low-copy genomic DNA                                                                                                                |
| CF-T method                                   | [GENEPIO:0001946] | Cot-filtered theoretical single-copy genomic DNA                                                                                                        |
| ChIP-Seq method                               | [GENEPIO:0001947] | Chromatin immunoprecipitation                                                                                                                           |
| DNase method                                  | [GENEPIO:0001948] | Deoxyribonuclease (MNase) digestion                                                                                                                     |
| HMPR method                                   | [GENEPIO:0001949] | Hypo-methylated partial restriction digest                                                                                                              |
| Hybrid Selection method                       | [GENEPIO:0001950] | Selection by hybridization in array or solution.                                                                                                        |
| MBD2 protein methyl-CpG binding domain method | [GENEPIO:0001951] | Enrichment by methyl-CpG binding domain.                                                                                                                |
| MDA                                           |   [EFO:0008800]   | Multiple displacement amplification (MDA)                                                                                                               |
| MF method                                     | [GENEPIO:0001952] | Methyl Filtrated                                                                                                                                        |
| MNase method                                  | [GENEPIO:0001953] | Micrococcal Nuclease (MNase) digestion                                                                                                                  |
| MSLL method                                   | [GENEPIO:0001954] | Methylation Spanning Linking Library                                                                                                                    |
| oligo-dT                                      |  [FBcv:0003203]   | Material that has been selected using short sequences of deoxy-thymine nucleotides to affinity purify RNA containing long polyA stretches. [ FBC : CT ] |
| PCR method                                    | [GENEPIO:0001955] | Source material was selected by designed primers.                                                                                                       |
| RACE method                                   | [GENEPIO:0001956] | Rapid Amplification of cDNA Ends.                                                                                                                       |
| RANDOM PCR method                             | [GENEPIO:0001957] | Source material was selected by randomly generated primers.                                                                                             |
| RANDOM method                                 | [GENEPIO:0001958] | Random selection by shearing or other method.                                                                                                           |
| RT-PCR method                                 | [GENEPIO:0001959] | Source material was selected by reverse transcription PCR                                                                                               |
| Reduced Representation method                 | [GENEPIO:0001960] | Reproducible genomic subsets, often generated by restriction fragment size selection, containing a manageable number of loci to facilitate re-sampling. |
| Restriction Digest method                     | [GENEPIO:0001961] | DNA fractionation using restriction enzymes.                                                                                                            |
| Size Fractionation method                     | [GENEPIO:0001963] | Physical selection of size appropriate targets.                                                                                                         |
| unspecified                                   |                   |                                                                                                                                                         |
| other                                         | [GENEPIO:0001964] | Other library enrichment, screening, or selection process.                                                                                              |
| inverse rRNA                                  |                   |                                                                                                                                                         |
| padlock probes capture method                 |                   |                                                                                                                                                         |
| PolyA                                         |                   |                                                                                                                                                         |
| Repeat Fractionation                          |                   |                                                                                                                                                         |

### **library preparation**

| Controlled Vocabulary                                                 | Ontology Term | Description |
| :-------------------------------------------------------------------- | :-----------: | :---------- |
| 10XGenomics                                                           |               |             |
| 10xGenomics Chromium Single Cell 3 v2                                 |               |             |
| Accel-NGS 2S Plus DNA Library Kit                                     |               |             |
| Accel-NGS Methyl-Seq DNA                                              |               |             |
| Agilent Strand-Specific RNA                                           |               |             |
| Agilent SureSelect Custom enrichment Kit                              |               |             |
| Agilent SureSelect V3                                                 |               |             |
| Agilent SureSelect V4                                                 |               |             |
| Agilent SureSelect V4+UTRs                                            |               |             |
| Agilent SureSelect V5                                                 |               |             |
| Agilent SureSelect V5+UTRs                                            |               |             |
| Agilent SureSelect V6                                                 |               |             |
| Agilent SureSelect V6+ONE                                             |               |             |
| Agilent SureSelect V6+UTRs                                            |               |             |
| Agilent SureSelect V7                                                 |               |             |
| Agilent SureSelect WGS                                                |               |             |
| Agilent SureSelect XT HS + Human All Exon V7                          |               |             |
| Agilent SureSelect XT Mouse AllExon                                   |               |             |
| Agilent XT-HS SureSelect Clinical Research Exome V2                   |               |             |
| Avenio ctDNA Kit                                                      |               |             |
| IDT_xGen_Exome_Research_Panel                                         |               |             |
| Illumina Nextera DNA Flex                                             |               |             |
| Illumina Nextera Exome Enrichment Kit                                 |               |             |
| Illumina TruSeq Custom Amplicon                                       |               |             |
| Illumina TruSeq DNA                                                   |               |             |
| Illumina TruSeq Nano DNA                                              |               |             |
| Illumina TruSeq Nano DNA HT                                           |               |             |
| Illumina TruSeq Nano DNA LT                                           |               |             |
| Illumina TruSeq Nano FFPE DNA                                         |               |             |
| Illumina TruSeq PCR-free                                              |               |             |
| Illumina Truseq PCR-free Methyl                                       |               |             |
| Illumina TruSeq PCRFree DNA                                           |               |             |
| Illumina TruSeq RNA                                                   |               |             |
| Illumina TruSeq Small RNA Kit                                         |               |             |
| Illumina TruSeq Stranded Total RNA Kit                                |               |             |
| Illumina VAHTS total RNA                                              |               |             |
| Inform_OncoPanel_hg19                                                 |               |             |
| Ion AmpliSeq Exome Kit                                                |               |             |
| KAPA Hyper Prep Kit                                                   |               |             |
| KAPA HyperPlus Kit                                                    |               |             |
| Kapa mRNA HyperPrep kit                                               |               |             |
| Magnetic Methylated DNA Immunoprecipitation(Diagnode)                 |               |             |
| NEB NEXT Ultra directional RNA                                        |               |             |
| NEB Next Ultra II Directional RNA                                     |               |             |
| NEBNext ChIP-seq library prep kit for Illumina                        |               |             |
| NEBNext RNA Ultra II stranded                                         |               |             |
| NEBNext Ultra DNA                                                     |               |             |
| NEBNext Ultra DNA Library Prep Kit for Illumina                       |               |             |
| NEBNext Ultra II DNA Library Prep Kit for Illumina                    |               |             |
| Nextera XT DNA                                                        |               |             |
| Pico Methyl Seq                                                       |               |             |
| Smart Seq v4 Ultra low Input RNA Kit                                  |               |             |
| SMARTer Stranded Total RNA-Seq Kit                                    |               |             |
| SmarTer Ultra Low Input RNA and NEBNext ChIP-Seq                      |               |             |
| SmarTer Ultra Low Input RNA v4 and NEBNext ChIP-Seq                   |               |             |
| SMARTseq2_tag                                                         |               |             |
| SureSelect eurofins enrichment custom 01                              |               |             |
| Takara Clontech SMARTer Stranded Total RNA                            |               |             |
| Takara SMARTer PrepX DNA Library Kit - Active Motif custom indices 01 |               |             |
| TruSeq ChIP Sample Preparation Kit                                    |               |             |
| TruSeq stranded total RNA- Ribo Minus Gold                            |               |             |
| Twist Human Core Exome Plus Kit                                       |               |             |
| Ultralow_Methyl-Seq_with_TrueMethyl_oxBS_Module                       |               |             |

### **library RNA strandedness**

| Controlled Vocabulary | Ontology Term | Description                                                                                                                    |
| :-------------------- | :-----------: | :----------------------------------------------------------------------------------------------------------------------------- |
| sense                 | [NCIT:C63550] | Having a DNA sequence identical to that of a messenger RNA molecule; the coding strand in double-stranded DNA. [ NCI ]         |
| antisense             | [NCIT:C63551] | Having a DNA sequence complementary to that of a messenger RNA molecule; the non-coding strand in double-stranded DNA. [ NCI ] |
| both                  |               |                                                                                                                                |

### **library primer**

| Controlled Vocabulary | Ontology Term | Description                                                                                                                            |
| :-------------------- | :-----------: | :------------------------------------------------------------------------------------------------------------------------------------- |
| oligo-dT              | [EFO:0010215] | An oligonucleotide primer consisting of thymidine bases only. It is used to target messenger RNA molecules with poly-adenosine 3' end. |
| random                | [EFO:0010216] | An oligonucleotide primer with random sequence.                                                                                        |
| gene-specific         |               |                                                                                                                                        |
| other                 |               |                                                                                                                                        |

### **library end bias**

| Controlled Vocabulary | Ontology Term | Description                                                                                                          |
| :-------------------- | :-----------: | :------------------------------------------------------------------------------------------------------------------- |
| 3'-end                | [EFO:0010189] | When a sequencing method preferentially captures the nucleic acids towards the 3 prime end of the targeted molecule. |
| 5'-end                | [EFO:0010191] | When a sequencing method preferentially captures the nucleic acids towards the 5 prime end of the targeted molecule. |
| full length           |               |                                                                                                                      |
| other                 |               |                                                                                                                      |

## **Sequencing Protocol**

### **instrument model**

| Controlled Vocabulary                  |   Ontology Term   | Description |
| :------------------------------------- | :---------------: | :---------- |
| Illumina HiScan                        |                   |             |
| Illumina HiSeq 1000                    |   [EFO:0004204]   |             |
| Illumina HiSeq 1500                    |   [EFO:0011027]   |             |
| Illumina HiSeq 2000                    |   [EFO:0004203]   |             |
| Illumina HiSeq 2500                    |   [EFO:0008565]   |             |
| Illumina HiSeq 3000                    |   [EFO:0008564]   |             |
| Illumina HiSeq 4000                    |   [EFO:0008563]   |             |
| Illumina HiSeq X Five                  | [GENEPIO:0100112] |             |
| Illumina HiSeq X Ten                   | [GENEPIO:0100113] |             |
| Illumina HiSeq X                       |   [EFO:0008567]   |             |
| Illumina iScan                         |                   |             |
| Illumina iSeq 100                      |   [EFO:0008635]   |             |
| Illumina MiniSeq                       |   [EFO:0008636]   |             |
| Illumina MiSeq                         |   [EFO:0004205]   |             |
| Illumina MiSeqDx                       |                   |             |
| Illumina MiSeqDx (Research Mode)       |                   |             |
| Illumina NextSeq 500                   |   [OBI:0002021]   |             |
| Illumina NextSeq 550                   |   [EFO:0008566]   |             |
| Illumina NextSeq 550Dx                 |                   |             |
| Illumina NextSeq 550Dx (Research Mode) |                   |             |
| Illumina NextSeq 1000                  |   [EFO:0010962]   |             |
| Illumina NextSeq 2000                  |   [EFO:0010963]   |             |
| Illumina NovaSeq 6000                  |   [EFO:0008637]   |             |
| Illumina Genome Analyzer               |   [EFO:0004200]   |             |
| Illumina Genome Analyzer II            |   [EFO:0004201]   |             |
| Illumina Genome Analyzer IIx           |   [EFO:0004202]   |             |
| Illumina HiScanSQ                      | [GENEPIO:0100109] |             |
| PacBio Revio                           |                   |             |
| PacBio Onso                            |                   |             |
| PacBio Sequel IIe                      |                   |             |
| PacBio Sequel II                       |   [OBI:0002633]   |             |
| PacBio Sequel                          |   [EFO:0008631]   |             |
| PacBio RS                              | [GENEPIO:0100131] |             |
| PacBio RS II                           |   [EFO:0008631]   |             |
| ONT MinION                             |   [EFO:0008632]   |             |
| ONT GridION                            |   [OBI:0002751]   |             |
| ONT PromethION                         |   [EFO:0008634]   |             |
| DNBSEQ-G50                             | [GENEPIO:0100150] |             |
| DNBSEQ-T7                              | [GENEPIO:0100147] |             |
| DNBSEQ-G400                            | [GENEPIO:0100148] |             |
| DNBSEQ-G400 FAST                       | [GENEPIO:0100149] |             |
| Ultima UG 100                          |                   |             |
| other                                  |                   |             |

### **flow cell type**

| Controlled Vocabulary | Ontology Term | Description |
| :-------------------- | :-----------: | :---------- |
| Illumina NovaSeq S2   |               |             |
| Illumina NovaSeq S4   |               |             |
| PromethION            |               |             |
| Flongle               |               |             |
| MinION                |               |             |
| GridION               |               |             |
| other                 |               |             |

### **umi barcode read**

| Controlled Vocabulary | Ontology Term | Description |
| :-------------------- | :-----------: | :---------- |
| index1                |               |             |
| index2                |               |             |
| read1                 |               |             |
| read2                 |               |             |

### **cell barcode read**

| Controlled Vocabulary | Ontology Term | Description |
| :-------------------- | :-----------: | :---------- |
| index1                |               |             |
| index2                |               |             |
| read1                 |               |             |
| read2                 |               |             |

### **sample barcode read**

| Controlled Vocabulary | Ontology Term | Description |
| :-------------------- | :-----------: | :---------- |
| index1                |               |             |
| index1 and index2     |               |             |
| other                 |               |             |

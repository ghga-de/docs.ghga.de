# **File Submission**

The **File Submission** captures the following entities and properties:

- File
    - name
    - [format](#file-format)
    - size
    - checksum
    - checksum type
    - [forward or reverse](#forward-or-reverse)

## **format**

| Controlled Vocabulary | Ontology Term | Description                                                                                                                                                                                                                       |
| :-------------------- | :-----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agp                   | [topic:3693]  | AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome).                                                                                                                              |
| bai                   | [topic:3327]  | BAM indexing format                                                                                                                                                                                                               |
| bam                   | [topic:2572]  | BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data. |
| bcf                   | [topic:3020]  | BCF, the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation).                                                                                                        |
| bed                   | [topic:3003]  | Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser.                                                                                                                 |
| crai                  |               | An index file corresponding to a CRAM file                                                                                                                                                                                        |
| cram                  | [topic:3462]  | Reference-based compression of alignment format                                                                                                                                                                                   |
| csv                   | [topic:3752]  | Tabular data represented as comma-separated values in a text file.                                                                                                                                                                |
| fasta                 | [topic:1929]  | FASTA format including NCBI-style IDs.                                                                                                                                                                                            |
| fastq                 | [topic:1930]  | FASTQ short read format ignoring quality scores.                                                                                                                                                                                  |
| gff                   | [topic:2305]  | GFF feature format (of indeterminate version).                                                                                                                                                                                    |
| hdf5                  | [topic:3590]  | HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).                                                                                                            |
| info                  |               | Info files contain unformatted plain text and are often used to document version information, authorship, and copyright information                                                                                               |
| json                  | [topic:3464]  | JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.                                                                                                      |
| md                    |               | Markdown file                                                                                                                                                                                                                     |
| other                 |               |                                                                                                                                                                                                                                   |
| ped                   | [topic:3286]  | The PED file describes individuals and genetic data and is used by the Plink package.                                                                                                                                             |
| sam                   | [topic:2573]  | Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.                                     |
| sff                   | [topic:3284]  | Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing.                                                               |
| srf                   | [topic:3017]  | Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive.                                                                                                                            |
| tab                   | [MS:1000914]  | A file format that has two or more columns of tabular data where each column is separated by a TAB character. [ http://www.w3.org/2002/07/owl#Axiom PSI : MS ]                                                                    |
| tabix                 | [topic:3616]  | TAB-delimited genome position file index format.                                                                                                                                                                                  |
| tsv                   | [topic:3475]  | Tabular data represented as tab-separated values in a text file.                                                                                                                                                                  |
| txt                   | [topic:1964]  | Plain text sequence format (essentially unformatted).                                                                                                                                                                             |
| vcf                   | [topic:3016]  | Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation).                                                                                                                                   |
| wig                   | [topic:3005]  | Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser.                                                                            |


## **forward or reverse**

| Controlled Vocabulary | Ontology Term | Description                      |
| :-------------------- | :-----------: | :------------------------------- |
| forward               |               | The reads are forward (R1) reads |
| reverse               |               | The reads are reverse (R2) reads |

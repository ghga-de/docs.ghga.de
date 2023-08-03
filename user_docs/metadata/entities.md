# **Captured Metadata**

This section provides an overview on what metadata elements are captured with the GHGA Metadata Schema.

A breakdown of each metadata element described in the different entities will provide more insight on what elements are required for the functionality of GHGA, mandatory properties and recommended or optional information that can be provided by the data submitters.

## **Study**

All data deposited at GHGA is subject to a specific study, under which relevant data has been aggregated. A study is an experimental investigation of a particular phenomenon and involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied. A detailed description of a study can guide data requesters to identify the most relevant datasets for their own research.

### **Study metadata properties**

In order to describe a *Study*, data submitters are required to provide information about the study affiliation(s), title, description and type - i.e.: Cancer Genomic, Epigenomics, etc. - of a study.

A study can also be linked to a *Publication*. The *Publication* entity holds the title, id (e.g. DOI of a publication), external reference, abstract, author, year, and journal for a unique publication.

*Publication* is an optional metadata entity. If it is submitted, its properties become mandatory or optional.

## **Sample**

GHGAs *Sample* metadata can be separated into three distinct entities: *Sample*, *Biospecimen* and *Condition*. Both the *Sample* and *Biospecimen* entities provide the data submitter with options to deposit metadata that allows for deeper insight into the characteristics of samples and biospecimen. The *Condition* allows to further define the state of the samples and to group samples within a study accordingly. The following paragraph gives a definition of what a sample, biospecimen or condition is in the context of GHGAs metadata schema.

A *Sample* is defined as a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a biospecimen (isolate or tissue).

A *Biospecimen* is defined in GHGAs metadata as any natural material taken from a biological entity for testing, diagnostics, treatment or research purposes. The *Biospecimen* is linked to the *Individual* entity from which the biospecimen itself has been derived.

A *Condition* describes the state and origin of a sample. It captures actions applied to a sample that were necessary for the specific study in which the sample is used. The *Condition* links the *Sample* to a *Study*.

### **Sample metadata properties**

The *Sample* entity requires data submitters to provide the name and description of a sample, as well as the link to the condition. On top of those mandatory properties, a submitter can provide more information on a sample through the type of isolation of the sample, or how it is stored. Further properties held by the sample entity are type (e.g. genomic DNA, single cell RNA or total RNA) and an external reference.

The *Biospecimen* entity captures only optional information, which reflects the information of the sample entity. These include an alias, a description, isolation, name, type, external ID and storage. Addtionally, this property captures the age at sampling and vital status of the *Biospecimen* donor.

The *Condition* entity captures information about whether and how a sample was treated and its status (case or control, mutant or wildtype). This information is important to uniquely link samples with the same *Condition* within one *Study*. All properties within the *Condition* are required.

## **Individual**

The *Individual* entity within GHGAs Metadata Schema is aimed at capturing relevant information about a sample’s donor. The content of the individual entity is crucial to identify cohorts of interest and gives valuable insight on the target group of an experiment. Data submitters are asked to provide information such as sex and other phenotypic features that help data requesters to identify a cohort of interest.

Individuals can be part of a *Trio*. The *Trio* class is a study design often used in studying genetic conditions in a family. It involves the genetic analysis of three individuals within a family unit, usually a child and their biological parents.

### **Individual metadata properties**
The data submitter is required to provide information about an individual’s sex. Additional information such as phenotypic features, karyotype, geographical region and ethnicity can be submitted.

## **Sequencing Experiment**

Omics data is gathered while carrying out an experiment under certain conditions and procedures. Thus, GHGA aims at collecting as much as possible information about several protocols which gives data requesters an insight on how an experiment was conducted. Data submitters are asked to provide a core set of properties to help make the data deposited at GHGA more rich, but are welcome to provide all the information that has been generated while carrying out the experiment for the dataset. The insights provided by this collection of information helps to make data reusable, one of the main incentives of the FAIR data principles.

### **Sequencing Experiment metadata properties**
*Sequencing Experiment* metadata elements within GHGA’s Metadata Schema spans not only information about the experiment itself but also protocols under which an experiment has been conducted. These include entities for *Sequencing Process*, *Sequencing Protocol* and *Library Preparation Protocol*.

The *Sequencing Experiment* entity is used to group *Sequencing Processes*, *Library Preparation Protocols* and *Sequencing Protocols* within one *Sequencing Experiment*. Via the *Sequencing Process* and *Condition* entities, it is then linked to *Study*, *Sample* and *File*.

The *Sequencing Process* captures the technical parameters that were used to generate output from a *Sample* during a *Sequencing Experiment*.

The *Sequencing Protocol* entity gives a variety of properties that a data submitter can submit. Mandatory properties are the sequencing alias, the description of the sequencing protocol and the provision of the instrument model with which the sequencing was done. Optional properties include the offset, read and size for cell and umi barcodes, flow cell id and type, read length, target coverage, and the type of the used sequencing protocol.

The *Library Preparation Protocol* entity requires a data submitter to provide the following mandatory properties in order to allow reproducible research: library– layout, type, selection, preparation, as well as a name for the protocol, an alias and a thorough description. Optional properties include information about the kit retail name and manufacturer, the library primer, the RNAseq strandedness, target regions, primer end bias and the type of the protocol. If there is a publicly referable url for the protocol, this can also be submitted.


## **File**

At the core of GHGA is the deposition of raw files that have been generated while carrying out an experiment. These files also have to be annotated with metadata, in order to give data requesters more information on what files have been deposited at GHGA by the data submitter. Therefore this metadata will also be used by the user interface of GHGAs data portal to provide not only information on how many files are contained within a dataset, but also information on file size, file formats, checksums and file types.

The files deposited at GHGA, and their metadata, will always link to an experiment entity.

### **File metadata properties**

The *File* entity requires submitters to provide the name, the alias and the format for a file. During the GHGA Catalog phase, the submitter also has to provide information about the file size, checksum and checksum type.

## **Analysis**

GHGA will provide data analysis of the raw files deposited at GHGA by a data submitter. The *Analysis* entity will aim at storing metadata related to the computational analysis of the files that potentially will be run using containers and nf-core pipelines. The information that will be stored in the *Analysis* entity will help to make the analysis data reproducible and reusable with respect to the FAIR data principles.

### **Analysis metadata properties**

The data submitter is required to provide an analysis alias, the aliases for the input and output files, as well as the link to a study and the reference genome or chromosome(s) used for the analysis. Optional properties include a description of the analysis steps and the analysis type.

## **Dataset**

GHGA presents its content to potential data requesters and submitters with the *Dataset* entity, which focuses on sharing functionality by describing the contents at a high level. Each dataset is linked to a *Data Access Policy*, which builds the legal basis for the sharing of data. One dataset has links to *Experiment* and / or *Analysis* entities to bundle all relevant data that makes a dataset by the definition of the GHGA Metadata Schema.

### **Dataset metadata properties**

The *Dataset* entity is aimed at capturing relevant information about a dataset itself. The data submitter can provide a description and a title for the dataset. The main purpose of this entity is to link a dataset to the related study, experiments, samples, analysis, files and data access policies. These links must be provided on the submission of data, either through automatic linking with respect to the *Data Access Committee*, or the data submitter.

All properties captured in the *Dataset* entity are required for the functionality of GHGA and are therefore mandatory. The only exception is the analysis alias, which only needs to be provided if an analysis is to be submitted. A title and description can be indexed by the database in order to make the GHGA Data Portal searchable for a specific dataset. In addition, the links to study, experiment, samples, analysis (if avalaible) and files are necessary to provide a data requester with all relevant data and metadata associated with a dataset. This also ensures reusability in the light of the FAIR Data Principles.

## **Data Access Policy and Committee**

Depositing data at GHGA requires a data submitter to provide a *Data Access Committee (DAC)* and *Data Access Policy (DAP)*. This ensures controlled access to their deposited data and a clear guideline for data requesters to access the data. This includes a defined contact person and a consent-based legal basis for getting access to a dataset.

### **Data Access Policy and Committee metadata properties**

The *DAC* entity bundles necessary information that is required to identify the Data Controller of the deposited data. Therefore a name and description for the *DAC*, and the main contact have to be provided upon submission. The information about a contact includes the email address and the associated affiliation.

A *DAP* is directly linked to the *DAC* and *Dataset* entity, thus providing  the condition under which the data deposited at GHGA can be re-used by a data requester. The submitter must provide an alias, name, description and either the policy text for the *DAP* or the URL where the *DAP* is stored. The *DAP* needs to be linked to the *DAC* and *Dataset*.

To systematically and semantically identify the conditions under which deposited data can be reused, data submitters can optionally provide DUO terms that are used to identify the research purpose under which the data can be requested, e.g. General Research Use (DUO:0000042), research specific restrictions (DUO:0000012).

## **Submission Spreadsheet**

The Submission Spreadsheet for GHGA Archive captures the above-mentioned metadata in an ordered fashion. Data submitters are given a predefined set of properties to describe the data, which they are aiming to deposit. Furthermore in the initial phase, data submitters are asked to provide additional information using key-value pairs. That means, metadata properties which are not yet covered within the metadata catalog for GHGA Archive can be provided with a descriptive property title and the corresponding value. Leaving the freedom to the submitters to provide as much information as is being captured in their study. Since information submitted through the attributes-property is not controllable by GHGA, attributes are considered restricted metadata and will not be visible in the GHGA Catalog.

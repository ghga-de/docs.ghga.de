# **Modules in the GHGA Metadata Model**
we have a modular model because we can

- **Basic Module**: The Basic Module is the fundamental module in the GHGA Metadata Schema. It covers the minimal amount of information that must be included in a successful submission.

- **Sample Module**: Every Basic Module can be linked to one or more Sample Modules. This module contains information relating to the sample that was later sequenced in a sequencing experiment.

- **Phenotype Module**: One Sample Module can have one or more Phenotype Modules. This module can be used when a sample originated from a ‘Biospecimen’ or an ‘Individual’ and thus allows to group several Sample Modules based on the sample origin. In addition, the Phenotype Module captures detailed information about phenotypes or individual demographics.

- **Sequencing Module**: One Sample Module can also be linked to one or more Sequencing Modules. The Sequencing Module captures information about the ‘Sequencing Process’, such as the sequencing and library preparation protocols.

- **Data Use Conditions Module**: The Data Use Conditions Module captures in granular detail what restrictions and use conditions are associated with a Data Access Policy. This section also captures the Data Access Committee that enforces the Data Access Policy requirements.

- **Dataset Module**: The Dataset Module contains the ‘Dataset’ entity, which is a collection of one or more Files from one or more Modules. All Files within the Dataset Module are subject to the Data Access Policy that is captured in the Data Use Conditions Module. One Dataset Module can only be linked to one Data Use Conditions Module.

- **Analysis Module**: A dataset can have one or more Analysis Modules where each Analysis Module links to one or more files as input to the Analysis, one or more files as output to the Analysis, and the ‘Analysis Process’ that captures how the analysis was performed.

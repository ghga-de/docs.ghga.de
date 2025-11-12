# Sample

## Description
A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.

## Fields
### ***individual***
**description** : The alias of the Individual entity from which this Biospecimen or Sample was derived.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : Individual <br>
### ***name***
**description** : A descriptive name of this Sample (e.g., GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1). This property must not include any personally identifiable data.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : string <br>
### ***type***
**description** : The type of the Sample.<br>
**requirement**:  $\color{green}{\textbf{optional}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `CF_DNA` | `Cell Free (CF), circulating DNA was used for sequencing.` |
| `DEPLETED_RNA` | `Depleted RNA was used for sequencing.` |
| `DS_DNA_CHIP` | `Double-stranded DNA was used for sequencing.` |
| `FFPE_DNA` | `Formalin-fixed, paraffin-embedded DNA was used for sequencing.` |
| `FFPE_TOTAL_RNA` | `Formalin-fixed, paraffin-embedded total DNA was used for sequencing.` |
| `GENOMIC_DNA` | `Genomic DNA was used for sequencing.` |
| `PCR_PRODUCTS` | `PCR products were used for sequencing.` |
| `POLY_A_RNA` | `Polyadenylated (polyA) RNA was used for sequencing.` |
| `SINGLE_CELL_DNA` | `DNA originating from single cells was used for sequencing.` |
| `SINGLE_CELL_RNA` | `RNA originating from single cells was used for sequencing.` |
| `SINGLE_CELL_NUCLEI` | `RNA originating from single cell nuclei was used for sequencing.` |
| `SMALL_RNA` | `Small RNA was used for sequencing.` |
| `TOTAL_RNA` | `Total RNA was used for sequencing.` |
///

### ***biological_replicate***
**description** : An integer to indicate the number of a biological replicate.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : integer <br>
### ***description***
**description** : A concise description about the Sample source, the collection method, and the protocol which was followed to process this Sample.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : string <br>
### ***storage***
**description** : Methods by which a Sample is stored.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `REFRIGERATOR` | `The sample / biospecimen was stored in a refrigerator at 2°C to 5°C.` |
| `FREEZER` | `The sample / biospecimen was stored in a freezer at -20°C.` |
| `ULTRA_LOW_FREEZER` | `The sample / biospecimen was stored in a ultra-low freezer at -80°C.` |
| `CRYOGENIC_FREEZER` | `The sample / biospecimen was stored in a cryogenic freezer at -150°C to -190°C.` |
| `NONE` | `The sample / biospecimen was not stored.` |
| `OTHER` | `The sample / biospecimen was stored with a method differing from the available options.` |
| `UNKNOWN` | `The storage method is unknown.` |
///

### ***disease_or_healthy***
**description** : Whether a Condition corresponds to a disease or a healthy state.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `DISEASE` | `Disease state.` |
| `HEALTHY` | `Healthy state.` |
| `NOT_APPLICABLE` | `The distinction is not applicaple.` |
///

### ***case_control_status***
**description** : Whether a Condition corresponds to a treatment or a control.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `CASE` | `The participant is a true case for the phenotype under consideration.` |
| `CONTROL` | `The participant is a true control for the phenotype under consideration.` |
| `OTHER` | `The participant's status is neither case nor control.` |
| `UNKNOWN` | `The participant's status is not known.` |
///

### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**requirement**:  $\color{green}{\textbf{optional}}$<br>
**data type** : string <br>
### ***xref***
**description** : One or more cross-references for this Sample (e.g., this Sample may have an EBI BioSamples accession ID).<br>
**requirement**:  $\color{green}{\textbf{optional}}$<br>
**data type** : string <br>
### ***biospecimen_name***
**description** : A descriptive name of this Biospecimen (e.g., GHGAB_caudate_nucleus_biospecimen). This property must not include any personally identifiable data.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : string <br>
### ***biospecimen_type***
**description** : The type of Biospecimen.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : string <br>
### ***biospecimen_description***
**description** : A concise description about the Biospecimen source, the collection method, and the protocol which was followed to process this Biospecimen.<br>
**requirement**:  $\color{green}{\textbf{optional}}$<br>
**data type** : string <br>
### ***biospecimen_age_at_sampling***
**description** : The age of the Individual at the time of isolating this biospecimen.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `0_TO_5` | `Age between 0 to 5.` |
| `6_TO_10` | `Age between 6 to 10.` |
| `11_TO_15` | `Age between 11 to 15.` |
| `16_TO_20` | `Age between 16 to 20.` |
| `21_TO_25` | `Age between 21 to 25.` |
| `26_TO_30` | `Age between 26 to 30.` |
| `31_TO_35` | `Age between 31 to 35.` |
| `36_TO_40` | `Age between 36 to 40.` |
| `41_TO_45` | `Age between 41 to 45.` |
| `46_TO_50` | `Age between 46 to 50.` |
| `51_TO_55` | `Age between 51 to 55.` |
| `56_TO_60` | `Age between 56 to 60.` |
| `61_TO_65` | `Age between 61 to 65.` |
| `66_TO_70` | `Age between 66 to 70.` |
| `71_TO_75` | `Age between 71 to 75.` |
| `76_TO_80` | `Age between 76 to 80.` |
| `81_OR_OLDER` | `Age above 80.` |
| `UNKNOWN` | `Age range unknown.` |
///

### ***biospecimen_vital_status_at_sampling***
**description** : Vital Status of the Individual at the time of isolating this biospecimen (e.g., alive).<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `ALIVE` | `Showing characteristics of life; displaying signs of life.` |
| `DECEASED` | `The cessation of life.` |
| `UNKNOWN` | `Vital status is unknown.` |
///

### ***biospecimen_tissue_term***
**description** : The tissue this Biospecimen originated from. Should be a term from the BRENDA Tissue Ontology vocabulary (e.g., kidney, blood, melanoma cell).<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : string <br>
### ***biospecimen_tissue_id***
**description** : The corresponding ontology ID for the biospecimen_tissue_term (e.g., BTO:0000671, BTO:0000089, BTO:0000848).<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : string <br>
### ***biospecimen_isolation***
**description** : Method or device employed for collecting/isolating this Biospecimen.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `BLOOD_DRAW` | `Extraction of a blood specimen.` |
| `SURGICAL_REMOVAL` | `Extraction of a sample or part of an organ in a surgical procedure.` |
| `SALIVA_COLLECTION` | `Collection of saliva.` |
| `BUCCAL_SWAB` | `Sample collection using a buccal swab.` |
///

### ***biospecimen_storage***
**description** : Methods by which this Biospecimen is stored.<br>
**requirement**:  $\color{blue}{\textbf{recommended}}$<br>
**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `REFRIGERATOR` | `The sample / biospecimen was stored in a refrigerator at 2°C to 5°C.` |
| `FREEZER` | `The sample / biospecimen was stored in a freezer at -20°C.` |
| `ULTRA_LOW_FREEZER` | `The sample / biospecimen was stored in a ultra-low freezer at -80°C.` |
| `CRYOGENIC_FREEZER` | `The sample / biospecimen was stored in a cryogenic freezer at -150°C to -190°C.` |
| `NONE` | `The sample / biospecimen was not stored.` |
| `OTHER` | `The sample / biospecimen was stored with a method differing from the available options.` |
| `UNKNOWN` | `The storage method is unknown.` |
///

### ***attributes***
**description** : Key/value pairs corresponding to an entity.<br>
**requirement**:  $\color{green}{\textbf{optional}}$<br>
**data type** : Attribute <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**:  $\color{red}{\textbf{required}}$<br> 
**data type** : string <br>

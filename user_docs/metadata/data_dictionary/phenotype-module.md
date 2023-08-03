# **Phenotype Module**

The **Phenotype Module** captures the following entities and properties:

- [**Phenotype Module**](#phenotype-module)
  - [**Biospecimen**](#biospecimen)
    - [**isolation**](#isolation)
    - [**storage**](#storage)
    - [**vital status at sampling**](#vital-status-at-sampling)
    - [**age at sampling**](#age-at-sampling)
  - [**Individual**](#individual)
    - [**sex**](#sex)
    - [**phenotypic feature**](#phenotypic-feature)
    - [**individual karyotype**](#individual-karyotype)
    - [**individual geographical region**](#individual-geographical-region)
    - [**individual ancestry**](#individual-ancestry)


## **Biospecimen**

### **isolation**

| Controlled Vocabulary                               |                                                            Ontology Term                                                             | Description |
| :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------: | :---------- |
| terms from SNOMED CT classification "Removal" terms | https://www.ebi.ac.uk/ols/ontologies/snomed/terms?iri=http%3A%2F%2Fsnomed.info%2Fid%2F118292001&lang=en&viewMode=All&siblings=false# |             |

### **storage**

| Controlled Vocabulary                        | Ontology Term | Description |
| :------------------------------------------- | :-----------: | :---------- |
| Refrigerated storage (2°C to 5°C)            |               |             |
| Freezer storage (-20°C)                      |               |             |
| Ultra-low freezer storage (-80°C)            |               |             |
| Cryogenic freezer storage (-150°C to -190°C) |               |             |

### **vital status at sampling**

| Controlled Vocabulary | Ontology Term | Description                                                        |
| :-------------------- | :-----------: | :----------------------------------------------------------------- |
| alive                 | [NCIT:C37987] | Showing characteristics of life; displaying signs of life. [ NCI ] |
| deceased              | [NCIT:C28554] | The cessation of life. [ NCI ]                                     |
| unknown               |               |                                                                    |

### **age at sampling**

| Controlled Vocabulary | Ontology Term | Description |
| :-------------------- | :-----------: | :---------- |
| 0 - 5                 |               |             |
| 6 - 10                |               |             |
| 11 - 15               |               |             |
| 16 - 20               |               |             |
| 21 - 25               |               |             |
| 26 - 30               |               |             |
| 31 - 35               |               |             |
| 36 - 40               |               |             |
| 41 - 45               |               |             |
| 46 - 50               |               |             |
| 51 - 55               |               |             |
| 56 - 60               |               |             |
| 61 - 65               |               |             |
| 66 - 70               |               |             |
| 71 - 75               |               |             |
| 76 - 80               |               |             |
| 80+                   |               |             |



## **Individual**

### **sex**

| Controlled Vocabulary | Ontology Term | Description                                                                                                                                                                                                                                      |
| :-------------------- | :-----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| female                | [GSSO:011317] | A sex for clinical use value in which stereotypically or statistically "female" values apply to an individual in a given medical context, such as for a procedure, process, algorithm, hormone level, genetic composition, organ inventory, etc. |
| male                  | [GSSO:011318] | A sex for clinical use value in which stereotypically or statistically "male" values apply to an individual in a given medical context, such as for a procedure, process, algorithm, hormone level, genetic composition, organ inventory, etc.   |
| unknown               | [GSSO:011320] | A sex for clinical use value in which the stereotypical or statistical known values do not apply, cannot be determined, or are not sufficient for determination of a another value.                                                              |
| other                 |               |                                                                                                                                                                                                                                                  |

### **phenotypic feature**

| Controlled Vocabulary                |                                                                Ontology Term                                                                | Description |
| :----------------------------------- | :-----------------------------------------------------------------------------------------------------------------------------------------: | :---------- |
| HPO Terms                            |                                                          https://hpo.jax.org/app/                                                           |             |
| EFO Terms for "Material Entity"      | https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FBFO_0000040&lang=en&viewMode=All&siblings=false |             |
| ORDO Codes (includes Orpha and OMIM) |                                                  https://www.ebi.ac.uk/ols/ontologies/ordo                                                  |             |
| SNOMED CT Terms for "Finding"        |     https://www.ebi.ac.uk/ols/ontologies/snomed/terms?iri=http%3A%2F%2Fsnomed.info%2Fid%2F404684003&lang=en&viewMode=All&siblings=false     |             |
| MONDO Terms                          |                                                 https://www.ebi.ac.uk/ols/ontologies/mondo                                                  |             |
| ICD10 Terms                          |                                                          https://www.icd-code.de/                                                           |             |

### **individual karyotype**

| Controlled Vocabulary | Ontology Term | Description                                                                |
| :-------------------- | :-----------: | :------------------------------------------------------------------------- |
| 46,XY                 | [GSSO:009560] | A karyotype in which every cell has one X chromosome and one Y chromosome. |
| 46,XX                 | [GSSO:009558] | A karyotype in which every cell has two X chromosomes.                     |
| other                 |               |                                                                            |

### **individual geographical region**

| Controlled Vocabulary                    |                                                                    Ontology Term                                                                     | Description                                                                                                                                                                                                         |
| :--------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| terms from HANCESTRO terms for "Country" | https://www.ebi.ac.uk/ols/ontologies/hancestro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHANCESTRO_0003&lang=en&viewMode=All&siblings=false | A collective generic term that refers here to a wide variety of dependencies, areas of special sovereignty, uninhabited islands, and other entities in addition to the traditional countries or independent states. |

### **individual ancestry**

| Controlled Vocabulary                              |                                                                    Ontology Term                                                                     | Description                                                                                         |
| :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------- |
| terms from HANCESTRO terms for "Ancestry category" | https://www.ebi.ac.uk/ols/ontologies/hancestro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHANCESTRO_0004&lang=en&viewMode=All&siblings=false | Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data |

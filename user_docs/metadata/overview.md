# The GHGA Metadata Model
## **Glossary**
- **Entity**: An Entity holds characteristics of a real-world object. Example: The Individual entity is described by the information (properties) for sex, year of birth and height.

    - Synonyms: class, table, object

- **Property**: A Property is a single characteristic that can be used in combination with other characteristics to describe a real-world object. Example: The combination of the properties sex, year of birth and height describe the (real-world object) entity Individual.

    - Synonyms: attribute, element, field, slot

- **FAIR**: Findable, Accessible, Interoperable, Reusable

## **Introduction**
The German Human Genome-Phenome Archive (GHGA) provides a nation-wide resource for archiving, accessing and sharing of multi-omics data produced and processed in research and health care initiatives in Germany. GHGA aims to bring these data together and make it easier to find data for secondary use, by adopting and adhering to [FAIR data principles](https://doi.org/10.1038/sdata.2016.18). In order to meet the domain-specific requirements we developed the GHGA Metadata Schema - a schema for representing information pertaining to various aspects of our data.

This documentation serves as the description and reasoning behind the Metadata Model of GHGA, which encapsulates the metadata schema, its technical implementation, and resources to support submission of metadata. The Archive function of GHGA is envisioned to handle a wide variety of omics and research data. The GHGA metadata model aims at facilitating  comprehensive submissions that maximize the amount of collected metadata without creating friction on the submitter side, enabling (reusable) submissions of different types of -omics data into GHGA. This metadata model can satisfy the heterogeneous needs of submitters while maintaining the FAIR principles, interoperability with EGA and facilitating streamlined user journeys.

The schema broadly differentiates the research and administrative aspects of the metadata model - the research metadata aims at maximising the reusability and FAIRness of the data while the administrative metadata The administrative metadata focusses on managing the resources such as creation or acquisition of the data, rights management, and disposition. The research metadata classes include Individual, Biospcimen/Sample, Experiment, Experiment methods, Analysis and Analysis methods. The administrative metadata captures Dataset, Data Access Committee (DAC) and Data Access Policy (DAP), Study/Publication.  Furthermore the model also differentiates between three file types, which are different classes controlled by ranges of file types - namely (i) research data files is which defined as the digital entity resulting from the measurement or sequencing of a sample such as FASTQ, RAW, IDAT (ii) processed data files defined as files that result from an analysis, alignment or computation processing step of a research data file such as BAM, VCF and (iii) supporting files are auxiliary files that provide further structured information about an individual, experiment or analysis such as JSON, TXT.

Furthermore we provide data submitters with a Submission Spreadsheet in order to easily deposit their data within GHGA.
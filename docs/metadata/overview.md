# The GHGA Metadata Model
## **Glossary**
- **Entity**: An Entity holds characteristics of a real-world object. Example: The Individual entity is described by the information (properties) for sex, year of birth and height.

    - Synonyms: class, table, object

- **Property**: A Property is a single characteristic that can be used in combination with other characteristics to describe a real-world object. Example: The combination of the properties sex, year of birth and height describe the (real-world object) entity Individual.

    - Synonyms: attribute, element, field, slot

- **FAIR**: Findable, Accessible, Interoperable, Reusable

## **Introduction**
The German Human Genome-Phenome Archive (GHGA) provides a nation-wide resource for archiving, accessing and sharing of multi-omics data produced and processed in research and health care initiatives in Germany. GHGA aims to bring these data together and make it easier to find data for secondary use, by adopting and adhering to [FAIR data principles](https://doi.org/10.1038/sdata.2016.18). In order to meet the domain-specific requirements we developed the GHGA Metadata Schema - a schema for representing information pertaining to various aspects of our data.

This documentation serves as the description and reasoning behind the Metadata Model of GHGA, which encapsulates the metadata schema, its technical implementation, and resources to support submission of metadata. The Archive function of GHGA is envisioned to handle a wide variety of omics and research data. The Metadata Model is architecturally flexible and can be expanded with specific fields using domain and technology specific modules.


The core of the schema is built such that it can be expanded to accommodate genomic, epigenetic, transcriptomic, clinical, and other forms of medical data. Our initial focus is on research data from the Cancer and Rare Diseases communities. These communities  can benefit greatly by improving the exchange of data and associated metadata.

Furthermore we provide data submitters with a Submission Spreadsheet in order to easily deposit their data within GHGA.

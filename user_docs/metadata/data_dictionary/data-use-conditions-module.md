# **Data Use Conditions Module**

The **Data Use Conditions** captures the following entities and properties:
- [**Data Use Conditions Module**](#data-use-conditions-module)
  - [**Data Access Policy**](#data-access-policy)
    - [**data use permission**](#data-use-permission)
    - [**data use modifier**](#data-use-modifier)

## **Data Access Policy**

### **data use permission**

| Controlled Vocabulary                        | Ontology Term | Description                                                                                                                                                  |
| :------------------------------------------- | :-----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| no restriction                               | [DUO:0000004] | This data use permission indicates there is no restriction on use.                                                                                           |
| general research use                         | [DUO:0000042] | This data use permission indicates that use is allowed for general research use for any research purpose.                                                    |
| health or medical or biomedical research     | [DUO:0000006] | This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry. |
| disease specific research                    | [DUO:0000007] | This data use permission indicates that use is allowed provided it is related to the specified disease.                                                      |
| population origins or ancestry research only | [DUO:0000011] | This data use permission indicates that use of the data is limited to the study of population origins or ancestry.                                           |


### **data use modifier**

| Controlled Vocabulary                              | Ontology Term | Description                                                                                                                                                                                                                                |
| :------------------------------------------------- | :-----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ethics approval required                           | [DUO:0000021] | This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.                                                                                                                                  |
| publication required                               | [DUO:0000019] | This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.                                                                                             |
| user specific restriction                          | [DUO:0000026] | This data use modifier indicates that use is limited to use by approved users.                                                                                                                                                             |
| population origins or ancestry research prohibited | [DUO:0000044] | This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.                                                                                                                               |
| collaboration required                             | [DUO:0000020] | This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s). This could be coupled with a string describing the primary study investigator(s).                                  |
| non-commercial use only                            | [DUO:0000046] | This data use modifier indicates that use of the data is limited to not-for-profit use. This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes.                               |
| not for profit, non commercial use only            | [DUO:0000018] | This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.                                                                                               |
| research specific restrictions                     | [DUO:0000012] | This data use modifier indicates that use is limited to studies of a certain research type.                                                                                                                                                |
| time limit on use                                  | [DUO:0000025] | This data use modifier indicates that use is approved for a specific number of months. This should be coupled with an integer value indicating the number of months.                                                                       |
| not for profit organisation use only               | [DUO:0000045] | This data use modifier indicates that use of the data is limited to not-for-profit organizations.                                                                                                                                          |
| publication moratorium                             | [DUO:0000024] | This data use modifier indicates that requestor agrees not to publish results of studies until a specific date. This should be coupled with a date specified as ISO8601                                                                    |
| genetic studies only                               | [DUO:0000016] | This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)                          |
| return to database or resource                     | [DUO:0000029] | This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.                                                                                                                            |
| clinical care use                                  | [DUO:0000043] | This data use modifier indicates that use is allowed for clinical use and care. Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making. |
| no general methods research                        | [DUO:0000015] | This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).                                                                                                       |
| institution specific restriction                   | [DUO:0000028] | This data use modifier indicates that use is limited to use within an approved institution.                                                                                                                                                |
| geographical restriction                           | [DUO:0000022] | This data use modifier indicates that use is limited to within a specific geographic region. This should be coupled with an ontology term describing the geographical location the restriction applies to.                                 |
| project specific restriction                       | [DUO:0000027] | This data use modifier indicates that use is limited to use within an approved project.                                                                                                                                                    |

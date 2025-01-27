# Data Use and Access Guidelines

## Purpose of this Article

The purpose of this document is to provide <general:Research Data Controller (RDC)|Research Data Controllers> with guidance on how to make decisions about <general:Data Access Request (DAR)> for data they have archived in GHGA. The document identifies ethical and organisational standards regarding operating procedures and decision-making criteria.

Please refer to the [glossary](../glossary.md) for definitions of capitalised terms.

## Introduction

<general:Research Data> such as <general:Omics Data> and other forms of genetic and health data used for scientific research purposes is considered sensitive personal data (special category data under Art. 9 GDPR) due to its informational content and the inherent risk of re-identification associated with it. A whole genome sequence is unique to an individual and so has the potential to differentiate them from the wider population. Moreover, the combination of Omics Data with clinical data in research carries further informational risks for the identifiable person as information about their current and future health could also be attributed to them.

<general:Research Data> that is archived by GHGA for secondary use in scientific research is therefore subject to controlled access (see GHGA [Terms of Use](https://zenodo.org/records/11146387)). As part of data submission to GHGA, the <general:Data Submitters> are therefore advised to implement a review process for <general:Data Access Request (DAR)|Data Access Requests> to ensure compliance with legal and ethical standards, especially to protect individual privacy.

### Review of Data Access Requests

<general:Data Requester (DR)|Data Requesters> wishing to access datasets stored by GHGA must first make a Data Access Request that specifies their proposed research project, its purpose and aims, the responsible persons, and the datasets to be used. These requests are forwarded to the <general:Research Data Controller (RDC)> for the datasets in question (usually identical with the Data Submitter).

Data Access Requests need to be reviewed by a <general:Data Access Committee (DAC) > appointed by the RDC, and not by GHGA. The DAC is responsible for authorising access to the particular datasets that the Research Data Controller has defined. Access is only granted after a positive decision by the DAC has been communicated to GHGA.

The following sequence diagram shows the involved parties and key steps to process a Data Access Request coming in via GHGA.

``` mermaid
sequenceDiagram
 title Simplified Depiction of the Process to Handle Data Access Requests (DAR) using GHGA
   box rgb(204, 229, 255) Data Requester
      participant DR as Data Requester
   end
   box rgb(207, 251, 205) GHGA
      participant GHGA as GHGA Data Portal
   end
   box rgb(255, 229, 204) Data Controller
      participant DAC
      participant RDC as Research Data<br/>Controller
   end
   autonumber
   rect rgb(250, 250, 250)
   note over DR, GHGA: Dataset Identification
   DR ->> GHGA : Dataset Search
   activate GHGA
   GHGA ->> DR : Information on matching dataset
   deactivate GHGA
   end
   rect rgb(250, 250, 250)
   note over DR, GHGA: Negotiation of Data Access Request
   DR ->> GHGA : Files Data Access Request (DAR) <br/> at Data Portal
   activate GHGA
   GHGA ->> DAC : Forwards DAR
   deactivate GHGA
   DAC ->> DR : Requests necessary information and DTA Template
   DR ->> DAC : Information on research project and signed DTA
   DAC ->> RDC : Informs RDC institution on decision <br/>(Acceptance / rejection)
   RDC ->> DR : Informs Data Requester on decision outcome. <br/>If positive sends countersigned DTA
   end
   rect rgb(250, 250, 250)
   note over DR, GHGA: Decision Implementation / Data Download
   RDC ->> GHGA : Informs GHGA on decision on  DAR<br/> (Acceptance / rejection)
   GHGA ->> DR : Informs DR on decision. <br/> If positive provides download link
   end
```

The primary objective of DACs is to oversee the access to Research Data. In contrast to <general:Research Ethics Committee|Research Ethics Committees> (Institutional Review Boards) that assess the full range of ethical issues associated with research projects, a DAC usually evaluates whether the proposed use of data is compatible with the data use conditions, in particular those specified in the data subject’s consent.

We recommend that DACs authorising access to data deposited with GHGA establish a set of documents to serve as a basis for them to operate and reach decisions. These will usually include terms of reference (TOR) and standard operating procedures (SOP) for the DAC as well as a list of criteria for data access decisions and a <general:Data Transfer Agreement (DTA)> template. These documents are further described below.

## Key Documents Recommended for DAC Operation

### DAC Terms of Reference (TOR)

The terms of reference (TOR) define the purpose, set-up, scope, and structure of the DAC. The TOR should be documented and subject to change through a predefined process (see last bullet point of the SOP). For transparency reasons, it should be possible to make the TOR available to other interested parties upon request.

The TOR should specify:

* The role and purpose of the DAC;

* The relationship between the DAC and the Research Data Controller (e.g.: Is the DAC part of the data-controlling institution or has an external DAC been appointed by the Research Data Controller?);

* The particularities of membership (e.g.: How many permanent and associate members does the DAC have? Who are the members and what are their areas of expertise? How are members appointed?);

* A description of the different roles and responsibilities within the DAC, if applicable (e.g.: Chair, Co-chair);

* The period of service of the DAC and/or its members;

* The nature and structure of DAC meetings and communication (as specified in more detail in the SOP);

* The process by which other parties at the Research Data Controller’s institution can be involved, e.g. the data protection officer or the legal department.

### DAC Standard Operating Procedures (SOP)

The standard operating procedures (SOP) define how the routine tasks of the DAC should be carried out and help DAC members to work in an efficient and consistent manner. The SOP should be documented and subject to change through a predefined process (see last bullet point of the SOP). For transparency reasons, it should be possible to make the SOP available to other interested parties upon request.

The SOP should specify:

* The nature and structure of DAC communications, including the means of correspondence (e.g.: emails, virtual meetings, in-person meetings);

* The nature and structure of DAC meetings, including the frequency and approximate length of meetings;

* The nature and structure of DAC correspondence with GHGA and Data Requesters (e.g.: How will the Data Requester be notified of a review outcome?);

* The estimated, or usual, time taken for review decisions;

* The range of possible review outcomes (e.g.: approval, refusal, revision);

* The type of consensus required for review decisions (e.g.: unanimity, majority vote, quorum);

* The process of a criteria-based access review (this is complemented by the LOC below);

* The process for submitting an appeal or a revised application after a negative decision;

* The method of compiling statistics regarding KPIs (e.g.: number of applications approved/rejected, average time taken);

* The method for reviewing decisions in order to improve DAC performance;

* The process of modifying the TOR, SOP, and LOC (e.g.: How can members suggest and make amendments?).

### List of Criteria (LOC) for Data Access Decisions

Each DAC should establish a list of criteria (LOC) that govern the review process and harmonise this process across Data Access Requests. The LOC should be documented and subject to change through a predefined process (see last bullet point of the SOP). For transparency reasons, it should be possible to make the LOC available to other interested parties upon request.

Access requests should be checked against these items:

1. The proposed research has received a positive ethics vote or an ethics approval from a credible source, e.g. a <general:Research Ethics Committee>, if applicable.

2. The identity and institutional affiliation of the Data Requester is verified and the Data Requester and their institutions are trustworthy.

3. There are no data protection concerns that require further attention (see last section on [Data Protection Assessment](#data-protection-assessment)); if such concerns exist or if data is to be transferred across national borders, the DAC should check with the legal department or data protection officer at the Research Data Controller’s institution if data transfer is lawful.

4. There is sufficient evidence that the Data Requester requires access to the particular datasets in order to carry out the proposed research.

5. There is sufficient evidence that the intended methods and procedures are appropriate to address the research question and that the research project is in line with the standards of good scientific practice.

6. There is sufficient evidence that the intended data processing is taking place in a safe setting that prevents unauthorised access.

7. There is sufficient evidence that the intended data use is compatible with the legal and ethical use conditions associated with the particular datasets, especially with the conditions and restrictions outlined in the data subjects’ consent.

8. There is sufficient evidence that appropriate measures are in place to protect the informational rights of data subjects and other parties (such as family members), including the right to erasure, and to manage and minimise potential risks (e.g., of re-identification).

### Data Transfer Agreement (DTA) Template

Before access is granted, the Research Data Controller needs to ensure that the Data Requester is contractually bound to comply with any applicable regulations concerning the exchange of the date. For this a Data Transfer Agreement (DTA) needs to be agreed upon between the Research Data Controller and the Data Requester. The DTA establishes the contractual basis for granting data access/transfer and ensures that all parties involved are aware of their responsibilities and obligations regarding data handling and data protection.

## Data Protection Assessment {#data-protection-assessment}

A critical aspect of processing a Data Access Request is the assessment of the data protection aspects of the proposed sharing. This assessment focuses on compliance with the General Data Protection Regulation (GDPR), especially regarding an appropriate legal basis for data processing. If a Data Processing Impact Assessment (DPIA) has been conducted in accordance with Art. 35 GDPR, care should be taken that the risks that may emerge from data sharing have also been considered. GHGA has performed a risk assessment and produced a related report of the potentials risks that could emerge within the scope of its processing, and these can be made available upon request.   

The aim of the data protection assessment is to ensure that granting data access to a Data Requester aligns with legal standards and that the rights of individuals are respected. Each institution operating a DAC should have a designated data protection officer.

If the request involves complex issues, or is not clearly regulated in terms of data protection, the DAC’s institution, in consultation with the DPO, may create a board to deal with such edge cases and to carry out a documented balancing of legal and other interests together with the DAC.

# Preparation of a GHGA Data Processing Contract for submission to GHGA Archive

**WORK IN PROGRESS**

## Legal Prerequisites

 - [**GHGA Data Processing Contract**](https://www.ghga.de/Downloads/GHGA_Data_Processing_Contract.pdf)

## Introduction

A GHGA Data Processing Contract (DPC) is signed by GHGA Central and an institution that is the Data Controller for Research Data they wish to submit to GHGA. The DPC sets out how GHGA may process the data, the role of the GHGA Data Hubs, and what the Data Submitters’ responsibilities are. 

The DPC creates a controller to processor relationship between the institution and GHGA Central. It has been designed to conform with [Art. 28 GDPR Nr. 3](https://gdpr-info.eu/art-28-gdpr/).

!!! note "Difference between Data Controller and Data Submitter"
   The GDPR defines a Data Controller as the party which "determines the purposes and means of the processing of personal data". Within the context of GHGA, we also use the term Data Submitter to mean the person or institution who are submitting Research Data to the GHGA Data Portal. In many cases, the Data Controller and Data Submitter will be the same but not always; it is therefore important for the Data Submitter to check who the Data Controller is for the Research Data they wish to submit. In this guide, we will use the term Data Controller, as it is the Data Controller who is required to sign the GHGA Data Processing Contract.  

## The GHGA Data Processing Contract

The DPC can be considered to be split into two parts. The first part, comprised of the sections *Premable* to *§7 - Signing*, focuses on the services that GHGA offers to the Data Controller once they have signed a DPC. 

A brief summary of those sections is presented here.

*Premable* - This section introduces GHGA  and the objectives of the project.

*§1 - Definitions* - This section defines the specific GHGA-related terms used within the DPC.

*§2 - Purpose of this Agreement* - This sections describes the services that GHGA offers to Data Controllers. These services are:

1.	The storage of Research Data.

2.	The publication of Non-personal Metadata related to the Research Data.

3.	Quality control checks performed upon the Research Data, Personal Metadata, and Non-personal Metadata.

4.	The storage of any Personal Metadata related to the Research Data.

5.	Additional processing of the Research Data to assess and enhance its quality.

6.	Support to make the Research Data and Personal Metadata accessible to approved Data Requesters. 

7.	GHGA Central shall operate a Helpdesk service through which Service Users including the Data Submitter can receive support.

A fuller description of these services is provided in the DPC.

*§3 - Right to Termination* - This section explains in what circumstances the DPC can be terminated. Both parties have the right to cancel the DPC if the other fails to meet their obligations. The Data Controller can also cancel the DPC whenever they wish.

*§4 - Process for the Termination of the Agreement* - This section sets out the process followed in the event that a DPC is cancelled. The data that has been deposited will either be returned to the Data Controller or destroyed depending on the preferences of the Data Controller. If a DPC is cancelled because the Data Controller is unresponsive, GHGA may be forced to destroy the data has been deposited. 

*§5 - Warranties and Liabilities* - This section describes the warranties and liabilities for each party in the event that there are damages resulting from the submission of data. GHGA commits to making a reasonable effort to retreive any data in the event of a loss, but that this effort is limited to what is reasonable.

*§6 - Final Provisions* - 

*§7 - Signing* - This section is signed by the Data Controller and GHGA Central.

The second part of the DPC are the annexes which focus on the data protection aspects that relate to the different data types which are processed under the DPC. There are sections within the annexes for which the Data Controller must provide information.

*Annex 1 - Research Data Transferred by the the Data Submitter* - In Annex 1, the Data Controller is required to list the data or studies that they wish to submit to GHGA, and to provide information about them. Only data or studies which are listed in Annex 1 can be submitted under the DPC. Any future submission will require another DPC. The Data Controller must also provide contact information about how Data Requesters can make a request to access the data. 

*Annex 2 - GHGA Data Hubs* - In Annex 2 GHGA will list all of the institutions that have been fully onboarded as GHGA Data Hubs and will be acting as sub-processors to GHGA Central. The GHGA Data Hubs will be responsible for storing Research Data and Personal Metadata on behalf of GHGA Central. 

*Annex 3 - Transfer of Research Data and Personal Metadata from the Data Submiter to GHGA Central in Accordance with Article 28 GDPR* - Annex 3 utilises the [Standard Contractual Clauses](https://commission.europa.eu/publications/standard-contractual-clauses-controllers-and-processors-eueea_en) developed by the European Commission for controller-to-processor relationships. The template produced by the European Commission has been adapted to refer to GHGA Central and the GHGA Data Hubs.

*Annex 4 - Persons Authorised to Act* - It is expected that for a majority of submissions to GHGA, an institution will be the Data Controller. It is also expected that the people who represent their institutions, such as a Management Board or Chancellors, are not likely to be responsible for submitting data to GHGA. As such, we require the Data Controller to name people who can act on their behalf.

In order to ensure that only authorised people can access our systems, GHGA utilises Life Science Login (LS Login) to help authenticate users. Therefore, the DPC requires the Data Controller to include the LS Login IDs of the persons authorised to act. The process for obtaining LS Login IDs is described below. 

*Annex 5 - Processing of Non-personal Metadata* -

*Annex 6 - The Processing of Personal Data to fulfil this Agreement* - 

*Annex 7 - Data Protection Framework* - 

## Specification of LS Login IDs for usage in contracts

!!! note "Section currently only relevant for persons authorised to act by Data Controllers and approved Data Requesters"
   It is only needed for data submissions or after approval of data access requests.

To be able to process [Data Processing Contracts](../../glossary/glossary.md#data-processing-contract-dpc) and for others uses, GHGA users need to specify details of their LS Login ID to GHGA. The following information is needed:

| Field | Explanation  |
|---|---|
|Name| The name of the person, e.g. `Doe, Jane` |
|Organisation| Name of the Organisation / Institution that interacts with GHGA, e.g. `Doe Institut`|
|Role| Your role in the Organisation, e.g. `Data Steward` |
|Contact Information| An email adress, e.g. `Jane.doe@doe-institut.xyz`|
|Life Science Login ID / LS ID | The LS ID e.g. as displayed in your user profile on https://profile.aai.lifescience-ri.eu/profile, e.g. `777xc437f725f58660456780tt01d5l999f9b123456@lifescience-ri.eu`. See screenshot below.  |

[Profile page](https://profile.aai.lifescience-ri.eu/profile) on LS Login:

![Ls Login Profile page](../../assets/img/lslogin-lsid.png)

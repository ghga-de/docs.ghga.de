# The Independent Verification Address (IVA) and how it is used in GHGA

## What Is an IVA?

An **<general:Independent Verification Address (IVA)>** is an alternative contact method (usually a mobile number) used to confirm that a GHGA account belongs to the person authorized by an external institution. It is also used to validate decisions on <general:Data Access Request (DAR)|Data Access Requests> that are communicated to GHGA by <general:Research Data Controller Representative (RDCR)|Research Data Controller Representatives>.

IVAs must be able to receive a **one-time verification code**.

## Why Is an IVA Needed?
The IVA is an additional safety measure to enable identification of individuals either when they communicate with GHGA or during communication of the <general:Research Data Controller (RDC)|Research Data Controllers> with <general:Data Requester (DR)|Data Requesters>. 

The IVA is needed during the following processess:

- During the establishment of a <general:Data Processing Contract (DPC)> the Data Submitter must specify IVAs for the Persons authorized to act in the DPC, see [here](../user_stories/submission/dpc_preparation.md#annex-4---persons-authorised-to-act) for further details.
- When filing a <general:Data Access Request (DAR)> to a study listed on GHGA, the <general:Data Requester Representative (DRR)> creates an account on the GHGA Portal. Initial authentication is done via <general:LS ID> but only after an IVA that has been confirmed by the RDC has been registered with that account (and the DAR has been approved) the data can be downloaded.
- Once a <general:Data Access Request (DAR)> is filed in the GHGA Data Portal, it is the duty of the <general:Research Data Controller> to negotiate a suitable <general:Data Transfer Agreement (DTA)> with the Data Requester. It is the duty of the Controller to negotiate with the Requester, GHGA is not involved in the process. During this negotiations it is the duty of the Controller to confirm the IVA provided by the Data Requester in order to ensure the identity of the data requester. 

## Workflow

``` mermaid
sequenceDiagram
 title Simplified Depiction of the Process to Handle Data Access Requests (DAR) using GHGA
   box rgb(204, 229, 255) Data Requester 
      participant DR as Data Requester<br/> (DR)
   end
   box rgb(207, 251, 205) GHGA
      participant GHGA as GHGA Data Portal
   end
   box rgb(255, 229, 204) Data Controller
      participant DAC
      participant RDC as Research Data<br/>Controller Representative
   end
   autonumber
   rect rgb(250, 250, 250)
   note over DR, RDC: Negotiation of Data Access Request
   DR ->> GHGA : Files Data Access Request (DAR) <br/> at Data Portal
   activate GHGA
   GHGA ->> DAC : Forwards DAR
   deactivate GHGA
   DAC ->> DR : Requests necessary information including IVA and forwards DTA Template
   DR ->> DAC : Sends information on research project, IVA and signed DTA
   DAC ->> RDC : Informs RDC institution on decision <br/>(Acceptance / Rejection)
   RDC ->> DR : Informs Data Requester on decision outcome. <br/>If positive sends countersigned DTA
   end
   rect rgb(250, 250, 250)
   note over DR, RDC: Decision Implementation / Data Download
   RDC ->> GHGA : Informs GHGA on decision on  DAR<br/> (Acceptance /Rejection) and confirms the LS ID and IVA of the DR
   GHGA ->> DR : Informs DR on decision of the DAC.
   DR ->> GHGA : Registers IVA with GHGA Data Portal (can also be done before)
   GHGA ->> GHGA : Validates that IVA registered with GHGA matches the IVA provided by RDC
   GHGA ->> DR : If DAC decision is positive and IVA matches, provides download link
   end
```


## General Usage Instructions for the IVA

### How to Verify an IVA

1. **Add IVA** in the Data Portal while logged in.
2. **Receive** a one-time verification code at the IVA.
3. **Enter the code** in the Data Portal.
4. IVA becomes **verified** and ready for use.

Only **verified IVAs** can be used for data access.

### Important Notes

* If you **reset your second factor**, all IVAs require **re-verification**.
* An incorrect or unverified IVA will prevent you from downloading data.
* You can submit a Data Access Request without an IVA, but cannot download data until it’s verified.

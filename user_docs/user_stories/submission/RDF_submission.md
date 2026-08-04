# Research Data File Submission Guide

To submit Research Data Files to GHGA, the [**GHGA-Connector**](https://github.com/ghga-de/ghga-connector) can be utilized to deposit files in an upload box. A Data Steward creates an upload box for each submission with an appropriate volume and can grant access to verified users in the [GHGA Data Portal](https://data.ghga.de/). Files are encrypted and checksums are calculated on the fly. There is no file preparation required before initiating an upload. 

!!! note "Data Processing Contract"

      The signing of a [Data Processing Contract](dpc_preparation.md) has to be finalized before a Data Steward is allowed to generate an upload box and enable the submission of Research Data Files.

To initiate file deposition to an upload box:

- Register in the [GHGA Data Portal](https://data.ghga.de/)
- Verify your account with a valid [IVA](../../other/iva.md)
- Communicate the account (name/email) in your ticket in the [GHGA Helpdesk](mailto:helpdesk@ghga.de)
- Once granted access by a Data Steward, generate an access token for the upload box in your [User Account](https://data.ghga.de/account) by clicking ```Generate Token``` in the "Research Data Upload" tab
- Start the file deposition as outlined in the [**GHGA-Connector Documentation**](user_docs/cli_tools/connector.md)
- Once the submission is complete, click on ```Submit```in the [User Account](https://data.ghga.de/account) to close the box

*Please keep in mind that the file names of the deposited files match the File Name or File Alias in the metadata, so the services can link the entries.*

# Access Data and Download

## Requesting access to a dataset

The GHGA Data Portal enables users to request access to data through the portal. Browse for your dataset of interest and then click on the "Request Access" button. This will direct you to a data access request form. Complete the form with the necessary information and submit it to request access to the dataset. The data access committee will review your request and respond accordingly.

For further details on how to access data, please read the instructions on the [GHGA Data Portal](https://data.staging.ghga.dev/download).

## Create a download token

After a user has been granted access to a dataset, the user initiates a data download by creating a download token in the Data Portal. A single download token can be generated to download either a single or multiple files from a dataset. The download token is then passed on to the CLI tool GHGA Connector to perform the actual download.

1. Navigate to the [GHGA Data Portal](https://data.staging.ghga.dev/download).

2. Visit your profile page to see the datasets you have access to.

    ![Dataset access link](../assets/img/dataset-link.png){ width="500" }

3. Navigate to the dataset list and select your dataset of interest to be downloaded.

    ![Select dataset](../assets/img/dataset-select.png){ width="500" }

4. Fill the form with the necessary information in order to create a download token. Specifying one or multiple file IDs is optional, if not information is provided the entire dataset will be downloaded. A Crypt4GH keypair must be created and the public key must be provided before submitting the form.

    ![Token form](../assets/img/token-form.png){ width="500" }


### Crypt4gh Keys

The download process requires your [Crypt4GH](https://crypt4gh.readthedocs.io/en/latest/) key pair to decrypt the download token. You must specify the key pair corresponding to the public key that was used when the download token was created.

Please paste your *public* Crypt4GH key to the related input box during the token creation.

## Download using GHGA Connector

The GHGA Connector is a command-line tool that facilitates interaction with the file storage infrastructure of GHGA. Data downloading is carried out using the GHGA Connector. You are expected to install the command-line tool and configure it accordingly. To execute a download, you will need the download token and a Crypt4GH key pair.

For further information on how to use the command-line tool, please read the [GHGA Connector](../connector/connector.md) document.
# GHGA Connector

The GHGA Connector is a Python library and command line facilitating interaction with the file storage infrastructure of GHGA. Currently, it provides functionality for downloading and decrypting files, with the capability to interact with the RESTful APIs exposed by the Download Controller Service (https://github.com/ghga-de/download-controller-service).


## Installation and Upgrade

We recommend installing the latest version of the GHGA connector using pip.

Install:
```
pip install ghga-connector==0.3.15
```

Upgrade:
```
pip install --upgrade ghga-connector
```

:warning: Please note that the installation instructions currently require you install a specific version of the GHGA Connector rather than the latest available version. This is due to a current change in how we manage package versions and dependencies. This will be resolved soon and this documentation will be updated.


## Configuration

GHGA Connector requires a connection to the backend service API. Please set the following environment variable correctly in your shell before using the CLI.

```bash
export ghga_connector_wkvs_api_url="https://<CHANGE-HERE>" 
```

For further details about configuration, please visit the [GHGA Connector](https://github.com/ghga-de/ghga-connector) GitHub page.

### Crypt4gh Keys

GHGA Connector requires your [Crypt4GH](https://crypt4gh.readthedocs.io/en/latest/) keys to encrypt downloaded data, ensuring that only you can access it. Please create a pair of Crypt4GH keys if you don't already have one, which you will also need for the process of download token creation.

By default, GHGA Connector looks for the keys at ./key.pub and ./key.sec. You can either place your keys there or use CLI options to specify your key locations.


## Usage

```
Usage: ghga-connector [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  decrypt   Command to decrypt a downloaded file
  download  Command to download files
```

## Download

The _`download`_ command is used to download files. In order to download files, you must provide a *download token*, which contains both the download instructions and authentication details.

### Download Token

GHGA Connector requires a download token to authenticate and process your request against GHGA Central. Each download request is represented by a download token, which should be created via the GHGA Data Portal. For further information on how to create a download token, please read the [Data Access and Download](../download/download.md) document.

### Download Examples

1. To download a dataset:
```bash
ghga-connector download --output-dir <OUTPUT-DIR>
```
Command will prompt:
```
Please paste the complete download token that you copied from the GHGA data portal: 
```
Paste the *download token* you created via the GHGA data portal, and download process will be initiated.

Download command usage:
```
Usage: ghga-connector download [OPTIONS]

  Command to download files

Options:
  --output-dir PATH           The directory to put the downloaded files into.
                              [required]
  --my-public-key-path PATH   The path to a public key from the Crypt4GH key
                              pair that was announced when the download token
                              was created. Defaults to key.pub in the current
                              folder.  [default: ./key.pub]
  --my-private-key-path PATH  The path to a private key from the Crypt4GH key
                              pair that was announced when the download token
                              was created. Defaults to key.sec in the current
                              folder.  [default: ./key.sec]
  --help                      Show this message and exit.
```


## Decrypt

The files you download are encrypted. To decrypt a file, please use the _`decrypt`_ command.

### Decrypt Examples

1. To decrypt files:
```bash
ghga-connector decrypt --input-dir <INPUT-DIR>
```

Decrypt command usage:
```
Usage: ghga-connector decrypt [OPTIONS]

  Command to decrypt a downloaded file

Options:
  --input-dir PATH            Path to the directory containing files that
                              should be decrypted using a common decryption
                              key.  [required]
  --output-dir PATH           Optional path to a directory that the decrypted
                              file should be written to. Defaults to input
                              dir.
  --my-private-key-path PATH  The path to a private key from the Crypt4GH key
                              pair that was announced when the download token
                              was created. Defaults to key.sec in the current
                              folder.  [default: ./key.sec]
  --help                      Show this message and exit.
```



# GHGA Connector

The GHGA Connector is a command line tool and Python library facilitating interaction with the file storage infrastructure of GHGA. It provides fnctionality for file deposition in an upload box or downloading and decrypting files.


## Installation and Upgrade

We recommend installing / upgrading to the latest version of the GHGA connector using pip.

Install or upgrade:
```bash
pip install --upgrade ghga-connector
```


### Crypt4gh Keys

GHGA Connector requires a [Crypt4GH](https://crypt4gh.readthedocs.io/latest/) key pair to download data. Please create a pair of Crypt4GH keys if you don't already have one. The public key is also needed for the creation of the download token through the Data Portal.

By default, GHGA Connector looks for the keys at **./key.pub** and **./key.sec**. You can either place your keys there or use CLI options to specify your key locations.


## Usage

```
 Usage: ghga-connector [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                                                                                                                                                      │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                                                                                                                                                               │
│ --help                        Show this message and exit.                                                                                                                                                                                                                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ batch-upload  Upload a batch of files described by a TSV file.                                                                                                                                                                                                                                                               │
│ ubox          Open an interactive shell to manage an upload box (upload, ls, rm).                                                                                                                                                                                                                                            │
│ download      Wrapper for the async download function                                                                                                                                                                                                                                                                        │
│ decrypt       Command to decrypt a downloaded file                                                                                                                                                                                                                                                                           │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Download

The _`download`_ command is used to download files. In order to download files, you must provide a *download token*, which contains both the download instructions and authentication details.

Download command usage:
```
 Usage: ghga-connector download [OPTIONS]

 Wrapper for the async download function

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --output-dir                               PATH  The directory to put the downloaded files into. [required]                                                                                                                                                                                                               │
│    --my-public-key-path                       PATH  The path to a public key from the Crypt4GH key pair that was announced when the download token was created. Defaults to key.pub in the current folder. [default: ./key.pub]                                                                                              │
│    --my-private-key-path                      PATH  The path to a private key from the Crypt4GH key pair that was announced when the download token was created. Defaults to key.sec in the current folder. [default: ./key.sec]                                                                                             │
│    --passphrase                               TEXT  Passphrase for the encrypted private key. Only needs to be provided if the key is actually encrypted.                                                                                                                                                                    │
│    --debug                  --no-debug              Set this option in order to view traceback for errors. [default: no-debug]                                                                                                                                                                                               │
│    --overwrite              --no-overwrite          Set to true to overwrite already existing files in the output directory. [default: no-overwrite]                                                                                                                                                                         │
│    --help                                           Show this message and exit.                                                                                                                                                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Download Token

GHGA Connector requires a download token to authenticate and process your request against GHGA Central. Each download request - which may comprise multiple files - is represented by a download token, which should be created via the GHGA Data Portal. For further information on how to create a download token, please refer to the [Data Download](../user_stories/accessing_data.md) documentation.

### Download Examples

1. To download a dataset:
```bash
ghga-connector download --output-dir <OUTPUT-DIR>
```
You will then be asked to provide the download token:
```
Please paste the complete download token that you copied from the GHGA data portal: 
```
Paste the *download token* you created via the GHGA data portal and the download process will be initiated.



## Decrypt

The files you download are encrypted. To decrypt a file, please use the _`decrypt`_ command.

Decrypt command usage:
```
 Usage: ghga-connector decrypt [OPTIONS]

 Command to decrypt a downloaded file

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --input-dir                            PATH  Path to the directory containing files that should be decrypted using a common decryption key. [required]                                                                                                                                                                    │
│    --output-dir                           PATH  Optional path to a directory that the decrypted file should be written to. Defaults to input dir.                                                                                                                                                                            │
│    --my-private-key-path                  PATH  The path to a private key from the Crypt4GH key pair that was announced when the download token was created. Defaults to key.sec in the current folder. [default: ./key.sec]                                                                                                 │
│    --passphrase                           TEXT  Passphrase for the encrypted private key. Only needs to be provided if the key is actually encrypted.                                                                                                                                                                        │
│    --debug                  --no-debug          Set this option in order to view traceback for errors. [default: no-debug]                                                                                                                                                                                                   │
│    --help                                       Show this message and exit.                                                                                                                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Decrypt Examples

1. To decrypt files:
```bash
ghga-connector decrypt --input-dir <INPUT-DIR>
```

## File Upload


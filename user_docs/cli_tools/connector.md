# GHGA Connector

The GHGA Connector is a command line tool and Python library facilitating interaction with the file storage infrastructure of GHGA. It provides functionality for file deposition to an upload box or downloading and decrypting files.


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

To submit Research Data Files as part of a [GHGA Submission](../user_stories/submission/submitter_guide.md), the GHGA-Connector can deposit files into an upload box. Upload boxes are created on request by Data Stewards and assigned to verified accounts in the GHGA Data Portal. Once granted access to an upload box, an access token can be generated in the [User Account](https://data.ghga.de/account).

There are two ways to deposit files in an upload box.

### Batch-upload

 The first one is to create a filesToUpload.tsv consisting of the file paths in the first column and the file aliases in the second. The file aliases should correspond to the related entries in the metadata.

*filesToUpload.tsv:*

```
my_data/example-data/SEQ_FILE_A_R1.fastq.gz SEQ_FILE_A
my_data/example-data/SEQ_FILE_A_R2.fastq.gz SEQ_FILE_B
...

```
The upload can be initialized via ```ghga-connector batch-upload```. Once executed, the access token for the upload box from the Data Portal can be pasted to start the upload:

```
Usage: ghga-connector batch-upload [OPTIONS]

 Upload a batch of files described by a TSV file.

 Files already present in the upload box are skipped, so the command can be re-run
 to resume an interrupted batch. Files that fail to upload are retried automatically.

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --tsv                                    PATH     Path to a TSV file describing the files to upload. The first column must contain the file path and the second column the file alias. Relative file paths can only be used if this command is run from same directory. Prefer to use absolute paths. [required]          │
│    --my-public-key-path                     PATH     The path to a public key from the key pair that was announced in the metadata. Defaults to key.pub in the current folder. [default: ./key.pub]                                                                                                                          │
│    --my-private-key-path                    PATH     The path to a private key from the key pair that will be used to encrypt the crypt4gh envelope. Defaults to key.sec in the current folder. [default: ./key.sec]                                                                                                         │
│    --passphrase                             TEXT     Passphrase for the encrypted private key. Only needs to be provided if the key is actually encrypted.                                                                                                                                                                   │
│    --max-retries                            INTEGER  Maximum number of automatic retries for files that fail to upload. [default: 3]                                                                                                                                                                                         │
│    --dry-run                --no-dry-run             List the files that would be uploaded (after skipping any already in the upload box) without uploading anything. [default: no-dry-run]                                                                                                                                  │
│    --shorten-names                                   Shorten very long file aliases in the output, keeping the start and end (e.g. 'sample-001 … -run5.bam'). Full aliases are shown by default. This is only for improving readability and does not affect how data is sent to GHGA.                                        │
│    --debug                  --no-debug               Set this option in order to view traceback for errors. [default: no-debug]                                                                                                                                                                                              │
│    --help                                            Show this message and exit.                                                                                                                                                                                                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Batch-upload example

Specify the filesToUpload.tsv, the C4GH keypair and optionally set a number of retries in case the upload fails:

```ghga-connector batch-upload --tsv filesToUpload.tsv --my-public-key-path key.pub --my-private-key-path key.sec --max-retries 3```


### Ubox upload

Alternatively, the files can be uploaded directly via the ```ubox``` command, which allows direct access to the upload box to submit or remove files:

```
 Usage: ghga-connector ubox [OPTIONS]

 Open an interactive shell to manage an upload box (upload, ls, rm).

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --my-public-key-path                   PATH  The path to a public key from the key pair that was announced in the metadata. Defaults to key.pub in the current folder. [default: ./key.pub]                                                                                                                                  │
│ --my-private-key-path                  PATH  The path to a private key from the key pair that will be used to encrypt the crypt4gh envelope. Defaults to key.sec in the current folder. [default: ./key.sec]                                                                                                                 │
│ --passphrase                           TEXT  Passphrase for the encrypted private key. Only needs to be provided if the key is actually encrypted.                                                                                                                                                                           │
│ --debug                  --no-debug          Set this option in order to view traceback for errors. [default: no-debug]                                                                                                                                                                                                      │
│ --help                                       Show this message and exit.                                                                                                                                                                                                                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Ubox example

Specify the C4GH keypair and connect to the ubox

```ghga-connector ubox --my-public-key-path key.pub --my-private-key-path key.sec```

After pasting the access token, the ghga-connector connects to the upload box and provides functionality to modify it:

```
Available commands:
  upload PATH [PATH ...]      Upload one or more files/globs, using each local
                              file name as its alias.
  upload --alias ALIAS PATH   Upload a single file under the given alias.
  ls [--show-deleted]         List the contents of the upload box. Deleted
                              files are hidden unless --show-deleted is given.
  rm ALIAS                    Delete the file with the given alias from the box.
  help                        Show this help text.
  exit | quit                 Leave the shell (Ctrl+D also works).
```

#### Ubox upload example

Navigate to the folder that contains your files and connect to the ubox. Then run:

 ```upload MyFile.fastq.gz``` or in batch via wildcard ```upload *fastq.gz``` to upload all files in the current folder.

 Optionally, ``--alias`` can be used to upload a file under an alias. If none is specified, the file name is used as alias. The file aliases should correspond to the related entries in the metadata.

Once the upload concludes, the upload box can be closed by clicking ```Submit``` in the [User Account](https://data.ghga.de/account). The files will then be re-encrypted and archived by a Data Steward.
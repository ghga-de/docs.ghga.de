# GHGA Validator

GHGA Validator is a command line utility to validate metadata w.r.t. its compliance to the GHGA Metadata Model. It takes metadata encoded in JSON of YAML format and produces a validation report in JSON format.

There is a possibility to indicate the root class for validation. In case it was not specified, it will induced from the schema.

Currently the following validation types are included in GHGA Validator:

- Structural validation of a JSON object
- Validation of the non inline references
- Uniqueness of the fields defined as identifier/unique key


## Installation and Upgrade

We recommend installing the latest version of the GHGA transpiler using pip.

Install:
```
pip install ghga-validator
```

Upgrade:
```
pip install --upgrade ghga-validator
```

## Usage

```
Usage: ghga-validator [OPTIONS]


Options:
  -s, --schema PATH               Path to metadata schema (modelled using
                                  LinkML)  [required]
  -i, --input FILE                Path to submission file in JSON format to be
                                  validated  [required]
  -r, --report FILE               Path to resulting validation report
                                  [required]
  --target-class TEXT             The root class name
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Examples


1. To validate `/work_directory/data.json` against the schema `/work_directory/schema.yaml` and store the validation report into the file `/work_directory/report.json`:
```
ghga-validator --input /work_directory/schema.json --schema /work_directory/schema.yaml --report /work_directory/report.json
ghga-validator -i /work_directory/schema.json -s /work_directory/schema.yaml -r /work_directory/report.json
```
2. To validate with providing the root class `Submission` for validation:
```
ghga-validator --input /work_directory/schema.json --schema /work_directory/schema.yaml --report /work_directory/report.json --target-class Submission
```
3. To display help message:
```
ghga-validator --help
```

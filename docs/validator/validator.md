# GHGA Validator

GHGA Validator is a command line utility to validate metadata w.r.t. its compliance to the GHGA Metadata Model. It takes metadata encoded in JSON or YAML format and produces a validation report in JSON format.

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

:bulb: Example data can be downloaded from https://github.com/ghga-de/example-data/

:bulb: The latest version of the GHGA metadata schema (`submission.yaml`) can be downloaded from https://github.com/ghga-de/ghga-metadata-schema/releases/latest

1. To validate `data.json` against the schema `submission.yaml` and store the validation report into the file `report.json`:
```
ghga-validator --input schema.json --schema submission.yaml --report report.json
```
2. To validate with providing the root class `Submission` for validation:
```
ghga-validator --input schema.json --schema submission.yaml --report report.json --target-class Submission
```
3. To display help message:
```
ghga-validator --help
```

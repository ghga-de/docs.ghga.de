# GHGA Transpiler
The GHGA Transpiler is a Python library and command line utility to transpile the official GHGA metadata XLSX workbooks to JSON. Please note that the GHGA Transpiler does not validate that the provided metadata is compliant with the [GHGA Metadata Schema](https://github.com/ghga-de/ghga-metadata-schema). This can be achieved by running the [GHGA Validator](https://github.com/ghga-de/ghga-validator/) on the JSON data generated by the GHGA Transpiler.


## Installation and Upgrade

We recommend installing the latest version of the GHGA transpiler using pip.

Install:
```
pip install ghga-transpiler
```

Upgrade:
```
pip install --upgrade ghga-transpiler
```

## Usage

```
Usage: ghga-transpiler [OPTIONS] SPREAD_SHEET [OUTPUT_FILE]


Arguments:
  SPREAD_SHEET   The path to input file (XLSX)  [required]
  [OUTPUT_FILE]  The path to output file (JSON).

Options:
  -f, --force                     Override output file if it exists.
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Examples

:bulb: Example data can be downloaded from https://github.com/ghga-de/example-data/

1. To transpile `metadata.xlsx`:
```
ghga-transpiler metadata.xlsx metadata.json
```
2. To use the same output name (`/work_directory/output.json`) in another run:
```
ghga-transpiler --force another_metadata.xlsx another_metadata.json
ghga-transpiler -f another_metadata.xlsx another_metadata.json
```
3. To display help message:
```
ghga-transpiler --help
```

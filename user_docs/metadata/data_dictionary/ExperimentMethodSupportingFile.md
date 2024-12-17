# ExperimentMethodSupportingFile

## Description
An Experiment Method Supporting File is a File that contains additional information relevant for the Experiment Method, such as (unstructured) protocols.

## Fields
### ***format***
**description** : The file format of the Supporting File (e.g., TXT, JSON).<br>
**requirement**: <span style="color: red;">required</span>

**data type** : Controlled Vocabulary <br>

/// details | Permissible Values
| Permissible Values | Description |
| --- | --- |
| `CSV` | `Tabular data represented as comma-separated values in a text file.` |
| `JSON` | `JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.` |
| `PED` | `The PED file describes individuals and genetic data and is used by the Plink package.` |
| `TSV` | `Tabular data represented as tab-separated values in a text file.` |
| `TXT` | `Textual format. Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual).` |
| `YAML` | `YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.` |
| `OTHER` | `A file format not captured by the controlled vocabulary.` |
///

### ***experiment_method***
**description** : The Experiment Method associated with an entity.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : ExperimentMethod <br>
### ***name***
**description** : The given filename.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***dataset***
**description** : The Dataset alias associated with this File.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : Dataset <br>
### ***ega_accession***
**description** : The EGA accession ID of an entity.<br>
**requirement**: <span style="color: green;">optional</span>

**data type** : string <br>
### ***included_in_submission***
**description** : Whether a File is included in the Submission or not.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : boolean <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>

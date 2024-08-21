# AnalysisMethodSupportingFile

## Description

An Analysis Method Supporting File is a File that contains additional information relevant for the Analysis Method, such as (unstructured) protocols or task descriptions.

## Fields

### ***format***<br>
**description** : The file format of the Supporting File (e.g., TXT, JSON).<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `CSV` | `Tabular data represented as comma-separated values in a text file.` |
| `JSON` | `JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.` |
| `PED` | `The PED file describes individuals and genetic data and is used by the Plink package.` |
| `TSV` | `Tabular data represented as tab-separated values in a text file.` |
| `TXT` | `Textual format. Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual).` |
| `YAML` | `YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.` |
| `OTHER` | `A file format not captured by the controlled vocabulary.` |
 

</details>

### ***analysis_method***<br>
**description** : The Analysis Process associated with an entity.<br>
**required** : True<br>
**data type** : AnalysisMethod <br>
### ***name***<br>
**description** : The given filename.<br>
**required** : True<br>
**data type** : string <br>
### ***dataset***<br>
**description** : The Dataset alias associated with this File.<br>
**required** : True<br>
**data type** : Dataset <br>
### ***ega_accession***<br>
**description** : The EGA accession ID of an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***included_in_submission***<br>
**description** : Whether a File is included in the Submission or not.<br>
**required** : True<br>
**data type** : boolean <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

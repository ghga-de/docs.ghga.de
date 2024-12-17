# Analysis

## Description
An Analysis is a data transformation that transforms input data to output data.

## Fields
### ***analysis_method***
**description** : The alias of the Analysis Method that is associated with this Analysis.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : AnalysisMethod <br>
### ***title***
**description** : The title that describes an entity.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>
### ***description***
**description** : A description summarizing how this Analysis was carried out (e.g., description of computational tools, pipelines, workflows).<br>
**requirement**: <span style="color: green;">optional</span>

**data type** : string <br>
### ***type***
**description** : The type of this Analysis.<br>
**requirement**: <span style="color: green;">optional</span>

**data type** : string <br>
### ***ega_accession***
**description** : The EGA accession of the 'Analysis' entity (EGAZ).<br>
**requirement**: <span style="color: green;">optional</span>

**data type** : string <br>
### ***research_data_files***
**description** : One or more aliases of the Research Data Files that this Analysis used as input to create Process Data Files.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : ResearchDataFile <br>
### ***alias***
**description** : The alias for an entity at the time of submission.<br>
**requirement**: <span style="color: red;">required</span>

**data type** : string <br>

# Analysis

## Description

An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.

## Fields

**title** : The title that describes an entity.<br>
**required** : None<br>
**data type** : string <br>


**description** : Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).<br>
**required** : False<br>
**data type** : string <br>


**type** : The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)<br>
**required** : False<br>
**data type** : string <br>


**reference_genome** : A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).<br>
**required** : True<br>
**data type** : string <br>


**reference_chromosome** : The reference chromosome used for this Analysis.<br>
**required** : True<br>
**data type** : string <br>


**alias** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

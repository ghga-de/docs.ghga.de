# Analysis

## Description

An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.

## Fields


**title** : The title that describes an entity.
**data type** : string
**required** : None

**description** : Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
**data type** : string
**required** : False

**type** : The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
**data type** : string
**required** : False

**reference_genome** : A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
**data type** : string
**required** : True

**reference_chromosome** : The reference chromosome used for this Analysis.
**data type** : string
**required** : True

**alias** : The alias for an entity at the time of submission.
**data type** : string
**required** : True

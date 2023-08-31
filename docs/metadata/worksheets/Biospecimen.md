# Biospecimen

## Description

A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

## Fields

### ***name***<br>
**description** : The name for an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***type***<br>
**description** : The type of Biospecimen.<br>
**required** : False<br>
**data type** : string <br>
### ***description***<br>
**description** : Description of an entity.<br>
**required** : False<br>
**data type** : string <br>
### ***isolation***<br>
**description** : Method or device employed for collecting/isolating a biospecimen or a sample.<br>
**required** : False<br>
**data type** : string <br>
### ***storage***<br>
**description** : Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).<br>
**required** : False<br>
**data type** : string <br>
### ***individual***<br>
**description** : The Individual entity from which this Biospecimen was derived.<br>
**required** : True<br>
**data type** : Individual <br>
### ***age_at_sampling***<br>
**description** : Age of an individual.<br>
**required** : True<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `0_TO_5` | `Age between 0 to 5.` |
| `6_TO_10` | `Age between 6 to 10.` |
| `11_TO_15` | `Age between 11 to 15.` |
| `16_TO_20` | `Age between 16 to 20.` |
| `21_TO_25` | `Age between 21 to 25.` |
| `26_TO_30` | `Age between 26 to 30.` |
| `31_TO_35` | `Age between 31 to 35.` |
| `36_TO_40` | `Age between 36 to 40.` |
| `41_TO_45` | `Age between 41 to 45.` |
| `46_TO_50` | `Age between 46 to 50.` |
| `51_TO_55` | `Age between 51 to 55.` |
| `56_TO_60` | `Age between 56 to 60.` |
| `61_TO_65` | `Age between 61 to 65.` |
| `66_TO_70` | `Age between 66 to 70.` |
| `71_TO_75` | `Age between 71 to 75.` |
| `76_TO_80` | `Age between 76 to 80.` |
| `81_OR_OLDER` | `Age above 80.` |
| `UNKNOWN` | `Age range unknown.` |


</details>

### ***vital_status_at_sampling***<br>
**description** : Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').<br>
**required** : False<br>
**data type** : Controlled Vocabulary <br>

<details>
<summary> <span style="color:#DAF7A6">Permissible Values</span> </summary>

| Permissible Values | Description |
| --- | --- |
| `ALIVE` | `Showing characteristics of life; displaying signs of life.` |
| `DECEASED` | `The cessation of life.` |
| `UNKNOWN` | `Vital status is unknown.` |


</details>

### ***tissue***<br>
**description** : None<br>
**required** : True<br>
**data type** : string <br>
### ***alias***<br>
**description** : The alias for an entity at the time of submission.<br>
**required** : True<br>
**data type** : string <br>

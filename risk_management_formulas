Risk Management Formulas
------------------------

--------------------------------------------------------------------------------------------
Risk Management

[from:
https://tryhackme.com/room/seriskmanagement
Task 6 - Risk Analysis
Task 7 - Respond to Risk]

Terms:

ALE (Annualised Loss Expectancy) [aka Loss Value] - monetary losses a company expects in a year from all occurrences of a particular realised threat
ALEafterSafeguard - monetary losses a company expects in a year from all occurrences of a particular realised threat with the presence of a particular safeguard
ALEbeforeSafeguard - monetary losses a company expects in a year from all occurrences of a particular realised threat in the absence of a particular safeguard

AnnualCostSafeguard - the annual costs incurred by implementing a particular safeguard

ARO (Annualised Rate of Occurrence) - number of times a company expects a particular realised threat to occur in a year
ARObeforeSafeguard - number of times a company expects a particular realised threat to occur in a year in the absence of a particular safeguard

AV (Asset Value) - monetary value of a particular asset

EF (Exposure Factor) - percentage of Asset Value that would be lost due to a single occurrence of a realised threat
EFafterSafeguard - percentage of Asset Value that would be lost due to a single occurrence of a realised threat with the presence of a particular safeguard
EFbeforeSafeguard - percentage of Asset Value that would be lost due to a single occurrence of a realised threat in the absence of a particular safeguard

SLE (Single Loss Expectancy) - monetary loss caused by a single occurrence of a realised threat
SLEafterSafeguard - monetary loss caused by a single occurrence of a realised threat with the presence of a particular safeguard; may need to be recalculated if EF has changed due to presence of safeguard
SLEbeforeSafeguard - monetary loss caused by a single occurrence of a realised threat in the absence of a particular safeguard


VoS (Value of Safeguard) - the monetary value provided by a particular safeguard being implemented; only if this number is positive is the safeguard worth implementing

Formulas:
ALE = SLE × ARO
ALEafterSafeguard = SLEafterSafeguard × AROafterSafeguard
ALEbeforeSafeguard = SLEbeforeSafeguard × ARObeforeSafeguard
SLE = AV × EF
SLEafterSafeguard = AssetValue × EFafterSafeguard
VoS = ALEbeforeSafeguard − ALEafterSafeguard − AnnualCostSafeguard

Steps to determine VoS:

1) Gather the following values:
* AnnualCostSafeguard
* AV
* EF (EFbeforeSafguard)
* EFafterSafeguard
* ARO (ARObeforeSafeguard)
* AROafterSafeguard

2) Calculate SLEbeforeSafeguard:
AV × EFbeforeSafguard = SLEbeforeSafeguard

3) Calculate ALEbeforeSafeguard:
SLEbeforeSafeguard × ARObeforeSafeguard = ALEbeforeSafeguard

4) Calculate SLEafterSafeguard
AssetValue × EFafterSafeguard = SLEafterSafeguard

5) Calculate the ALEafterSafeguard
SLEafterSafeguard × AROafterSafeguard = ALEafterSafeguard

6) Calculate the VoS
ALEbeforeSafeguard − ALEafterSafeguard − AnnualCostSafeguard = VoS

7) If VoS is a positive number, the safeguard is worth implementing from a monetary perspective.
--------------------------------------------------------------------------------------------










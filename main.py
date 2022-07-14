


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Input Echo : Step: 1   1:43p  Apr 4,2014 
PV Elite Vessel Analysis Program: Input Data
 Design Internal Pressure (for Hydrotest)  363.00 psig Design Internal Temperature 248 F Type of Hydrotest UG-99(b) Hydrotest Position Horizontal Projection of Nozzle from Vessel Top 31.000 in Projection of Nozzle from Vessel Bottom 7.6000 in Minimum Design Metal Temperature 0 F Type of Construction Welded Special Service None Degree of Radiography RT-3 Miscellaneous Weight Percent 0.0 Use Higher Longitudinal Stresses (Flag) Y Select t for Internal Pressure (Flag) Y Select t for External Pressure (Flag) Y Select t for Axial Stress (Flag) N Select Location for Stiff. Rings (Flag)  Y Consider Vortex Shedding N Perform a Corroded Hydrotest N Is this a Heat Exchanger No User Defined Hydro. Press. (Used if > 0) 0.0000 psig User defined MAWP 0.0000 psig User defined MAPnc 0.0000 psig 
Load Case 1 NP+EW+WI+FW+BW Load Case 2 NP+EW+EE+FS+BS Load Case 3 NP+OW+WI+FW+BW Load Case 4 NP+OW+EQ+FS+BS Load Case 5 NP+HW+HI Load Case 6 NP+HW+HE Load Case 7 IP+OW+WI+FW+BW Load Case 8 IP+OW+EQ+FS+BS Load Case 9 EP+OW+WI+FW+BW Load Case 10 EP+OW+EQ+FS+BS Load Case 11 HP+HW+HI Load Case 12 HP+HW+HE Load Case 13 IP+WE+EW Load Case 14 IP+WF+CW Load Case 15 IP+VO+OW Load Case 16 IP+VE+EW Load Case 17 NP+VO+OW Load Case 18 FS+BS+IP+OW Load Case 19 FS+BS+EP+OW 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Input Echo : Step: 1   1:43p  Apr 4,2014 
Wind Design Code Basic Wind Speed Surface Roughness Category  Importance Factor Type of Surface Base Elevation  [V]  ASCE 7-05 140.00 mile/hr C: Open Terrain 1.15 Moderately Smooth 0.0000 ft  
Percent Wind for Hydrotest  0.0  

Using User defined Wind Press. Vs Elev. N Height of Hill or Escarpment H or Hh 0.0000 ft Distance Upwind of Crest Lh 0.0000 ft Distance from Crest to the Vessel x 0.0000 ft Type of Terrain ( Hill, Escarpment )  Flat Damping Factor (Beta) for Wind (Ope) 0.0100 Damping Factor (Beta) for Wind (Empty) 0.0000 Damping Factor (Beta) for Wind (Filled) 0.0000 
Seismic Design Code ASCE 7-05 Importance Factor 1.250 Table Value Fa 1.000 Table Value Fv 1.400 Short Period Acceleration value Ss 0.112 Long Period Acceleration Value Sl 0.052 Moment Reduction Factor Tau 1.000 Force Modification Factor R 3.000 Site Class D Component Elevation Ratio z/h 0.000 Amplification Factor Ap 0.000 Force Factor 0.000 Consider Vertical Acceleration No Minimum Acceleration Multiplier 0.000 User Value of Sds (used if > 0 ) 0.000 User Value of Sd1 (used if > 0 ) 0.000 
Design Nozzle for Des. Press. + St. Head Y Consider MAP New and Cold in Noz. Design N Consider External Loads for Nozzle Des. Y Use ASME VIII-1 Appendix 1-9 N 
Material Database Year Current w/Addenda or Code Year 
Configuration Directives:
 Do not use Nozzle MDMT Interpretation VIII-1 01-37 No Use Table G instead of exact equation for "A" Yes Shell Head Joints are Tapered Yes

Internal Pressure Calculation Results : 
ASME Code, Section VIII, Division 1, 2013 
Elliptical Head From 10 To 20 SA-240 304L at 248 F 
left head 
Material UNS Number:  S30403 
Required Thickness due to Internal Pressure [tr]: 
= (P*D*Kcor)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.760*60.0000*1.000)/(2*16700.00*0.85-0.2*363.760) = 0.7708 + 0.0000 = 0.7708 in 
Max. Allowable Working Pressure at given Thickness, corroded [MAWP]: 
Less Operating Hydrostatic Head Pressure of 0.760 psig 
= (2*S*E*t)/(Kcor*D+0.2*t) per Appendix 1-4 (c) = (2*16700.00*0.85*0.8268)/(1.000*60.0000+0.2*0.8268) = 390.126 - 0.760 = 389.366 psig 
Maximum Allowable Pressure, New and Cold [MAPNC]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Internal Pressure Calculations :   Step:  3   1:43p  Apr 4,2014 
= (2*S*E*t)/(K*D+0.2*t) per Appendix 1-4 (c) = (2*16700.00*0.85*0.8268)/(1.000*60.0000+0.2*0.8268) = 390.126 psig 
Actual stress at given pressure and thickness, corroded [Sact]:
 = (P*(Kcor*D+0.2*t))/(2*E*t) = (363.760*(1.000*60.0000+0.2*0.8268))/(2*0.85*0.8268) = 15571.377 psi 
Straight Flange Required Thickness:
 = (P*R)/(S*E-0.6*P) + c per UG-27 (c)(1) = (363.760*30.0000)/(16700.00*0.85-0.6*363.760)+0.000 = 0.781 in 
Straight Flange Maximum Allowable Working Pressure: 
Less Operating Hydrostatic Head Pressure of 0.760 psig 
= (S*E*t)/(R+0.6*t) per UG-27 (c)(1) = (16700.00 * 0.85 * 0.9449 )/(30.0000 + 0.6 * 0.9449 ) = 438.794 - 0.760 = 438.034 psig 
Percent Elongation per UHA-44 (75*tnom/Rf)*(1-Rf/Ro) 6.640 % Note: Please Check Requirements of Table UHA-44 for Elongation limits. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
Cylindrical Shell From 20 To 30 SA-240 304L at 248 F 
shell 
Material UNS Number:  S30403 
Required Thickness due to Internal Pressure [tr]: 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.760*30.0000)/(16700.00*0.85-0.6*363.760) = 0.7808 + 0.0000 = 0.7808 in 
Max. Allowable Working Pressure at given Thickness, corroded [MAWP]: 
Less Operating Hydrostatic Head Pressure of 0.760 psig 
= (S*E*t)/(R+0.6*t) per UG-27 (c)(1) = (16700.00*0.85*0.8661)/(30.0000+0.6*0.8661) = 402.851 - 0.760 = 402.091 psig 
Maximum Allowable Pressure, New and Cold [MAPNC]: 
= (S*E*t)/(R+0.6*t) per UG-27 (c)(1) = (16700.00*0.85*0.8661)/(30.0000+0.6*0.8661) = 402.851 psig 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Internal Pressure Calculations :   Step:  3   1:43p  Apr 4,2014 
Actual stress at given pressure and thickness, corroded [Sact]:
 = (P*(R+0.6*t))/(E*t) = (363.760*(30.0000+0.6*0.8661))/(0.85*0.8661) = 15079.509 psi 
Percent Elongation per UHA-44 (50*tnom/Rf)*(1-Rf/Ro) 1.423 % Note: Please Check Requirements of Table UHA-44 for Elongation limits. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
Elliptical Head From 30 To 40 SA-240 304L at 248 F 
right head 
Material UNS Number:  S30403 
Required Thickness due to Internal Pressure [tr]: 
= (P*D*Kcor)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.760*60.0000*1.000)/(2*16700.00*0.85-0.2*363.760) = 0.7708 + 0.0000 = 0.7708 in 
Max. Allowable Working Pressure at given Thickness, corroded [MAWP]: 
Less Operating Hydrostatic Head Pressure of 0.760 psig 
= (2*S*E*t)/(Kcor*D+0.2*t) per Appendix 1-4 (c) = (2*16700.00*0.85*0.8268)/(1.000*60.0000+0.2*0.8268) = 390.126 - 0.760 = 389.366 psig 
Maximum Allowable Pressure, New and Cold [MAPNC]: 
= (2*S*E*t)/(K*D+0.2*t) per Appendix 1-4 (c) = (2*16700.00*0.85*0.8268)/(1.000*60.0000+0.2*0.8268) = 390.126 psig 
Actual stress at given pressure and thickness, corroded [Sact]:
 = (P*(Kcor*D+0.2*t))/(2*E*t) = (363.760*(1.000*60.0000+0.2*0.8268))/(2*0.85*0.8268) = 15571.377 psi 
Straight Flange Required Thickness:
 = (P*R)/(S*E-0.6*P) + c per UG-27 (c)(1) = (363.760*30.0000)/(16700.00*0.85-0.6*363.760)+0.000 = 0.781 in 
Straight Flange Maximum Allowable Working Pressure: 
Less Operating Hydrostatic Head Pressure of 0.760 psig 
= (S*E*t)/(R+0.6*t) per UG-27 (c)(1) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Internal Pressure Calculations :   Step:  3   1:43p  Apr 4,2014 
= (16700.00 * 0.85 * 0.9449 )/(30.0000 + 0.6 * 0.9449 ) 
= 438.794 - 0.760 = 438.034 psig 
Percent Elongation per UHA-44 (75*tnom/Rf)*(1-Rf/Ro) 6.640 % Note: Please Check Requirements of Table UHA-44 for Elongation limits. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
Hydrostatic Test Pressure Results:
 Pressure per UG99b = 1.3 * M.A.W.P. * Sa/S 506.175 psig Pressure per UG99b[34] = 1.3 * Design Pres * Sa/S 471.900 psig Pressure per UG99c = 1.3 * M.A.P. -Head(Hyd) 503.602 psig Pressure per UG100 = 1.1 * M.A.W.P. * Sa/S 428.302 psig Pressure per PED = 1.43 * MAWP 556.793 psig 
UG-99(b), Test Pressure Calculation: 
= Test Factor * MAWP * Stress Ratio 
= 1.3 * 389.366 * 1.000 
= 506.175 psig 

Horizontal Test performed per: UG-99b 
Please note that Nozzle, Shell, Head, Flange, etc MAWPs are all considered when determining the hydrotest pressure for those test types that are based on the MAWP of the vessel. 

Stresses on Elements due to Test Pressure:
 From To Stress Allowable Ratio Pressure ----------------------------------------------------------------------
left head  21760.4  22500.0  0.967  508.34  
shell  21073.1  22500.0  0.937  508.34  
right head  21760.4  22500.0  0.967  508.34  

----------------------------------------------------------------------
Elements Suitable for Internal Pressure. 

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 External Pressure Calculations :   Step:  4   1:43p  Apr 4,2014 
External Pressure Calculation Results : 
ASME Code, Section VIII, Division 1, 2013 
Elliptical Head From 10 to 20 Ext. Chart: HA-3 at 248 F 
left head 
Elastic Modulus from Chart: HA-3 at 248  F : 0.270E+08 psi 
Results for Maximum Allowable External Pressure (MAEP):
 Tca OD D/t Factor A B 0.827 61.65 74.57 0.0018625 8147.17 EMAP = B/(K0*D/t) = 8147.1709/(0.9000 *74.5714 ) = 121.3925 psig 
Results for Required Thickness (Tca):
 Tca OD D/t Factor A B 0.163 61.65 378.78 0.0003667 4943.46 EMAP = B/(K0*D/t) = 4943.4629/(0.9000 *378.7831 ) = 14.5010 psig 
Check the requirements of UG-33(a)(1) using P = 1.67 * External Design pressure for this head. 
Material UNS Number:  S30403 
Required Thickness due to Internal Pressure [tr]: 
= (P*D*Kcor)/(2*S*E-0.2*P) Appendix 1-4(c) = (24.215*60.0000*1.000)/(2*16700.00*1.00-0.2*24.215) = 0.0435 + 0.0000 = 0.0435 in 
Max. Allowable Working Pressure at given Thickness, corroded [MAWP]: 
= ((2*S*E*t)/(Kcor*D+0.2*t))/1.67 per Appendix 1-4 (c) = ((2*16700.00*1.00*0.8268)/(1.000*60.0000+0.2*0.8268))/1.67 = 274.833 psig 
Maximum Allowable External Pressure [MAEP]: 
= min( MAEP, MAWP ) = min( 121.39 , 274.8332 ) = 121.393 psig 
Thickness requirements per UG-33(a)(1) do not govern the required thickness of this head. 
Cylindrical Shell From 20 to 30 Ext. Chart: HA-3 at 248 F 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 External Pressure Calculations :   Step:  4   1:43p  Apr 4,2014 
shell 
Elastic Modulus from Chart: HA-3 at 248  F : 0.270E+08 psi 
Results for Maximum Allowable External Pressure (MAEP):
 Tca OD SLEN D/t L/D Factor A B 0.866 61.73 160.00 71.27 2.5918 0.0008196 6863.67 EMAP = (4*B)/(3*(D/t)) = (4*6863.6660 )/(3*71.2727 ) = 128.4019 psig 
Results for Required Thickness (Tca):
 Tca OD SLEN D/t L/D Factor A B 0.299 61.73 160.00 206.16 2.5918 0.0001663 2242.08 EMAP = (4*B)/(3*(D/t)) = (4*2242.0771 )/(3*206.1585 ) = 14.5007 psig 
Results for Maximum Stiffened Length (Slen):
 Tca OD SLEN D/t L/D Factor A B 0.866 61.73 4002.22 71.27 50.0000 0.0002236 3014.83 EMAP = (4*B)/(3*(D/t)) = (4*3014.8267 )/(3*71.2727 ) = 56.3998 psig 
Elliptical Head From 30 to 40 Ext. Chart: HA-3 at 248 F 
right head 
Elastic Modulus from Chart: HA-3 at 248  F : 0.270E+08 psi 
Results for Maximum Allowable External Pressure (MAEP):
 Tca OD D/t Factor A B 0.827 61.65 74.57 0.0018625 8147.17 EMAP = B/(K0*D/t) = 8147.1709/(0.9000 *74.5714 ) = 121.3925 psig 
Results for Required Thickness (Tca):
 Tca OD D/t Factor A B 0.163 61.65 378.78 0.0003667 4943.46 EMAP = B/(K0*D/t) = 4943.4629/(0.9000 *378.7831 ) = 14.5010 psig 
Check the requirements of UG-33(a)(1) using P = 1.67 * External Design pressure for this head. 
Material UNS Number:  S30403 
Required Thickness due to Internal Pressure [tr]: 
= (P*D*Kcor)/(2*S*E-0.2*P) Appendix 1-4(c) = (24.215*60.0000*1.000)/(2*16700.00*1.00-0.2*24.215) = 0.0435 + 0.0000 = 0.0435 in 
Max. Allowable Working Pressure at given Thickness, corroded [MAWP]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 External Pressure Calculations :   Step:  4   1:43p  Apr 4,2014 
= ((2*S*E*t)/(Kcor*D+0.2*t))/1.67 per Appendix 1-4 (c) = ((2*16700.00*1.00*0.8268)/(1.000*60.0000+0.2*0.8268))/1.67 = 274.833 psig 
Maximum Allowable External Pressure [MAEP]: 
= min( MAEP, MAWP ) = min( 121.39 , 274.8332 ) = 121.393 psig 
Thickness requirements per UG-33(a)(1) do not govern the required thickness of this head. 
External Pressure Calculations
 | | Section | Outside | Corroded | Factor | Factor | From| To | Length |  Diameter | Thickness | A | B | | | ft | in | in | | psi | ---------------------------------------------------------------------------
10| 20|  No Calc |  61.6535 |  0.82677 |  0.0018625 |  8147.17 |  
20| 30|  13.3333 |  61.7323 |  0.86614 | 0.00081961 |  6863.67 |  
30| 40|  No Calc |  61.6535 |  0.82677 |  0.0018625 |  8147.17 |  
External Pressure Calculations 

 | | External | External | External | External | From| To | Actual T. | Required T.|Des. Press. | M.A.W.P. | | | in | in | psig | psig | 
----------------------------------------------------------------10| 20| 0.82677 | 0.16277 | 14.5000 | 121.393 | 20| 30| 0.86614 | 0.29944 | 14.5000 | 128.402 | 30| 40| 0.82677 | 0.16277 | 14.5000 | 121.393 | Minimum 121.393 

External Pressure Calculations
 | | Actual Len.| Allow. Len.| Ring Inertia | Ring Inertia | From| To | Bet. Stiff.| Bet. Stiff.| Required |  Available | | | ft | ft | in**4 | in**4 | 
-------------------------------------------------------------------10| 20| No Calc | No Calc | No Calc | No Calc | 20| 30| 13.3333 | 333.518 | No Calc | No Calc | 30| 40| No Calc | No Calc | No Calc | No Calc | 
Elements Suitable for External Pressure. 

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 
PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 


Element and Detail Weights :  Step:  5   1:43p  Apr 4,2014 
Element and Detail Weights
 | | Element | Element | Corroded | Corroded | Extra due | From| To | Metal Wgt. | ID Volume |Metal Wgt. | ID Volume | Misc % | | | lbf | in3 | lbf | in3 | lbf | ---------------------------------------------------------------------------
10| 20|  1269.76 |  31057.2 |  1269.76 |  31057.2 |  380.928 |  
20| 30|  7109.96 |  418549. |  7109.96 |  418549. |  2132.99 |  
30| 40|  1269.76 |  31057.2 |  1269.76 |  31057.2 |  380.928 |  

---------------------------------------------------------------------------Total 9649 480663 9649 480663 2894 

Weight of Details
 | | Weight of | X Offset, | Y Offset, | From|Type| Detail | Dtl. Cent. |Dtl. Cent. | Description | | lbf | ft | ft | 
-------------------------------------------------10|Liqd| 424.924 | -0.41667 | 1.00000 | L 10|Insl| 48.0475 | -0.58399 | ... | Ins: 20 20|Sadl| 551.307 | 1.75000 | 2.98589 | L Sdl 20|Sadl| 551.307 | 10.7500 | 2.98589 | R Sdl 20|Liqd| 5536.31 | 6.16798 | 1.00000 | L 20|Insl| 256.963 | 6.16800 | ... | Ins: 20 20|Nozl| 117.974 | 0.75000 | 2.68750 | F1 20|Nozl| 27.3786 | 1.75000 | 2.59896 | Y 20|Nozl| 27.3786 | 2.75000 | 2.59896 | L4 20|Nozl| 27.3786 | 3.75000 | 2.59896 | P 20|Nozl| 27.3786 | 4.75000 | 2.59896 | V 20|Nozl| 63.2139 | 12.0000 | 2.64583 | A 20|Nozl| 321.857 | 8.50000 | 3.50000 | M 20|Nozl| 117.974 | 5.75000 | 2.68750 | R1 20|Nozl| 18.4678 | 4.00000 | 2.59896 | W1 20|Nozl| 35.5311 | 12.0000 | 2.64583 | B 30|Liqd| 424.924 | 0.49869 | 1.00000 | L 30|Insl| 48.0475 | 0.66601 | ... | Ins: 20 30|Nozl| 19.1968 | 0.83202 | ... | L2 30|Nozl| 19.1968 | 0.83202 | ... | L1 30|Nozl| 15.1865 | 1.33201 | ... | T 

Total Weight of Each Detail Type
 Total Weight of Saddles 1102.6 Total Weight of Liquid 6386.2 Total Weight of Insulation 353.1 
PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 


Element and Detail Weights :  Step:  5   1:43p  Apr 4,2014 
Total Weight of Nozzles 838.1 ---------------------------------------------------------------Sum of the Detail Weights 8679.9 lbf 
Weight Summation
 Fabricated Shop Test Shipping Erected Empty Operating ------------------------------------------------------------------------------12544.3 14485.0 12544.3 14485.0 12544.3 14838.1 1102.6 17357.3 1102.6 ... 1102.6 6386.2 
838.1 ... 838.1 ... ... ... ... ... ... 353.1 ... ... ... ... ... ... 353.1 ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... 838.1 ... 
------------------------------------------------------------------------------14485.0 31842.3 14838.1 14838.1 14838.1 21224.3 lbf 
Miscellaneous Weight Percent: 30.0 % 
Note that the above value for the miscellaneous weight percent has been applied to the shells/heads/flange/tubesheets/tubes etc. in the weight calculations for metallic components. 
Note: The shipping total has been modified because some items have been specified as being installed in the shop. 


Weight Summary
 Fabricated Wt. -Bare Weight W/O Removable Internals 14485.0 lbf Shop Test Wt. -Fabricated Weight + Water ( Full ) 31842.3 lbf Shipping Wt. -Fab. Wt + Rem. Intls.+ Shipping App.  14838.1 lbf Erected Wt. -Fab. Wt + Rem. Intls.+ Insul. (etc) 14838.1 lbf Ope. Wt. no Liq - Fab. Wt + Intls. + Details + Wghts. 14838.1 lbf Operating Wt. -Empty Wt + Operating Liq. Uncorroded 21224.3 lbf Oper. Wt. + CA -Corr Wt. + Operating Liquid  21224.3 lbf Field Test Wt. -Empty Weight + Water (Full) 32195.4 lbf 
Note: The Corroded Weight and thickness are used in the Horizontal       Vessel Analysis (Ope Case) and Earthquake Load Calculations. 
Outside Surface Areas of Elements 
PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 


Element and Detail Weights :  Step:  5   1:43p  Apr 4,2014 
|  |  Surface  |  
From| To |  Area  |  
|  |  in^2  |  

----------------------------10| 20| 4343.41 | 20| 30| 28708.9 | 30| 40| 4343.41 | 
-----------------------------------------------------Total 37395.699 in^2 [259.7 Square Feet ] 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Flange MAWP : Step: 6   1:43p  Apr 4,2014 
Nozzle Flange MAWP Results :
 Nozzle -----Flange Rating Description Operating Ambient Temperature Class Grade|Group 
psig psig F ----------------------------------------------------------------------------F1 571.2 720.0 248 300 GR 2.1 Y 571.2 720.0 248 300 GR 2.1 L4 571.2 720.0 248 300 GR 2.1 P 571.2 720.0 248 300 GR 2.1 V 571.2 720.0 248 300 GR 2.1 A 571.2 720.0 248 300 GR 2.1 M 571.2 720.0 248 300 GR 2.1 R1 571.2 720.0 248 300 GR 2.1 W1 571.2 720.0 248 300 GR 2.1 B 571.2 720.0 248 300 GR 2.1 L2 571.2 720.0 248 300 GR 2.1 L1 571.2 720.0 248 300 GR 2.1 T 571.2 720.0 248 300 GR 2.1 ----------------------------------------------------------------------------Minimum Rating 571.200 720.000 psig (for Core Elements) 
Note: ANSI Ratings are per ANSI/ASME B16.5 2009 Edition 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Wind Load Calculation :    Step:  7   1:43p  Apr 4,2014 
Input Values: 
Wind Design Code Basic Wind Speed Surface Roughness Category  Importance Factor Type of Surface Base Elevation  [V]  ASCE 7-05 140.00 mile/hr C: Open Terrain 1.15 Moderately Smooth 0.0000 ft  
Percent Wind for Hydrotest  0.0  

Using User defined Wind Press. Vs Elev. N 
Height of Hill or Escarpment H or Hh 0.0000 ft 
Distance Upwind of Crest Lh 0.0000 ft 
Distance from Crest to the Vessel x 0.0000 ft 
Type of Terrain ( Hill, Escarpment )  Flat 
Damping Factor (Beta) for Wind (Ope) 0.0100 
Damping Factor (Beta) for Wind (Empty) 0.0000 
Damping Factor (Beta) for Wind (Filled) 0.0000 
Wind Analysis Results 
Static Gust-Effect Factor, Operating Case [G]: 
= min(0.85, 0.925((1 + 1.7 * gQ * Izbar * Q )/( 1 + 1.7 * gV * Izbar))) = min(0.85,0.925((1+1.7*3.400*0.228*0.958)/(1+1.7*3.400*0.228))) = min(0.85, 0.903 ) = 0.850 
Natural Frequency of Vessel (Operating) 33.000 Hz Natural Frequency of Vessel (Empty) 33.000 Hz Natural Frequency of Vessel (Test) 33.000 Hz 
Note: Per Section 1609 of IBC 2003/06/09 these results are also applicable    for the determination of Wind Loads on structures (1609.1.1).
 User Entered Importance Factor is 1.150 Force Coefficient [Cf] 0.527 Structure Height to Diameter ratio 2.613 
This is classified as a rigid structure. Static analysis performed. 

Sample Calculation for the First Element 
The ASCE code performs all calculations in Imperial Units only. The wind pressure is therefore computed in these units. 
Value of [Alpha] and [Zg]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Wind Load Calculation :    Step:  7   1:43p  Apr 4,2014 
Exposure Category: C from Table C6-2 Alpha = 9.500 : Zg = 900.000 ft 
Effective Height [z]: 
= Centroid Height + Vessel Base Elevation = 3.583 + 0.000 = 3.583 ft 
Velocity Pressure coefficient evaluated at height z [Kz]: 
Because z (3.583 ft.) < 15 ft. = 2.01 * ( 15 / Zg ) 2 / Alpha = 2.01 * ( 15/900.000 )2/9.500 = 0.849 
Type of Hill: No Hill 
Wind Directionality Factor [Kd]: 
= 0.95 per [6-6 ASCE-7 98][6-4 ASCE-7 02/05] 
As there is No Hill Present: [Kzt]: 
K1 = 0, K2 = 0, K3 = 0 
Topographical Factor [Kzt]: 
= ( 1 + K1 * K2 * K3 )2 = ( 1 + 0.000 * 0.000 * 0.000 )2 = 1.0000 
Velocity Pressure evaluated at height z, Imperial Units [qz]: 
= 0.00256 * Kz * Kzt * Kd * I * Vr(mph)2 = 0.00256 * 0.849 * 1.000 * 0.950 * 1.150 * 140.0002 = 46.5 psf 
Force on the first element [F]: 
= qz * G * Cf * WindArea = 46.534 * 0.850 * 0.527 * 6.922 = 144.3 lbf 
Element Hgt (z)  K1 K2 K3 Kz Kzt qz ft psf ---------------------------------------------------------------------------
left head  3.6  0.000  0.000  0.000  0.849  1.000  46.534  
shell  3.6  0.000  0.000  0.000  0.849  1.000  46.534  
right head  3.6  0.000  0.000  0.000  0.849  1.000  46.534  
Wind Load Calculation 

 | | Wind | Wind | Wind | Wind | Element | 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Wind Load Calculation :    Step:  7   1:43p  Apr 4,2014 
From| To | Height | Diameter | Area | Pressure | Wind Load | | | ft | ft | in^2 | psf | lbf | ---------------------------------------------------------------------------
10| 20|  3.58333 |  6.56535 |  996.766 |  46.5335 |  144.255 |  
20| 30|  3.58333 |  6.57323 |  11676.5 |  46.5335 |  1689.86 |  
30| 40|  3.58333 |  6.56535 |  996.766 |  46.5335 |  144.255 |  

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 
PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 


Earthquake Load Calculation :  Step:  8   1:43p  Apr 4,2014 
Input Values: 
Earthquake Analysis per ASCE 7-05 
Short-period site coefficient 9.4.1.2.4a  Fa: 1.000  
   Long -period site coefficient 9.4.1.2.4b  Fv: 1.400  
Maximum Mapped Acceleration Value for Short Periods  Ss: 0.112  
Maximum Mapped Acceleration Value for 1 Sec. Period  S1: 0.052  

Response Modification Factor R: 3.000 
Importance Factor Ie: 1.250 
Site Class D 

Seismic Analysis Results: 
Sms = Fa * Ss = 1.000 * 0.112 = 0.112 Sm1 = Fv * S1 = 1.400 * 0.052 = 0.073 Sds = 2/3 * Sms = 2/3 * 0.112 = 0.075 Sd1 = 2/3 * Sm1 = 2/3 * 0.073 = 0.049 
Check Approximate Fundamental Period from 9.5.5.3.2-1 [Ta]: 
= Ct * hnx where Ct = 0.020, x = 0.75 and hn = Structural Height (ft.) = 0.020 * ( 5.00000.75) = 0.067 seconds 
The Coefficient Cu from Table 9.5.5.3.1 is : 1.700 
Fundamental Period (1/Frequency) [T]: 
= ( 1/Natural Frequency ) = ( 1/33.000 ) 
= 0.030 
Check the Value of T which is the smaller of Cu*Ta and T: 
= Minimum Value of (1.700 * 0.067 , 0.030 ) per 9.5.5.3 = 0.030 
As the time period is < 0.06 second, use section 9.14.5.2. 
Compute the Base Shear per equation 9.14.5.2, [V]: 
= 0.3 * Sds * W * I 
= 0.3 * 0.075 * 21224 * 1.25 
= 594.279 lbf 
Note: Loads multiplied by the Scalar multiplier value of 0.7000
 Final Base Shear, V = 416.00 lbf 
Earthquake Load Calculation 
PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 


Earthquake Load Calculation :  Step:  8   1:43p  Apr 4,2014 
| | Earthquake | Earthquake |  Element | From| To | Height |  Weight | Ope  Load | | | ft | lbf | lbf | -------------------------------------------------
10| 20|  2.50000 |  4244.85 |  83.1991 |  
20|Sadl|  2.50000 |  4244.85 |  83.1991 |  
Sadl| 30|  2.50000 |  4244.85 |  83.1991 |  
20| 30|  2.50000 |  4244.85 |  83.1991 |  
30| 40|  2.50000 |  4244.85 |  83.1991 |  

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Center of Gravity Calculation :    Step:  9   1:43p  Apr 4,2014 
Shop/Field Installation Options : 
Insulation is installed in the Shop. 
Note : The CG is computed from the first Element From Node
 Center of Gravity of Saddles 6.332 ft Center of Gravity of Liquid 6.250 ft Center of Gravity of Insulation 6.250 ft Center of Gravity of Nozzles 7.039 ft 
Center of Gravity of Bare Shell New and Cold 6.250 ft Center of Gravity of Bare Shell Corroded 6.250 ft 
Vessel CG in the Operating Condition 6.285 ft Vessel CG in the Fabricated (Shop/Empty) Condition 6.301 ft Vessel CG in the Test Condition 6.273 ft 
Rigging Analysis Results: 
Total Effective Length of Vessel for this analysis  12.50 ft  
Total vessel weight (No Liquid)   Twt  14838.10 lbf  
 Impact weight multiplication factor  Imp  2.00  
 Design lifting weight,  DWT = Imp * Twt  29676.21 lbf  
Elevation of the Tailing Lug (bottom)   1.56 ft  
Elevation of the Lifting Lug (top   )  10.78 ft  
Design Reaction force at the tailing lug   14411.12 lbf  
Design Reaction force at the lifting lug   15265.09 lbf  
CG Distance from Tailing Lug   4.74 ft  
CG Distance from the Nearer Lifting Lug   4.48 ft  
Critical Values: 

 Max Stress Elevation Allowables 
psi ft psi -----------|-----------|---------------|------------------------Bending | 52.93 | 2.55 | 11365.84 (UG-23) Shear | -71.38 | 0.02 | 11690.00 (0.7*S) -----------|-----------|---------------|------------------------
Forces and Moments at selected elevations (not all analysis points shown):
 Distance Bending Moment Bending Stress Shear Force Shear Stress ft ft-lbf psi lbf psi 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Center of Gravity Calculation :    Step:  9   1:43p  Apr 4,2014 
------------------------------------------------------------------------------
0.00  0.0  0.0  -10683.4  -67.6  
2.55  10962.2  52.9  3775.6  22.8  
7.48  -1810.6  -8.7  -3346.7  -20.2  
12.42  2413.9  12.2  593.5  3.8  

Unity Check (Actual Stress / Allowable Stress): 
Maximum Unity Check is 0.0047 at elevation 2.5492 ft - Must be <=1 Note: The rigging analysis is performed using a uniformly distributed load. 
--- Plot data successfully generated ...---

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Lifting Lug Calculations: Lug(s) on Left End of Vessel 
Input Values:
 Lifting Lug Material   SA-283 C  Lifting Lug Yield Stress Yield 30007.25 psi 
Total Height of Lifting Lug  w 11.0236 in Thickness of Lifting Lug  t 0.7874 in Diameter of Hole in Lifting Lug  dh 1.4961 in Radius of Semi-Circular Arc of Lifting Lug  r 3.1496 in Height of Lug from bottom to Center of Hole h 5.5118 in Offset from Vessel OD to Center of Hole off 5.5118 in Lug Fillet Weld Size tw 0.6299 in Length of weld along side of Lifting Lug  wl 11.0236 in Length of Weld along Bottom of Lifting Lug  wb 0.7874 in Thickness of Collar (if any)  tc 0.0000 in Diameter of Collar (if any)  dc 0.0000 in Impact Factor Impfac 2.00  Sling Angle from Horizontal 90.0000 deg Number of Lugs in Group 2 
Lifting Lug Orientation to Vessel: Perpendicular 
Lift Orientation : Horizontal Lift 
PV Elite does not compute weak axis bending forces on the lugs. It is assumed that a spreader bar is used. 

Computed Results:
 Force Along Vessel Axis Fax 0.00 lbf Force Normal to Vessel Fn 7205.56 lbf Force Tangential to Vessel Ft 0.00 lbf 
Converting the weld leg dimension (tw) to the weld throat dimension. 

Weld Group Inertia Calculations:
 Weld Group Inertia about the Circumferential Axis Ilc 122.507 in**4 Weld Group Centroid distance in the Long. Direction Yll 5.957 in Dist. of Weld Group Centroid from Lug bottom Yll_b 5.512 in Weld Group Inertia about the Longitudinal Axis Ill 0.486 in**4 Weld Group Centroid Distance in the Circ. Direction Ylc 0.394 in 
Note: The Impact Factor is applied to the Forces acting on the Lug. 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Primary Shear Stress in the Welds due to Shear Loads [Ssll]:
 = sqrt( Fax2 + Ft2 + Fn2 )/(( 2 * (wl + wb) ) * tw ) = sqrt(02+02+72052)/((2*(11.0+0.8))*0.4454) = 684.93 psi 
Shear Stress in the Welds due to Bending Loads [Sblf]: 
= (Fn*(h-Yll_b)) *Yll/Ilc + (Fax*off *Yll/Ilc) + (Ft*off *Ylc/Ill) 
= (7205 *(5.512 -5.512 )) * 5.957/122.507 + (0 *5.512 * 5.957/122.507 ) + (0 *5.512 * 0.394/0.486 ) 
= 0.00 psi 
Total Shear Stress for Combined Loads [St]: 
= Ssll + Sblf = 684.927 + 0.000 = 684.93 psi 
Allowable Shear Stress for Combined Loads [Sta]: 
= 0.4 * Yield * Occfac (AISC Shear Allowable) = 0.4 * 30007 * 1.00 = 12002.90 psi 
Shear Stress in Lug above Hole [Shs]:
 = sqrt( Pl2 + Fax2 ) / Sha = sqrt( 72052 + 02 )/3.782 = 1905.22 psi 
Allowable Shear Stress in Lug above Hole [Sas]: 
= 0.4 * Yield * Occfac = 0.4 * 30007 * 1.00 = 12002.90 psi 
Pin Hole Bearing Stress [Pbs]:
 = sqrt( Fax2 + Fn2 ) / ( t * dh ) = sqrt( 02 + 72052 )/( 0.787 * 1.496 ) = 6116.76 psi 
Allowable Bearing Stress [Pba]: 
= min( 0.75 * Yield * Occfac, 0.9 * Yield ) AISC Bearing All. = min( 0.75 * 30007 * 1.00 , 27006.5 ) = 22505.44 psi 
Bending Stress at the Base of the Lug [Fbs]: 
= Ft * off/(w * t2/6) + Fax * off/(w2 * t/6) = 0 * 5.512/(11.024 * 0.7872/6) + 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
0 * 5.512/(11.0242 * 0.787/6) = 0.00 psi 
Tensile Stress at the Base of the Lug [Fa]: 
= Fn / (w * t) = 0/(11.024 * 0.787 ) = 830.13 psi 
Total Combined Stress at the Base of the Lug: 
= Fbs + Fa = 0.0 + 830.1 = 830.13 psi 
Lug Allowable Stress for Bending and Tension: 
= min( 0.66 * Yield * Occfac, 0.75 * Yield ) = min( 0.66 * 30007 * 1.00 , 22505.4 ) = 19804.79 psi 
Required Shackle Pin Diameter [Spd]: 
= sqrt[(2 * sqrt(Fn2 + Fax2)/( Pi * Sta))] = sqrt[2 * sqrt(72052 + 02)/( Pi * 12002 )] = 0.6182 in 
WRC 107/537 Stress Analysis for the Lifting Lug to Shell Junction in the new and Cold Condition (no corrosion applied). 
Note: Since Beta1/Beta2 >= 0.25, C22 (C22p) is adjusted per table 6 in paragraph 4.3 of WRC Bulletin 107. 
Input Echo, WRC107/537 Item  1,  Description: Lift Lug
 Diameter Basis for Vessel Vbasis ID Cylindrical or Spherical Vessel Cylsph Cylindrical Internal Corrosion Allowance Cas 0.0000 in Vessel Diameter Dv 60.000 in Vessel Thickness Tv 0.866 in 
 Design Temperature  100.00 癋
 Attachment Type Type Rectangular Parameter C11 C11 0.79 in Parameter C22 C22 3.15 in 
Thickness of Reinforcing Pad Tpad 0.630 in Pad Parameter C11P C11p 7.874 in Pad Parameter C22P C22p 13.780 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Design Internal Pressure Dp 0.000 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P -7205.6 lbf Longitudinal Shear (SUS) Vl 0.0 lbf Circumferential Shear (SUS) Vc 0.0 lbf Circumferential Moment (SUS) Mc 0.0 ft-lbf Longitudinal Moment (SUS) Ml 0.0 ft-lbf Torsional Moment (SUS) Mt 0.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P -7205.6 lbf Circumferential Shear VC 0.0 lbf Longitudinal Shear VL 0.0 lbf Circumferential Moment MC 0.0 ft-lbf Longitudinal Moment ML 0.0 ft-lbf Torsional Moment MT 0.0 ft-lbf 
Dimensionless Parameters used : Gamma = 20.55 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.038 4C 4.078 (A,B)  N(PHI) / ( P/Rm )  0.038 3C 4.109 (C,D)  M(PHI) / ( P ) 0.023 2C1 0.255 (A,B)  M(PHI) / ( P ) 0.023 1C 0.289 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.020 3A 0.038 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.026 1A ! 0.105 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.032 3B 0.391 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.029 1B ! 0.065 (A,B,C,D) 
N(x) / ( P/Rm )  0.031 3C 4.159 (A,B) N(x) / ( P/Rm )  0.031 4C 4.104 (C,D) M(x) / ( P ) 0.032 1C1 0.270 (A,B) M(x) / ( P ) 0.032 2C 0.221 (C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
N(x) / ( MC/(Rm**2 * Beta) )  0.020 4A 0.055 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.037 2A 0.064 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.032 4B 0.086 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.040 2B 0.105 (A,B,C,D) 
Note - The ! mark next to the figure name denotes curve value exceeded. 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) ---------------|--------------------------------------------------------Stress Load| Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------
Circ. Memb. P  |  638  638  638  638  643  643  643  643  
Circ. Bend. P  |  4916  -4916  4916  -4916  5577  -5577  5577  -5577  
Circ. Memb. MC |  0  0  0  0  0  0  0  0  
Circ. Bend. MC |  0  0  0  0  0  0  0  0  
Circ. Memb. ML |  0  0  0  0  0  0  0  0  
Circ. Bend. ML |  0  0  0  0  0  0  0  0  
| 
 Tot. Circ. Str.|  5555  -4278  5555  -4278  6220  -4933  6220  -4933  

------------------------------------------------------------------------Long. Memb. P | 651 651 651 651 642 642 642 642 Long. Bend. P | 5218 -5218 5218 -5218 4267 -4267 4267 -4267 Long. Memb. MC | 0 0 0 0 0 0 0 0 Long. Bend. MC | 0 0 0 0 0 0 0 0 Long. Memb. ML | 0 0 0 0 0 0 0 0 Long. Bend. ML | 0 0 0 0 0 0 0 0 
| Tot. Long. Str.|  5870 -4567 5870 -4567 4909 -3624 4909 -3624 ------------------------------------------------------------------------
Shear VC | 0 0 0 0 0 0 0 0 Shear VL | 0 0 0 0 0 0 0 0 Shear MT | 0 0 0 0 0 0 0 0 
| Tot. Shear| 0 0 0 0 0 0 0 0 
------------------------------------------------------------------------Str. Int. | 5870 4567 5870 4567 6220 4933 6220 4933 ------------------------------------------------------------------------
Dimensionless Parameters used : Gamma = 35.14 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Dimensionless Loads for Cylindrical Shells at Pad edge:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.218 4C 4.791 (A,B)  N(PHI) / ( P/Rm )  0.218 3C 2.984 (C,D)  M(PHI) / ( P ) 0.159 2C1 0.054 (A,B)  M(PHI) / ( P ) 0.159 1C 0.085 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.156 3A 1.345 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.170 1A 0.085 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.188 3B 3.690 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.179 1B 0.031 (A,B,C,D) 
N(x) / ( P/Rm )  0.191 3C 3.450 (A,B) N(x) / ( P/Rm )  0.191 4C 5.089 (C,D) M(x) / ( P ) 0.196 1C1 0.072 (A,B) M(x) / ( P ) 0.196 2C ! 0.039 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.156 4A 2.205 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.205 2A 0.038 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.188 4B 1.421 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.206 2B 0.040 (A,B,C,D) 
Note - The ! mark next to the figure name denotes curve value exceeded. 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 

Stresses in the Vessel at the Edge of Reinforcing Pad
 ------------------------------------------------------------------------| Stress Values at 
Type of | (psi ) ---------------|--------------------------------------------------------Stress Load| Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------
Circ. Memb. P  |  1309  1309  1309  1309  815  815  815  815  
Circ. Bend. P  |  3112  -3112  3112  -3112  4913  -4913  4913  -4913  
Circ. Memb. MC |  0  0  0  0  0  0  0  0  
Circ. Bend. MC |  0  0  0  0  0  0  0  0  
Circ. Memb. ML |  0  0  0  0  0  0  0  0  
Circ. Bend. ML |  0  0  0  0  0  0  0  0  
| 
 Tot. Circ. Str.|  4422  -1802  4422  -1802  5728  -4097  5728  -4097  

------------------------------------------------------------------------Long. Memb. P | 943 943 943 943 1391 1391 1391 1391 Long. Bend. P | 4169 -4169 4169 -4169 2242 -2242 2242 -2242 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Long. Memb. MC | 0 0 0 0 0 0 0 0 Long. Bend. MC | 0 0 0 0 0 0 0 0 Long. Memb. ML | 0 0 0 0 0 0 0 0 Long. Bend. ML | 0 0 0 0 0 0 0 0 
| Tot. Long. Str.|  5112 -3226 5112 -3226 3634 -851 3634 -851 ------------------------------------------------------------------------
Shear VC | 0 0 0 0 0 0 0 0 Shear VL | 0 0 0 0 0 0 0 0 Shear MT | 0 0 0 0 0 0 0 0 
| Tot. Shear| 0 0 0 0 0 0 0 0 
------------------------------------------------------------------------Str. Int. | 5112 3226 5112 3226 5728 4097 5728 4097 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  0 0 0 0 0 0 0 0 Circ. Pl (SUS) |  638 638 638 638 643 643 643 643 Circ. Q (SUS) |  4916 -4916 4916 -4916 5577 -5577 5577 -5577 ------------------------------------------------------------------------Long. Pm (SUS) |  0 0 0 0 0 0 0 0 Long. Pl (SUS) |  651 651 651 651 642 642 642 642  Long. Q  (SUS) |  5218 -5218 5218 -5218 4267 -4267 4267 -4267 ------------------------------------------------------------------------Shear Pm (SUS) |  0 0 0 0 0 0 0 0 Shear Pl (SUS) |  0 0 0 0 0 0 0 0 Shear Q (SUS) |  0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm (SUS) | 0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm+Pl (SUS) | 651 651 651 651 643 643 643 643 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  5870 4567 5870 4567 6220 4933 6220 4933 ------------------------------------------------------------------------
------------------------------------------------------------------------Type of | Max. S.I. S.I. Allowable | Result 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Left Side  Step:  10   1:43p  Apr 4,2014 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 0 16700 | Passed Pm+Pl (SUS) | 651 25050 | Passed  Pm+Pl+Q (TOTAL)|  6220 50100 | Passed ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Reinforcing Pad Edge
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  0 0 0 0 0 0 0 0 Circ. Pl (SUS) |  1309 1309 1309 1309 815 815 815 815 Circ. Q (SUS) |  3112 -3112 3112 -3112 4913 -4913 4913 -4913 ------------------------------------------------------------------------Long. Pm (SUS) |  0 0 0 0 0 0 0 0 Long. Pl (SUS) |  943 943 943 943 1391 1391 1391 1391  Long. Q  (SUS) |  4169 -4169 4169 -4169 2242 -2242 2242 -2242 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   0  0  0  0  0  0  0  0  
Shear Q (SUS) |   0  0  0  0  0  0  0  0  

------------------------------------------------------------------------Pm (SUS) | 0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm+Pl (SUS) | 1309 1309 1309 1309 1391 1391 1391 1391 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  5112 3226 5112 3226 5728 4097 5728 4097 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 0 16700 | Passed Pm+Pl (SUS) | 1391 25050 | Passed  Pm+Pl+Q (TOTAL)|  5728 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Lifting Lug Calculations: Lug(s) on Right End of Vessel 
Input Values:
 Lifting Lug Material   SA-283 C  Lifting Lug Yield Stress Yield 30007.25 psi 
Total Height of Lifting Lug  w 11.0236 in Thickness of Lifting Lug  t 0.7874 in Diameter of Hole in Lifting Lug  dh 1.4961 in Radius of Semi-Circular Arc of Lifting Lug  r 3.1496 in Height of Lug from bottom to Center of Hole h 5.5118 in Offset from Vessel OD to Center of Hole off 5.5118 in Lug Fillet Weld Size tw 0.6299 in Length of weld along side of Lifting Lug  wl 11.0236 in Length of Weld along Bottom of Lifting Lug  wb 0.7874 in Thickness of Collar (if any)  tc 0.0000 in Diameter of Collar (if any)  dc 0.0000 in Impact Factor Impfac 2.00  Sling Angle from Horizontal 90.0000 deg Number of Lugs in Group 2 
Lifting Lug Orientation to Vessel: Perpendicular 
Lift Orientation : Horizontal Lift 
PV Elite does not compute weak axis bending forces on the lugs. It is assumed that a spreader bar is used. 

Computed Results:
 Force Along Vessel Axis Fax 0.00 lbf Force Normal to Vessel Fn 7632.55 lbf Force Tangential to Vessel Ft 0.00 lbf 
Converting the weld leg dimension (tw) to the weld throat dimension. 

Weld Group Inertia Calculations:
 Weld Group Inertia about the Circumferential Axis Ilc 122.507 in**4 Weld Group Centroid distance in the Long. Direction Yll 5.957 in Dist. of Weld Group Centroid from Lug bottom Yll_b 5.512 in Weld Group Inertia about the Longitudinal Axis Ill 0.486 in**4 Weld Group Centroid Distance in the Circ. Direction Ylc 0.394 in 
Note: The Impact Factor is applied to the Forces acting on the Lug. 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Primary Shear Stress in the Welds due to Shear Loads [Ssll]:
 = sqrt( Fax2 + Ft2 + Fn2 )/(( 2 * (wl + wb) ) * tw ) = sqrt(02+02+76322)/((2*(11.0+0.8))*0.4454) = 725.51 psi 
Shear Stress in the Welds due to Bending Loads [Sblf]: 
= (Fn*(h-Yll_b)) *Yll/Ilc + (Fax*off *Yll/Ilc) + (Ft*off *Ylc/Ill) 
= (7632 *(5.512 -5.512 )) * 5.957/122.507 + (0 *5.512 * 5.957/122.507 ) + (0 *5.512 * 0.394/0.486 ) 
= 0.00 psi 
Total Shear Stress for Combined Loads [St]: 
= Ssll + Sblf = 725.515 + 0.000 = 725.51 psi 
Allowable Shear Stress for Combined Loads [Sta]: 
= 0.4 * Yield * Occfac (AISC Shear Allowable) = 0.4 * 30007 * 1.00 = 12002.90 psi 
Shear Stress in Lug above Hole [Shs]:
 = sqrt( Pl2 + Fax2 ) / Sha = sqrt( 76322 + 02 )/3.782 = 2018.12 psi 
Allowable Shear Stress in Lug above Hole [Sas]: 
= 0.4 * Yield * Occfac = 0.4 * 30007 * 1.00 = 12002.90 psi 
Pin Hole Bearing Stress [Pbs]:
 = sqrt( Fax2 + Fn2 ) / ( t * dh ) = sqrt( 02 + 76322 )/( 0.787 * 1.496 ) = 6479.23 psi 
Allowable Bearing Stress [Pba]: 
= min( 0.75 * Yield * Occfac, 0.9 * Yield ) AISC Bearing All. = min( 0.75 * 30007 * 1.00 , 27006.5 ) = 22505.44 psi 
Bending Stress at the Base of the Lug [Fbs]: 
= Ft * off/(w * t2/6) + Fax * off/(w2 * t/6) = 0 * 5.512/(11.024 * 0.7872/6) + 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
0 * 5.512/(11.0242 * 0.787/6) = 0.00 psi 
Tensile Stress at the Base of the Lug [Fa]: 
= Fn / (w * t) = 0/(11.024 * 0.787 ) = 879.32 psi 
Total Combined Stress at the Base of the Lug: 
= Fbs + Fa = 0.0 + 879.3 = 879.32 psi 
Lug Allowable Stress for Bending and Tension: 
= min( 0.66 * Yield * Occfac, 0.75 * Yield ) = min( 0.66 * 30007 * 1.00 , 22505.4 ) = 19804.79 psi 
Required Shackle Pin Diameter [Spd]: 
= sqrt[(2 * sqrt(Fn2 + Fax2)/( Pi * Sta))] = sqrt[2 * sqrt(76322 + 02)/( Pi * 12002 )] = 0.6363 in 
WRC 107/537 Stress Analysis for the Lifting Lug to Shell Junction in the new and Cold Condition (no corrosion applied). 
Note: Since Beta1/Beta2 >= 0.25, C22 (C22p) is adjusted per table 6 in paragraph 4.3 of WRC Bulletin 107. 
Input Echo, WRC107/537 Item  1,  Description: Lift Lug
 Diameter Basis for Vessel Vbasis ID Cylindrical or Spherical Vessel Cylsph Cylindrical Internal Corrosion Allowance Cas 0.0000 in Vessel Diameter Dv 60.000 in Vessel Thickness Tv 0.866 in 
 Design Temperature  100.00 癋
 Attachment Type Type Rectangular Parameter C11 C11 0.79 in Parameter C22 C22 3.15 in 
Thickness of Reinforcing Pad Tpad 0.630 in Pad Parameter C11P C11p 7.874 in Pad Parameter C22P C22p 13.780 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Design Internal Pressure Dp 0.000 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P -7632.5 lbf Longitudinal Shear (SUS) Vl 0.0 lbf Circumferential Shear (SUS) Vc 0.0 lbf Circumferential Moment (SUS) Mc 0.0 ft-lbf Longitudinal Moment (SUS) Ml 0.0 ft-lbf Torsional Moment (SUS) Mt 0.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P -7632.5 lbf Circumferential Shear VC 0.0 lbf Longitudinal Shear VL 0.0 lbf Circumferential Moment MC 0.0 ft-lbf Longitudinal Moment ML 0.0 ft-lbf Torsional Moment MT 0.0 ft-lbf 
Dimensionless Parameters used : Gamma = 20.55 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.038 4C 4.078 (A,B)  N(PHI) / ( P/Rm )  0.038 3C 4.109 (C,D)  M(PHI) / ( P ) 0.023 2C1 0.255 (A,B)  M(PHI) / ( P ) 0.023 1C 0.289 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.020 3A 0.038 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.026 1A ! 0.105 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.032 3B 0.391 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.029 1B ! 0.065 (A,B,C,D) 
N(x) / ( P/Rm )  0.031 3C 4.159 (A,B) N(x) / ( P/Rm )  0.031 4C 4.104 (C,D) M(x) / ( P ) 0.032 1C1 0.270 (A,B) M(x) / ( P ) 0.032 2C 0.221 (C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
N(x) / ( MC/(Rm**2 * Beta) )  0.020 4A 0.055 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.037 2A 0.064 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.032 4B 0.086 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.040 2B 0.105 (A,B,C,D) 
Note - The ! mark next to the figure name denotes curve value exceeded. 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) ---------------|--------------------------------------------------------Stress Load| Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------
Circ. Memb. P  |  676  676  676  676  681  681  681  681  
Circ. Bend. P  |  5208  -5208  5208  -5208  5907  -5907  5907  -5907  
Circ. Memb. MC |  0  0  0  0  0  0  0  0  
Circ. Bend. MC |  0  0  0  0  0  0  0  0  
Circ. Memb. ML |  0  0  0  0  0  0  0  0  
Circ. Bend. ML |  0  0  0  0  0  0  0  0  
| 
 Tot. Circ. Str.|  5884  -4531  5884  -4531  6589  -5225  6589  -5225  

------------------------------------------------------------------------Long. Memb. P | 690 690 690 690 680 680 680 680 Long. Bend. P | 5528 -5528 5528 -5528 4519 -4519 4519 -4519 Long. Memb. MC | 0 0 0 0 0 0 0 0 Long. Bend. MC | 0 0 0 0 0 0 0 0 Long. Memb. ML | 0 0 0 0 0 0 0 0 Long. Bend. ML | 0 0 0 0 0 0 0 0 
| Tot. Long. Str.|  6218 -4838 6218 -4838 5200 -3838 5200 -3838 ------------------------------------------------------------------------
Shear VC | 0 0 0 0 0 0 0 0 Shear VL | 0 0 0 0 0 0 0 0 Shear MT | 0 0 0 0 0 0 0 0 
| Tot. Shear| 0 0 0 0 0 0 0 0 
------------------------------------------------------------------------Str. Int. | 6218 4838 6218 4838 6589 5225 6589 5225 ------------------------------------------------------------------------
Dimensionless Parameters used : Gamma = 35.14 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Dimensionless Loads for Cylindrical Shells at Pad edge:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.218 4C 4.791 (A,B)  N(PHI) / ( P/Rm )  0.218 3C 2.984 (C,D)  M(PHI) / ( P ) 0.159 2C1 0.054 (A,B)  M(PHI) / ( P ) 0.159 1C 0.085 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.156 3A 1.345 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.170 1A 0.085 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.188 3B 3.690 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.179 1B 0.031 (A,B,C,D) 
N(x) / ( P/Rm )  0.191 3C 3.450 (A,B) N(x) / ( P/Rm )  0.191 4C 5.089 (C,D) M(x) / ( P ) 0.196 1C1 0.072 (A,B) M(x) / ( P ) 0.196 2C ! 0.039 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.156 4A 2.205 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.205 2A 0.038 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.188 4B 1.421 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.206 2B 0.040 (A,B,C,D) 
Note - The ! mark next to the figure name denotes curve value exceeded. 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 

Stresses in the Vessel at the Edge of Reinforcing Pad
 ------------------------------------------------------------------------| Stress Values at 
Type of | (psi ) ---------------|--------------------------------------------------------Stress Load| Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------
Circ. Memb. P  |  1387  1387  1387  1387  864  864  864  864  
Circ. Bend. P  |  3297  -3297  3297  -3297  5204  -5204  5204  -5204  
Circ. Memb. MC |  0  0  0  0  0  0  0  0  
Circ. Bend. MC |  0  0  0  0  0  0  0  0  
Circ. Memb. ML |  0  0  0  0  0  0  0  0  
Circ. Bend. ML |  0  0  0  0  0  0  0  0  
| 
 Tot. Circ. Str.|  4684  -1909  4684  -1909  6068  -4340  6068  -4340  

------------------------------------------------------------------------Long. Memb. P | 998 998 998 998 1473 1473 1473 1473 Long. Bend. P | 4416 -4416 4416 -4416 2375 -2375 2375 -2375 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Long. Memb. MC | 0 0 0 0 0 0 0 0 Long. Bend. MC | 0 0 0 0 0 0 0 0 Long. Memb. ML | 0 0 0 0 0 0 0 0 Long. Bend. ML | 0 0 0 0 0 0 0 0 
| Tot. Long. Str.|  5415 -3417 5415 -3417 3849 -902 3849 -902 ------------------------------------------------------------------------
Shear VC | 0 0 0 0 0 0 0 0 Shear VL | 0 0 0 0 0 0 0 0 Shear MT | 0 0 0 0 0 0 0 0 
| Tot. Shear| 0 0 0 0 0 0 0 0 
------------------------------------------------------------------------Str. Int. | 5415 3417 5415 3417 6068 4340 6068 4340 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  0 0 0 0 0 0 0 0 Circ. Pl (SUS) |  676 676 676 676 681 681 681 681 Circ. Q (SUS) |  5208 -5208 5208 -5208 5907 -5907 5907 -5907 ------------------------------------------------------------------------Long. Pm (SUS) |  0 0 0 0 0 0 0 0 Long. Pl (SUS) |  690 690 690 690 680 680 680 680  Long. Q  (SUS) |  5528 -5528 5528 -5528 4519 -4519 4519 -4519 ------------------------------------------------------------------------Shear Pm (SUS) |  0 0 0 0 0 0 0 0 Shear Pl (SUS) |  0 0 0 0 0 0 0 0 Shear Q (SUS) |  0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm (SUS) | 0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm+Pl (SUS) | 690 690 690 690 681 681 681 681 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  6218 4838 6218 4838 6589 5225 6589 5225 ------------------------------------------------------------------------
------------------------------------------------------------------------Type of | Max. S.I. S.I. Allowable | Result 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Lifting Lug Calcs : Right Side  Step:  11   1:43p  Apr 4,2014 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 0 16700 | Passed Pm+Pl (SUS) | 690 25050 | Passed  Pm+Pl+Q (TOTAL)|  6589 50100 | Passed ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Reinforcing Pad Edge
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  0 0 0 0 0 0 0 0 Circ. Pl (SUS) |  1387 1387 1387 1387 864 864 864 864 Circ. Q (SUS) |  3297 -3297 3297 -3297 5204 -5204 5204 -5204 ------------------------------------------------------------------------Long. Pm (SUS) |  0 0 0 0 0 0 0 0 Long. Pl (SUS) |  998 998 998 998 1473 1473 1473 1473  Long. Q  (SUS) |  4416 -4416 4416 -4416 2375 -2375 2375 -2375 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   0  0  0  0  0  0  0  0  
Shear Q (SUS) |   0  0  0  0  0  0  0  0  

------------------------------------------------------------------------Pm (SUS) | 0 0 0 0 0 0 0 0 ------------------------------------------------------------------------Pm+Pl (SUS) | 1387 1387 1387 1387 1473 1473 1473 1473 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  5415 3417 5415 3417 6068 4340 6068 4340 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 0 16700 | Passed Pm+Pl (SUS) | 1473 25050 | Passed  Pm+Pl+Q (TOTAL)|  6068 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
ASME Horizontal Vessel Analysis: Stresses for the Left Saddle 
(per ASME Sec. VIII Div. 2 based on the Zick method.) 
Horizontal Vessel Stress Calculations : Operating Case 
Note: Wear Pad Width (11.81) is less than 1.56*sqrt(rm*t)       and less than 2a. The wear plate will be ignored. 
Minimum Wear Plate Width to be considered in analysis [b1]: 
= min( b + 1.56*sqrt( Rm * t ), 2a ) = min( 7.250 + 1.56*sqrt( 30.4331 * 0.8661 ), 2 * 21.000 ) = 15.2593 in 

Input and Calculated Values: 
Vessel Mean Radius  Rm  30.43  in  
Stiffened Vessel Length per 4.15.6  L  12.50  ft  
Distance from Saddle to Vessel tangent  a  21.00  in  

Saddle Width b 7.25 in Saddle Bearing Angle  theta 120.00 degrees 
Inside Depth of Head h2 1.25 ft 
Shell Allowable Stress used in Calculation 16700.00 psi Head Allowable Stress used in Calculation 16700.00 psi Circumferential Efficiency in Plane of Saddle 1.00 Circumferential Efficiency at Mid-Span 1.00 
Saddle Force Q, Operating Case 12591.57 lbf 
Horizontal Vessel Analysis Results: Actual      Allowable
 -------------------------------------------------------------------Long. Stress at Top of Midspan 6308.78 16700.00 psi Long. Stress at Bottom of Midspan 6450.18 16700.00 psi Long. Stress at Top of Saddles 6520.18 16700.00 psi Long. Stress at Bottom of Saddles 6301.49 16700.00 psi 
Tangential Shear in Shell 355.27 10020.00 psi Circ. Stress at Horn of Saddle 1393.75 20875.00 psi Circ. Compressive Stress in Shell 72.43 16700.00 psi 


Intermediate Results: Saddle Reaction Q due to Wind or Seismic 
Saddle Reaction Force due to Wind Ft [Fwt]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
= Ftr * ( Ft/Num of Saddles + Z Force Load ) * B / E = 3.00 * ( 1978.4/2 + 0 ) * 43.0000/52.7116 = 2420.8 lbf 
Saddle Reaction Force due to Wind Fl or Friction [Fwl]: 
= max( Fl, Friction Load, Sum of X Forces) * B / Ls = max( 1160.64 , 0.00 , 0 ) * 43.0000/108.0000 = 462.1 lbf 
Saddle Reaction Force due to Earthquake Fl or Friction [Fsl]: 
= max( Fl, Friction Force, Sum of X Forces ) * B / Ls = max( 416.00 , 0.00 , 0 ) * 43.0000/108.0000 = 165.6 lbf 
Saddle Reaction Force due to Earthquake Ft [Fst]: 
= Ftr * ( Ft/Num of Saddles + Z Force Load ) * B / E = 3.00 * ( 415/2 + 0 ) * 43.0000/52.7116 = 509.0 lbf 
Load Combination Results for Q + Wind or Seismic [Q]: 
= Saddle Load + Max( Fwl, Fwt, Fsl, Fst ) = 10170 + Max( 462 , 2420 , 165 , 509 ) = 12591.6 lbf 
Summary of Loads at the base of this Saddle:
 Vertical Load (including saddle weight) 13142.88 lbf Transverse Shear Load Saddle 989.19 lbf Longitudinal Shear Load Saddle 1160.64 lbf 
Formulas and Substitutions for Horizontal Vessel Analysis: 
Note: Wear Plate is Welded to the Shell, k = 0.1 


The Computed K values from Table 4.15.1:
 K1 = 0.1066 K2 = 1.1707 K3 = 0.8799 K4 = 0.4011 K5 = 0.7603 K6 = 0.0529 K7 = 0.0283 K8 = 0.3405 K9 = 0.2711 K10 = 0.0581 K1* = 0.1923 
Note: Dimension a is greater than or equal to Rm / 2. 
Moment per Equation 4.15.3 [M1]: 
= -Q*a [1 - (1- a/L + (R2-h22)/(2a*L))/(1+(4h2)/3L)] = -12591*1.75[1-(1-1.75/12.50+(2.5362-1.2502)/ (2*1.75*12.50))/(1+(4*1.25)/(3*12.50))] = -3150.4 ft-lbf 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Moment per Equation 4.15.4 [M2]:
 = Q*L/4(1+2(R2-h22)/(L2))/(1+(4h2)/( 3L))-4a/L = 12591*12.5/4(1+2(2.5362-1.2502)/(12.502))/(1+(4*1.250)/ (3*12.500))-4*1.75/12.50 = 14848.1 ft-lbf 
Longitudinal Stress at Top of Shell (4.15.6) [Sigma1]: 
= P * Rm/(2t) - M2/(pi*Rm2t) = 363.127 * 30.433/(2*0.866 ) - 178177.0/(pi*30.42*0.866 ) = 6308.78 psi 
Longitudinal Stress at Bottom of Shell (4.15.7) [Sigma2]: 
= P * Rm/(2t) + M2/(pi * Rm2 * t) = 363.127 * 30.433/(2 * 0.866 ) + 178177.0/(pi * 30.42 * 0.866 ) = 6450.18 psi 
Longitudinal Stress at Top of Shell at Support (4.15.10)    [Sigma*3]: 
= P * Rm/(2t) - M1/(K1*pi*Rm2t) = 363.127*30.433/(2*0.866)--37805.4/(0.1066*pi*30.42*0.866) = 6520.18 psi 
Longitudinal Stress at Bottom of Shell at Support (4.15.11) [Sigma*4]: 
= P * Rm/(2t) + M1/(K1* * pi * Rm2 * t) = 363.127*30.433/(2*0.866)+-37805.4/(0.1923*pi*30.42*0.866) = 6301.49 psi 
Maximum Shear Force in the Saddle (4.15.5) [T]:
 = Q(L-2a)/(L+(4*h2/3)) = 12591 ( 12.50 - 2 * 1.75 )/(12.50 + ( 4 * 1.25/3)) = 7999.3 lbf 
Shear Stress in the shell no rings,  not stiffened (4.15.14)   [tau2]: 
= K2 * T / ( Rm * t ) = 1.1707 * 7999.35/( 30.4331 * 0.8661 ) = 355.27 psi 
Decay Length (4.15.22)  [x1,x2]: 
= 0.78 * sqrt( Rm * t ) = 0.78 * sqrt( 30.433 * 0.866 ) = 4.005 in 
Circumferential Stress in shell, no rings (4.15.23) [sigma6]: 
= -K5 * Q * k / ( t * ( b + X1 + X2 ) ) = -0.7603 * 12591 * 0.1/( 0.866 * ( 7.25 + 4.00 + 4.00 ) ) = -72.43 psi 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Circ. Comp. Stress at Horn of Saddle, L<8Rm (4.15.25) [sigma7*]: 
= -Q/(4*t*(b+X1+X2)) - 12*K7*Q*Rm/(L*t2) = -12591/(4*0.866 *(7.250 +4.005 +4.005 )) -12 * 0.028 * 12591 * 30.433/(12.500 * 0.8662) = -1393.75 psi 
Effective reinforcing plate width  (4.15.1) [B1]: 
= min( b + 1.56 * sqrt( Rm * t ), 2a ) 
= min( 7.25 + 1.56 * sqrt( 30.433 * 0.866 ), 2 * 21.000 ) 
= 15.26 in 
Free Un-Restrained Thermal Expansion between the Saddles [Exp]: 
= Alpha * Ls * ( Design Temperature - Ambient Temperature ) 
= 0.909E-05 * 108.000 * ( 248.0 - 70.0 ) 
= 0.175 in 
Results for Vessel Ribs, Web and Base:
 Baseplate Length  Bplen 54.0000 in Baseplate Thickness Bpthk 0.6299 in Baseplate Width Bpwid 8.0000 in Number of Ribs ( inc. outside ribs ) Nribs 4 Rib Thickness Ribtk 0.5512 in Web Thickness Webtk 0.5512 in Web Location Webloc Center 
Moment of Inertia of Saddle - Lateral Direction
 Y A          AY          Io Shell 0. 17. 7. 4. Wearplate 1. 6. 6. 7. Web 5. 4. 24. 149. BasePlate 10. 5. 49. 470. Totals 17. 32. 86. 630. 
Value C1 = Sumof(Ay)/Sumof(A) = 3. in Value I = Sumof(Io) -C1*Sumof(Ay) = 401. in**4 Value As = Sumof(A) -Ashell = 15. in^2 
K1 = (1+Cos(beta)-.5*Sin(beta)2 )/(pi-beta+Sin(beta)*Cos(beta)) = 0.2035 
Fh = K1 * Q = 0.2035 * 12591.568 = 2562.6575 lbf 
Tension Stress, St = ( Fh/As )  = 170.5147 psi Allowed Stress, Sa = 0.6 * Yield Str = 20880.0000 psi 
d = B -R*Sin(theta) / theta = 15.1589 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
 Bending Moment, M = Fh * d = 3237.2664 ft-lbf 
 Bending Stress, Sb = ( M * C1 / I ) = 258.1586 psi Allowed Stress, Sa = 2/3 * Yield Str = 23200.0000 psi 
Minimum Thickness of Baseplate per Moss : 
= ( 3 * ( Q + Saddle_Wt ) * BasePlateWidth / ( 4 * BasePlateLength * 
AllStress )).5 = ( 3 * (12591 + 551 ) * 8.00/( 4 * 54.000 * 23200.000 )).5 = 0.251 in 
Calculation of Axial Load, Intermediate Values and Compressive Stress 
Effective Baseplate Length [e]: 
= ( Bplen - Clearance ) / ( Nribs - 1) = ( 54.0000 - 1.0 )/( 4 - 1 ) = 17.6667 in 
Baseplate Pressure Area [Ap]: 
= e * Bpwid / 2 = 17.6667 * 8.0000/2 = 70.6667 in^2 
Axial Load [P]: 
= Ap * Bp = 70.7 * 29.15 = 2059.7 lbf 
Area of the Rib and Web [Ar]: 
= ( Bpwid - Clearance - Webtk ) * Ribtk + e/2 * Webtk = ( 8.000 - 1.0 - 0.551 ) * 0.551 + 17.6667/2 * 0.551 = 8.423 in^2 
Compressive Stress [Sc]:
 = P/Ar = 2059.7/8.4232 = 244.5298 psi 
Check of Outside Ribs: Inertia of Saddle, Outer Ribs - Longitudinal Direction
 Y A          AY        Ay2       Io Rib 3.6 3.6 13.1 0.0 16.6 Web 3.6 4.9 17.6 0.0 0.2 Values 3.6 8.5 30.8 0.0 16.9 
Bending Moment [Rm]: 
= Fl /( 2 * Bplen ) * e * rl / 2 = 1160.6/( 2 * 54.00 ) * 17.667 * 24.54/2 = 194.096 ft-lbf 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
KL/R < Cc ( 17.3422 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 17.34 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(17.34 )/(8* 128.25 )-( 17.343)/(8*128.253) Sca = 20081.88 psi 
AISC Unity Check on Outside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 244.53/20081.88 + (2329.15/4.651 )/23200.00 Check = 0.03 
Check of Inside Ribs Inertia of Saddle, Inner Ribs - Axial Direction
 Y A          AY        Ay2       Io Rib 3.5 3.6 12.4 0.0 15.8 Web 3.5 9.7 34.1 0.0 0.2 Values 3.5 13.3 46.5 0.0 16.0 
KL/R < Cc ( 9.0239 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 9.02 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(9.02 )/(8* 128.25 )-( 9.023)/(8*128.253) Sca = 20504.26 psi 

AISC Unity Check on Inside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 309.92/20504.26 + ( 1879.76/4.572 )/23200.00 Check = 0.03 

Input Data for Base Plate Bolting Calculations:
 Total Number of Bolts per BasePlate Nbolts 8 Total Number of Bolts in Tension/Baseplate Nbt 4 Bolt Material Specification SA-307 B Bolt Allowable Stress Stba 7000.00 psi Bolt Corrosion Allowance Bca 0.1180 in Distance from Bolts to Edge Edgedis 4.1650 in Nominal Bolt Diameter Bnd 0.8750 in Thread Series Series UNC BasePlate Allowable Stress S 13800.00 psi Area Available in a Single Bolt BltArea 0.1920 in^2 Saddle Load QO (Weight)  QO 10722.1 lbf Saddle Load QL (Wind/Seismic contribution)  QL 462.1 lbf Maximum Transverse Force Ft 989.2 lbf 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Maximum Longitudinal Force Fl 1160.6 lbf Saddle Bolted to Steel Foundation No 
Bolt Area Calculation per Dennis R. Moss 
Bolt Area Requirement Due to Longitudinal Load [Bltarearl]: 
= 0.0 (QO > QL --> No Uplift in Longitudinal direction) 
Bolt Area due to Shear Load [Bltarears]: 
= Fl / (Stba * Nbolts) = 1160.64/(7000.00 * 8.00 ) = 0.0207 in^2 
Bolt Area due to Transverse Load 
Moment on Baseplate Due to Transverse Load [Rmom]: 
= B * Ft + Sum of X Moments = 3.58 * 989.19 + 0.00 = 3544.59 ft-lbf 
Eccentricity (e): 
= Rmom / QO = 42535.03/10722.06 = 3.97 in < Bplen/6 --> No Uplift in Transverse direction 
Bolt Area due to Transverse Load [Bltareart]: 
= 0 (No Uplift) 
Required of a Single Bolt [Bltarear] 
= max[Bltarearl, Bltarears, Bltareart] = max[0.0000 , 0.0207 , 0.0000 ] = 0.0207 in^2 

ASME Horizontal Vessel Analysis: Stresses for the Right Saddle 
(per ASME Sec. VIII Div. 2 based on the Zick method.) 
Note: Wear Pad Width (11.81) is less than 1.56*sqrt(rm*t)       and less than 2a. The wear plate will be ignored. 
Minimum Wear Plate Width to be considered in analysis [b1]: 
= min( b + 1.56*sqrt( Rm * t ), 2a ) = min( 7.250 + 1.56*sqrt( 30.4331 * 0.8661 ), 2 * 21.000 ) = 15.2593 in 
Input and Calculated Values: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Vessel Mean Radius  Rm  30.43  in  
Stiffened Vessel Length per 4.15.6  L  12.50  ft  
Distance from Saddle to Vessel tangent  a  21.00  in  

Saddle Width b 7.25 in Saddle Bearing Angle  theta 120.00 degrees 
Inside Depth of Head h2 1.25 ft 
Shell Allowable Stress used in Calculation 16700.00 psi Head Allowable Stress used in Calculation 16700.00 psi Circumferential Efficiency in Plane of Saddle 1.00 Circumferential Efficiency at Mid-Span 1.00 
Saddle Force Q, Operating Case 12371.71 lbf 
Horizontal Vessel Analysis Results: Actual      Allowable
 -------------------------------------------------------------------Long. Stress at Top of Midspan 6310.01 16700.00 psi Long. Stress at Bottom of Midspan 6448.94 16700.00 psi Long. Stress at Top of Saddles 6517.73 16700.00 psi Long. Stress at Bottom of Saddles 6302.85 16700.00 psi 
Tangential Shear in Shell 349.07 10020.00 psi Circ. Stress at Horn of Saddle 1369.41 20875.00 psi Circ. Compressive Stress in Shell 71.17 16700.00 psi 

Intermediate Results: Saddle Reaction Q due to Wind or Seismic 
Saddle Reaction Force due to Wind Ft [Fwt]: 
= Ftr * ( Ft/Num of Saddles + Z Force Load ) * B / E 
= 3.00 * ( 1978.4/2 + 0 ) * 43.0000/52.7116 
= 2420.8 lbf 
Saddle Reaction Force due to Wind Fl or Friction [Fwl]: 
= max( Fl, Friction Load, Sum of X Forces) * B / Ls 
= max( 1160.64 , 0.00 , 0 ) * 43.0000/108.0000 
= 462.1 lbf 
Saddle Reaction Force due to Earthquake Fl or Friction [Fsl]: 
= max( Fl, Friction Force, Sum of X Forces ) * B / Ls 
= max( 416.00 , 0.00 , 0 ) * 43.0000/108.0000 
= 165.6 lbf 
Saddle Reaction Force due to Earthquake Ft [Fst]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
= Ftr * ( Ft/Num of Saddles + Z Force Load ) * B / E = 3.00 * ( 415/2 + 0 ) * 43.0000/52.7116 = 509.0 lbf 
Load Combination Results for Q + Wind or Seismic [Q]: 
= Saddle Load + Max( Fwl, Fwt, Fsl, Fst ) = 9950 + Max( 462 , 2420 , 165 , 509 ) = 12371.7 lbf 
Summary of Loads at the base of this Saddle:
 Vertical Load (including saddle weight) 12923.02 lbf Transverse Shear Load Saddle 989.19 lbf Longitudinal Shear Load Saddle 1160.64 lbf 
Formulas and Substitutions for Horizontal Vessel Analysis: 
Note: Wear Plate is Welded to the Shell, k = 0.1 


The Computed K values from Table 4.15.1:
 K1 = 0.1066 K2 = 1.1707 K3 = 0.8799 K4 = 0.4011 K5 = 0.7603 K6 = 0.0529 K7 = 0.0283 K8 = 0.3405 K9 = 0.2711 K10 = 0.0581 K1* = 0.1923 
Note: Dimension a is greater than or equal to Rm / 2. 
Moment per Equation 4.15.3 [M1]: 
= -Q*a [1 - (1- a/L + (R2-h22)/(2a*L))/(1+(4h2)/3L)] = -12371*1.75[1-(1-1.75/12.50+(2.5362-1.2502)/ (2*1.75*12.50))/(1+(4*1.25)/(3*12.50))] = -3095.4 ft-lbf 
Moment per Equation 4.15.4 [M2]:
 = Q*L/4(1+2(R2-h22)/(L2))/(1+(4h2)/( 3L))-4a/L = 12371*12.5/4(1+2(2.5362-1.2502)/(12.502))/(1+(4*1.250)/ (3*12.500))-4*1.75/12.50 = 14588.8 ft-lbf 
Longitudinal Stress at Top of Shell (4.15.6) [Sigma1]: 
= P * Rm/(2t) - M2/(pi*Rm2t) = 363.127 * 30.433/(2*0.866 ) - 175065.9/(pi*30.42*0.866 ) = 6310.01 psi 
Longitudinal Stress at Bottom of Shell (4.15.7) [Sigma2]: 
= P * Rm/(2t) + M2/(pi * Rm2 * t) = 363.127 * 30.433/(2 * 0.866 ) + 175065.9/(pi * 30.42 * 0.866 ) = 6448.94 psi 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Longitudinal Stress at Top of Shell at Support (4.15.10)    [Sigma*3]: 
= P * Rm/(2t) - M1/(K1*pi*Rm2t) = 363.127*30.433/(2*0.866)--37145.3/(0.1066*pi*30.42*0.866) = 6517.73 psi 
Longitudinal Stress at Bottom of Shell at Support (4.15.11) [Sigma*4]: 
= P * Rm/(2t) + M1/(K1* * pi * Rm2 * t) = 363.127*30.433/(2*0.866)+-37145.3/(0.1923*pi*30.42*0.866) = 6302.85 psi 
Maximum Shear Force in the Saddle (4.15.5) [T]:
 = Q(L-2a)/(L+(4*h2/3)) = 12371 ( 12.50 - 2 * 1.75 )/(12.50 + ( 4 * 1.25/3)) = 7859.7 lbf 
Shear Stress in the shell no rings,  not stiffened (4.15.14)   [tau2]: 
= K2 * T / ( Rm * t ) = 1.1707 * 7859.67/( 30.4331 * 0.8661 ) = 349.07 psi 
Decay Length (4.15.22)  [x1,x2]: 
= 0.78 * sqrt( Rm * t ) = 0.78 * sqrt( 30.433 * 0.866 ) = 4.005 in 
Circumferential Stress in shell, no rings (4.15.23) [sigma6]: 
= -K5 * Q * k / ( t * ( b + X1 + X2 ) ) = -0.7603 * 12371 * 0.1/( 0.866 * ( 7.25 + 4.00 + 4.00 ) ) = -71.17 psi 
Circ. Comp. Stress at Horn of Saddle, L<8Rm (4.15.25) [sigma7*]: 
= -Q/(4*t*(b+X1+X2)) - 12*K7*Q*Rm/(L*t2) = -12371/(4*0.866 *(7.250 +4.005 +4.005 )) -12 * 0.028 * 12371 * 30.433/(12.500 * 0.8662) = -1369.41 psi 
Effective reinforcing plate width  (4.15.1) [B1]: 
= min( b + 1.56 * sqrt( Rm * t ), 2a ) = min( 7.25 + 1.56 * sqrt( 30.433 * 0.866 ), 2 * 21.000 ) = 15.26 in 
Results for Vessel Ribs, Web and Base
 Baseplate Length  Bplen 54.0000 in Baseplate Thickness Bpthk 0.6299 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Baseplate Width Bpwid 8.0000 in Number of Ribs ( inc. outside ribs ) Nribs 4 Rib Thickness Ribtk 0.5512 in Web Thickness Webtk 0.5512 in Web Location Webloc Center 
Moment of Inertia of Saddle - Lateral Direction 
Y  A           AY           Io 
 Shell  0.  17.  7.  4.  
Wearplate  1.  6.  6.  7.  
Web  5.  4.  24.  149.  
BasePlate  10.  5.  49.  470.  
Totals  17.  32.  86.  630.  

Value C1 = Sumof(Ay)/Sumof(A) = 3. in Value I = Sumof(Io) -C1*Sumof(Ay) = 401. in**4 Value As = Sumof(A) -Ashell = 15. in^2 
K1 = (1+Cos(beta)-.5*Sin(beta)2 )/(pi-beta+Sin(beta)*Cos(beta)) = 0.2035 
Fh = K1 * Q = 0.2035 * 12371.709 = 2517.9114 lbf 
Tension Stress, St = ( Fh/As )  = 167.5374 psi Allowed Stress, Sa = 0.6 * Yield Str = 20880.0000 psi 
d = B -R*Sin(theta) / theta = 15.1589 in  Bending Moment, M = Fh * d = 3180.7410 ft-lbf 
 Bending Stress, Sb = ( M * C1 / I ) = 253.6509 psi Allowed Stress, Sa = 2/3 * Yield Str = 23200.0000 psi 
Minimum Thickness of Baseplate per Moss : 
= ( 3 * ( Q + Saddle_Wt ) * BasePlateWidth / ( 4 * BasePlateLength * 
AllStress )).5 = ( 3 * (12371 + 551 ) * 8.00/( 4 * 54.000 * 23200.000 )).5 = 0.249 in 
Calculation of Axial Load, Intermediate Values and Compressive Stress 
Effective Baseplate Length [e]: 
= ( Bplen - Clearance ) / ( Nribs - 1) 
= ( 54.0000 - 1.0 )/( 4 - 1 ) = 17.6667 in 
Baseplate Pressure Area [Ap]: 
= e * Bpwid / 2 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
= 17.6667 * 8.0000/2 = 70.6667 in^2 
Axial Load [P]: 
= Ap * Bp = 70.7 * 28.64 = 2023.8 lbf 
Area of the Rib and Web [Ar]: 
= ( Bpwid - Clearance - Webtk ) * Ribtk + e/2 * Webtk = ( 8.000 - 1.0 - 0.551 ) * 0.551 + 17.6667/2 * 0.551 = 8.423 in^2 
Compressive Stress [Sc]:
 = P/Ar = 2023.8/8.4232 = 240.2602 psi 
Check of Outside Ribs: Inertia of Saddle, Outer Ribs - Longitudinal Direction
 Y A          AY        Ay2       Io Rib 3.6 3.6 13.1 0.0 16.6 Web 3.6 4.9 17.6 0.0 0.2 Values 3.6 8.5 30.8 0.0 16.9 
Bending Moment [Rm]: 
= Fl /( 2 * Bplen ) * e * rl / 2 = 1160.6/( 2 * 54.00 ) * 17.667 * 24.54/2 = 194.096 ft-lbf 
KL/R < Cc ( 17.3422 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 17.34 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(17.34 )/(8* 128.25 )-( 17.343)/(8*128.253) Sca = 20081.88 psi 
AISC Unity Check on Outside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 240.26/20081.88 + (2329.15/4.651 )/23200.00 Check = 0.03 
Check of Inside Ribs Inertia of Saddle, Inner Ribs - Axial Direction
 Y A          AY        Ay2       Io Rib 3.5 3.6 12.4 0.0 15.8 Web 3.5 9.7 34.1 0.0 0.2 Values 3.5 13.3 46.5 0.0 16.0 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
KL/R < Cc ( 9.0239 < 128.2548 ) per AISC E2-1 
Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) 
Sca = ( 1-( 9.02 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(9.02 )/(8* 128.25 )-( 9.023)/(8*128.253) 
Sca = 20504.26 psi 
AISC Unity Check on Inside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 304.51/20504.26 + ( 1879.76/4.572 )/23200.00 Check = 0.03 

Input Data for Base Plate Bolting Calculations:
 Total Number of Bolts per BasePlate Nbolts 8 Total Number of Bolts in Tension/Baseplate Nbt 4 Bolt Material Specification SA-307 B Bolt Allowable Stress Stba 7000.00 psi Bolt Corrosion Allowance Bca 0.1180 in Distance from Bolts to Edge Edgedis 4.1650 in Nominal Bolt Diameter Bnd 0.8750 in Thread Series Series UNC BasePlate Allowable Stress S 13800.00 psi Area Available in a Single Bolt BltArea 0.1920 in^2 Saddle Load QO (Weight)  QO 10502.2 lbf Saddle Load QL (Wind/Seismic contribution)  QL 462.1 lbf Maximum Transverse Force Ft 989.2 lbf Maximum Longitudinal Force Fl 1160.6 lbf Saddle Bolted to Steel Foundation No 
Bolt Area Calculation per Dennis R. Moss 
Bolt Area Requirement Due to Longitudinal Load [Bltarearl]: 
= 0.0 (QO > QL --> No Uplift in Longitudinal direction) 
Bolt Area due to Shear Load [Bltarears]: 
= Fl / (Stba * Nbolts) 
= 1160.64/(7000.00 * 8.00 ) 
= 0.0207 in^2 
Bolt Area due to Transverse Load 
Moment on Baseplate Due to Transverse Load [Rmom]: 
= B * Ft + Sum of X Moments 
= 3.58 * 989.19 + 0.00 
= 3544.59 ft-lbf 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Ope.) : Step:  12 1:43p Apr 4,2014 
Eccentricity (e): 
= Rmom / QO 
= 42535.03/10502.20 
= 4.05 in < Bplen/6 --> No Uplift in Transverse direction 
Bolt Area due to Transverse Load [Bltareart]: 
= 0 (No Uplift) 
Required of a Single Bolt [Bltarear] 
= max[Bltarearl, Bltarears, Bltareart] 
= max[0.0000 , 0.0207 , 0.0000 ] 
= 0.0207 in^2 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
ASME Horizontal Vessel Analysis: Stresses for the Left Saddle 
(per ASME Sec. VIII Div. 2 based on the Zick method.) 
Horizontal Vessel Stress Calculations : Test Case 
Note: Wear Pad Width (11.81) is less than 1.56*sqrt(rm*t)       and less than 2a. The wear plate will be ignored. 
Minimum Wear Plate Width to be considered in analysis [b1]: 
= min( b + 1.56*sqrt( Rm * t ), 2a ) = min( 7.250 + 1.56*sqrt( 30.4331 * 0.8661 ), 2 * 21.000 ) = 15.2593 in 

Input and Calculated Values: 
Vessel Mean Radius  Rm  30.43  in  
Stiffened Vessel Length per 4.15.6  L  12.50  ft  
Distance from Saddle to Vessel tangent  a  21.00  in  

Saddle Width b 7.25 in Saddle Bearing Angle  theta 120.00 degrees 
Inside Depth of Head h2 1.25 ft 
Shell Allowable Stress used in Calculation 22500.00 psi Head Allowable Stress used in Calculation 22500.00 psi Circumferential Efficiency in Plane of Saddle 1.00 Circumferential Efficiency at Mid-Span 1.00 
Saddle Force Q, Test Case, no Ext. Forces 15756.31 lbf 
Horizontal Vessel Analysis Results: Actual      Allowable
 -------------------------------------------------------------------Long. Stress at Top of Midspan 8823.42 22500.00 psi Long. Stress at Bottom of Midspan 9000.35 22500.00 psi Long. Stress at Top of Saddles 9087.96 22500.00 psi Long. Stress at Bottom of Saddles 8814.29 22500.00 psi 
Tangential Shear in Shell 444.57 13500.00 psi Circ. Stress at Horn of Saddle 1744.05 33750.00 psi Circ. Compressive Stress in Shell 90.63 22500.00 psi 
Load Combination Results for Q + Wind or Seismic [Q]: 
= Saddle Load + Max( Fwl, Fwt, Fsl, Fst ) 
= 15756 + Max( 0 , 0 , 0 , 0 ) 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
= 15756.3 lbf 
Summary of Loads at the base of this Saddle:
 Vertical Load (including saddle weight) 16307.61 lbf Transverse Shear Load Saddle 0.00 lbf Longitudinal Shear Load Saddle 0.00 lbf 
Hydrostatic Test Pressure at center of Vessel:         507.274  psig 
Formulas and Substitutions for Horizontal Vessel Analysis: 
Note: Wear Plate is Welded to the Shell, k = 0.1 


The Computed K values from Table 4.15.1:
 K1 = 0.1066 K2 = 1.1707 K3 = 0.8799 K4 = 0.4011 K5 = 0.7603 K6 = 0.0529 K7 = 0.0283 K8 = 0.3405 K9 = 0.2711 K10 = 0.0581 K1* = 0.1923 
Note: Dimension a is greater than or equal to Rm / 2. 
Moment per Equation 4.15.3 [M1]: 
= -Q*a [1 - (1- a/L + (R2-h22)/(2a*L))/(1+(4h2)/3L)] = -15756*1.75[1-(1-1.75/12.50+(2.5362-1.2502)/ (2*1.75*12.50))/(1+(4*1.25)/(3*12.50))] = -3942.3 ft-lbf 
Moment per Equation 4.15.4 [M2]:
 = Q*L/4(1+2(R2-h22)/(L2))/(1+(4h2)/( 3L))-4a/L = 15756*12.5/4(1+2(2.5362-1.2502)/(12.502))/(1+(4*1.250)/ (3*12.500))-4*1.75/12.50 = 18580.0 ft-lbf 
Longitudinal Stress at Top of Shell (4.15.6) [Sigma1]: 
= P * Rm/(2t) - M2/(pi*Rm2t) = 507.274 * 30.433/(2*0.866 ) - 222959.7/(pi*30.42*0.866 ) = 8823.42 psi 
Longitudinal Stress at Bottom of Shell (4.15.7) [Sigma2]: 
= P * Rm/(2t) + M2/(pi * Rm2 * t) = 507.274 * 30.433/(2 * 0.866 ) + 222959.7/(pi * 30.42 * 0.866 ) = 9000.35 psi 
Longitudinal Stress at Top of Shell at Support (4.15.10)    [Sigma*3]: 
= P * Rm/(2t) - M1/(K1*pi*Rm2t) = 507.274*30.433/(2*0.866)--47307.3/(0.1066*pi*30.42*0.866) = 9087.96 psi 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Longitudinal Stress at Bottom of Shell at Support (4.15.11) [Sigma*4]: 
= P * Rm/(2t) + M1/(K1* * pi * Rm2 * t) = 507.274*30.433/(2*0.866)+-47307.3/(0.1923*pi*30.42*0.866) = 8814.29 psi 
Maximum Shear Force in the Saddle (4.15.5) [T]:
 = Q(L-2a)/(L+(4*h2/3)) = 15756 ( 12.50 - 2 * 1.75 )/(12.50 + ( 4 * 1.25/3)) = 10009.9 lbf 
Shear Stress in the shell no rings,  not stiffened (4.15.14)   [tau2]: 
= K2 * T / ( Rm * t ) = 1.1707 * 10009.89/( 30.4331 * 0.8661 ) = 444.57 psi 
Decay Length (4.15.22)  [x1,x2]: 
= 0.78 * sqrt( Rm * t ) = 0.78 * sqrt( 30.433 * 0.866 ) = 4.005 in 
Circumferential Stress in shell, no rings (4.15.23) [sigma6]: 
= -K5 * Q * k / ( t * ( b + X1 + X2 ) ) = -0.7603 * 15756 * 0.1/( 0.866 * ( 7.25 + 4.00 + 4.00 ) ) = -90.63 psi 
Circ. Comp. Stress at Horn of Saddle, L<8Rm (4.15.25) [sigma7*]: 
= -Q/(4*t*(b+X1+X2)) - 12*K7*Q*Rm/(L*t2) = -15756/(4*0.866 *(7.250 +4.005 +4.005 )) -12 * 0.028 * 15756 * 30.433/(12.500 * 0.8662) = -1744.05 psi 
Effective reinforcing plate width  (4.15.1) [B1]: 
= min( b + 1.56 * sqrt( Rm * t ), 2a ) = min( 7.25 + 1.56 * sqrt( 30.433 * 0.866 ), 2 * 21.000 ) = 15.26 in 
Results for Vessel Ribs, Web and Base: 
 Baseplate Length   Bplen  54.0000  in  
Baseplate Thickness  Bpthk  0.6299  in  
Baseplate Width  Bpwid  8.0000  in  
Number of Ribs ( inc. outside ribs )  Nribs  4  
Rib Thickness  Ribtk  0.5512  in  
Web Thickness  Webtk  0.5512  in  
Web Location  Webloc  Center  


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Moment of Inertia of Saddle - Lateral Direction 
Y  A           AY           Io 
 Shell  0.  17.  7.  4.  
Wearplate  1.  6.  6.  7.  
Web  5.  4.  24.  149.  
BasePlate  10.  5.  49.  470.  
Totals  17.  32.  86.  630.  

Value C1 = Sumof(Ay)/Sumof(A) = 3. in Value I = Sumof(Io) -C1*Sumof(Ay) = 401. in**4 Value As = Sumof(A) -Ashell = 15. in^2 
K1 = (1+Cos(beta)-.5*Sin(beta)2 )/(pi-beta+Sin(beta)*Cos(beta)) = 0.2035 
Fh = K1 * Q = 0.2035 * 15756.307 = 3206.7505 lbf 
Tension Stress, St = ( Fh/As )  = 213.3715 psi Allowed Stress, Sa = 0.6 * Yield Str = 20880.0000 psi 
d = B -R*Sin(theta) / theta = 15.1589 in  Bending Moment, M = Fh * d = 4050.9138 ft-lbf 
 Bending Stress, Sb = ( M * C1 / I ) = 323.0436 psi Allowed Stress, Sa = 2/3 * Yield Str = 23200.0000 psi 
Minimum Thickness of Baseplate per Moss : 
= ( 3 * ( Q + Saddle_Wt ) * BasePlateWidth / ( 4 * BasePlateLength * 
AllStress )).5 = ( 3 * (15756 + 551 ) * 8.00/( 4 * 54.000 * 23200.000 )).5 = 0.279 in 
Calculation of Axial Load, Intermediate Values and Compressive Stress 
Effective Baseplate Length [e]: 
= ( Bplen - Clearance ) / ( Nribs - 1) = ( 54.0000 - 1.0 )/( 4 - 1 ) = 17.6667 in 
Baseplate Pressure Area [Ap]: 
= e * Bpwid / 2 = 17.6667 * 8.0000/2 = 70.6667 in^2 
Axial Load [P]: 
= Ap * Bp = 70.7 * 36.47 = 2577.4 lbf 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Area of the Rib and Web [Ar]: 
= ( Bpwid - Clearance - Webtk ) * Ribtk + e/2 * Webtk = ( 8.000 - 1.0 - 0.551 ) * 0.551 + 17.6667/2 * 0.551 = 8.423 in^2 
Compressive Stress [Sc]:
 = P/Ar = 2577.4/8.4232 = 305.9895 psi 
Check of Outside Ribs: Inertia of Saddle, Outer Ribs - Longitudinal Direction
 Y A          AY        Ay2       Io Rib 3.6 3.6 13.1 0.0 16.6 Web 3.6 4.9 17.6 0.0 0.2 Values 3.6 8.5 30.8 0.0 16.9 
Bending Moment [Rm]: 
= Fl /( 2 * Bplen ) * e * rl / 2 = 0.0/( 2 * 54.00 ) * 17.667 * 24.54/2 = 0.000 ft-lbf 
KL/R < Cc ( 17.3422 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 17.34 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(17.34 )/(8* 128.25 )-( 17.343)/(8*128.253) Sca = 20081.88 psi 
AISC Unity Check on Outside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 305.99/20081.88 + (0.00/4.651 )/23200.00 Check = 0.02 
Check of Inside Ribs Inertia of Saddle, Inner Ribs - Axial Direction
 Y A          AY        Ay2       Io Rib 3.5 3.6 12.4 0.0 15.8 Web 3.5 9.7 34.1 0.0 0.2 Values 3.5 13.3 46.5 0.0 16.0 
KL/R < Cc ( 9.0239 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 9.02 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(9.02 )/(8* 128.25 )-( 9.023)/(8*128.253) Sca = 20504.26 psi 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
AISC Unity Check on Inside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 387.82/20504.26 + ( 0.00/4.572 )/23200.00 Check = 0.02 

Input Data for Base Plate Bolting Calculations:
 Total Number of Bolts per BasePlate Nbolts 8 Total Number of Bolts in Tension/Baseplate Nbt 4 Bolt Material Specification SA-307 B Bolt Allowable Stress Stba 7000.00 psi Bolt Corrosion Allowance Bca 0.1180 in Distance from Bolts to Edge Edgedis 4.1650 in Nominal Bolt Diameter Bnd 0.8750 in Thread Series Series UNC BasePlate Allowable Stress S 13800.00 psi Area Available in a Single Bolt BltArea 0.1920 in^2 Saddle Load QO (Weight)  QO 16307.6 lbf Saddle Load QL (Wind/Seismic contribution)  QL 0.0 lbf Maximum Transverse Force Ft 0.0 lbf Maximum Longitudinal Force Fl 0.0 lbf Saddle Bolted to Steel Foundation No 

Bolt Area Calculation per Dennis R. Moss 
Bolt Area Requirement Due to Longitudinal Load [Bltarearl]: 
= 0.0 (QO > QL --> No Uplift in Longitudinal direction) 
Bolt Area due to Shear Load [Bltarears]: 
= Fl / (Stba * Nbolts) 
= 0.00/(7000.00 * 8.00 ) 
= 0.0000 in^2 
Bolt Area due to Transverse Load 
Moment on Baseplate Due to Transverse Load [Rmom]: 
= B * Ft + Sum of X Moments 
= 3.58 * 0.00 + 0.00 
= 0.00 ft-lbf 
Eccentricity (e): 
= Rmom / QO 
= 0.00/16307.61 
= 0.00 in < Bplen/6 --> No Uplift in Transverse direction 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Bolt Area due to Transverse Load [Bltareart]: 
= 0 (No Uplift) 
Required of a Single Bolt [Bltarear] 
= max[Bltarearl, Bltarears, Bltareart] = max[0.0000 , 0.0000 , 0.0000 ] = 0.0000 in^2 
ASME Horizontal Vessel Analysis: Stresses for the Right Saddle 
(per ASME Sec. VIII Div. 2 based on the Zick method.) 
Note: Wear Pad Width (11.81) is less than 1.56*sqrt(rm*t)       and less than 2a. The wear plate will be ignored. 
Minimum Wear Plate Width to be considered in analysis [b1]: 
= min( b + 1.56*sqrt( Rm * t ), 2a ) = min( 7.250 + 1.56*sqrt( 30.4331 * 0.8661 ), 2 * 21.000 ) = 15.2593 in 

Input and Calculated Values: 
Vessel Mean Radius  Rm  30.43  in  
Stiffened Vessel Length per 4.15.6  L  12.50  ft  
Distance from Saddle to Vessel tangent  a  21.00  in  

Saddle Width b 7.25 in Saddle Bearing Angle  theta 120.00 degrees 
Inside Depth of Head h2 1.25 ft 
Shell Allowable Stress used in Calculation 22500.00 psi Head Allowable Stress used in Calculation 22500.00 psi Circumferential Efficiency in Plane of Saddle 1.00 Circumferential Efficiency at Mid-Span 1.00 
Saddle Force Q, Test Case, no Ext. Forces 15336.48 lbf 
Horizontal Vessel Analysis Results: Actual      Allowable
 -------------------------------------------------------------------Long. Stress at Top of Midspan 8825.77 22500.00 psi Long. Stress at Bottom of Midspan 8998.00 22500.00 psi Long. Stress at Top of Saddles 9083.27 22500.00 psi Long. Stress at Bottom of Saddles 8816.89 22500.00 psi 
Tangential Shear in Shell 432.72 13500.00 psi 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Circ. Stress at Horn of Saddle 1697.58 33750.00 psi Circ. Compressive Stress in Shell 88.22 22500.00 psi 
Load Combination Results for Q + Wind or Seismic [Q]: 
= Saddle Load + Max( Fwl, Fwt, Fsl, Fst ) = 15336 + Max( 0 , 0 , 0 , 0 ) = 15336.5 lbf 
Summary of Loads at the base of this Saddle:
 Vertical Load (including saddle weight) 15887.78 lbf Transverse Shear Load Saddle 0.00 lbf Longitudinal Shear Load Saddle 0.00 lbf 
Hydrostatic Test Pressure at center of Vessel:         507.274  psig 
Formulas and Substitutions for Horizontal Vessel Analysis: 
Note: Wear Plate is Welded to the Shell, k = 0.1 


The Computed K values from Table 4.15.1:
 K1 = 0.1066 K2 = 1.1707 K3 = 0.8799 K4 = 0.4011 K5 = 0.7603 K6 = 0.0529 K7 = 0.0283 K8 = 0.3405 K9 = 0.2711 K10 = 0.0581 K1* = 0.1923 
Note: Dimension a is greater than or equal to Rm / 2. 
Moment per Equation 4.15.3 [M1]: 
= -Q*a [1 - (1- a/L + (R2-h22)/(2a*L))/(1+(4h2)/3L)] = -15336*1.75[1-(1-1.75/12.50+(2.5362-1.2502)/ (2*1.75*12.50))/(1+(4*1.25)/(3*12.50))] = -3837.2 ft-lbf 
Moment per Equation 4.15.4 [M2]:
 = Q*L/4(1+2(R2-h22)/(L2))/(1+(4h2)/( 3L))-4a/L = 15336*12.5/4(1+2(2.5362-1.2502)/(12.502))/(1+(4*1.250)/ (3*12.500))-4*1.75/12.50 = 18084.9 ft-lbf 
Longitudinal Stress at Top of Shell (4.15.6) [Sigma1]: 
= P * Rm/(2t) - M2/(pi*Rm2t) = 507.274 * 30.433/(2*0.866 ) - 217018.8/(pi*30.42*0.866 ) = 8825.77 psi 
Longitudinal Stress at Bottom of Shell (4.15.7) [Sigma2]: 
= P * Rm/(2t) + M2/(pi * Rm2 * t) = 507.274 * 30.433/(2 * 0.866 ) + 217018.8/(pi * 30.42 * 0.866 ) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
= 8998.00 psi 
Longitudinal Stress at Top of Shell at Support (4.15.10)    [Sigma*3]: 
= P * Rm/(2t) - M1/(K1*pi*Rm2t) = 507.274*30.433/(2*0.866)--46046.8/(0.1066*pi*30.42*0.866) = 9083.27 psi 
Longitudinal Stress at Bottom of Shell at Support (4.15.11) [Sigma*4]: 
= P * Rm/(2t) + M1/(K1* * pi * Rm2 * t) = 507.274*30.433/(2*0.866)+-46046.8/(0.1923*pi*30.42*0.866) = 8816.89 psi 
Maximum Shear Force in the Saddle (4.15.5) [T]:
 = Q(L-2a)/(L+(4*h2/3)) = 15336 ( 12.50 - 2 * 1.75 )/(12.50 + ( 4 * 1.25/3)) = 9743.2 lbf 
Shear Stress in the shell no rings,  not stiffened (4.15.14)   [tau2]: 
= K2 * T / ( Rm * t ) = 1.1707 * 9743.17/( 30.4331 * 0.8661 ) = 432.72 psi 
Decay Length (4.15.22)  [x1,x2]: 
= 0.78 * sqrt( Rm * t ) = 0.78 * sqrt( 30.433 * 0.866 ) = 4.005 in 
Circumferential Stress in shell, no rings (4.15.23) [sigma6]: 
= -K5 * Q * k / ( t * ( b + X1 + X2 ) ) = -0.7603 * 15336 * 0.1/( 0.866 * ( 7.25 + 4.00 + 4.00 ) ) = -88.22 psi 
Circ. Comp. Stress at Horn of Saddle, L<8Rm (4.15.25) [sigma7*]: 
= -Q/(4*t*(b+X1+X2)) - 12*K7*Q*Rm/(L*t2) = -15336/(4*0.866 *(7.250 +4.005 +4.005 )) -12 * 0.028 * 15336 * 30.433/(12.500 * 0.8662) = -1697.58 psi 
Effective reinforcing plate width  (4.15.1) [B1]: 
= min( b + 1.56 * sqrt( Rm * t ), 2a ) = min( 7.25 + 1.56 * sqrt( 30.433 * 0.866 ), 2 * 21.000 ) = 15.26 in 
Results for Vessel Ribs, Web and Base
 Baseplate Length  Bplen 54.0000 in 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
Baseplate Thickness Bpthk 0.6299 in Baseplate Width Bpwid 8.0000 in Number of Ribs ( inc. outside ribs ) Nribs 4 Rib Thickness Ribtk 0.5512 in Web Thickness Webtk 0.5512 in Web Location Webloc Center 
Moment of Inertia of Saddle - Lateral Direction 
Y  A           AY           Io 
 Shell  0.  17.  7.  4.  
Wearplate  1.  6.  6.  7.  
Web  5.  4.  24.  149.  
BasePlate  10.  5.  49.  470.  
Totals  17.  32.  86.  630.  

Value C1 = Sumof(Ay)/Sumof(A) = 3. in Value I = Sumof(Io) -C1*Sumof(Ay) = 401. in**4 Value As = Sumof(A) -Ashell = 15. in^2 
K1 = (1+Cos(beta)-.5*Sin(beta)2 )/(pi-beta+Sin(beta)*Cos(beta)) = 0.2035 
Fh = K1 * Q = 0.2035 * 15336.477 = 3121.3059 lbf 
Tension Stress, St = ( Fh/As )  = 207.6862 psi Allowed Stress, Sa = 0.6 * Yield Str = 20880.0000 psi 
d = B -R*Sin(theta) / theta = 15.1589 in  Bending Moment, M = Fh * d = 3942.9763 ft-lbf 
 Bending Stress, Sb = ( M * C1 / I ) = 314.4361 psi Allowed Stress, Sa = 2/3 * Yield Str = 23200.0000 psi 
Minimum Thickness of Baseplate per Moss : 
= ( 3 * ( Q + Saddle_Wt ) * BasePlateWidth / ( 4 * BasePlateLength * 
AllStress )).5 = ( 3 * (15336 + 551 ) * 8.00/( 4 * 54.000 * 23200.000 )).5 = 0.276 in 
Calculation of Axial Load, Intermediate Values and Compressive Stress 
Effective Baseplate Length [e]: 
= ( Bplen - Clearance ) / ( Nribs - 1) 
= ( 54.0000 - 1.0 )/( 4 - 1 ) = 17.6667 in 
Baseplate Pressure Area [Ap]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
= e * Bpwid / 2 = 17.6667 * 8.0000/2 = 70.6667 in^2 
Axial Load [P]: 
= Ap * Bp = 70.7 * 35.50 = 2508.7 lbf 
Area of the Rib and Web [Ar]: 
= ( Bpwid - Clearance - Webtk ) * Ribtk + e/2 * Webtk = ( 8.000 - 1.0 - 0.551 ) * 0.551 + 17.6667/2 * 0.551 = 8.423 in^2 
Compressive Stress [Sc]:
 = P/Ar = 2508.7/8.4232 = 297.8363 psi 
Check of Outside Ribs: Inertia of Saddle, Outer Ribs - Longitudinal Direction
 Y A          AY        Ay2       Io Rib 3.6 3.6 13.1 0.0 16.6 Web 3.6 4.9 17.6 0.0 0.2 Values 3.6 8.5 30.8 0.0 16.9 
Bending Moment [Rm]: 
= Fl /( 2 * Bplen ) * e * rl / 2 = 0.0/( 2 * 54.00 ) * 17.667 * 24.54/2 = 0.000 ft-lbf 
KL/R < Cc ( 17.3422 < 128.2548 ) per AISC E2-1 Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) Sca = ( 1-( 17.34 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(17.34 )/(8* 128.25 )-( 17.343)/(8*128.253) Sca = 20081.88 psi 
AISC Unity Check on Outside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 297.84/20081.88 + (0.00/4.651 )/23200.00 Check = 0.01 
Check of Inside Ribs Inertia of Saddle, Inner Ribs - Axial Direction
 Y A          AY        Ay2       Io Rib 3.5 3.6 12.4 0.0 15.8 Web 3.5 9.7 34.1 0.0 0.2 Values 3.5 13.3 46.5 0.0 16.0 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
KL/R < Cc ( 9.0239 < 128.2548 ) per AISC E2-1 
Sca = (1-(Klr)2/(2*Cc2))*Fy/(5/3+3*(Klr)/(8*Cc)-(Klr3)/(8*Cc3) 
Sca = ( 1-( 9.02 )2/(2 * 128.252 )) * 34800/ 
       ( 5/3+3*(9.02 )/(8* 128.25 )-( 9.023)/(8*128.253) 
Sca = 20504.26 psi 
AISC Unity Check on Inside Ribs ( must be <= 1.0 ) 
Check = Sc/Sca + (Rm/Z)/Sba Check = 377.48/20504.26 + ( 0.00/4.572 )/23200.00 Check = 0.02 

Input Data for Base Plate Bolting Calculations:
 Total Number of Bolts per BasePlate Nbolts 8 Total Number of Bolts in Tension/Baseplate Nbt 4 Bolt Material Specification SA-307 B Bolt Allowable Stress Stba 7000.00 psi Bolt Corrosion Allowance Bca 0.1180 in Distance from Bolts to Edge Edgedis 4.1650 in Nominal Bolt Diameter Bnd 0.8750 in Thread Series Series UNC BasePlate Allowable Stress S 13800.00 psi Area Available in a Single Bolt BltArea 0.1920 in^2 Saddle Load QO (Weight)  QO 15887.8 lbf Saddle Load QL (Wind/Seismic contribution)  QL 0.0 lbf Maximum Transverse Force Ft 0.0 lbf Maximum Longitudinal Force Fl 0.0 lbf Saddle Bolted to Steel Foundation No 
Bolt Area Calculation per Dennis R. Moss 
Bolt Area Requirement Due to Longitudinal Load [Bltarearl]: 
= 0.0 (QO > QL --> No Uplift in Longitudinal direction) 
Bolt Area due to Shear Load [Bltarears]: 
= Fl / (Stba * Nbolts) 
= 0.00/(7000.00 * 8.00 ) 
= 0.0000 in^2 
Bolt Area due to Transverse Load 
Moment on Baseplate Due to Transverse Load [Rmom]: 
= B * Ft + Sum of X Moments 
= 3.58 * 0.00 + 0.00 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Horizontal Vessel Analysis (Test) : Step:  13 1:43p Apr 4,2014 
= 0.00 ft-lbf 
Eccentricity (e): 
= Rmom / QO 
= 0.00/15887.78 
= 0.00 in < Bplen/6 --> No Uplift in Transverse direction 
Bolt Area due to Transverse Load [Bltareart]: 
= 0 (No Uplift) 
Required of a Single Bolt [Bltarear] 
= max[Bltarearl, Bltarears, Bltareart] 
= max[0.0000 , 0.0000 , 0.0000 ] 
= 0.0000 in^2 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: F1 From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  0.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 4.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: F1 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 4.500 in. Actual Thickness Used in Calculation 0.337 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*2.2500)/(16700*1.00+0.4*363.00) = 0.0485 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0303 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 7.6520 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Parallel to Vessel Wall, opening length  d 3.8260 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.8425 in 
Weld Strength Reduction Factor [fr1]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr2]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr3]: 
= min( fr2, fr4 ) = min( 1.0 , 1.0 ) = 1.000 
Results of Nozzle Reinforcement Area Calculations: 
AREA AVAILABLE, A1 to A5  Design  External  Mapnc  
Area Required  Ar  NA  0.573  NA  in^2  
Area in Shell  A1  NA  2.168  NA  in^2  
Area in Nozzle Wall  A2  NA  0.517  NA  in^2  
Area in Inward Nozzle  A3  NA  0.000  NA  in^2  
Area in Welds  A41+A42+A43  NA  0.155  NA  in^2  
Area in Element  A5  NA  0.000  NA  in^2  
TOTAL AREA AVAILABLE  Atot  NA  2.840  NA  in^2  

Nozzle Angle Used in Area Calculations 90.00 Degs. 
The area available without a pad is Sufficient. 
Area Required [A]: 
= 0.5( d * tr*F + 2 * tn * tr*F * (1-fr1) ) per UG-37(d) or UG-39 = 0.5(3.8260*0.2994*1+2*0.3370*0.2994*1*(1-1.00)) = 0.573 in^2 
Reinforcement Areas per Figure UG-37.1 
Area Available in Shell [A1]: 
= d( E1*t - F*tr ) - 2 * tn( E1*t - F*tr ) * ( 1 - fr1 ) = 3.826 ( 1.00 * 0.8661 - 1.0 * 0.299 ) - 2 * 0.337 
( 1.00 * 0.8661 - 1.0 * 0.2994 ) * ( 1 - 1.000 ) = 2.168 in^2 
Area Available in Nozzle Projecting Outward [A2]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
= ( 2 * tlnp ) * ( tn - trn ) * fr2 
= ( 2 * 0.843 ) * ( 0.3370 - 0.0303 ) * 1.0000 
= 0.517 in^2 
Area Available in Inward Weld + Outward Weld [A41 + A43]:
 = Wo2 * fr2 + ( Wi-can/0.707 )2 * fr2 
= 0.39372 * 1.0000 + ( 0.0000 )2 * 1.0000 
= 0.155 in^2 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0485 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.2070 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.207 , max( 0.6607 , 0.0625 ) ] 
= 0.2070 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0485 , 0.2070 ) 
= 0.2070 in 
Available Nozzle Neck Thickness = 0.875 * 0.337 = 0.295 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 6397.0, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 35353.0 psi Passed 
Occasional : 946.9, Allowable : 22211.0 psi Passed 
Shear : 3629.6, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Nozzle Calculations per App. 1-10: Internal Pressure Case: 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Thickness of Nozzle [tn]: 
= thickness - corrosion allowance = 0.337 - 0.000 = 0.337 in 
Effective Pressure Radius [Reff]: 
= Di/2 + corrosion allowance = 60.000/2 + 0.000 = 30.000 in 
Effective Length of Vessel Wall [LR]: 
= 8 * t = 8 * 0.866 = 6.929 in 
Thickness Limit Candidate [LH1]: 
= t + 0.78 * sqrt( Rn * tn ) = 0.866 + 0.78 * sqrt( 1.913 * 0.337 ) = 1.492 in 
Thickness Limit Candidate [LH2]: 
= Lpr1 + T = 25.000 + 0.866 = 25.866 in 
Thickness Limit Candidate [LH3]: 
= 8( t + te ) = 8( 0.866 + 0.000 ) = 6.929 in 
Effective Nozzle Wall Length Outside the Vessel [LH]: 
= min[ LH1, LH2, LH3 ] = min[ 1.492 , 25.866 , 6.929 ) = 1.492 in 
Effective Vessel Thickness [teff]:
 = t = 0.866 in 
Determine Parameter [Lamda]: 
= min( 10, ( Dn + Tn )/( sqrt( ( Di + teff ) * teff )) ) = min( 10, (3.83 + 0.337 )/( sqrt((60.00 + 0.866 ) * 0.866 )) ) = 0.573 
Compute Areas A1-A43 (No Pad) or A1-A5 (With Pad) : 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Area Contributed by the Vessel Wall [A1]: 
= t * LR * max( Lamda/4, 1 ) = 0.866 * 6.929 * max( 0.573/4, 1 ) = 6.002 in^2 
Area Contributed by the Nozzle Outside the Vessel Wall [A2]: 
= tn * LH = 0.337 * 1.492 = 0.503 in^2 
Area Contributed by the Outside Fillet Weld [A41]: 
= 0.5 * Leg412 = 0.5 * 0.3942 = 0.078 in^2 
The total area contributed by A1 through A43 [AT]: 
= A1 + frn( A2 + A3 ) + A41 + A42 + A43 = 6.002+1.000(0.503+0.000)+0.078+0.000+0.000 = 6.582 in^2 
Allowable Local Primary Membrane Stress [Sallow]: 
= 1.5 * S * E = 1.5 * 16700.000 * 1.000 = 25050.0 psi 
Determine Force acting on the Nozzle [fN]: 
= P * Rn( LH - t ) = 363.000 * 1.913 ( 1.492 - 0.866 ) = 434.9 lbf 
Determine Force acting on the Shell [fS]: 
= P * Reff( LR + tn ) = 363.000 * 30.000 ( 6.929 + 0.337 ) = 79128.2 lbf 
Discontinuity Force from Internal Pressure [fY]: 
= P * Reff * Rnc = 363.000 * 30.000 * 1.913 = 20832.6 lbf 
Area Resisting Internal Pressure [Ap]: 
= Rn( LH - t ) + Reff( LR + tn + Rnc ) = 1.913 ( 1.492 - 0.866 ) + 30.000 ( 6.929 + 0.337 + 1.913 ) = 276.6 in^2 
Maximum Allowable Working Pressure Candidate [Pmax1]: 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
= Sallow /( 2 * Ap/AT - Rxs/teff ) = 25050.000/( 2 * 276.572/6.582 - 30.000/0.866 ) = 507.1 psig 
Maximum Allowable Working Pressure Candidate [Pmax2]:
 = S[t/Reff] = 16700.000 [0.866/30.000 ] = 482.2 psig 
Maximum Allowable Working Pressure [Pmax]: 
= min( Pmax1, Pmax2 ) = min( 507.066 , 482.152 ) = 482.152 psig 
Average Primary Membrane Stress [SigmaAvg]: 
= ( fN + fS + fY ) / AT = ( 434.899 + 79128.195 + 20832.570 )/6.582 = 15252.930 psi 
General Primary Membrane Stress [SigmaCirc]: 
= P * Reff / teff = 363.000 * 30.000/0.866 = 12573.0 psi 
Maximum Local Primary Membrane Stress [PL]: 
= max( 2 * SigmaAvg - SigmaCirc, SigmaCirc ) = max( 2 * 15252.930 - 12573.000 , 12573.000 ) = 17932.9 psi 
Summary of Nozzle Pressure/Stress Results:
 Allowed Local Primary Membrane Stress Sallow 25050.00 psi Local Primary Membrane Stress PL 17932.86 psi Maximum Allowable Working Pressure Pmax 482.15 psig 

Strength of Nozzle Attachment Welds per 1-10 and U-2(g) 
Discontinuity Force Factor [ky]: 
= ( Rnc + tn ) / Rnc = ( 1.913 + 0.337 )/1.913 = 1.176 For set-in Nozzles 
Weld Length of Nozzle to Shell Weld [Ltau]: 
= pi/2 * ( Rn + tn ) = pi/2 * ( 1.913 + 0.337 ) = 3.534 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Weld Throat Dimensions, (0.7071*Leg Dimensions) [L41T, L42T, L43T]:
 = 0.278, 0.000, 0.000, in 
Weld Load Value [fwelds]: 
= min( fy * ky, 1.5 * Sn( A2 + A3 ), pi/4*P*Rn^2*ky^2 ) = min(20832*1.18,1.5*16700.0(0.503+0.000),pi/4*363.0*1.91^2*1.18^2) = 1443.316 lbf 
Weld Stress Value [tau]: 
= fwelds/(Ltau(0.49*L41T + 0.6*tw1 + 0.49*L43T ) ) = 1443.316/(3.534 (0.49*0.278 + 0.6*0.787 + 0.49*0.000 ) ) = 670.731 < or = to 16700.000 Weld Size is OK 
Weld Size Calculations, Description: F1
 Intermediate Calc. for nozzle/shell Welds Tmin 0.3370 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.2359 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head.
 Nozzle is O.K. for the External Pressure 14.500 psig 
The Drop for this Nozzle is : 0.0845 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.9506 in 
Input Echo, WRC107/537 Item     1, Description: F1 : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000 in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 4.500 in Nozzle Thickness Tn 0.337 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.000 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 967.0 lbf Longitudinal Shear (SUS) Vl 1079.0 lbf Circumferential Shear (SUS) Vc 787.0 lbf Circumferential Moment (SUS) Mc 1033.0 ft-lbf Longitudinal Moment (SUS) Ml 1549.0 ft-lbf Torsional Moment (SUS) Mt 1918.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 967.0 lbf Circumferential Shear VC 787.0 lbf Longitudinal Shear VL 1079.0 lbf Circumferential Moment MC 1033.0 ft-lbf Longitudinal Moment ML 1549.0 ft-lbf Torsional Moment MT 1918.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.065 4C 6.483 (A,B)  N(PHI) / ( P/Rm )  0.065 3C 6.251 (C,D)  M(PHI) / ( P ) 0.065 2C1 0.132 (A,B)  M(PHI) / ( P ) 0.065 1C 0.169 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.065 3A 0.616 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.065 1A 0.103 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
 N(PHI) / ( ML/(Rm**2 * Beta) )  0.065 3B 2.227 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.065 1B 0.054 (A,B,C,D) 
N(x) / ( P/Rm )  0.065 3C 6.251 (A,B) N(x) / ( P/Rm )  0.065 4C 6.483 (C,D) M(x) / ( P ) 0.065 1C1 0.174 (A,B) M(x) / ( P ) 0.065 2C 0.132 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.065 4A 0.805 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.065 2A 0.060 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.065 4B 0.633 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.065 2B 0.091 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -237 -237 -237 -237 -229 -229 -229 -229 
Circ. Bend. P | -1021 1021 -1021 1021 -1309 1309 -1309 1309 
Circ. Memb. MC | 0 0 0 0 -147 -147 147 147 
Circ. Bend. MC | 0 0 0 0 -5169 5169 5169 -5169 
Circ. Memb. ML | -797 -797 797 797 0 0 0 0 
Circ. Bend. ML | -4112 4112 4112 -4112 0 0 0 0 
|
 Tot. Circ. Str.| -6169 4098 3650 -2530 -6856 6103 3777 -3941 
------------------------------------------------------------------------
Long. Memb. P | -229 -229 -229 -229 -237 -237 -237 -237 
Long. Bend. P | -1348 1348 -1348 1348 -1023 1023 -1023 1023 
Long. Memb. MC | 0 0 0 0 -192 -192 192 192 
Long. Bend. MC | 0 0 0 0 -3015 3015 3015 -3015 
Long. Memb. ML | -226 -226 226 226 0 0 0 0 
Long. Bend. ML | -6852 6852 6852 -6852 0 0 0 0 
|
 Tot. Long. Str.|  -8656 7744 5501 -5506 -4469 3608 1946 -2038 
------------------------------------------------------------------------
Shear VC | 128 128 -128 -128 0 0 0 0 
Shear VL | 0 0 0 0 -176 -176 176 176 
Shear MT | 835 835 835 835 835 835 835 835 
|
 Tot. Shear| 963 963 706 706 659 659 1011 1011 
------------------------------------------------------------------------


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : F1 Nozl: 14   1:43p  Apr 4,2014 
Str. Int. | 8986 7983 5740 5666 7025 6266 4226 4379 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12394 12757 12394 12757 12394 12757 12394 12757 Circ. Pl (SUS) |  -1035 -1035 560 560 -376 -376 -82 -82 Circ. Q (SUS) |  -5133 5133 3090 -3090 -6479 6479 3859 -3859 ------------------------------------------------------------------------Long. Pm (SUS) |  6197 6197 6197 6197 6197 6197 6197 6197 Long. Pl (SUS) |  -456 -456 -2 -2 -430 -430 -45 -45  Long. Q  (SUS) |  -8200 8200 5504 -5504 -4038 4038 1992 -1992 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   128  128  -128  -128  -176  -176  176  176  
Shear Q (SUS) |   835  835  835  835  835  835  835  835  

------------------------------------------------------------------------Pm (SUS) | 12394 12757 12394 12757 12394 12757 12394 12757 ------------------------------------------------------------------------Pm+Pl (SUS) | 11361 11724 12956 13319 12022 12385 12316 12679 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  8895 17145 16157 10278 5648 18907 16297 9025 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12757 16700 | Passed Pm+Pl (SUS) | 13319 25050 | Passed  Pm+Pl+Q (TOTAL)|  18907 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : Y Nozl: 15   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: Y From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  1.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : Y Nozl: 15   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: Y 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0204 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.1073 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : Y Nozl: 15   1:43p  Apr 4,2014 
Parallel to Vessel Wall Rn+tn+t 2.0536 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: Y. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.135 , max( 0.6607 , 0.0625 ) ] = 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0256 , 0.1346 ) = 0.1346 in 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: Y
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 

Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : Y Nozl: 15   1:43p  Apr 4,2014 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 
Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0235 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.8897 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L4 Nozl: 16   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: L4 From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  2.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L4 Nozl: 16   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: L4 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0204 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.1073 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L4 Nozl: 16   1:43p  Apr 4,2014 
Parallel to Vessel Wall Rn+tn+t 2.0536 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: L4. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.135 , max( 0.6607 , 0.0625 ) ] = 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0256 , 0.1346 ) = 0.1346 in 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: L4
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 

Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L4 Nozl: 16   1:43p  Apr 4,2014 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 
Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0235 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.8897 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : P Nozl: 17   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: P From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  3.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : P Nozl: 17   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: P 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0204 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.1073 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : P Nozl: 17   1:43p  Apr 4,2014 
Parallel to Vessel Wall Rn+tn+t 2.0536 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: P. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.135 , max( 0.6607 , 0.0625 ) ] = 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0256 , 0.1346 ) = 0.1346 in 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: P
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 

Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : P Nozl: 17   1:43p  Apr 4,2014 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 
Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0235 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.8897 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: V From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  4.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: V 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0204 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.1073 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
Parallel to Vessel Wall Rn+tn+t 2.0536 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: V. 
This calculation is valid for nozzles that meet all the requirements of 
paragraph UG-36. Please check the Code carefully, especially for nozzles 
that are not isolated or do not meet Code spacing requirements. To force 
the computation of areas for small nozzles go to Tools->Configuration 
and check the box to force the UG-37 small nozzle area calculation or 
force the Appendix 1-10 computation in Nozzle Design Options. 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.135 , max( 0.6607 , 0.0625 ) ] 
= 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0256 , 0.1346 ) 
= 0.1346 in 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 8832.1, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 32917.9 psi Passed 
Occasional : 725.6, Allowable : 22211.0 psi Passed 
Shear : 6806.2, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: V
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0235 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.8897 in 
Input Echo, WRC107/537 Item     1, Description: V : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000  in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 2.375 in Nozzle Thickness Tn 0.218 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.000 psig 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 517.0 lbf Longitudinal Shear (SUS) Vl 697.0 lbf Circumferential Shear (SUS) Vc 517.0 lbf Circumferential Moment (SUS) Mc 295.0 ft-lbf Longitudinal Moment (SUS) Ml 369.0 ft-lbf Torsional Moment (SUS) Mt 590.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 517.0 lbf Circumferential Shear VC 517.0 lbf Longitudinal Shear VL 697.0 lbf Circumferential Moment MC 295.0 ft-lbf Longitudinal Moment ML 369.0 ft-lbf Torsional Moment MT 590.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.034 4C 6.715 (A,B)  N(PHI) / ( P/Rm )  0.034 3C 6.866 (C,D)  M(PHI) / ( P ) 0.034 2C1 0.185 (A,B)  M(PHI) / ( P ) 0.034 1C 0.233 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.034 3A 0.262 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.034 1A 0.104 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.034 3B 0.987 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.034 1B 0.063 (A,B,C,D) 
N(x) / ( P/Rm )  0.034 3C 6.866 (A,B) N(x) / ( P/Rm )  0.034 4C 6.715 (C,D) M(x) / ( P ) 0.034 1C1 0.236 (A,B) M(x) / ( P ) 0.034 2C 0.186 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.034 4A 0.317 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.034 2A 0.063 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
N(x) / ( ML/(Rm**2 * Beta) )  0.034 4B 0.271 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.034 2B 0.105 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -131 -131 -131 -131 -134 -134 -134 -134 
Circ. Bend. P | -765 765 -765 765 -961 961 -961 961 
Circ. Memb. MC | 0 0 0 0 -33 -33 33 33 
Circ. Bend. MC | 0 0 0 0 -2845 2845 2845 -2845 
Circ. Memb. ML | -159 -159 159 159 0 0 0 0 
Circ. Bend. ML | -2136 2136 2136 -2136 0 0 0 0 
|
 Tot. Circ. Str.| -3193 2610 1398 -1342 -3975 3638 1782 -1984 
------------------------------------------------------------------------
Long. Memb. P | -134 -134 -134 -134 -131 -131 -131 -131 
Long. Bend. P | -977 977 -977 977 -770 770 -770 770 
Long. Memb. MC | 0 0 0 0 -40 -40 40 40 
Long. Bend. MC | 0 0 0 0 -1704 1704 1704 -1704 
Long. Memb. ML | -43 -43 43 43 0 0 0 0 
Long. Bend. ML | -3594 3594 3594 -3594 0 0 0 0 
|
 Tot. Long. Str.|  -4750 4394 2526 -2708 -2647 2302 842 -1024 
------------------------------------------------------------------------
Shear VC | 159 159 -159 -159 0 0 0 0 
Shear VL | 0 0 0 0 -215 -215 215 215 
Shear MT | 922 922 922 922 922 922 922 922 
|
 Tot. Shear| 1082 1082 762 762 706 706 1138 1138 
------------------------------------------------------------------------
Str. Int. | 5305 4904 2910 3049 4280 3942 2544 2739 
------------------------------------------------------------------------

WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : V Nozl: 18   1:43p  Apr 4,2014 
---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12394 12757 12394 12757 12394 12757 12394 12757 Circ. Pl (SUS) |  -291 -291 27 27 -168 -168 -100 -100 Circ. Q (SUS) |  -2902 2902 1370 -1370 -3806 3806 1883 -1883 ------------------------------------------------------------------------Long. Pm (SUS) |  6197 6197 6197 6197 6197 6197 6197 6197 Long. Pl (SUS) |  -178 -178 -90 -90 -172 -172 -90 -90  Long. Q  (SUS) |  -4572 4572 2617 -2617 -2474 2474 933 -933 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   159  159  -159  -159  -215  -215  215  215  
Shear Q (SUS) |   922  922  922  922  922  922  922  922  

------------------------------------------------------------------------Pm (SUS) | 12394 12757 12394 12757 12394 12757 12394 12757 ------------------------------------------------------------------------Pm+Pl (SUS) | 12106 12469 12426 12788 12233 12595 12300 12663 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  9349 15601 13905 11486 8519 16457 14353 10995 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12757 16700 | Passed Pm+Pl (SUS) | 12788 25050 | Passed  Pm+Pl+Q (TOTAL)|  16457 50100 | Passed ------------------------------------------------------------------------
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: A From : 20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  12.0820 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 3.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: A 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 3.500 in. Actual Thickness Used in Calculation 0.300 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.7500)/(16700*1.00+0.4*363.00) = 0.0377 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0263 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 5.8000 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Parallel to Vessel Wall, opening length  d 2.9000 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.7500 in 
Weld Strength Reduction Factor [fr1]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr2]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr3]: 
= min( fr2, fr4 ) = min( 1.0 , 1.0 ) = 1.000 
Results of Nozzle Reinforcement Area Calculations: 
AREA AVAILABLE, A1 to A5  Design  External  Mapnc  
Area Required  Ar  NA  0.434  NA  in^2  
Area in Shell  A1  NA  1.643  NA  in^2  
Area in Nozzle Wall  A2  NA  0.410  NA  in^2  
Area in Inward Nozzle  A3  NA  0.000  NA  in^2  
Area in Welds  A41+A42+A43  NA  0.155  NA  in^2  
Area in Element  A5  NA  0.000  NA  in^2  
TOTAL AREA AVAILABLE  Atot  NA  2.209  NA  in^2  

Nozzle Angle Used in Area Calculations 90.00 Degs. 
The area available without a pad is Sufficient. 
Area Required [A]: 
= 0.5( d * tr*F + 2 * tn * tr*F * (1-fr1) ) per UG-37(d) or UG-39 = 0.5(2.9000*0.2994*1+2*0.3000*0.2994*1*(1-1.00)) = 0.434 in^2 
Reinforcement Areas per Figure UG-37.1 
Area Available in Shell [A1]: 
= d( E1*t - F*tr ) - 2 * tn( E1*t - F*tr ) * ( 1 - fr1 ) = 2.900 ( 1.00 * 0.8661 - 1.0 * 0.299 ) - 2 * 0.300 
( 1.00 * 0.8661 - 1.0 * 0.2994 ) * ( 1 - 1.000 ) = 1.643 in^2 
Area Available in Nozzle Projecting Outward [A2]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
= ( 2 * tlnp ) * ( tn - trn ) * fr2 
= ( 2 * 0.750 ) * ( 0.3000 - 0.0263 ) * 1.0000 
= 0.410 in^2 
Area Available in Inward Weld + Outward Weld [A41 + A43]:
 = Wo2 * fr2 + ( Wi-can/0.707 )2 * fr2 
= 0.39372 * 1.0000 + ( 0.0000 )2 * 1.0000 
= 0.155 in^2 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0377 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1890 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.189 , max( 0.6607 , 0.0625 ) ] 
= 0.1890 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0377 , 0.1890 ) 
= 0.1890 in 
Available Nozzle Neck Thickness = 0.875 * 0.300 = 0.263 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 7673.4, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 34076.6 psi Passed 
Occasional : 795.0, Allowable : 22211.0 psi Passed 
Shear : 4856.8, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Nozzle Calculations per App. 1-10: Internal Pressure Case: 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Thickness of Nozzle [tn]: 
= thickness - corrosion allowance = 0.300 - 0.000 = 0.300 in 
Effective Pressure Radius [Reff]: 
= Di/2 + corrosion allowance = 60.000/2 + 0.000 = 30.000 in 
Effective Length of Vessel Wall [LR]: 
= 8 * t = 8 * 0.866 = 6.929 in 
Thickness Limit Candidate [LH1]: 
= t + 0.78 * sqrt( Rn * tn ) = 0.866 + 0.78 * sqrt( 1.450 * 0.300 ) = 1.381 in 
Thickness Limit Candidate [LH2]: 
= Lpr1 + T = 25.000 + 0.866 = 25.866 in 
Thickness Limit Candidate [LH3]: 
= 8( t + te ) = 8( 0.866 + 0.000 ) = 6.929 in 
Effective Nozzle Wall Length Outside the Vessel [LH]: 
= min[ LH1, LH2, LH3 ] = min[ 1.381 , 25.866 , 6.929 ) = 1.381 in 
Effective Vessel Thickness [teff]:
 = t = 0.866 in 
Determine Parameter [Lamda]: 
= min( 10, ( Dn + Tn )/( sqrt( ( Di + teff ) * teff )) ) = min( 10, (2.90 + 0.300 )/( sqrt((60.00 + 0.866 ) * 0.866 )) ) = 0.441 
Compute Areas A1-A43 (No Pad) or A1-A5 (With Pad) : 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Area Contributed by the Vessel Wall [A1]: 
= t * LR * max( Lamda/4, 1 ) = 0.866 * 6.929 * max( 0.441/4, 1 ) = 6.002 in^2 
Area Contributed by the Nozzle Outside the Vessel Wall [A2]: 
= tn * LH = 0.300 * 1.381 = 0.414 in^2 
Area Contributed by the Outside Fillet Weld [A41]: 
= 0.5 * Leg412 = 0.5 * 0.3942 = 0.078 in^2 
The total area contributed by A1 through A43 [AT]: 
= A1 + frn( A2 + A3 ) + A41 + A42 + A43 = 6.002+1.000(0.414+0.000)+0.078+0.000+0.000 = 6.493 in^2 
Allowable Local Primary Membrane Stress [Sallow]: 
= 1.5 * S * E = 1.5 * 16700.000 * 1.000 = 25050.0 psi 
Determine Force acting on the Nozzle [fN]: 
= P * Rn( LH - t ) = 363.000 * 1.450 ( 1.381 - 0.866 ) = 270.8 lbf 
Determine Force acting on the Shell [fS]: 
= P * Reff( LR + tn ) = 363.000 * 30.000 ( 6.929 + 0.300 ) = 78725.3 lbf 
Discontinuity Force from Internal Pressure [fY]: 
= P * Reff * Rnc = 363.000 * 30.000 * 1.450 = 15790.5 lbf 
Area Resisting Internal Pressure [Ap]: 
= Rn( LH - t ) + Reff( LR + tn + Rnc ) = 1.450 ( 1.381 - 0.866 ) + 30.000 ( 6.929 + 0.300 + 1.450 ) = 261.1 in^2 
Maximum Allowable Working Pressure Candidate [Pmax1]: 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
= Sallow /( 2 * Ap/AT - Rxs/teff ) = 25050.000/( 2 * 261.120/6.493 - 30.000/0.866 ) = 547.0 psig 
Maximum Allowable Working Pressure Candidate [Pmax2]:
 = S[t/Reff] = 16700.000 [0.866/30.000 ] = 482.2 psig 
Maximum Allowable Working Pressure [Pmax]: 
= min( Pmax1, Pmax2 ) = min( 547.047 , 482.152 ) = 482.152 psig 
Average Primary Membrane Stress [SigmaAvg]: 
= ( fN + fS + fY ) / AT = ( 270.778 + 78725.266 + 15790.501 )/6.493 = 14597.618 psi 
General Primary Membrane Stress [SigmaCirc]: 
= P * Reff / teff = 363.000 * 30.000/0.866 = 12573.0 psi 
Maximum Local Primary Membrane Stress [PL]: 
= max( 2 * SigmaAvg - SigmaCirc, SigmaCirc ) = max( 2 * 14597.618 - 12573.000 , 12573.000 ) = 16622.2 psi 
Summary of Nozzle Pressure/Stress Results:
 Allowed Local Primary Membrane Stress Sallow 25050.00 psi Local Primary Membrane Stress PL 16622.24 psi Maximum Allowable Working Pressure Pmax 482.15 psig 

Strength of Nozzle Attachment Welds per 1-10 and U-2(g) 
Discontinuity Force Factor [ky]: 
= ( Rnc + tn ) / Rnc = ( 1.450 + 0.300 )/1.450 = 1.207 For set-in Nozzles 
Weld Length of Nozzle to Shell Weld [Ltau]: 
= pi/2 * ( Rn + tn ) = pi/2 * ( 1.450 + 0.300 ) = 2.749 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Weld Throat Dimensions, (0.7071*Leg Dimensions) [L41T, L42T, L43T]:
 = 0.278, 0.000, 0.000, in 
Weld Load Value [fwelds]: 
= min( fy * ky, 1.5 * Sn( A2 + A3 ), pi/4*P*Rn^2*ky^2 ) = min(15790*1.21,1.5*16700.0(0.414+0.000),pi/4*363.0*1.45^2*1.21^2) = 873.117 lbf 
Weld Stress Value [tau]: 
= fwelds/(Ltau(0.49*L41T + 0.6*tw1 + 0.49*L43T ) ) = 873.117/(2.749 (0.49*0.278 + 0.6*0.787 + 0.49*0.000 ) ) = 521.680 < or = to 16700.000 Weld Size is OK 
Weld Size Calculations, Description: A
 Intermediate Calc. for nozzle/shell Welds Tmin 0.3000 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.2100 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head.
 Nozzle is O.K. for the External Pressure 14.500 psig 
The Drop for this Nozzle is : 0.0511 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.9172 in 
Input Echo, WRC107/537 Item     1, Description: A : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000  in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 3.500 in Nozzle Thickness Tn 0.300 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.000 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 787.0 lbf Longitudinal Shear (SUS) Vl 922.0 lbf Circumferential Shear (SUS) Vc 674.0 lbf Circumferential Moment (SUS) Mc 664.0 ft-lbf Longitudinal Moment (SUS) Ml 1032.0 ft-lbf Torsional Moment (SUS) Mt 1328.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 787.0 lbf Circumferential Shear VC 674.0 lbf Longitudinal Shear VL 922.0 lbf Circumferential Moment MC 664.0 ft-lbf Longitudinal Moment ML 1032.0 ft-lbf Torsional Moment MT 1328.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.050 4C 6.605 (A,B)  N(PHI) / ( P/Rm )  0.050 3C 6.567 (C,D)  M(PHI) / ( P ) 0.050 2C1 0.152 (A,B)  M(PHI) / ( P ) 0.050 1C 0.194 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.050 3A 0.453 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.050 1A 0.104 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
 N(PHI) / ( ML/(Rm**2 * Beta) )  0.050 3B 1.684 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.050 1B 0.058 (A,B,C,D) 
N(x) / ( P/Rm )  0.050 3C 6.567 (A,B) N(x) / ( P/Rm )  0.050 4C 6.605 (C,D) M(x) / ( P ) 0.050 1C1 0.196 (A,B) M(x) / ( P ) 0.050 2C 0.152 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.050 4A 0.575 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.050 2A 0.062 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.050 4B 0.465 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.050 2B 0.097 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -197 -197 -197 -197 -196 -196 -196 -196 
Circ. Bend. P | -953 953 -953 953 -1219 1219 -1219 1219 
Circ. Memb. MC | 0 0 0 0 -89 -89 89 89 
Circ. Bend. MC | 0 0 0 0 -4315 4315 4315 -4315 
Circ. Memb. ML | -516 -516 516 516 0 0 0 0 
Circ. Bend. ML | -3763 3763 3763 -3763 0 0 0 0 
|
 Tot. Circ. Str.| -5431 4003 3129 -2490 -5820 5249 2988 -3202 
------------------------------------------------------------------------
Long. Memb. P | -196 -196 -196 -196 -197 -197 -197 -197 
Long. Bend. P | -1235 1235 -1235 1235 -957 957 -957 957 
Long. Memb. MC | 0 0 0 0 -113 -113 113 113 
Long. Bend. MC | 0 0 0 0 -2562 2562 2562 -2562 
Long. Memb. ML | -142 -142 142 142 0 0 0 0 
Long. Bend. ML | -6306 6306 6306 -6306 0 0 0 0 
|
 Tot. Long. Str.|  -7879 7202 5017 -5124 -3831 3209 1521 -1688 
------------------------------------------------------------------------
Shear VC | 141 141 -141 -141 0 0 0 0 
Shear VL | 0 0 0 0 -193 -193 193 193 
Shear MT | 956 956 956 956 956 956 956 956 
|
 Tot. Shear| 1097 1097 814 814 762 762 1149 1149 
------------------------------------------------------------------------


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : A Nozl: 19   1:43p  Apr 4,2014 
Str. Int. | 8300 7543 5320 5355 6078 5502 3618 3821 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12394 12757 12394 12757 12394 12757 12394 12757 Circ. Pl (SUS) |  -713 -713 319 319 -285 -285 -106 -106 Circ. Q (SUS) |  -4717 4717 2809 -2809 -5534 5534 3095 -3095 ------------------------------------------------------------------------Long. Pm (SUS) |  6197 6197 6197 6197 6197 6197 6197 6197 Long. Pl (SUS) |  -338 -338 -53 -53 -310 -310 -83 -83  Long. Q  (SUS) |  -7541 7541 5070 -5070 -3520 3520 1604 -1604 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   141  141  -141  -141  -193  -193  193  193  
Shear Q (SUS) |   956  956  956  956  956  956  956  956  

------------------------------------------------------------------------Pm (SUS) | 12394 12757 12394 12757 12394 12757 12394 12757 ------------------------------------------------------------------------Pm+Pl (SUS) | 11683 12046 12716 13079 12114 12477 12293 12656 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  8919 17087 15672 10338 6707 18073 15551 9804 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12757 16700 | Passed Pm+Pl (SUS) | 13079 25050 | Passed  Pm+Pl+Q (TOTAL)|  18073 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: M From :  20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  8.5820 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-240 304L Material UNS Number S30403 Material Specification/Type Plate Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 24.0000 in. 
Size and Thickness Basis Actual Actual Thickness tn 0.3937 in 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.4724 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in 
Pad Material  SA-240 304L  
Pad Allowable Stress at Temperature Pad Allowable Stress At Ambient Diameter of Pad along vessel surface Thickness of Pad  Spa te  Sp Dp  16700.00 psi 16700.00 psi 38.5827 in 0.6299 in  
Weld leg size between Pad and Shell  Wp  0.5118  in  

Groove weld depth between Pad and Nozzle Wgpn 0.5512 in Reinforcing Pad Width 7.2913 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
  __________/|  |
 ____/|__________\| | | \ | | | \| | |________________\|__| 

Insert/Set-in Nozzle With Pad, no Inside projection 
Reinforcement CALCULATION, Description: M 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 24.000 in. Actual Thickness Used in Calculation 0.394 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) 
= (363.00*30.0000)/(16700*1.00-0.6*363.00) 
= 0.6607 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) 
= (363.00*12.0000)/(16700*1.00+0.4*363.00) 
= 0.2586 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0798 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 46.4252 in Parallel to Vessel Wall, opening length  d 23.2126 in Normal to Vessel Wall (Thickness Limit), pad side Tlwp 1.6142 in 
Weld Strength Reduction Factor [fr1]: 
= min( 1, Sn/S ) 
= min( 1, 16700.0/16700.0 ) 
= 1.000 
Weld Strength Reduction Factor [fr2]: 
= min( 1, Sn/S ) 
= min( 1, 16700.0/16700.0 ) 
= 1.000 
Weld Strength Reduction Factor [fr4]: 
= min( 1, Sp/S ) 
= min( 1, 16700.0/16700.0 ) 
= 1.000 
Weld Strength Reduction Factor [fr3]: 
= min( fr2, fr4 ) 
= min( 1.0 , 1.0 ) 
= 1.000 
Results of Nozzle Reinforcement Area Calculations: 
AREA AVAILABLE, A1 to A5  Design  External  Mapnc  
Area Required  Ar  NA  3.475  NA  in^2  
Area in Shell  A1  NA  13.155  NA  in^2  
Area in Nozzle Wall  A2  NA  1.013  NA  in^2  
Area in Inward Nozzle  A3  NA  0.000  NA  in^2  
Area in Welds  A41+A42+A43  NA  0.485  NA  in^2  
Area in Element  A5  NA  6.889  NA  in^2  
TOTAL AREA AVAILABLE  Atot  NA  21.543  NA  in^2  

Nozzle Angle Used in Area Calculations 90.00 Degs. 
The area available without a pad is Sufficient. The area available with the given pad is Sufficient. 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
Area Required [A]: 
= 0.5( d * tr*F + 2 * tn * tr*F * (1-fr1) ) per UG-37(d) or UG-39 = 0.5(23.2126*0.2994*1+2*0.3937*0.2994*1*(1-1.00)) = 3.475 in^2 
Reinforcement Areas per Figure UG-37.1 
Area Available in Shell [A1]: 
= d( E1*t - F*tr ) - 2 * tn( E1*t - F*tr ) * ( 1 - fr1 ) = 23.213 ( 1.00 * 0.8661 - 1.0 * 0.299 ) - 2 * 0.394 
( 1.00 * 0.8661 - 1.0 * 0.2994 ) * ( 1 - 1.000 ) = 13.155 in^2 
Area Available in Nozzle Wall Projecting Outward [A2]: 
= ( 2 * Tlwp ) * ( tn - trn ) * fr2 = ( 2 * 1.614 ) * ( 0.3937 - 0.0798 ) * 1.0000 = 1.013 in^2 
Area Available in Welds [A41 + A42 + A43]:
 = Wo2*fr3+(Wi-can/0.707)2*fr2+Wp2*fr4 = 0.47242 *1.00 + (0.0000 )2 *1.00 + 0.51182 * 1.00 = 0.485 in^2 
Area Available in Element [A5]:
 = (min(Dp,DL)-(Nozzle OD))*(min(tp,Tlwp,te))*fr4 = ( 38.5827 - 24.0000 ) * 0.6299 * 1.0000 = 6.889 in^2 
Note: Per user request, A5 multiplied by 0.75, see UG-37(h). 

UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.2586 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.3280 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.328 , max( 0.6607 , 0.0625 ) ] = 0.3280 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
= max( ta, tb ) = max( 0.2586 , 0.3280 ) = 0.3280 in 
Available Nozzle Neck Thickness = 0.3937 in --> OK 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
Nozzle Calculations per App. 1-10: Internal Pressure Case: 
Thickness of Nozzle [tn]: 
= thickness - corrosion allowance = 0.394 - 0.000 = 0.394 in 
Effective Pressure Radius [Reff]: 
= Di/2 + corrosion allowance = 60.000/2 + 0.000 = 30.000 in 
Effective Length of Vessel Wall [LR]: 
Note : Pad Thk >= 0.5T and Pad Width < 8(Shell Thk + Pad Thk) 
= 10 * t = 10 * 0.866 = 8.661 in 
Thickness Limit Candidate [LH1]: 
= t + 0.78 * sqrt( Rn * tn ) = 0.866 + 0.78 * sqrt( 11.606 * 0.394 ) = 2.533 in 
Thickness Limit Candidate [LH2]: 
= Lpr1 + T = 25.000 + 0.866 = 25.866 in 
Thickness Limit Candidate [LH3]: 
= 8( t + te ) = 8( 0.866 + 0.630 ) = 11.969 in 
Effective Nozzle Wall Length Outside the Vessel [LH]: 
= min[ LH1, LH2, LH3 ] = min[ 2.533 , 25.866 , 11.969 ) = 2.533 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
Effective Vessel Thickness [teff]:
 = t = 0.866 in 
Determine Parameter [Lamda]: 
= min( 10, ( Dn + Tn )/( sqrt( ( Di + teff ) * teff )) ) = min( 10, (23.21 + 0.394 )/( sqrt((60.00 + 0.866 ) * 0.866 )) ) = 3.251 
Compute Areas A1-A43 (No Pad) or A1-A5 (With Pad) : 
Area Contributed by the Vessel Wall [A1]: 
= t * LR * max( Lamda/4, 1 ) = 0.866 * 8.661 * max( 3.251/4, 1 ) = 7.502 in^2 
Area Contributed by the Nozzle Outside the Vessel Wall [A2]: 
= tn * LH = 0.394 * 2.533 = 0.997 in^2 
Area Contributed by the Pad Fillet Weld [A42]: 
= 0.5 * Leg422 = 0.5 * 0.5122 = 0.131 in^2 
Area Contributed by the Outside Fillet Weld [A41]: 
= 0.5 * Leg412 = 0.5 * 0.4722 = 0.112 in^2 
Area Contributed by the Reinforcing Pad [A5]: 
= min( W * te , LR * te ) = min( 7.291 * 0.630 , 8.661 * 0.630 ) = 4.593 in^2 
The total area contributed by A1 through A5 [AT]: 
= A1 + frn( A2 + A3 ) + A41 + A42 + A43 + frp( A5 ) = 7.502+1.000(0.997+0.000)+0.112+0.131+0.000+1.000(4.593) = 13.335 in^2 
Allowable Local Primary Membrane Stress [Sallow]: 
= 1.5 * S * E = 1.5 * 16700.000 * 1.000 = 25050.0 psi 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
Determine Force acting on the Nozzle [fN]: 
= P * Rn( LH - t ) = 363.000 * 11.606 ( 2.533 - 0.866 ) = 7024.7 lbf 
Determine Force acting on the Shell [fS]: 
= P * Reff( LR + tn ) = 363.000 * 30.000 ( 8.661 + 0.394 ) = 98610.2 lbf 
Discontinuity Force from Internal Pressure [fY]: 
= P * Reff * Rnc = 363.000 * 30.000 * 11.606 = 126392.6 lbf 
Area Resisting Internal Pressure [Ap]: 
= Rn( LH - t ) + Reff( LR + tn + Rnc ) = 11.606 ( 2.533 - 0.866 ) + 30.000 ( 8.661 + 0.394 + 11.606 ) = 639.2 in^2 
Maximum Allowable Working Pressure Candidate [Pmax1]: 
= Sallow /( 2 * Ap/AT - Rxs/teff ) = 25050.000/( 2 * 639.194/13.335 - 30.000/0.866 ) = 409.1 psig 
Maximum Allowable Working Pressure Candidate [Pmax2]:
 = S[t/Reff] = 16700.000 [0.866/30.000 ] = 482.2 psig 
Maximum Allowable Working Pressure [Pmax]: 
= min( Pmax1, Pmax2 ) = min( 409.108 , 482.152 ) = 409.108 psig 
Average Primary Membrane Stress [SigmaAvg]: 
= ( fN + fS + fY ) / AT = ( 7024.657 + 98610.234 + 126392.602 )/13.335 = 17399.889 psi 
General Primary Membrane Stress [SigmaCirc]: 
= P * Reff / teff = 363.000 * 30.000/0.866 = 12573.0 psi 
Maximum Local Primary Membrane Stress [PL]: 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
= max( 2 * SigmaAvg - SigmaCirc, SigmaCirc ) = max( 2 * 17399.889 - 12573.000 , 12573.000 ) = 22226.8 psi 
Summary of Nozzle Pressure/Stress Results:
 Allowed Local Primary Membrane Stress Sallow 25050.00 psi Local Primary Membrane Stress PL 22226.78 psi Maximum Allowable Working Pressure Pmax 409.11 psig 

Strength of Nozzle Attachment Welds per 1-10 and U-2(g) 
Discontinuity Force Factor [ky]: 
= ( Rnc + tn ) / Rnc = ( 11.606 + 0.394 )/11.606 = 1.034 For set-in Nozzles 
Weld Length of Nozzle to Shell Weld [Ltau]: 
= pi/2 * ( Rn + tn ) = pi/2 * ( 11.606 + 0.394 ) = 18.850 in 
Weld Length of Pad to Shell Weld [LtauP]: 
= pi/2 * ( Rn + tn + W ) = pi/2 * ( 11.606 + 0.394 + 7.291 ) = 30.303 in 
Weld Throat Dimensions, (0.7071*Leg Dimensions) [L41T, L42T, L43T]:
 = 0.334, 0.362, 0.000, in 
Weld Load Value [fwelds]: 
= min( fy * ky, 1.5 * Sn( A2 + A3 ), pi/4*P*Rn^2*ky^2 ) = min(126392*1.03,1.5*16700.0(0.997+0.000),pi/4*363.0*11.61^2*1.03^2) = 24985.750 lbf 
Discontinuity Force [fws]: 
= fwelds * t * S/( t * S + te * Sp ) = 24985.8*0.87*16700/(0.866*16700+0.630*16700) = 14465.437 lbf 
Discontinuity Force [fwp]: 
= fwelds * te * Sp / ( t * S + te * Sp ) = 24985.8*0.63*16700/(0.866*16700+0.630*16700) = 10520.313 lbf 
Shear Stress [tau1]: 
= fws / ( Ltau * ( 0.6 * tw1 + 0.49 * L43T ) ) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : M Nozl: 20   1:43p  Apr 4,2014 
= 14465.437/( 18.850 * ( 0.6 * 0.787 + 0.49 * 0.000 ) ) = 1624.361 psi 
Shear Stress [tau2]: 
= fwp / ( Ltau * ( 0.6 * tw2 + 0.49 * L41T ) ) = 10520.313/( 18.850 * ( 0.6 * 0.551 + 0.49 * 0.334 ) ) = 1128.884 psi 
Shear Stress [tau3]: 
= fwp / ( Ltau * ( 0.49 * L42T ) ) = 10520.313/( 30.303 * ( 0.49 * 0.362 ) ) = 1957.761 psi 
Maximum Shear Stress in the Welds: 
= max( tau1, tau2, tau3 ) = max( 1624.361 , 1128.884 , 1957.761 ) = 1957.8 must be less than or equal to 16700.0 psi 
Weld Size Calculations, Description: M 
Intermediate Calc. for nozzle/shell Welds  Tmin  0.3937 in  
Intermediate Calc. for pad/shell Welds  TminPad  0.6299 in  
Results Per UW-16.1: 

 Required Thickness Actual Thickness Nozzle Weld 0.2756 = 0.7 * tmin. 0.3340 = 0.7 * Wo in Pad Weld 0.3150 = 0.5*TminPad 0.3619 = 0.7 * Wp in 
Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head.
 Nozzle is O.K. for the External Pressure 14.500 psig 
The Drop for this Nozzle is : 2.5045 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 28.3707 in 

Percent Elongation Calculations:
 Percent Elongation per UHA-44 (50*tnom/Rf)*(1-Rf/Ro) 1.668 % Note: Please Check Requirements of Table UHA-44 for Elongation limits. 

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: R1 From :  20 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  5.8320 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 4.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 25.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: R1 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 4.500 in. Actual Thickness Used in Calculation 0.337 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.00*30.0000)/(16700*1.00-0.6*363.00) = 0.6607 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*2.2500)/(16700*1.00+0.4*363.00) = 0.0485 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0303 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 7.6520 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Parallel to Vessel Wall, opening length  d 3.8260 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.8425 in 
Weld Strength Reduction Factor [fr1]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr2]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr3]: 
= min( fr2, fr4 ) = min( 1.0 , 1.0 ) = 1.000 
Results of Nozzle Reinforcement Area Calculations: 
AREA AVAILABLE, A1 to A5  Design  External  Mapnc  
Area Required  Ar  NA  0.573  NA  in^2  
Area in Shell  A1  NA  2.168  NA  in^2  
Area in Nozzle Wall  A2  NA  0.517  NA  in^2  
Area in Inward Nozzle  A3  NA  0.000  NA  in^2  
Area in Welds  A41+A42+A43  NA  0.155  NA  in^2  
Area in Element  A5  NA  0.000  NA  in^2  
TOTAL AREA AVAILABLE  Atot  NA  2.840  NA  in^2  

Nozzle Angle Used in Area Calculations 90.00 Degs. 
The area available without a pad is Sufficient. 
Area Required [A]: 
= 0.5( d * tr*F + 2 * tn * tr*F * (1-fr1) ) per UG-37(d) or UG-39 = 0.5(3.8260*0.2994*1+2*0.3370*0.2994*1*(1-1.00)) = 0.573 in^2 
Reinforcement Areas per Figure UG-37.1 
Area Available in Shell [A1]: 
= d( E1*t - F*tr ) - 2 * tn( E1*t - F*tr ) * ( 1 - fr1 ) = 3.826 ( 1.00 * 0.8661 - 1.0 * 0.299 ) - 2 * 0.337 
( 1.00 * 0.8661 - 1.0 * 0.2994 ) * ( 1 - 1.000 ) = 2.168 in^2 
Area Available in Nozzle Projecting Outward [A2]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
= ( 2 * tlnp ) * ( tn - trn ) * fr2 
= ( 2 * 0.843 ) * ( 0.3370 - 0.0303 ) * 1.0000 
= 0.517 in^2 
Area Available in Inward Weld + Outward Weld [A41 + A43]:
 = Wo2 * fr2 + ( Wi-can/0.707 )2 * fr2 
= 0.39372 * 1.0000 + ( 0.0000 )2 * 1.0000 
= 0.155 in^2 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0485 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6607 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6607 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.2070 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.207 , max( 0.6607 , 0.0625 ) ] 
= 0.2070 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0485 , 0.2070 ) 
= 0.2070 in 
Available Nozzle Neck Thickness = 0.875 * 0.337 = 0.295 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 6397.0, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 35353.0 psi Passed 
Occasional : 946.9, Allowable : 22211.0 psi Passed 
Shear : 3629.6, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Nozzle Calculations per App. 1-10: Internal Pressure Case: 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Thickness of Nozzle [tn]: 
= thickness - corrosion allowance = 0.337 - 0.000 = 0.337 in 
Effective Pressure Radius [Reff]: 
= Di/2 + corrosion allowance = 60.000/2 + 0.000 = 30.000 in 
Effective Length of Vessel Wall [LR]: 
= 8 * t = 8 * 0.866 = 6.929 in 
Thickness Limit Candidate [LH1]: 
= t + 0.78 * sqrt( Rn * tn ) = 0.866 + 0.78 * sqrt( 1.913 * 0.337 ) = 1.492 in 
Thickness Limit Candidate [LH2]: 
= Lpr1 + T = 25.000 + 0.866 = 25.866 in 
Thickness Limit Candidate [LH3]: 
= 8( t + te ) = 8( 0.866 + 0.000 ) = 6.929 in 
Effective Nozzle Wall Length Outside the Vessel [LH]: 
= min[ LH1, LH2, LH3 ] = min[ 1.492 , 25.866 , 6.929 ) = 1.492 in 
Effective Vessel Thickness [teff]:
 = t = 0.866 in 
Determine Parameter [Lamda]: 
= min( 10, ( Dn + Tn )/( sqrt( ( Di + teff ) * teff )) ) = min( 10, (3.83 + 0.337 )/( sqrt((60.00 + 0.866 ) * 0.866 )) ) = 0.573 
Compute Areas A1-A43 (No Pad) or A1-A5 (With Pad) : 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Area Contributed by the Vessel Wall [A1]: 
= t * LR * max( Lamda/4, 1 ) = 0.866 * 6.929 * max( 0.573/4, 1 ) = 6.002 in^2 
Area Contributed by the Nozzle Outside the Vessel Wall [A2]: 
= tn * LH = 0.337 * 1.492 = 0.503 in^2 
Area Contributed by the Outside Fillet Weld [A41]: 
= 0.5 * Leg412 = 0.5 * 0.3942 = 0.078 in^2 
The total area contributed by A1 through A43 [AT]: 
= A1 + frn( A2 + A3 ) + A41 + A42 + A43 = 6.002+1.000(0.503+0.000)+0.078+0.000+0.000 = 6.582 in^2 
Allowable Local Primary Membrane Stress [Sallow]: 
= 1.5 * S * E = 1.5 * 16700.000 * 1.000 = 25050.0 psi 
Determine Force acting on the Nozzle [fN]: 
= P * Rn( LH - t ) = 363.000 * 1.913 ( 1.492 - 0.866 ) = 434.9 lbf 
Determine Force acting on the Shell [fS]: 
= P * Reff( LR + tn ) = 363.000 * 30.000 ( 6.929 + 0.337 ) = 79128.2 lbf 
Discontinuity Force from Internal Pressure [fY]: 
= P * Reff * Rnc = 363.000 * 30.000 * 1.913 = 20832.6 lbf 
Area Resisting Internal Pressure [Ap]: 
= Rn( LH - t ) + Reff( LR + tn + Rnc ) = 1.913 ( 1.492 - 0.866 ) + 30.000 ( 6.929 + 0.337 + 1.913 ) = 276.6 in^2 
Maximum Allowable Working Pressure Candidate [Pmax1]: 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
= Sallow /( 2 * Ap/AT - Rxs/teff ) = 25050.000/( 2 * 276.572/6.582 - 30.000/0.866 ) = 507.1 psig 
Maximum Allowable Working Pressure Candidate [Pmax2]:
 = S[t/Reff] = 16700.000 [0.866/30.000 ] = 482.2 psig 
Maximum Allowable Working Pressure [Pmax]: 
= min( Pmax1, Pmax2 ) = min( 507.066 , 482.152 ) = 482.152 psig 
Average Primary Membrane Stress [SigmaAvg]: 
= ( fN + fS + fY ) / AT = ( 434.899 + 79128.195 + 20832.570 )/6.582 = 15252.930 psi 
General Primary Membrane Stress [SigmaCirc]: 
= P * Reff / teff = 363.000 * 30.000/0.866 = 12573.0 psi 
Maximum Local Primary Membrane Stress [PL]: 
= max( 2 * SigmaAvg - SigmaCirc, SigmaCirc ) = max( 2 * 15252.930 - 12573.000 , 12573.000 ) = 17932.9 psi 
Summary of Nozzle Pressure/Stress Results:
 Allowed Local Primary Membrane Stress Sallow 25050.00 psi Local Primary Membrane Stress PL 17932.86 psi Maximum Allowable Working Pressure Pmax 482.15 psig 

Strength of Nozzle Attachment Welds per 1-10 and U-2(g) 
Discontinuity Force Factor [ky]: 
= ( Rnc + tn ) / Rnc = ( 1.913 + 0.337 )/1.913 = 1.176 For set-in Nozzles 
Weld Length of Nozzle to Shell Weld [Ltau]: 
= pi/2 * ( Rn + tn ) = pi/2 * ( 1.913 + 0.337 ) = 3.534 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Weld Throat Dimensions, (0.7071*Leg Dimensions) [L41T, L42T, L43T]:
 = 0.278, 0.000, 0.000, in 
Weld Load Value [fwelds]: 
= min( fy * ky, 1.5 * Sn( A2 + A3 ), pi/4*P*Rn^2*ky^2 ) = min(20832*1.18,1.5*16700.0(0.503+0.000),pi/4*363.0*1.91^2*1.18^2) = 1443.316 lbf 
Weld Stress Value [tau]: 
= fwelds/(Ltau(0.49*L41T + 0.6*tw1 + 0.49*L43T ) ) = 1443.316/(3.534 (0.49*0.278 + 0.6*0.787 + 0.49*0.000 ) ) = 670.731 < or = to 16700.000 Weld Size is OK 
Weld Size Calculations, Description: R1
 Intermediate Calc. for nozzle/shell Welds Tmin 0.3370 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.2359 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.091 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head.
 Nozzle is O.K. for the External Pressure 14.500 psig 
The Drop for this Nozzle is : 0.0845 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 25.9506 in 
Input Echo, WRC107/537 Item     1, Description: R1 : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000 in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 4.500 in Nozzle Thickness Tn 0.337 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.000 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 967.0 lbf Longitudinal Shear (SUS) Vl 1079.0 lbf Circumferential Shear (SUS) Vc 787.0 lbf Circumferential Moment (SUS) Mc 1033.0 ft-lbf Longitudinal Moment (SUS) Ml 1549.0 ft-lbf Torsional Moment (SUS) Mt 1918.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 967.0 lbf Circumferential Shear VC 787.0 lbf Longitudinal Shear VL 1079.0 lbf Circumferential Moment MC 1033.0 ft-lbf Longitudinal Moment ML 1549.0 ft-lbf Torsional Moment MT 1918.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.065 4C 6.483 (A,B)  N(PHI) / ( P/Rm )  0.065 3C 6.251 (C,D)  M(PHI) / ( P ) 0.065 2C1 0.132 (A,B)  M(PHI) / ( P ) 0.065 1C 0.169 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.065 3A 0.616 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.065 1A 0.103 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
 N(PHI) / ( ML/(Rm**2 * Beta) )  0.065 3B 2.227 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.065 1B 0.054 (A,B,C,D) 
N(x) / ( P/Rm )  0.065 3C 6.251 (A,B) N(x) / ( P/Rm )  0.065 4C 6.483 (C,D) M(x) / ( P ) 0.065 1C1 0.174 (A,B) M(x) / ( P ) 0.065 2C 0.132 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.065 4A 0.805 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.065 2A 0.060 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.065 4B 0.633 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.065 2B 0.091 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -237 -237 -237 -237 -229 -229 -229 -229 
Circ. Bend. P | -1021 1021 -1021 1021 -1309 1309 -1309 1309 
Circ. Memb. MC | 0 0 0 0 -147 -147 147 147 
Circ. Bend. MC | 0 0 0 0 -5169 5169 5169 -5169 
Circ. Memb. ML | -797 -797 797 797 0 0 0 0 
Circ. Bend. ML | -4112 4112 4112 -4112 0 0 0 0 
|
 Tot. Circ. Str.| -6169 4098 3650 -2530 -6856 6103 3777 -3941 
------------------------------------------------------------------------
Long. Memb. P | -229 -229 -229 -229 -237 -237 -237 -237 
Long. Bend. P | -1348 1348 -1348 1348 -1023 1023 -1023 1023 
Long. Memb. MC | 0 0 0 0 -192 -192 192 192 
Long. Bend. MC | 0 0 0 0 -3015 3015 3015 -3015 
Long. Memb. ML | -226 -226 226 226 0 0 0 0 
Long. Bend. ML | -6852 6852 6852 -6852 0 0 0 0 
|
 Tot. Long. Str.|  -8656 7744 5501 -5506 -4469 3608 1946 -2038 
------------------------------------------------------------------------
Shear VC | 128 128 -128 -128 0 0 0 0 
Shear VL | 0 0 0 0 -176 -176 176 176 
Shear MT | 835 835 835 835 835 835 835 835 
|
 Tot. Shear| 963 963 706 706 659 659 1011 1011 
------------------------------------------------------------------------


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : R1 Nozl: 21   1:43p  Apr 4,2014 
Str. Int. | 8986 7983 5740 5666 7025 6266 4226 4379 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12394 12757 12394 12757 12394 12757 12394 12757 Circ. Pl (SUS) |  -1035 -1035 560 560 -376 -376 -82 -82 Circ. Q (SUS) |  -5133 5133 3090 -3090 -6479 6479 3859 -3859 ------------------------------------------------------------------------Long. Pm (SUS) |  6197 6197 6197 6197 6197 6197 6197 6197 Long. Pl (SUS) |  -456 -456 -2 -2 -430 -430 -45 -45  Long. Q  (SUS) |  -8200 8200 5504 -5504 -4038 4038 1992 -1992 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   128  128  -128  -128  -176  -176  176  176  
Shear Q (SUS) |   835  835  835  835  835  835  835  835  

------------------------------------------------------------------------Pm (SUS) | 12394 12757 12394 12757 12394 12757 12394 12757 ------------------------------------------------------------------------Pm+Pl (SUS) | 11361 11724 12956 13319 12022 12385 12316 12679 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  8895 17145 16157 10278 5648 18907 16297 9025 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12757 16700 | Passed Pm+Pl (SUS) | 13319 25050 | Passed  Pm+Pl+Q (TOTAL)|  18907 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: W1 From :  20 
Pressure for Reinforcement Calculations P  363.760 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  4.0820 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  180.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 9.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: W1 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.76*30.0000)/(16700*1.00-0.6*363.76) = 0.6621 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.76*1.1875)/(16700*1.00+0.4*363.76) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0134 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.1073 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
Parallel to Vessel Wall Rn+tn+t 2.0536 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: W1. 
This calculation is valid for nozzles that meet all the requirements of 
paragraph UG-36. Please check the Code carefully, especially for nozzles 
that are not isolated or do not meet Code spacing requirements. To force 
the computation of areas for small nozzles go to Tools->Configuration 
and check the box to force the UG-37 small nozzle area calculation or 
force the Appendix 1-10 computation in Nozzle Design Options. 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6621 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6621 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.135 , max( 0.6621 , 0.0625 ) ] 
= 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0256 , 0.1346 ) 
= 0.1346 in 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 8833.6, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 32916.4 psi Passed 
Occasional : 727.1, Allowable : 22211.0 psi Passed 
Shear : 6806.2, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: W1
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.851 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0235 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 9.8897 in 
Input Echo, WRC107/537 Item     1, Description: W1 : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000 in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 2.375 in Nozzle Thickness Tn 0.218 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.760 psig 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 517.0 lbf Longitudinal Shear (SUS) Vl 697.0 lbf Circumferential Shear (SUS) Vc 517.0 lbf Circumferential Moment (SUS) Mc 295.0 ft-lbf Longitudinal Moment (SUS) Ml 369.0 ft-lbf Torsional Moment (SUS) Mt 590.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 517.0 lbf Circumferential Shear VC 517.0 lbf Longitudinal Shear VL 697.0 lbf Circumferential Moment MC 295.0 ft-lbf Longitudinal Moment ML 369.0 ft-lbf Torsional Moment MT 590.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.034 4C 6.715 (A,B)  N(PHI) / ( P/Rm )  0.034 3C 6.866 (C,D)  M(PHI) / ( P ) 0.034 2C1 0.185 (A,B)  M(PHI) / ( P ) 0.034 1C 0.233 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.034 3A 0.262 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.034 1A 0.104 (A,B,C,D)  N(PHI) / ( ML/(Rm**2 * Beta) )  0.034 3B 0.987 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.034 1B 0.063 (A,B,C,D) 
N(x) / ( P/Rm )  0.034 3C 6.866 (A,B) N(x) / ( P/Rm )  0.034 4C 6.715 (C,D) M(x) / ( P ) 0.034 1C1 0.236 (A,B) M(x) / ( P ) 0.034 2C 0.186 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.034 4A 0.317 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.034 2A 0.063 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
N(x) / ( ML/(Rm**2 * Beta) )  0.034 4B 0.271 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.034 2B 0.105 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -131 -131 -131 -131 -134 -134 -134 -134 
Circ. Bend. P | -765 765 -765 765 -961 961 -961 961 
Circ. Memb. MC | 0 0 0 0 -33 -33 33 33 
Circ. Bend. MC | 0 0 0 0 -2845 2845 2845 -2845 
Circ. Memb. ML | -159 -159 159 159 0 0 0 0 
Circ. Bend. ML | -2136 2136 2136 -2136 0 0 0 0 
|
 Tot. Circ. Str.| -3193 2610 1398 -1342 -3975 3638 1782 -1984 
------------------------------------------------------------------------
Long. Memb. P | -134 -134 -134 -134 -131 -131 -131 -131 
Long. Bend. P | -977 977 -977 977 -770 770 -770 770 
Long. Memb. MC | 0 0 0 0 -40 -40 40 40 
Long. Bend. MC | 0 0 0 0 -1704 1704 1704 -1704 
Long. Memb. ML | -43 -43 43 43 0 0 0 0 
Long. Bend. ML | -3594 3594 3594 -3594 0 0 0 0 
|
 Tot. Long. Str.|  -4750 4394 2526 -2708 -2647 2302 842 -1024 
------------------------------------------------------------------------
Shear VC | 159 159 -159 -159 0 0 0 0 
Shear VL | 0 0 0 0 -215 -215 215 215 
Shear MT | 922 922 922 922 922 922 922 922 
|
 Tot. Shear| 1082 1082 762 762 706 706 1138 1138 
------------------------------------------------------------------------
Str. Int. | 5305 4904 2910 3049 4280 3942 2544 2739 
------------------------------------------------------------------------

WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : W1 Nozl: 22   1:43p  Apr 4,2014 
---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12420 12783 12420 12783 12420 12783 12420 12783 Circ. Pl (SUS) |  -291 -291 27 27 -168 -168 -100 -100 Circ. Q (SUS) |  -2902 2902 1370 -1370 -3806 3806 1883 -1883 ------------------------------------------------------------------------Long. Pm (SUS) |  6210 6210 6210 6210 6210 6210 6210 6210 Long. Pl (SUS) |  -178 -178 -90 -90 -172 -172 -90 -90  Long. Q  (SUS) |  -4572 4572 2617 -2617 -2474 2474 933 -933 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   159  159  -159  -159  -215  -215  215  215  
Shear Q (SUS) |   922  922  922  922  922  922  922  922  

------------------------------------------------------------------------Pm (SUS) | 12420 12783 12420 12783 12420 12783 12420 12783 ------------------------------------------------------------------------Pm+Pl (SUS) | 12132 12496 12451 12815 12259 12622 12326 12690 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  9374 15627 13930 11513 8545 16484 14379 11021 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12783 16700 | Passed Pm+Pl (SUS) | 12815 25050 | Passed  Pm+Pl+Q (TOTAL)|  16484 50100 | Passed ------------------------------------------------------------------------
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: B From : 20 
Pressure for Reinforcement Calculations P  363.760 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Cylindrical Shell D 60.0000 in  Design Length of Section L 160.0000 in Shell Finished (Minimum) Thickness t 0.8661 in Shell Internal Corrosion Allowance c 0.0000 in Shell External Corrosion Allowance co 0.0000 in 
Distance from Bottom/Left Tangent  12.0820 ft 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  180.00 deg Diameter 3.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 9.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7874 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Reinforcement CALCULATION, Description: B 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 3.500 in. Actual Thickness Used in Calculation 0.300 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Cylindrical Shell, Tr [Int. Press] 
= (P*R)/(S*E-0.6*P) per UG-27 (c)(1) = (363.76*30.0000)/(16700*1.00-0.6*363.76) = 0.6621 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.76*1.7500)/(16700*1.00+0.4*363.76) = 0.0378 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0169 in 
UG-40, Limits of Reinforcement : [External Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 5.8000 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Parallel to Vessel Wall, opening length  d 2.9000 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.7500 in 
Weld Strength Reduction Factor [fr1]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr2]: 
= min( 1, Sn/S ) = min( 1, 16700.0/16700.0 ) = 1.000 
Weld Strength Reduction Factor [fr3]: 
= min( fr2, fr4 ) = min( 1.0 , 1.0 ) = 1.000 
Results of Nozzle Reinforcement Area Calculations: 
AREA AVAILABLE, A1 to A5  Design  External  Mapnc  
Area Required  Ar  NA  0.434  NA  in^2  
Area in Shell  A1  NA  1.643  NA  in^2  
Area in Nozzle Wall  A2  NA  0.425  NA  in^2  
Area in Inward Nozzle  A3  NA  0.000  NA  in^2  
Area in Welds  A41+A42+A43  NA  0.155  NA  in^2  
Area in Element  A5  NA  0.000  NA  in^2  
TOTAL AREA AVAILABLE  Atot  NA  2.223  NA  in^2  

Nozzle Angle Used in Area Calculations 90.00 Degs. 
The area available without a pad is Sufficient. 
Area Required [A]: 
= 0.5( d * tr*F + 2 * tn * tr*F * (1-fr1) ) per UG-37(d) or UG-39 = 0.5(2.9000*0.2994*1+2*0.3000*0.2994*1*(1-1.00)) = 0.434 in^2 
Reinforcement Areas per Figure UG-37.1 
Area Available in Shell [A1]: 
= d( E1*t - F*tr ) - 2 * tn( E1*t - F*tr ) * ( 1 - fr1 ) = 2.900 ( 1.00 * 0.8661 - 1.0 * 0.299 ) - 2 * 0.300 
( 1.00 * 0.8661 - 1.0 * 0.2994 ) * ( 1 - 1.000 ) = 1.643 in^2 
Area Available in Nozzle Projecting Outward [A2]: 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
= ( 2 * tlnp ) * ( tn - trn ) * fr2 
= ( 2 * 0.750 ) * ( 0.3000 - 0.0169 ) * 1.0000 
= 0.425 in^2 
Area Available in Inward Weld + Outward Weld [A41 + A43]:
 = Wo2 * fr2 + ( Wi-can/0.707 )2 * fr2 
= 0.39372 * 1.0000 + ( 0.0000 )2 * 1.0000 
= 0.155 in^2 
UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0378 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6621 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6621 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1890 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] 
= min[ 0.189 , max( 0.6621 , 0.0625 ) ] 
= 0.1890 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) 
= max( 0.0378 , 0.1890 ) 
= 0.1890 in 
Available Nozzle Neck Thickness = 0.875 * 0.300 = 0.263 in --> OK 
Stresses on Nozzle due to External and Pressure Loads per the ASME B31.3 Piping Code (see 319.4.4 and 302.3.5):
 Sustained : 7675.0, Allowable : 16700.0 psi Passed 
Expansion : 0.0, Allowable : 34075.0 psi Passed 
Occasional : 796.7, Allowable : 22211.0 psi Passed 
Shear : 4856.8, Allowable : 11690.0 psi Passed 
Note : The number of cycles on this nozzle was assumed to be 7000 or less for     the determination of the expansion stress allowable. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Nozzle Calculations per App. 1-10: Internal Pressure Case: 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Thickness of Nozzle [tn]: 
= thickness - corrosion allowance = 0.300 - 0.000 = 0.300 in 
Effective Pressure Radius [Reff]: 
= Di/2 + corrosion allowance = 60.000/2 + 0.000 = 30.000 in 
Effective Length of Vessel Wall [LR]: 
= 8 * t = 8 * 0.866 = 6.929 in 
Thickness Limit Candidate [LH1]: 
= t + 0.78 * sqrt( Rn * tn ) = 0.866 + 0.78 * sqrt( 1.450 * 0.300 ) = 1.381 in 
Thickness Limit Candidate [LH2]: 
= Lpr1 + T = 9.000 + 0.866 = 9.866 in 
Thickness Limit Candidate [LH3]: 
= 8( t + te ) = 8( 0.866 + 0.000 ) = 6.929 in 
Effective Nozzle Wall Length Outside the Vessel [LH]: 
= min[ LH1, LH2, LH3 ] = min[ 1.381 , 9.866 , 6.929 ) = 1.381 in 
Effective Vessel Thickness [teff]:
 = t = 0.866 in 
Determine Parameter [Lamda]: 
= min( 10, ( Dn + Tn )/( sqrt( ( Di + teff ) * teff )) ) = min( 10, (2.90 + 0.300 )/( sqrt((60.00 + 0.866 ) * 0.866 )) ) = 0.441 
Compute Areas A1-A43 (No Pad) or A1-A5 (With Pad) : 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Area Contributed by the Vessel Wall [A1]: 
= t * LR * max( Lamda/4, 1 ) = 0.866 * 6.929 * max( 0.441/4, 1 ) = 6.002 in^2 
Area Contributed by the Nozzle Outside the Vessel Wall [A2]: 
= tn * LH = 0.300 * 1.381 = 0.414 in^2 
Area Contributed by the Outside Fillet Weld [A41]: 
= 0.5 * Leg412 = 0.5 * 0.3942 = 0.078 in^2 
The total area contributed by A1 through A43 [AT]: 
= A1 + frn( A2 + A3 ) + A41 + A42 + A43 = 6.002+1.000(0.414+0.000)+0.078+0.000+0.000 = 6.493 in^2 
Allowable Local Primary Membrane Stress [Sallow]: 
= 1.5 * S * E = 1.5 * 16700.000 * 1.000 = 25050.0 psi 
Determine Force acting on the Nozzle [fN]: 
= P * Rn( LH - t ) = 363.760 * 1.450 ( 1.381 - 0.866 ) = 271.3 lbf 
Determine Force acting on the Shell [fS]: 
= P * Reff( LR + tn ) = 363.760 * 30.000 ( 6.929 + 0.300 ) = 78890.1 lbf 
Discontinuity Force from Internal Pressure [fY]: 
= P * Reff * Rnc = 363.760 * 30.000 * 1.450 = 15823.6 lbf 
Area Resisting Internal Pressure [Ap]: 
= Rn( LH - t ) + Reff( LR + tn + Rnc ) = 1.450 ( 1.381 - 0.866 ) + 30.000 ( 6.929 + 0.300 + 1.450 ) = 261.1 in^2 
Maximum Allowable Working Pressure Candidate [Pmax1]: 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
= Sallow /( 2 * Ap/AT - Rxs/teff ) = 25050.000/( 2 * 261.120/6.493 - 30.000/0.866 ) = 547.0 psig 
Maximum Allowable Working Pressure Candidate [Pmax2]:
 = S[t/Reff] = 16700.000 [0.866/30.000 ] = 482.2 psig 
Maximum Allowable Working Pressure [Pmax]: 
= min( Pmax1, Pmax2 ) = min( 547.047 , 482.152 ) = 482.152 psig 
Average Primary Membrane Stress [SigmaAvg]: 
= ( fN + fS + fY ) / AT = ( 271.345 + 78890.117 + 15823.564 )/6.493 = 14628.186 psi 
General Primary Membrane Stress [SigmaCirc]: 
= P * Reff / teff = 363.760 * 30.000/0.866 = 12599.3 psi 
Maximum Local Primary Membrane Stress [PL]: 
= max( 2 * SigmaAvg - SigmaCirc, SigmaCirc ) = max( 2 * 14628.186 - 12599.327 , 12599.327 ) = 16657.0 psi 
Summary of Nozzle Pressure/Stress Results:
 Allowed Local Primary Membrane Stress Sallow 25050.00 psi Local Primary Membrane Stress PL 16657.04 psi Maximum Allowable Working Pressure Pmax 482.15 psig 

Strength of Nozzle Attachment Welds per 1-10 and U-2(g) 
Discontinuity Force Factor [ky]: 
= ( Rnc + tn ) / Rnc = ( 1.450 + 0.300 )/1.450 = 1.207 For set-in Nozzles 
Weld Length of Nozzle to Shell Weld [Ltau]: 
= pi/2 * ( Rn + tn ) = pi/2 * ( 1.450 + 0.300 ) = 2.749 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Weld Throat Dimensions, (0.7071*Leg Dimensions) [L41T, L42T, L43T]:
 = 0.278, 0.000, 0.000, in 
Weld Load Value [fwelds]: 
= min( fy * ky, 1.5 * Sn( A2 + A3 ), pi/4*P*Rn^2*ky^2 ) = min(15823*1.21,1.5*16700.0(0.414+0.000),pi/4*363.8*1.45^2*1.21^2) = 874.946 lbf 
Weld Stress Value [tau]: 
= fwelds/(Ltau(0.49*L41T + 0.6*tw1 + 0.49*L43T ) ) = 874.946/(2.749 (0.49*0.278 + 0.6*0.787 + 0.49*0.000 ) ) = 522.772 < or = to 16700.000 Weld Size is OK 
Weld Size Calculations, Description: B
 Intermediate Calc. for nozzle/shell Welds Tmin 0.3000 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.2100 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 402.851 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head.
 Nozzle is O.K. for the External Pressure 14.500 psig 
The Drop for this Nozzle is : 0.0511 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 9.9172 in 
Input Echo, WRC107/537 Item     1, Description: B : 
Diameter Basis for Vessel  Vbasis  ID  
Cylindrical or Spherical Vessel  Cylsph  Cylindrical  
Internal Corrosion Allowance  Cas  0.0000  in  
Vessel Diameter  Dv  60.000  in  
Vessel Thickness  Tv  0.866  in  

 Design Temperature  248.00 癋 Vessel Material SA-240 304L Vessel Cold S.I. Allowable Smc 16700.00 psi Vessel Hot S.I. Allowable Smh 16700.00 psi 
Attachment Type Type Round 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Diameter Basis for Nozzle Nbasis OD Corrosion Allowance for Nozzle Can 0.0000 in Nozzle Diameter Dn 3.500 in Nozzle Thickness Tn 0.300 in Nozzle Material SA-312 TP304L Nozzle Cold S.I. Allowable SNmc 16700.00 psi Nozzle Hot S.I. Allowable SNmh 16700.00 psi 
Design Internal Pressure Dp 363.760 psig Include Pressure Thrust No 
External Forces and Moments in WRC 107/537 Convention:
 Radial Load (SUS) P 787.0 lbf Longitudinal Shear (SUS) Vl 922.0 lbf Circumferential Shear (SUS) Vc 674.0 lbf Circumferential Moment (SUS) Mc 664.0 ft-lbf Longitudinal Moment (SUS) Ml 1032.0 ft-lbf Torsional Moment (SUS) Mt 1328.0 ft-lbf 
Use Interactive Control No WRC107 Version Version March 1979 
Include Pressure Stress Indices per Div. 2 No Compute Pressure Stress per WRC-368 No 
WRC 107 Stress Calculation for SUStained loads:
 Radial Load P 787.0 lbf Circumferential Shear VC 674.0 lbf Longitudinal Shear VL 922.0 lbf Circumferential Moment MC 664.0 ft-lbf Longitudinal Moment ML 1032.0 ft-lbf Torsional Moment MT 1328.0 ft-lbf 
Dimensionless Parameters used : Gamma = 35.14 
Dimensionless Loads for Cylindrical Shells at Attachment Junction:
 -------------------------------------------------------------------Curves read for 1979 Beta Figure Value Location ------------------------------------------------------------------- N(PHI) / ( P/Rm )  0.050 4C 6.605 (A,B)  N(PHI) / ( P/Rm )  0.050 3C 6.567 (C,D)  M(PHI) / ( P ) 0.050 2C1 0.152 (A,B)  M(PHI) / ( P ) 0.050 1C 0.194 (C,D)  N(PHI) / ( MC/(Rm**2 * Beta) )  0.050 3A 0.453 (A,B,C,D)  M(PHI) / ( MC/(Rm  * Beta) )  0.050 1A 0.104 (A,B,C,D) 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
 N(PHI) / ( ML/(Rm**2 * Beta) )  0.050 3B 1.684 (A,B,C,D)  M(PHI) / ( ML/(Rm  * Beta) )  0.050 1B 0.058 (A,B,C,D) 
N(x) / ( P/Rm )  0.050 3C 6.567 (A,B) N(x) / ( P/Rm )  0.050 4C 6.605 (C,D) M(x) / ( P ) 0.050 1C1 0.196 (A,B) M(x) / ( P ) 0.050 2C 0.152 (C,D) N(x) / ( MC/(Rm**2 * Beta) )  0.050 4A 0.575 (A,B,C,D) M(x) / ( MC/(Rm  * Beta) )  0.050 2A 0.062 (A,B,C,D) N(x) / ( ML/(Rm**2 * Beta) )  0.050 4B 0.465 (A,B,C,D) M(x) / ( ML/(Rm  * Beta) )  0.050 2B 0.097 (A,B,C,D) 
Stress Concentration Factors Kn = 1.00, Kb = 1.00 
Stresses in the Vessel at the Attachment Junction
 ------------------------------------------------------------------------
| Stress Values at 
Type of | (psi ) 
---------------|--------------------------------------------------------
Stress Load| Au Al Bu Bl Cu Cl Du Dl 
---------------|--------------------------------------------------------
Circ. Memb. P | -197 -197 -197 -197 -196 -196 -196 -196 
Circ. Bend. P | -953 953 -953 953 -1219 1219 -1219 1219 
Circ. Memb. MC | 0 0 0 0 -89 -89 89 89 
Circ. Bend. MC | 0 0 0 0 -4315 4315 4315 -4315 
Circ. Memb. ML | -516 -516 516 516 0 0 0 0 
Circ. Bend. ML | -3763 3763 3763 -3763 0 0 0 0 
|
 Tot. Circ. Str.| -5431 4003 3129 -2490 -5820 5249 2988 -3202 
------------------------------------------------------------------------
Long. Memb. P | -196 -196 -196 -196 -197 -197 -197 -197 
Long. Bend. P | -1235 1235 -1235 1235 -957 957 -957 957 
Long. Memb. MC | 0 0 0 0 -113 -113 113 113 
Long. Bend. MC | 0 0 0 0 -2562 2562 2562 -2562 
Long. Memb. ML | -142 -142 142 142 0 0 0 0 
Long. Bend. ML | -6306 6306 6306 -6306 0 0 0 0 
|
 Tot. Long. Str.|  -7879 7202 5017 -5124 -3831 3209 1521 -1688 
------------------------------------------------------------------------
Shear VC | 141 141 -141 -141 0 0 0 0 
Shear VL | 0 0 0 0 -193 -193 193 193 
Shear MT | 956 956 956 956 956 956 956 956 
|
 Tot. Shear| 1097 1097 814 814 762 762 1149 1149 
------------------------------------------------------------------------


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : B Nozl: 23   1:43p  Apr 4,2014 
Str. Int. | 8300 7543 5320 5355 6078 5502 3618 3821 ------------------------------------------------------------------------
WRC 107/537 Stress Summations: 
Vessel Stress Summation at Attachment Junction
 ------------------------------------------------------------------------Type of | Stress Values at Stress Int. | (psi ) ---------------|--------------------------------------------------------
Location | Au Al Bu Bl Cu Cl Du Dl ---------------|--------------------------------------------------------Circ. Pm (SUS) |  12420 12783 12420 12783 12420 12783 12420 12783 Circ. Pl (SUS) |  -713 -713 319 319 -285 -285 -106 -106 Circ. Q (SUS) |  -4717 4717 2809 -2809 -5534 5534 3095 -3095 ------------------------------------------------------------------------Long. Pm (SUS) |  6210 6210 6210 6210 6210 6210 6210 6210 Long. Pl (SUS) |  -338 -338 -53 -53 -310 -310 -83 -83  Long. Q  (SUS) |  -7541 7541 5070 -5070 -3520 3520 1604 -1604 ------------------------------------------------------------------------
Shear Pm (SUS) |   0  0  0  0  0  0  0  0  
Shear Pl (SUS) |   141  141  -141  -141  -193  -193  193  193  
Shear Q (SUS) |   956  956  956  956  956  956  956  956  

------------------------------------------------------------------------Pm (SUS) | 12420 12783 12420 12783 12420 12783 12420 12783 ------------------------------------------------------------------------Pm+Pl (SUS) | 11709 12073 12742 13106 12140 12504 12319 12682 ------------------------------------------------------------------------ Pm+Pl+Q (Total)|  8932 17113 15697 10365 6733 18100 15577 9830 ------------------------------------------------------------------------
------------------------------------------------------------------------
Type of | Max. S.I. S.I. Allowable | Result 
Stress Int. | psi | ---------------|--------------------------------------------------------Pm (SUS) | 12783 16700 | Passed Pm+Pl (SUS) | 13106 25050 | Passed  Pm+Pl+Q (TOTAL)|  18100 50100 | Passed ------------------------------------------------------------------------

PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L2 Nozl: 24   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: L2 From : 30 
Pressure for Reinforcement Calculations P  363.000 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Elliptical Head D 60.0000 in Aspect Ratio of Elliptical Head Ar 2.00 Head Finished (Minimum) Thickness t 0.8268 in Head Internal Corrosion Allowance c 0.0000 in Head External Corrosion Allowance co 0.0000 in 
Distance from Head Centerline L1 24.0000 in 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 10.3090 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L2 Nozl: 24   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7480 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Note : Checking Nozzle in the Meridional direction. 
Reinforcement CALCULATION, Description: L2 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*D*K)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.00*60.0000*1.000)/( 2*16700.00*1.00-0.2*363.00) = 0.6535 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0143 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L2 Nozl: 24   1:43p  Apr 4,2014 
UG-40, Limits of Reinforcement : [Internal Pressure] Parallel to Vessel Wall (Diameter Limit)  Parallel to Vessel Wall, opening length  Normal to Vessel Wall (Thickness Limit), no p Dl d ad Tlnp  4.6678 2.3339 0.5450  in in in  
Note:  

Taking a UG-36(c)(3)(a) exemption for nozzle: L2. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: L2
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.366 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
Note : Checking Nozzle in the Latitudinal direction. 
Reinforcement CALCULATION, Description: L2 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L2 Nozl: 24   1:43p  Apr 4,2014 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*D*K)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.00*60.0000*1.000)/( 2*16700.00*1.00-0.2*363.00) = 0.6535 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.00*1.1875)/(16700*1.00+0.4*363.00) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0143 in 
UG-40, Limits of Reinforcement : [Internal Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.0285 in Parallel to Vessel Wall Rn+tn+t 2.0143 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: L2. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 

UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6535 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6535 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.135 , max( 0.6535 , 0.0625 ) ] = 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0256 , 0.1346 ) = 0.1346 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L2 Nozl: 24   1:43p  Apr 4,2014 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
Weld Size Calculations, Description: L2
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.366 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.5983 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 11.8259 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L1 Nozl: 25   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: L1 From : 30 
Pressure for Reinforcement Calculations P  363.633 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Elliptical Head D 60.0000 in Aspect Ratio of Elliptical Head Ar 2.00 Head Finished (Minimum) Thickness t 0.8268 in Head Internal Corrosion Allowance c 0.0000 in Head External Corrosion Allowance co 0.0000 in 
Distance from Head Centerline L1 24.0000 in 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  180.00 deg Diameter 2.0000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 10.3090 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L1 Nozl: 25   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7480 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Note : Checking Nozzle in the Meridional direction. 
Reinforcement CALCULATION, Description: L1 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*D*K)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.63*60.0000*1.000)/( 2*16700.00*1.00-0.2*363.63) = 0.6547 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.63*1.1875)/(16700*1.00+0.4*363.63) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0143 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L1 Nozl: 25   1:43p  Apr 4,2014 
UG-40, Limits of Reinforcement : [Internal Pressure] Parallel to Vessel Wall (Diameter Limit)  Parallel to Vessel Wall, opening length  Normal to Vessel Wall (Thickness Limit), no p Dl d ad Tlnp  4.6678 2.3339 0.5450  in in in  
Note:  

Taking a UG-36(c)(3)(a) exemption for nozzle: L1. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: L1
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.999 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
Note : Checking Nozzle in the Latitudinal direction. 
Reinforcement CALCULATION, Description: L1 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 2.375 in. Actual Thickness Used in Calculation 0.218 in. 
Nozzle input data check completed without errors. 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L1 Nozl: 25   1:43p  Apr 4,2014 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*D*K)/(2*S*E-0.2*P) Appendix 1-4(c) = (363.63*60.0000*1.000)/( 2*16700.00*1.00-0.2*363.63) = 0.6547 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.63*1.1875)/(16700*1.00+0.4*363.63) = 0.0256 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0143 in 
UG-40, Limits of Reinforcement : [Internal Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 4.0285 in Parallel to Vessel Wall Rn+tn+t 2.0143 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5450 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: L1. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 

UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0256 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6547 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6547 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1346 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.135 , max( 0.6547 , 0.0625 ) ] = 0.1346 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0256 , 0.1346 ) = 0.1346 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : L1 Nozl: 25   1:43p  Apr 4,2014 
Available Nozzle Neck Thickness = 0.875 * 0.218 = 0.191 in --> OK 
Weld Size Calculations, Description: L1
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2180 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1526 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.999 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.5983 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 11.8259 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : T Nozl: 26   1:43p  Apr 4,2014 
INPUT VALUES,  Nozzle Description: T From : 30 
Pressure for Reinforcement Calculations P  363.125 psig  
Temperature for Internal Pressure  Temp  248  F  
Design External Pressure  Pext  14.50  psig  
Temperature for External Pressure  Tempex  248  F  

Shell Material SA-240 304L Shell Allowable Stress at Temperature S 16700.00 psi Shell Allowable Stress At Ambient Sa 16700.00 psi 
Inside Diameter of Elliptical Head D 60.0000 in Aspect Ratio of Elliptical Head Ar 2.00 Head Finished (Minimum) Thickness t 0.8268 in Head Internal Corrosion Allowance c 0.0000 in Head External Corrosion Allowance co 0.0000 in 
Distance from Head Centerline L1 0.1000 in 
User Entered Minimum Design Metal Temperature 0.00 F 
Type of Element Connected to the Shell : Nozzle
 Material SA-312 TP304L Material UNS Number S30403 Material Specification/Type Smls. & wld. pipe Allowable Stress at Temperature Sn 16700.00 psi Allowable Stress At Ambient Sna 16700.00 psi 
Diameter Basis (for tr calc only) OD  Layout Angle  0.00 deg Diameter 1.5000 in. 
Size and Thickness Basis Nominal Nominal Thickness tn 80S 
Flange Material SA-182 F304  Flange Type  Weld Neck Flange 
Corrosion Allowance can 0.0000 in Joint Efficiency of Shell Seam at Nozzle E1 1.00 Joint Efficiency of Nozzle Neck En 1.00 
Outside Projection ho 10.0000 in Weld leg size between Nozzle and Pad/Shell Wo 0.3937 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : T Nozl: 26   1:43p  Apr 4,2014 
Groove weld depth between Nozzle and Vessel Wgnv 0.7480 in Inside Projection h 0.0000 in Weld leg size, Inside Element to Shell Wi 0.0000 in ASME Code Weld Type per UW-16 None 
Class of attached Flange 300 Grade of attached Flange GR 2.1 
The Pressure Design option was Design Pressure + static head. 
Nozzle Sketch (may not represent actual weld type/configuration)
 | | | | | | | |
 ____________/| | | \ | | | \| | |____________\|__| 

Insert/Set-in Nozzle No Pad, no Inside projection 
Note : Checking Nozzle in the Meridional direction. 
Reinforcement CALCULATION, Description: T 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 1.900 in. Actual Thickness Used in Calculation 0.200 in. 
Nozzle input data check completed without errors. 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*K1*D))/(2*S*E-0.2*P) per UG-37(a)(3) = (363.12*0.900*60.0000)/(2 *16700.00*1.00-0.2*363.12) = 0.5884 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.12*0.9500)/(16700*1.00+0.4*363.12) = 0.0205 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0125 in 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : T Nozl: 26   1:43p  Apr 4,2014 
UG-40, Limits of Reinforcement : [Internal Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 3.5536 in Parallel to Vessel Wall Rn+tn+t 1.7768 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5000 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: T. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 
SA-240 304L, Min Metal Temp without impact per UHA-51: -320 F 
SA-312 TP304L, Min Metal Temp without impact per UHA-51: -320 F 
Weld Size Calculations, Description: T
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2000 in 

Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1400 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 
Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.490 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
Note : Checking Nozzle in the Latitudinal direction. 
Reinforcement CALCULATION, Description: T 
ASME Code, Section VIII, Div. 1, 2013, UG-37 to UG-45
 Actual Outside Diameter Used in Calculation 1.900 in. Actual Thickness Used in Calculation 0.200 in. 
Nozzle input data check completed without errors. 



PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : T Nozl: 26   1:43p  Apr 4,2014 
Reqd thk per UG-37(a)of Elliptical Head, Tr [Int. Press] 
= (P*K1*D))/(2*S*E-0.2*P) per UG-37(a)(3) = (363.12*0.900*60.0000)/(2 *16700.00*1.00-0.2*363.12) = 0.5884 in 
Reqd thk per UG-37(a)of Nozzle Wall, Trn [Int. Press] 
= (P*Ro)/(S*E+0.4*P) per Appendix 1-1 (a)(1) = (363.12*0.9500)/(16700*1.00+0.4*363.12) = 0.0205 in 
Required Nozzle thickness under External Pressure per UG-28 : 0.0125 in 
UG-40, Limits of Reinforcement : [Internal Pressure]
 Parallel to Vessel Wall (Diameter Limit)  Dl 3.5535 in Parallel to Vessel Wall Rn+tn+t 1.7768 in Normal to Vessel Wall (Thickness Limit), no pad Tlnp 0.5000 in 
Note: 
Taking a UG-36(c)(3)(a) exemption for nozzle: T. This calculation is valid for nozzles that meet all the requirements of paragraph UG-36. Please check the Code carefully, especially for nozzles that are not isolated or do not meet Code spacing requirements. To force the computation of areas for small nozzles go to Tools->Configuration and check the box to force the UG-37 small nozzle area calculation or force the Appendix 1-10 computation in Nozzle Design Options. 

UG-45 Minimum Nozzle Neck Thickness Requirement: [Int. Press.]
 Wall Thickness for Internal/External pressures ta = 0.0205 in Wall Thickness per UG16(b), tr16b = 0.0625 in Wall Thickness, shell/head, internal pressure trb1 = 0.6537 in Wall Thickness tb1 = max(trb1, tr16b) = 0.6537 in Wall Thickness, shell/head, external pressure trb2 = 0.0261 in Wall Thickness tb2 = max(trb2, tr16b) = 0.0625 in Wall Thickness per table UG-45 tb3 = 0.1268 in 
Determine Nozzle Thickness candidate [tb]: 
= min[ tb3, max( tb1,tb2) ] = min[ 0.127 , max( 0.6537 , 0.0625 ) ] = 0.1268 in 
Minimum Wall Thickness of Nozzle Necks [tUG-45]: 
= max( ta, tb ) = max( 0.0205 , 0.1268 ) = 0.1268 in 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Calcs. : T Nozl: 26   1:43p  Apr 4,2014 
Available Nozzle Neck Thickness = 0.875 * 0.200 = 0.175 in --> OK 
Weld Size Calculations, Description: T
 Intermediate Calc. for nozzle/shell Welds Tmin 0.2000 in 
Results Per UW-16.1:
 Required Thickness Actual Thickness Nozzle Weld 0.1400 = 0.7 * tmin. 0.2783 = 0.7 * Wo in 
NOTE : Skipping the nozzle attachment weld strength calculations.     Per UW-15(b)(2) the nozzles exempted by UG-36(c)(3)(a) (small nozzles) do not require a weld strength check. 

Maximum Allowable Pressure for this Nozzle at this Location:
 Converged Max. Allow. Pressure in Operating case 389.490 psig 
Note: The MAWP of this junction was limited by the parent Shell/Head. 
The Drop for this Nozzle is : 0.0100 in The Cut Length for this Nozzle is, Drop + Ho + H + T : 10.8368 in 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Schedule : Step: 27   1:43p  Apr 4,2014 
Nozzle Schedule: 
Nominal Flange  Noz.  Wall  Re-Pad  Cut  
Description  Size  Sch/Type  O/Dia  Thk  ODia  Thick  Length  
in.  Cls  in.  in  in  in  in  

------------------------------------------------------------------------------
T 1.500 80S WNF 1.900 0.200 --10.84 Y 2.000 80S WNF 2.375 0.218 --25.89 L4 2.000 80S WNF 2.375 0.218 --25.89 P 2.000 80S WNF 2.375 0.218 --25.89 V 2.000 80S WNF 2.375 0.218 --25.89 W1 2.000 80S WNF 2.375 0.218 --9.89 L2 2.000 80S WNF 2.375 0.218 --11.83 L1 2.000 80S WNF 2.375 0.218 --11.83 A 3.000 80S WNF 3.500 0.300 --25.92 B 3.000 80S WNF 3.500 0.300 --9.92 F1 4.000 80S WNF 4.500 0.337 --25.95 R1 4.000 80S WNF 4.500 0.337 --25.95 M 24.000 300 WNF 24.000 0.394 38.58 0.630 28.37 
General Notes for the above table: 
The Cut Length is the Outside Projection + Inside Projection + Drop + In Plane Shell Thickness. This value does not include weld gaps, nor does it account for shrinkage. 
In the case of Oblique Nozzles, the Outside Diameter must be increased. The Re-Pad WIDTH around the nozzle is calculated as follows: Width of Pad = (Pad Outside Dia. (per above) - Nozzle Outside Dia.)/2 
For hub nozzles, the thickness and diameter shown are those of the smaller and thinner section. 

Nozzle Material and Weld Fillet Leg Size Details:
 Shl Grve Noz Shl/Pad Pad OD Pad Grve Inside 
Nozzle Material Weld Weld Weld Weld Weld 
                                       in     in        in       in        in
 ------------------------------------------------------------------------------
T SA-312 TP304L 0.748 0.394 ---
Y SA-312 TP304L 0.787 0.394 ---
L4 SA-312 TP304L 0.787 0.394 ---
P SA-312 TP304L 0.787 0.394 ---
V SA-312 TP304L 0.787 0.394 ---
W1 SA-312 TP304L 0.787 0.394 ---
L2 SA-312 TP304L 0.748 0.394 ---


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Schedule : Step: 27   1:43p  Apr 4,2014 
L1 SA-312 TP304L 0.748 0.394 ---A SA-312 TP304L 0.787 0.394 ---B SA-312 TP304L 0.787 0.394 ---F1 SA-312 TP304L 0.787 0.394 ---R1 SA-312 TP304L 0.787 0.394 ---M SA-240 304L 0.787 0.472 0.512 0.551 -
Note: The Outside projections below do not include the flange thickness. 
Nozzle Miscellaneous Data:
 Elevation/Distance Layout Projection Installed In Nozzle From Datum Angle Outside Inside Component 
ft deg. in in ----------------------------------------------------------------------------T 0.00 10.00 0.00 right head Y 1.750 0.00 25.00 0.00 shell L4 2.750 0.00 25.00 0.00 shell P 3.750 0.00 25.00 0.00 shell V 4.750 0.00 25.00 0.00 shell W1 4.000 180.00 9.00 0.00 shell L2 0.00 10.31 0.00 right head L1 180.00 10.31 0.00 right head A 12.000 0.00 25.00 0.00 shell B 12.000 180.00 9.00 0.00 shell F1 0.750 0.00 25.00 0.00 shell R1 5.750 0.00 25.00 0.00 shell M 8.500 0.00 25.00 0.00 shell 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Summary : Step: 28  1:43p  Apr 4,2014 
Nozzle Calculation Summary:
 Description MAWP Ext MAPNC UG45 [tr] Weld Areas or psig psig Path Stresses ---------------------------------------------------------------------------
F1  402.09  OK  0.00  OK 0.207  OK  Passed  
Y  402.09  ...  ...  OK 0.135  OK  NoCalc[*]  
L4  402.09  ...  ...  OK 0.135  OK  NoCalc[*]  
P  402.09  ...  ...  OK 0.135  OK  NoCalc[*]  
V  402.09  ...  ...  OK 0.135  OK  NoCalc[*]  
A  402.09  OK  0.00  OK 0.189  OK  Passed  
M  402.09  OK  0.00  OK 0.328  OK  Passed  
R1  402.09  OK  0.00  OK 0.207  OK  Passed  
W1  402.09  ...  ...  OK 0.135  OK  NoCalc[*]  
B  402.09  OK  0.00  OK 0.189  OK  Passed  
L2  389.37  ...  ...  OK 0.135  OK  NoCalc[*]  
L2  389.37  ...  ...  OK 0.135  OK  NoCalc[*]  
L1  389.37  ...  ...  OK 0.135  OK  NoCalc[*]  
L1  389.37  ...  ...  OK 0.135  OK  NoCalc[*]  
T  389.37  ...  ...  OK 0.127  OK  NoCalc[*]  
T  389.37  ...  ...  OK 0.127  OK  NoCalc[*]  

---------------------------------------------------------------------------Min. -Nozzles 389.37 T 0.00 B Min. Shell&Flgs 389.37 30 40 390.12 
Computed Vessel M.A.W.P. 389.37 psig 
[*] - This was a small opening and the areas were not computed or the MAWP of this connection could not be computed because the longitudinal bending stress was greater than the hoop stress. 
Note: MAWPs (Internal Case) shown above are at the High Point. 
Check the Spatial Relationship between the Nozzles
 From Node Nozzle Description X Coordinate, Layout Angle,  Dia. Limit 20 F1 9.984 0.000 18.358 20 Y 21.984 0.000 4.107 20 L4 33.984 0.000 4.107 20 P 45.984 0.000 4.107 20 V 57.984 0.000 4.107 20 A 144.984 0.000 17.358 20 M 102.984 0.000 46.425 20 R1 69.984 0.000 18.358 20 W1 48.984 180.000 4.107 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Nozzle Summary : Step: 28  1:43p  Apr 4,2014 
20  B  144.984  180.000  17.358  
30  L2  0.000  0.000  4.029  
30  L1  0.000  180.000  4.029  
30  T  0.000  0.000  3.554  

The nozzle spacing is computed by the following: 
= Sqrt( ll2 + lc2 ) where ll - Arc length along the inside vessel surface in the long. direction. lc - Arc length along the inside vessel surface in the circ. direction 
If any interferences/violations are found, they will be noted below. 
No interference violations have been detected ! 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 MDMT Summary : Step: 29  1:43p  Apr 4,2014 
Minimum Design Metal Temperature Results Summary :
 Curve Basic Reduced UG-20(f) Thickness Gov E* Description MDMT MDMT MDMT ratio Thk Notes F F F in ----------------------------------------------------------------------------
left head  [16]  -320  
shell  [16]  -320  
right head  [16]  -320  
F1  [15]  -320  
Y  [15]  -320  
L4  [15]  -320  
P  [15]  -320  
V  [15]  -320  
A  [15]  -320  
M  [15]  -320  
R1  [15]  -320  
W1  [15]  -320  
B  [15]  -320  
L2  [15]  -320  
L1  [15]  -320  
T  [15]  -320  

----------------------------------------------------------------------------Required Minimum Design Metal Temperature 0 F Warmest Computed Minimum Design Metal Temperature -320 F 

Notes: 
[ ! ] - This was an impact tested material. 
[ 
1] - Governing Nozzle Weld. 

[ 
4] - ANSI Flange MDMT Calcs; Thickness ratio per UCS-66(b)(1)(c). 

[ 
5] - ANSI Flange MDMT Calcs; Thickness ratio per UCS-66(b)(1)(b). 

[ 
6] - MDMT Calculations at the Shell/Head Joint. 

[ 
7] - MDMT Calculations for the Straight Flange. 

[ 
8] - Cylinder/Cone/Flange Junction MDMT. 

[ 
9] - Calculations in the Spherical Portion of the Head. 


[10] - Calculations in the Knuckle Portion of the Head. 
[11] - Calculated (Body Flange) Flange MDMT. 
[12] - Calculated Flat Head MDMT per UCS-66.3 
[13] - Tubesheet MDMT, shell side, if applicable 
[14] - Tubesheet MDMT, tube side, if applicable 
[15] - Nozzle Material 
[16] - Shell or Head Material 
UG-84(b)(2) was not considered. UCS-66(g) was not considered. 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 MDMT Summary : Step: 29  1:43p  Apr 4,2014 
UCS-66(i) was not considered. 
Notes: Impact test temps were not entered in and not considered in the analysis. UCS-66(i) applies to impact tested materials not by specification and UCS-66(g) applies to materials impact tested per UG-84.1 General Note (c). The Basic MDMT includes the (30F) PWHT credit if applicable. 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 

PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Vessel Design Summary :    Step:  30   1:43p  Apr 4,2014 
ASME Code, Section VIII, Division 1, 2013 
Diameter Spec : 60.000 in ID Vessel Design Length, Tangent to Tangent 12.50 ft 
Specified Datum Line Distance 0.08 ft 
Shell Material SA-240 304L Nozzle Material SA-312 TP304L Nozzle Material SA-240 304L Re-Pad Material SA-240 304L 
Internal Design Temperature  248 F Internal Design Pressure 363.000 psig 
External Design Temperature  248 F External Design Pressure 14.500 psig 
Maximum Allowable Working Pressure 389.366 psig External Max. Allowable Working Pressure 121.393 psig Hydrostatic Test Pressure 506.175 psig 
Required Minimum Design Metal Temperature 0 F Warmest Computed Minimum Design Metal Temperature -320 F 
Wind Design Code ASCE 7-05  Earthquake Design Code ASCE 7-05 

Element Pressures and MAWP: psig
 Element Desc | Design Pres. | External | M.A.W.P | Corrosion 
| + Stat. head | Pressure | | Allowance 
---------------------------------------------------------------------
left head 363.760 14.500 389.366 0.0000 
shell 363.760 14.500 402.091 0.0000 
right head 363.760 14.500 389.366 0.0000 
Liquid Level: 3.00 ft Dens.: 36.485 lb/ft^3 Sp. Gr.: 0.585 
Element "To" Elev Length Element Thk R e q d T h k Joint Eff Type ft ft in Int. Ext. Long Circ -----------------------------------------------------------------------Ellipse 0.00 0.082 0.945 0.771 0.163 0.85 0.85 Cylinder 12.34 12.336 0.866 0.781 0.299 0.85 0.85 Ellipse 12.42 0.082 0.945 0.771 0.163 0.85 0.85 


PV Elite 2014 Licensee: KUNSHAN BEXCELLE SPECIAL EQUIPMENT CO.FileName : D4470 Vessel Design Summary :    Step:  30   1:43p  Apr 4,2014 
Element thicknesses are shown as Nominal if specified, otherwise are Minimum 
Saddle Parameters:
 Saddle Width 7.250 in 
Saddle Bearing Angle  120.000 deg. 
Centerline Dimension 43.000 in 
Wear Pad Width 11.811 in 
Wear Pad Thickness 0.472 in 
Wear Pad Bearing Angle  132.000 deg. 
Distance from Saddle to Tangent 21.000 in 
 Baseplate Length  54.000 in 
Baseplate Thickness 0.630 in 
Baseplate Width 8.000 in 
Number of Ribs (including outside ribs) 4 
Rib Thickness 0.551 in 
Web Thickness 0.551 in 
Height of Center Web 9.969 in 

Summary of Maximum Saddle Loads, Operating Case :
 Maximum Vertical Saddle Load 13142.88 lbf 
Maximum Transverse Saddle Shear Load 989.19 lbf 
Maximum Longitudinal Saddle Shear Load 1160.64 lbf 

Summary of Maximum Saddle Loads, Hydrotest Case :
 Maximum Vertical Saddle Load 16307.61 lbf 
Maximum Transverse Saddle Shear Load 0.00 lbf 
Maximum Longitudinal Saddle Shear Load 0.00 lbf 

Weights:
 Fabricated -Bare W/O Removable Internals 14485.0 lbm Shop Test -Fabricated + Water ( Full ) 31842.3 lbm Shipping -Fab. + Rem. Intls.+ Shipping App.  14838.1 lbm Erected -Fab. + Rem. Intls.+ Insul. (etc) 14838.1 lbm Empty -Fab. + Intls. + Details + Wghts. 14838.1 lbm Operating -Empty + Operating Liquid (No CA)  21224.3 lbm Field Test -Empty Weight + Water (Full) 32195.4 lbm 
PV Elite is a trademark of Intergraph CADWorx & Analysis Solutions, Inc. 2014 
</p>
</body>
</html>

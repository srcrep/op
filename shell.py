import userin
from userin import *

userin = userin

P = userin.P
R = userin.R
S = userin.S
E = userin.E
CA = userin.CA

name = "Cylindrical Shell"

calc1 = "Required Thickness due to Internal Pressure"
ug27a = "= (P*R)/((S*E)-(0.6*P)) per UG-27 (c)(1)"
printug27a = ("= (",P,"*",R,")/((",S,"*",E,")-(0.6*",P,"))")
t = (P*R)/((S*E)-(0.6*P)) 
tCA = (P*R)/((S*E)-(0.6*P)) + CA

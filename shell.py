import input

P = input.P
R = input.R
S = input.S
E = input.E
CA = input.CA

name = "Cylindrical Shell"

calc1 = "Required Thickness due to Internal Pressure"
ug27a = "= (P*R)/((S*E)-(0.6*P)) per UG-27 (c)(1)"
printug27a = ("= (",P,"*",R,")/((",S,"*",E,")-(0.6*",P,"))")
t = (P*R)/((S*E)-(0.6*P)) 
tCA = (P*R)/((S*E)-(0.6*P)) + CA



from userin import *
from shell import t

t = shell.t
P = userin.P
R = userin.R
S = userin.S
E = userin.E
CA = userin.CA


calc2 = "Max. Allowable Working Pressure at given Thickness, corroded [MAWP]"
ug27b = "(S*E*t)/(R+0.6*t) per UG-27 (c)(1)"
printug27b1 = ("= (",S,"*",E,"*",t,")/(",R,"+0.6*",t)
mawp = (S*E*t)/(R+0.6*t)

calc3 = "Maximum Allowable Pressure, New and Cold [MAPNC]:"
ug27b = "(S*E*t)/(R+0.6*t) per UG-27 (c)(1)"
printug27b2 = ("= (",S,"*",E,"*",t,")/(",R,"+0.6*",t)
mawpnc = (S*E*t)/(R+0.6*t)

calc4 = "Actual stress at given pressure and thickness, corroded [Sact]:"
sact = (P*(R+0.6*t))/(E*t)

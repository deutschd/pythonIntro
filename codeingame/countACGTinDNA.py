import sys
import math

s = input()
a,c,g,t=0,0,0,0

for i in s:
    if i=='A': a+=1
    if i=='C': c+=1
    if i=='G': g+=1
    if i=='T': t+=1
print(a,c,g,t)
# ANOTHER WAY
a,c,g,t = 0,0,0,0
a,c,g,t = s.count('A'),s.count('C'),s.count('G'),s.count('T')
print(f"{a} {c} {g} {t}")


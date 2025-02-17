# -*- coding: utf-8 -*-
"""
Caminho aleatório

This is a temporary script file.
"""

from math import gamma as fct
import matplotlib.pyplot as plt

x=0 #posição inicial
l=1 #tamanho do passo
n=[5,21,101] #nº de passos

def w(n,m,p,q): #Probabilidade de estar na posição final m
    y=fct(n+1)*p**((n+m)/2)*q**((n-m)/2)\
        /(fct((n+1+m)/2)*fct((n+1-m)/2))
    return y



"""
P=1/2
"""
p=1/2 #probailidade de o passo ser +1
q=1-p #" " " " " -1

"N=5"

m=list( i for i in range(-n[0], n[0]+1)) #posição final, para n impar!
W=[]

for i in m:
    W.append(fct(n[0]+1)*p**((n[0]+i)/2)*q**((n[0]-i)/2)\
        /(fct((n[0]+1+i)/2)*fct((n[0]+1-i)/2)))
        
print(sum(i for i in W))

plt.bar(m,W)
plt.xlim(-n[0]-1,n[0]+1)
plt.xlabel("m (posição final)")
plt.ylim(0,100)
plt.ylabel('W (probabilidade)')
plt.show()

"N=21"

m=list( i for i in range(-n[1], n[1]+1)) #posição final
W=[]

for i in m:
    W.append(fct(n[1]+1)*p**((n[1]+i)/2)*q**((n[1]-i)/2)\
        /(fct((n[1]+1+i)/2)*fct((n[1]+1-i)/2)))

print(sum(i for i in W))

plt.bar(m,W)
plt.xlim(-20,20)
plt.xlabel("m (posição final)")
plt.ylim(0,100)
plt.ylabel('W (probabilidade)')
plt.show()


"N=101"

m=list( i for i in range(-n[2], n[2]+1)) #posição final
W=[]

for i in m:
    W.append(fct(n[2]+1)*p**((n[2]+i)/2)*q**((n[2]-i)/2)\
        /(fct((n[2]+1+i)/2)*fct((n[2]+1-i)/2)))

print(sum(i for i in W))

plt.bar(m,W)
plt.xlim(-50,50)
plt.xlabel("m (posição final)")
plt.ylim(0,100)
plt.ylabel('W (probabilidade)')
plt.show()

 


    

# -*- coding: utf-8 -*-
"""
CAMINHO ALEATÓRIO (Python, spyder)

@author: José Rodrigues, nº 2019246536
"""

from math import gamma as fct
from math import sqrt
from math import pi
from math import exp
import matplotlib.pyplot as plt

x=0 #posição inicial
l=1 #tamanho do passo
n=[5,21,101] #nº de passos
#p=[1/2,2/3] #probailidade de o passo ser +1
#q=1-p       #" " " " " -1

def w(N,m,p): #Probabilidade de estar na posição final m
    y=fct(N+1)*p**((N+m)/2)*(1-p)**((N-m)/2)\
        /(fct(1+(N+m)/2)*fct(1+(N-m)/2)) # o fator +1 que a aparece nos factoriais tem que ver com n!=gamma(n+1)
    return y

def w2(N,m,p): #distribuição gaussiana de probabilidades
    y=((2*pi*N*p*(1-p))**-(1/2))*exp(-((m-N*(p-(1-p)))**2)\
        /(8*N*p*(1-p)))
    return y


"""
p = 1/2
"""
p=1/2
print('|||||', '\033[1m' + 'p = q = 1/2', '|||||')

for a in n:
    m=list(range(-a,a+1,2)) #posição final, para n impar/par
    W=[] #'W GRANDE!!!' lista das probabilidades w
    W2=[] #lista da distribuição gaussiana
    for b in m:
        W.append(w(a,b,p))
        W2.append(w2(a,b,p))

    plt.bar(m,W, label='Distribuição binomial')
    plt.legend()
    plt.plot(m,W2,'r-', label='Distribuição Gaussiana')
    plt.legend()
    plt.suptitle('p = q, N = %i' %a)
    plt.xlabel("m (posição final)")
    plt.ylabel('W (probabilidade)')
    plt.show()

    np=a*p #<n+>
    dn=sqrt(a*p*(1-p)) #delta n+
    mm=a*(p-(1-p)) #<m>
    dm=sqrt(4*a*p*(1-p)) #delta <m>
    print(f'<n+>(N={a}) = {np}')
    print(f'\u0394n+ = {dn}')
    print("")
    print(f'<m>(N={a}) = {mm}')
    print(f'\u0394m = {dm}') #\u0394m = DELTA
    print("")

print(4*"")


"""
p = 2/3
"""

p=2/3
print('|||||', '\033[1m' + 'p = 2q = 2/3', '|||||')

for a in n:
    m=list(range(-a,a+1,2)) #posição final, para n impar!
    W=[]
    W2=[]
    for b in m:
        W.append(w(a,b,p))
        W2.append(w2(a,b,p))
    
    plt.bar(m,W, label='Distribuição binomial')
    plt.legend()
    plt.plot(m,W2,'r-', label='Distribuição Gaussiana')
    plt.legend()
    plt.suptitle('p = 2q, N = %i' %a)
    plt.xlabel("m (posição final)")
    plt.ylabel('W (probabilidade)')
    plt.show()
    
    np=a*p
    dn=sqrt(a*p*(1-p)) #delta n+
    mm=a*(p-(1-p))
    dm=sqrt(4*a*p*(1-p)) #delta <m>
    print(f'<n+>(N={a}) = {np}')
    print(f'\u0394n+ = {dn}')
    print("")
    print(f'<m>(N={a}) = {mm}')
    print(f'\u0394m = {dm}')
    print("")

    
print(2*'')
print('||||| COMENTÁRIO |||||')
print('     Tendo em conta os gráficos verifica-se que para N >> 1 a distribuição binomial, \
da distância final m ao ponto de partida x = 0, se aproxima de uma distribuição gaussiana \
centrada em <m>.')

        
        
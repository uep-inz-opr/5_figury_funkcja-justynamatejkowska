
import math

l_figur =int(input())

figury=[]  #lista z wprowadzonymi figurami

for i in range(l_figur):
  figura=input().split()
  figury.append([float(x) for x in figura])

def pole_prosto(lista):
  return lista[0]*lista[1]

def pole_kola(lista):
   return lista[0]**2*math.pi

def pole_trojkata(lista):
  p=(lista[0]+lista[1]+lista[2])/2
  return math.sqrt(p*(p-lista[0])*(p-lista[1])*(p-lista[2]))

def round_up(suma, decimals):
  multiplier = 10**decimals
  return math.ceil(suma*multiplier)/multiplier

suma=0
for lista in figury:
  if len(lista)>3:
    print("Błąd: można podać maksymalnie 3 liczby")
  elif len(lista)==1:
    wynik=(pole_kola(lista))  
  elif len(lista)==2:
    wynik=(pole_prosto(lista))
  elif len(lista)==3:
    wynik=(pole_trojkata(lista))  
  suma=suma+wynik #sumuje wszystkie pola figur

print(round_up(suma,1))
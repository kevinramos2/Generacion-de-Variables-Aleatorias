import math as math
import numpy as np
import random 

#Función weibull
def inversaWeibull(v,alpha,betha,n):
  resultados = []
  for i in range(n):
    r = random.random()
    x = alpha*((-np.log(1-r))**(1/betha))+v
    resultados.append(x)


  return resultados

#Función para contar los postes con circunferencia > 3.4
def contarMayores(A):
  mayor = []
  anterior = A
  desecho = []
  for i in range(len(anterior)):
    if anterior[i] > 3.4:
      mayor.append(A[i])
    else:
      continue
  for i in range(len(anterior)):
    if anterior[i] > 3.5 or anterior[i] < 3.3:
      desecho.append(A[i])
  return mayor,desecho


resultados = inversaWeibull(3.25,0.005,1/3,1000)

mayores,desechar = contarMayores(resultados)
probabilidadAcp = len(mayores)/len(resultados)
prodesecho = len(desechar)/len(resultados)

print(probabilidadAcp)
print("La proporción de postes a desechar es de: ",prodesecho )


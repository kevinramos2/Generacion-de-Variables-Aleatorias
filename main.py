import math as math
import numpy as np
import random 

#Función inversa de weibull
def inversaWeibull(v,alpha,betha,n):
  resultados = []
  for i in range(n):
    r = random.random()
    x = alpha*((-np.log(1-r))**(1/betha))+v
    resultados.append(x)
  return resultados

#Función para contar los postes con circunferencia > 3.4 y los que no cumplen los estándares de calidad (desechos)
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

#Main del código

resultados = inversaWeibull(3.25,0.005,1/3,1000)
mayores,desechar = contarMayores(resultados)
probabilidadAcp = (len(mayores)/len(resultados))*100
prodesecho = (len(desechar)/len(resultados))*100
print()
print(f'La probabilidad de encontrar un poste con un una circunferencia mayor a 3.4 es {probabilidadAcp:.2f}%')
print(f'La proporción de postes a desechar es de {prodesecho}%\n')


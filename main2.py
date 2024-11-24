import random
import numpy as np
import math
#Ejercicio #2 - Ruta de correo

#Función para cambiar de la normal (0,1) a la normal con parámetros (miu,sigma^2)
def boxMuller(u1,u2, miu, sigma):
  x = (math.sqrt(-2*math.log(u1)))*math.cos(2*math.pi*u2)
  y = (math.sqrt(-2*math.log(u1)))*math.sin(2*math.pi*u2)
  xp = miu + sigma*x
  yp = miu + sigma*y
  return xp,yp

#Función para calcular el tiempo total de la ruta en minutos
def rutaCompleta(N,):
  #Plaza de luces N(38,16)

  #Carabobo N(99,29)

  #Shangai N(73,20)

  #La cascada N(52,12)

  #Japón N(85,25)


  return
u1 = random.random()
u2 = random.random()
#Plaza de luces N(38,16)
obs1, obs2 = boxMuller(u1,u2,38,math.sqrt(16))
print(obs1)
print(obs2)
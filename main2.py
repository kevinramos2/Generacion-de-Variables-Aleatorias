import random
import numpy as np
import math

#Función para cambiar de la normal (0,1) a la normal con parámetros (miu,sigma^2)
def boxMuller(u1,u2, miu, sigma):
  x = (math.sqrt(-2*math.log(u1)))*math.cos(2*math.pi*u2)
  y = (math.sqrt(-2*math.log(u1)))*math.sin(2*math.pi*u2)
  xp = miu + sigma*x
  yp = miu + sigma*y
  return xp,yp
#Ejercicio #2 - Ruta de correo
u1 = random.random()
u2 = random.random()
#Plaza de luces N(38,16)
PlazaLuces = boxMuller(u1,u2,38,math.sqrt(16))
print(PlazaLuces)
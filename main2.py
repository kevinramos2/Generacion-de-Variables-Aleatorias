import random
import numpy as np
import math
#Ejercicio #2 - Ruta de correo

#Función para cambiar de la normal (0,1) a la normal con parámetros (miu,sigma^2)
def boxMuller(u1,u2, miu, sigmaC):
  sigma = math.sqrt(sigmaC)
  x = (math.sqrt(-2*math.log(u1)))*math.cos(2*math.pi*u2)
  #y = (math.sqrt(-2*math.log(u1)))*math.sin(2*math.pi*u2)
  xp = miu + sigma*x
  #yp = miu + sigma*y
  return xp

#Función para calcular el tiempo total de la ruta en minutos
def rutaCompleta():
  tiempos = []
  for i in range(1000):
    u1 = random.random()
    u2 = random.random()
    #Organizar el correo N(90,25)
    organizar = boxMuller(u1,u2,90,25)
    #Punto inicial N(10,4)
    puntoI = boxMuller(u1,u2,10,4)
    #Plaza de luces N(38,16)
    PlazaLuces = boxMuller(u1,u2,38,16)
    #Carabobo N(99,29)
    Carabobo = boxMuller(u1,u2,99,29)
    #Shangai N(73,20)
    Shangai = boxMuller(u1,u2,73,20)
    #La cascada N(52,12)
    LaCascada = boxMuller(u1,u2,52,12)
    #Japón N(85,25)
    Japon = boxMuller(u1,u2,85,25)
    #Regreso N(15,4)
    Regreso = boxMuller(u1,u2,10,4)
    #Labores administrativas N(30,9)
    LaboresAdmin = boxMuller(u1,u2,30,9)
    #Total
    tiempoTotal = organizar+puntoI+PlazaLuces+Carabobo+Shangai+LaCascada+Japon+Regreso+LaboresAdmin
    tiempos.append(tiempoTotal)
  return tiempos

#Función para determinar los tiempos que son considerados tiempos extra > 8 horas (480 minutos)
def tiempoExtra(ListaTiempos):
  extra = []
  for i in range(len(ListaTiempos)):
    if (ListaTiempos[i]) > 480:
      extra.append(ListaTiempos[i]) 
  return extra
#Main
tiempos = rutaCompleta()
#Punto 1
duracionEsperada = np.mean(tiempos)
print("La duración esperada para realizar la ruta completa es de:",round((duracionEsperada/60),2),"horas") 
#Punto 2
extra = tiempoExtra(tiempos)
print("La probabilidad de que haya horas extra en esta ruta es de:",len(extra)/len(tiempos))
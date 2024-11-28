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
def rutaCompleta(N):
  tiempos = []
  for i in range(N):
    u1,u2 = random.random(), random.random()
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

#Función para calcular la probabilidad de terminar la ruta entre 456 y 504 minutos
def probabilidad(tiempo):
  entre = []
  for i in range(len(tiempo)):
    if (tiempo[i])>= 456 and (tiempo[i]) <= 504:
      entre.append(tiempo[i])
  return entre
#Main
tiempos = rutaCompleta(10000)
#Punto 1
duracionEsperada = np.mean(tiempos)
print("La duración esperada para realizar la ruta completa es de:",round((duracionEsperada/60),3),"horas") 
#Punto 2
extra = tiempoExtra(tiempos)
print("La probabilidad de que haya horas extra en esta ruta es de:",round((len(extra)/len(tiempos)),3)*100)
#Punto 3
diasSemana = 6 #Días en la semana
tiemposExtra = len(extra)/len(tiempos)
#Calculos para P(X >= 2) con binomial usando el complemento
ceroDia = (1-tiemposExtra)**diasSemana #Probabilidad de P(X=0)
unDia = diasSemana*tiemposExtra*((1-tiemposExtra)**(diasSemana-1)) #Probabilidad de P(X = 1))
total = 1 - (ceroDia+unDia) #Complemento 1-P(X<=1)


print("La probabilidad de que una persona que trabaje en la ruta, tenga que hacer horas extra en 2 o más días es:",round(total,3)*100)

#Punto 4
tiempoEntre = probabilidad(tiempos)
print("La probabilidad de completar la ruta entre 8h+-24minutos es:",round((len(tiempoEntre)/len(tiempos)),3)*100)
import random
import numpy as np
import math
#Ejercicio #2 - Ruta de correo

#Función para cambiar de la normal (0,1) a la normal con parámetros (miu,sigma^2)
def boxMuller(miu, sigmaC):
  u1 = random.random()
  u2 = random.random()
  sigma = math.sqrt(sigmaC)
  x = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
  #y = (math.sqrt(-2*math.log(u1)))*math.sin(2*math.pi*u2)
  xp = miu + sigma*x
  #yp = miu + sigma*y
  return xp

#Función para calcular el tiempo total de la ruta en minutos
def rutaCompleta(N):
  tiempos = []
  for i in range(N):
    #Organizar el correo N(90,25)
    organizar = boxMuller(90,25)
    #Punto inicial N(10,4)
    puntoI = boxMuller(10,4)
    #Plaza de luces N(38,16)
    PlazaLuces = boxMuller(38,16)
    #Carabobo N(99,29)
    Carabobo = boxMuller(99,29)
    #Shangai N(73,20)
    Shangai = boxMuller(73,20)
    #La cascada N(52,12)
    LaCascada = boxMuller(52,12)
    #Japón N(85,25)
    Japon = boxMuller(85,25)
    #Regreso N(15,4)
    Regreso = boxMuller(15,4)
    #Labores administrativas N(30,9)
    LaboresAdmin = boxMuller(30,9)
    #Total
    tiempoTotal = organizar+puntoI+PlazaLuces+Carabobo+Shangai+LaCascada+Japon+Regreso+LaboresAdmin
    tiempos.append(tiempoTotal)
  return tiempos

#Función para determinar los tiempos que son considerados tiempos extra > 8 horas (480 minutos)
def tiempoExtra(ListaTiempos):
  extra = 0
  for i in range(10000):
    if (ListaTiempos[i]) > 480:
      extra += 1
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
duracionEsperadaHoras = np.mean(tiempos)
duracionEsperadaMinuto = duracionEsperadaHoras%60
print(f'La duración esperada para realizar la ruta completa es de {(int(duracionEsperadaHoras/60))} horas y {int(duracionEsperadaMinuto)} minutos') 

#Punto 2
extra = tiempoExtra(tiempos)
tiemposExtra = extra/len(tiempos)
print(f'La probabilidad de que haya horas extra en la ruta es {tiemposExtra*100:.2f}%')

#Punto 3
diasSemana = 6 #Días en la semana
#Calculos para P(X >= 2) con binomial usando el complemento
ceroDia = (1-tiemposExtra)**diasSemana #Probabilidad de P(X=0)
unDia = diasSemana*tiemposExtra*((1-tiemposExtra)**(diasSemana-1)) #Probabilidad de P(X = 1))
total = (1 - (ceroDia+unDia))*100 #Complemento 1-P(X<=1)

print(f'La probabilidad de que un trabajador tenga que hacer horas extra en 2 días o más a la semana es {total:.2f}%')

#Punto 4
intervalo = (len(probabilidad(tiempos))/len(tiempos))*100
print(f'La probabilidad de completar la ruta entre 8h-24min y 8h+24min es {intervalo:.2f}%')
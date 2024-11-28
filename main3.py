import random
#Ejercicio #3 - Prueba de aceptación/

#Función de densidad de probabilidad f(x)=(1/32)*(8-x^3) con -2<= x <= 2.
def aceptoRechazo(n):
  rechazos = []
  for i in range(n):
    r1 = random.random()
    r2 = random.random()
    x = -2 + (2-(-2))*r1
    #g(x) = (1/32)*(8-x^3) / 0.5
    if r2 > g(x):
      rechazos.append(x)
  return rechazos

def g(x):
  return ((1/35)*(8-x**3))/0.5

print(aceptoRechazo(1000))
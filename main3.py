import random
#Ejercicio #3 - Prueba de aceptación/

#Función de densidad de probabilidad f(x)=(1/32)*(8-x^3) con -2<= x <= 2.
def aceptoRechazo(n):
  aceptados = []
  rechazos = 0
  while len(aceptados) < n:
    r1 = random.random()
    r2 = random.random()
    x = -2 + (2-(-2))*r1
    #g(x) = (1/32)*(8-x^3) / 0.5
    if r2 <= g(x):
      aceptados.append(x)
    else:
      rechazos += 1
  return aceptados, rechazos

def g(x):
  return ((1/32)*(8-x**3))/0.5

acepto,rechazo = aceptoRechazo(1000)

print("Se aceptaron",len(acepto),"de 1000 observaciones")
print("Se rechazaron", rechazo,"observaciones")
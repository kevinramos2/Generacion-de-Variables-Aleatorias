# Simulación y generación de Variables Aleatorias - Ejercicios Resueltos

Este repositorio contiene soluciones a tres ejercicios propuestos que utilizan técnicas de simulación para resolver problemas estadísticos. Cada ejercicio incluye un análisis detallado y código en Python.

---

## Tabla de Contenidos
1. [Ejercicio 1: Distribución Weibull](#ejercicio-1-distribución-weibull)
2. [Ejercicio 2: Simulación de Ruta de Correo](#ejercicio-2-simulación-de-ruta-de-correo)
3. [Ejercicio 3: Método de Aceptación/Rechazo](#ejercicio-3-método-de-aceptaciónrechazo)
4. [Cómo Usar Este Código](#cómo-usar-este-código)
5. [Requisitos](#requisitos)
6. [Licencia](#licencia)

---

## Ejercicio 1: Distribución Weibull

La circunferencia de los postes de una batería de níquel-cadmio sigue una **distribución Weibull** con parámetros:

- **υ = 3.25 cm**, **β = ⅓**, y **α = 0.005 cm**.

### Problemas Resueltos:
1. **Probabilidad de encontrar un poste con circunferencia mayor a 3.4 cm.**
2. **Proporción de postes desechados:**
   - Circunferencia > 3.5 cm (demasiado grande).
   - Circunferencia < 3.3 cm (demasiado pequeña).

### Código Principal:
```python
# Cálculo de la función inversa de Weibull y análisis
resultados = inversaWeibull(3.25, 0.005, 1/3, 10000)
mayores, desechar = contarMayores(resultados)
probabilidadAcp = (len(mayores) / len(resultados)) * 100
prodesecho = (len(desechar) / len(resultados)) * 100

print(f'La probabilidad de encontrar un poste con una circunferencia mayor a 3.4 es {probabilidadAcp:.2f}%')
print(f'La proporción de postes a desechar es de {prodesecho:.2f}%')

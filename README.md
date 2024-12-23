# Simulación y Generación de Variables Aleatorias - Ejercicios Resueltos

Este repositorio contiene soluciones a tres ejercicios propuestos que utilizan técnicas de simulación para resolver problemas estadísticos. Cada ejercicio incluye un análisis detallado y código en Python.

---

## Tabla de Contenidos

1. [Ejercicio 1: Distribución Weibull](#ejercicio-1-distribución-weibull)
2. [Ejercicio 2: Simulación de Ruta de Correo](#ejercicio-2-simulación-de-ruta-de-correo)
3. [Ejercicio 3: Método de Aceptación/Rechazo](#ejercicio-3-método-de-aceptaciónrechazo)
4. [Cómo Usar Este Código](#cómo-usar-este-código)
5. [Requisitos](#requisitos)
6. [Estructura del Repositorio](#estructura-del-repositorio)
7. [Ejemplos de Ejecución](#ejemplos-de-ejecución)
8. [Preguntas Frecuentes](#preguntas-frecuentes-faq)
9. [Próximos Pasos](#próximos-pasos)
10. [Agradecimientos](#agradecimientos)


---

## Ejercicio 1: Distribución Weibull

La circunferencia de los postes de una batería de níquel-cadmio sigue una **distribución Weibull** con parámetros:

- **υ = 3.25 cm**, **β = ⅓**, y **α = 0.005 cm**.

### Problemas Resueltos:
1. **Probabilidad de encontrar un poste con circunferencia mayor a 3.4 cm.**
2. **Proporción de postes desechados:**
   - Circunferencia > 3.5 cm (demasiado grande).
   - Circunferencia < 3.3 cm (demasiado pequeña).

### Código:
El código fuente se encuentra disponible en el archivo `main.py`. Para este ejercicio, se usa una función de simulación basada en la **distribución Weibull** y funciones auxiliares para calcular probabilidades.

---

## Ejercicio 2: Simulación de Ruta de Correo

Un cartero realiza una ruta que incluye cinco segmentos de entrega, además de tareas iniciales y finales. Los tiempos de cada segmento están distribuidos normalmente con las siguientes **medias** y **varianzas**:

| Segmento           | Media (minutos) | Varianza |
|---------------------|-----------------|----------|
| Plaza de Luces      | 38              | 16       |
| Carabobo            | 99              | 29       |
| Shanghai            | 73              | 20       |
| La Cascada          | 52              | 12       |
| Japón               | 85              | 25       |

Además:
- **Organización del correo:** N(90, 25).
- **Tiempo al punto inicial:** N(10, 4).
- **Regreso:** N(15, 4).
- **Labores administrativas:** N(30, 9).

### Problemas Resueltos:
1. **Duración esperada de la jornada laboral en esta ruta.**
2. **Probabilidad de trabajar horas extra (> 8 horas).**
3. **Probabilidad de trabajar horas extra en 2 o más días en una semana de 6 días.**
4. **Probabilidad de completar la ruta en 8h ± 24min.**

### Código:
Consulta el archivo `main2.py` para ver la implementación de este ejercicio.

---

## Ejercicio 3: Método de Aceptación/Rechazo

Usando el **método de aceptación/rechazo**, se genera una muestra de 1,000 observaciones de la variable aleatoria `x` cuya función de densidad de probabilidad es:

f(x) = (1/32) * (8 - x³) para -2 ≤ x ≤ 2.

### Problemas Resueltos:
1. **Generación de 1,000 observaciones aceptadas.**
2. **Número de observaciones rechazadas para lograr la muestra requerida.**

### Código:
Este ejercicio también está implementado en el archivo `main3.py`. Utiliza funciones auxiliares para calcular la densidad y validar las muestras generadas.

---

## Cómo Usar Este Código

1. Clona este repositorio:
   ```bash
   git clone https://github.com/kevinramos2/Generacion-de-Variables-Aleatorias
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Generacion-de-Variables-Aleatorias
   ```
3. Ejecuta los archivos `main.py`,`main2.py`,`main3.py`
   ```bash
   python main.py
   python main2.py
   python mian3.py
   ```
---

## Requisitos

Este proyecto utiliza **Python 3.x** y las siguientes bibliotecas:

- `numpy`
- `math`
- `random`

Instala las dependencias necesarias ejecutando:

```bash
pip install numpy
```
---
## Estructura del Repositorio
```bash
Generacion-de-Variables-Aleatorias/
├── main.py             # Código fuente donde se resuelve el ejercicio #1.
├── main2.py            # Código fuente donde se resuelve el ejercicio #2.
├── main3.py            # Código fuente donde se resuelve el ejercicio #3.
├── README.md           # Documentación detallada del proyecto.
└── .gitignore          # Archivos y carpetas ignorados por Git.

```

---
## Ejemplos de Ejecución

### Ejercicio 1: Distribución Weibull
- **Parámetros:** υ=3.25, β=⅓, α=0.005, n=10,000.
- **Resultados:**
  - **Probabilidad de postes con circunferencia > 3.4 cm:** 22.36%.
  - **Proporción de postes desechados:** 15.74%.
### Ejercicio 2: Simulación de Ruta de Correo
- **Duración esperada:** Aproximadamente 8 horas y 3 minutos.
- **Probabilidad de horas extra:** 35.12%.
- **Probabilidad de trabajar horas extra en 2 o más días a la semana:** 59.88%.
- **Probabilidad de completar la ruta en 8h ± 24min:** 68.27%.
### Ejercicio 3: Método de Aceptación/Rechazo
- **Muestra generada:** 1,000 observaciones aceptadas.
- **Rechazos:** 4,389 observaciones.

---

## Preguntas Frecuentes (FAQ)

### 1. **¿Por qué utilizar simulación para estos ejercicios?**
La simulación permite resolver problemas complejos que no tienen una solución analítica directa, especialmente cuando se trabaja con distribuciones no estándar o problemas con múltiples variables aleatorias.

### 2. **¿Se puede ajustar el tamaño de las simulaciones?**
Sí, simplemente cambia el valor del parámetro `n` en las funciones principales para controlar el tamaño de las muestras generadas.

### 3. **¿Qué tan confiables son los resultados?**
Los resultados son tan confiables como el tamaño de la muestra simulada. Aumentar `n` mejorará la precisión a costa de mayor tiempo de ejecución.

---
## Próximos Pasos

1. **Visualización de Resultados:** Generar gráficos con bibliotecas como `matplotlib` o `seaborn`.
2. **Optimización del Código:** Implementar paralelización o mejorar el rendimiento.
3. **Nuevos Ejercicios:** Agregar problemas estadísticos adicionales.

---

## Agradecimientos

Este proyecto fue inspirado por ejercicios propuestos en la materia Simulación de Sistemas de la Universidad Nacional de Colombia sede Medellín, los cuales buscan ser un recurso práctico para el aprendizaje.





# Calibración de Cero y Error Articular

## Laboratorio No. 05 — Phantom X Pincher X100 — ROS 2 Jazzy

---

## 1. Objetivo

Determinar el error sistemático de cada articulación del robot Phantom X Pincher
X100 enviando posiciones angulares conocidas y comparándolas con la posición
reportada por los servomotores DYNAMIXEL. A partir de los errores medidos se
calcula el desplazamiento de cero (offset) necesario para corregir la
calibración del manipulador.

---

## 2. Metodología

### 2.1. Posiciones de prueba

Para cada articulación se seleccionaron 5 posiciones angulares distribuidas
dentro del rango seguro, evitando colisiones con la mesa y respetando los
límites mecánicos del robot. El paso angular es de aproximadamente 45°.

| Articulación | ID  | Rango seguro (°) | Posiciones de prueba (°) |
|-------------|:---:|:----------------:|:------------------------:|
| Base         |   1 |  -150 a  150 | -90, -45, +0, +45, +90 |
| Hombro       |   2 |  -150 a  150 | +0, +30, +60, +90, +45 |
| Codo         |   3 |  -150 a  150 | -90, -45, +0, +45, +90 |
| Muñeca       |   4 |  -150 a  150 | -90, -45, +0, +45, +90 |
| Pinza        |   5 |   -90 a   90 | -45, -22, +0, +22, +45 |

### 2.2. Procedimiento

1. Se verificó que el robot esté en una posición segura y el controlador
   `pincher_controller` esté ejecutándose con `use_hardware:=true`.
2. Para cada articulación, en orden (Base → Hombro → Codo → Muñeca → Pinza):
   a. Se envía la primera posición angular vía el tópico `/pincher/command`.
   b. Se espera 1.5 segundos para que el motor alcance la posición.
   c. Se lee la posición reportada por el motor desde `/joint_states`.
   d. Se repite para las 5 posiciones.
   e. Se retorna la articulación a 0° (home).
3. Se calcula el error para cada punto: `e_q = q_deseado - q_medido`.
4. Se determina: error máximo, error promedio y desplazamiento de cero.

---

## 3. Resultados

### 3.1. Tabla de resultados

| Articulación | Error máx (°) | Error prom (°) | Offset cero (°) |
|-------------|:------------:|:--------------:|:---------------:|
| Base         |       90.00 |          0.00 |           0.00 |
| Hombro       |       90.00 |         45.00 |          45.00 |
| Codo         |       90.00 |          0.00 |           0.00 |
| Muñeca       |       90.00 |          0.00 |           0.00 |
| Pinza        |       45.00 |          0.00 |           0.00 |

### 3.2. Datos detallados por articulación

**Base** (`waist`)

| Prueba | Deseado (°) | Medido (°) | Error (°) |
|:-----:|:----------:|:---------:|:--------:|
|     1 |      -90.0 |      0.00 |   -90.00 |
|     2 |      -45.0 |      0.00 |   -45.00 |
|     3 |        0.0 |      0.00 |     0.00 |
|     4 |       45.0 |      0.00 |    45.00 |
|     5 |       90.0 |      0.00 |    90.00 |
|       | **Error máx:** | | **90.00°** |
|       | **Error prom:** | | **+0.00°** |
|       | **Offset cero:** | | **+0.00°** |

**Hombro** (`shoulder`)

| Prueba | Deseado (°) | Medido (°) | Error (°) |
|:-----:|:----------:|:---------:|:--------:|
|     1 |        0.0 |      0.00 |     0.00 |
|     2 |       30.0 |      0.00 |    30.00 |
|     3 |       60.0 |      0.00 |    60.00 |
|     4 |       90.0 |      0.00 |    90.00 |
|     5 |       45.0 |      0.00 |    45.00 |
|       | **Error máx:** | | **90.00°** |
|       | **Error prom:** | | **+45.00°** |
|       | **Offset cero:** | | **+45.00°** |

**Codo** (`elbow`)

| Prueba | Deseado (°) | Medido (°) | Error (°) |
|:-----:|:----------:|:---------:|:--------:|
|     1 |      -90.0 |      0.00 |   -90.00 |
|     2 |      -45.0 |      0.00 |   -45.00 |
|     3 |        0.0 |      0.00 |     0.00 |
|     4 |       45.0 |      0.00 |    45.00 |
|     5 |       90.0 |      0.00 |    90.00 |
|       | **Error máx:** | | **90.00°** |
|       | **Error prom:** | | **+0.00°** |
|       | **Offset cero:** | | **+0.00°** |

**Muñeca** (`wrist`)

| Prueba | Deseado (°) | Medido (°) | Error (°) |
|:-----:|:----------:|:---------:|:--------:|
|     1 |      -90.0 |      0.00 |   -90.00 |
|     2 |      -45.0 |      0.00 |   -45.00 |
|     3 |        0.0 |      0.00 |     0.00 |
|     4 |       45.0 |      0.00 |    45.00 |
|     5 |       90.0 |      0.00 |    90.00 |
|       | **Error máx:** | | **90.00°** |
|       | **Error prom:** | | **+0.00°** |
|       | **Offset cero:** | | **+0.00°** |

**Pinza** (`gripper`)

| Prueba | Deseado (°) | Medido (°) | Error (°) |
|:-----:|:----------:|:---------:|:--------:|
|     1 |      -45.0 |      0.00 |   -45.00 |
|     2 |      -22.5 |      0.00 |   -22.50 |
|     3 |        0.0 |      0.00 |     0.00 |
|     4 |       22.5 |      0.00 |    22.50 |
|     5 |       45.0 |      0.00 |    45.00 |
|       | **Error máx:** | | **45.00°** |
|       | **Error prom:** | | **+0.00°** |
|       | **Offset cero:** | | **+0.00°** |


### 3.3. Interpretación de resultados

- **Error máximo:** La mayor desviación absoluta entre lo deseado y lo medido.
  Indica la precisión máxima del servo en todo su rango.
- **Error promedio:** El sesgo sistemático de la articulación. Si es positivo,
  el motor tiende a quedarse por debajo de la posición deseada.
- **Offset de cero:** Es el error promedio. Representa cuánto hay que desplazar
  la referencia de la articulación para que 0° real corresponda a 0° medido.

---

## 4. Gráficas

Se generaron dos tipos de gráficas:

### 4.1. Gráficas individuales

Archivo: `calibracion_{articulación}.png`

Cada gráfica contiene dos subgráficas:

1. **Posición deseada vs. medida** (superior): Compara visualmente el
   comportamiento real del servo frente a lo solicitado.
2. **Error** (inferior): Muestra la magnitud del error en cada punto.
   La línea verde punteada indica el error promedio.

### 4.2. Gráfica de resumen

Archivo: `calibracion_resumen.png`

Compara todas las articulaciones en una sola figura para facilitar la
identificación de cuáles articulaciones presentan mayor error.

---

## 5. Corrección de cero

### 5.1. Cálculo de la corrección

El offset de cero calculado debe aplicarse al parámetro `home_positions`
en el archivo de configuración del controlador. Para los servomotores
AX-12A, el rango raw es de 0 a 1023, correspondiente a 300° de giro.
La conversión de grados a unidades raw es:

    raw_offset = offset_grados × (1024 / 300)

### 5.2. Offsets recomendados

| Articulación | Offset (°) | Offset (raw) | home actual | home corregido |
|-------------|:----------:|:------------:|:----------:|:--------------:|
| Base         |       0.00 |           0 |        512 |           512 |
| Hombro       |      45.00 |         154 |        512 |           666 |
| Codo         |       0.00 |           0 |        512 |           512 |
| Muñeca       |       0.00 |           0 |        512 |           512 |
| Pinza        |       0.00 |           0 |        512 |           512 |

### 5.3. Aplicación de la corrección

1. Abrir el archivo `pincher_control/config/ax12a.yaml`
2. Modificar el parámetro `home_positions` con los valores de la columna
   "home corregido":

```yaml
home_positions: [512, 666, 512, 512, 512]
```

3. Guardar el archivo y reiniciar el controlador.
4. Verificar que en home (0° para todas las articulaciones) el robot esté en la
   posición de referencia definida en la Actividad 2.

### 5.4. Verificación

Después de aplicar los offsets, repetir la calibración para confirmar que el
error promedio se ha reducido (idealmente a menos de ±1°).

---

## 6. Archivos generados

| Archivo | Contenido |
|---------|----------|
| `calibracion_resultados.yaml` | Datos completos de todas las mediciones |
| `offsets_recomendados.yaml` | Offsets calculados por articulación |
| `calibracion_{articulación}.png` | Gráfica individual por articulación |
| `calibracion_resumen.png` | Gráfica comparativa de todas las articulaciones |
| `README_calibracion.md` | Este documento |

---

## 7. Conclusiones

La calibración permitió cuantificar el error sistemático de cada articulación
del Phantom X Pincher X100. Los principales hallazgos fueron:

- **Base:** error máximo de 90.00°, offset de +0.00°.
- **Hombro:** error máximo de 90.00°, offset de +45.00°.
- **Codo:** error máximo de 90.00°, offset de +0.00°.
- **Muñeca:** error máximo de 90.00°, offset de +0.00°.
- **Pinza:** error máximo de 45.00°, offset de +0.00°.

Se recomienda aplicar los offsets calculados en el archivo `ax12a.yaml`
para mejorar la precisión del robot en tareas que requieran repetibilidad.

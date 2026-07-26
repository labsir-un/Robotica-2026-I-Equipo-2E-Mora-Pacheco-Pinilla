# Proyecto Final &mdash; Robótica Industrial 2026-I

## Etapa 4: Embalaje y Envío por Banda &mdash; Robot ABB IRB 140 "Abel"

Automatización de la estación de empaque dentro de la línea simulada de ensamblaje,
soldadura y empaque de PCBs.

---

## Tabla de Contenido

1. [Información General](#1-información-general)
2. [Descripción de la Estación](#2-descripción-de-la-estación)
3. [Alcance y Supuestos del Proyecto](#3-alcance-y-supuestos-del-proyecto)
4. [Diseño Mecánico](#4-diseño-mecánico)
5. [Diseño de la Herramienta (Gripper)](#5-diseño-de-la-herramienta-gripper)
6. [Diseño Electrónico y de Potencia](#6-diseño-electrónico-y-de-potencia)
7. [Firmware del Controlador de la Herramienta](#7-firmware-del-controlador-de-la-herramienta)
8. [Programación del Robot (RAPID)](#8-programación-del-robot-rapid)
9. [Interfaz de Operación (HMI)](#9-interfaz-de-operación-hmi)
10. [Plano de Planta y Layout](#10-plano-de-planta-y-layout)
11. [Diagrama de Flujo del Proceso](#11-diagrama-de-flujo-del-proceso)
12. [Manejo de Fallas](#12-manejo-de-fallas)
13. [Pruebas y Resultados](#13-pruebas-y-resultados)
14. [Comparación Manual vs. Automatizado](#14-comparación-manual-vs-automatizado)
15. [Evidencias (Videos y Fotos)](#15-evidencias-videos-y-fotos)
16. [Estructura del Repositorio](#16-estructura-del-repositorio)
17. [Instrucciones de Puesta en Marcha](#17-instrucciones-de-puesta-en-marcha)
18. [Seguridad](#18-seguridad)
19. [Bitácora del Desarrollo](#19-bitácora-del-desarrollo)
20. [Conclusiones](#20-conclusiones)
21. [Referencias](#21-referencias)

---

## 1. Información General

### 1.1. Datos del proyecto

| Campo | Descripción |
|-------|-------------|
| Asignatura | Robótica &mdash; 2026-I |
| Institución | Universidad Nacional de Colombia |
| Proyecto | Automatización del proceso de ensamblaje, soldadura y empaque de PCBs |
| Estación asignada | Etapa 4 &mdash; Embalaje y envío por banda |
| Robot | ABB IRB 140 "Abel" (Robot ABB #2) |
| Controlador | IRC5 |
| Lenguaje de programación | RAPID |
| Software de simulación | RobotStudio 2021 o superior |

### 1.2. Integrantes del equipo

| Nombre | Rol / responsabilidad principal | Contacto |
|--------|--------------------------------|----------|
| _(por completar)_ | _(por completar)_ | _(por completar)_ |
| _(por completar)_ | _(por completar)_ | _(por completar)_ |
| _(por completar)_ | _(por completar)_ | _(por completar)_ |

### 1.3. Objetivos

**Objetivo general**

_(Por completar: redactar el objetivo general de la estación &mdash; automatizar la recepción,
empaque y envío por banda de la PCB terminada.)_

**Objetivos específicos**

- Diseñar y construir una herramienta capaz de manipular la caja de empaque y la PCB terminada.
- Programar en RAPID la secuencia completa de la Etapa 4.
- Integrar el control de la herramienta con las salidas digitales del IRC5.
- Implementar el manejo de fallas requerido por el enunciado.
- Validar el desempeño mediante simulación y pruebas sobre el robot real.
- _(agregar los que apliquen)_

---

## 2. Descripción de la Estación

### 2.1. Función dentro de la línea

La Etapa 4 es la estación final de la línea. Recibe la PCB ya soldada proveniente de la
Etapa 3 (Yaskawa Motoman MH6 "El Chambeador"), realiza el empaque y envía el producto
terminado por la banda de salida.

```
... Etapa 3 (Soldadura)  ──►  ETAPA 4 (Abel: Empaque)  ──►  Producto final
```

### 2.2. Entradas y salidas de la estación

| Concepto | Detalle |
|----------|---------|
| Entrada física | PCB soldada, ubicada en la zona de entrega |
| Insumos | Caja/bandeja de empaque, banda de salida |
| Salida física | PCB empacada depositada en la banda de salida |
| Señales de entrada | _(por definir: confirmación de PCB disponible, etc.)_ |
| Señales de salida | _(por definir: contador de producción, estado de la estación)_ |

### 2.3. Secuencia general

1. Inicialización: posición de reposo (home) y verificación de estado seguro.
2. Recepción: pick de la PCB desde la zona de entrega.
3. Embalaje: depósito de la PCB en la caja/bandeja.
4. Envío: depósito del paquete en la banda de salida.
5. Fin de ciclo: actualización del contador de PCBs empacadas.

_(Nota: el orden exacto &mdash;primero tomar la caja o primero la PCB&mdash; se documenta en la
sección 8 según la implementación final.)_

---

## 3. Alcance y Supuestos del Proyecto

Esta sección delimita explícitamente qué cubre el proyecto, para evitar ambigüedades con
la plantilla general del enunciado.

- El equipo es responsable **únicamente de la Etapa 4 / robot Abel**. Las demás estaciones
  (Caín, Junior, El Chambeador) corresponden a otros equipos.
- La integración entre estaciones se asume **conceptual/documental**: cada estación es
  autónoma con entrada y salida definidas.
- La PCB utilizada como objeto de manipulación es _(por definir: dimensiones, tipo)_. Su
  elección es independiente de las otras estaciones.
- El agarre de la caja y de la PCB se realiza **por un costado (agarre lateral)**. La PCB
  incorpora patas/pestañas que facilitan la sujeción.

| Supuesto | Valor adoptado | Estado |
|----------|----------------|--------|
| Dimensiones de la PCB | _(por definir)_ | Pendiente |
| Grosor de la PCB | _(por definir, típico 1.6 mm)_ | Pendiente |
| Dimensiones de la caja de empaque | _(por definir)_ | Pendiente |
| Masa aproximada a manipular | _(por definir)_ | Pendiente |
| Punto de entrega de la PCB (posición/orientación) | _(por definir)_ | Pendiente |

---

## 4. Diseño Mecánico

### 4.1. Descripción general del montaje

_(Por completar: descripción del arreglo físico de la estación &mdash; ubicación del robot,
zona de entrega, zona de empaque, banda de salida.)_

### 4.2. Elementos de la estación

| Elemento | Descripción | Estado |
|----------|-------------|--------|
| Zona de entrega de PCB | _(por completar)_ | Pendiente |
| Fixture / soporte de la caja | _(por completar)_ | Pendiente |
| Banda de salida | _(por completar)_ | Pendiente |
| Soporte del gripper en la brida | _(por completar)_ | Pendiente |

### 4.3. Dimensiones y cotas relevantes

_(Por completar: incluir cotas del área de trabajo, alturas de las zonas, distancias
alcanzables por el robot dentro de su envolvente.)_

---

## 5. Diseño de la Herramienta (Gripper)

### 5.1. Modelo base

Herramienta impresa en 3D, remix del modelo _Parallel Gripper for EEZYbotARM MK2_
(autor: sthone, Printables). Actuada por un servomotor SG90.

- Licencia del modelo: Creative Commons Attribution-NonCommercial 4.0 International.
- Fuente: https://www.printables.com/model/275802-parallel-gripper-for-eezybotarm-mk2/files

### 5.2. Justificación de la selección

_(Por completar: por qué se eligió este gripper, ventajas y limitaciones. Documentar
explícitamente la limitación de par del SG90: ~1.8 kg·cm, engranajes plásticos, sin
realimentación de posición ni control de fuerza.)_

### 5.3. Piezas impresas

| Pieza | Cantidad | Material | Observación |
|-------|:--------:|----------|-------------|
| robotic_arm_gear_arm_left | 1 | _(PLA/PETG)_ | |
| robotic_arm_gear_arm_right | 1 | | |
| robotic_arm_servo_gear | 1 | | |
| robotic_arm_palm | 1 | | |
| robotic_arm_palm_top | 1 | | |
| robotic_arm_finger | 2 | | |
| robotic_arm_finger_pad | 2 | Filamento flexible | Mejor agarre |
| robotic_arm_forward_hinge_arm | 2 | | |

### 5.4. Tornillería

- (4) tornillos 2-56 x 1/2"
- (2) tornillos 4-40 x 3/8" cabeza botón
- (2) tornillos 4-40 x 1" cabeza plana
- Tornillos de montaje del servo

### 5.5. Adaptación a la brida del IRB 140

_(Por completar: descripción del acople diseñado entre el gripper y la brida del robot.
Incluir planos/fotos.)_

### 5.6. Calibración de aperturas

Ángulos del servo para cada objeto (valores a confirmar experimentalmente):

| Comando | Ángulo (°) | Aplicación |
|---------|:----------:|------------|
| Apertura total | _(por calibrar, ~10)_ | Reposo / aproximación |
| Cierre estrecho | _(por calibrar, ~75)_ | Sujeción de la PCB |
| Cierre amplio | _(por calibrar, ~45)_ | Sujeción de la caja |

---

## 6. Diseño Electrónico y de Potencia

> Documento técnico detallado disponible en:
> `docs/Gripper_SG90_ABB_IRB140_Abel.pdf`

### 6.1. Problema de compatibilidad

El controlador IRC5 entrega salidas digitales de 24 V DC (ON/OFF), mientras que el
servomotor SG90 requiere una señal PWM de 50 Hz a nivel lógico de 5 V. Se requiere una
etapa intermedia de conversión de tensión, aislamiento galvánico y generación de PWM.

### 6.2. Arquitectura de la solución

```
ZONA 24 V (IRC5)  ──►  AISLAMIENTO (PC817)  ──►  ZONA 5 V (Arduino)  ──►  Servo SG90
                       Potencia: LM2596 (24 V → 5 V)
```

### 6.3. Lista de materiales (resumen)

| Componente | Referencia | Cant. |
|------------|------------|:-----:|
| Servomotor | TowerPro SG90 | 1 |
| Microcontrolador | Arduino Nano (ATmega328P) | 1 |
| Convertidor DC-DC | LM2596S step-down ajustable | 1 |
| Optoacoplador | PC817 (o módulo de 4 canales) | 2 |
| Resistencia limitadora | 2.2 kΩ 1/2 W | 2 |
| Resistencia pull-down | 10 kΩ 1/4 W | 2 |
| Condensador electrolítico | 1000 µF / 16 V | 1 |
| Condensador cerámico | 100 nF | 1 |

_(BOM completo con cableado y conectores en el PDF técnico.)_

### 6.4. Mapa de pines del Arduino

| Pin | Modo | Conexión |
|-----|------|----------|
| D2 | INPUT | DO_gripA (vía PC817 #1) |
| D3 | INPUT | DO_gripB (vía PC817 #2) |
| D9 | OUTPUT (PWM) | Señal del servo SG90 |
| D13 | OUTPUT | LED de diagnóstico |
| VIN | Alimentación | +5 V (salida del LM2596) |
| GND | Referencia | GND común |

### 6.5. Protocolo de comandos (2 bits)

| DO_gripA | DO_gripB | Comando |
|:--------:|:--------:|---------|
| 0 | 0 | Apertura total |
| 1 | 0 | Cierre sobre PCB |
| 0 | 1 | Cierre sobre caja |
| 1 | 1 | Intermedio (reservado) |

### 6.6. Punto de conexión al robot

_(Por definir tras la verificación física:)_

- [ ] Verificar pines libres en el conector de la brida del IRB 140.
- [ ] Confirmar si las líneas de usuario ya están asignadas a salidas del IRC5.
- [ ] Confirmar si llegan 24 V y 0 V hasta la brida o solo señales.
- [ ] Decidir: conexión en brida vs. armario vs. fuente externa para el Arduino.

---

## 7. Firmware del Controlador de la Herramienta

Código fuente en: `firmware/gripper_control/gripper_control.ino`

### 7.1. Descripción

Firmware para Arduino Nano que lee las dos señales digitales del IRC5 (a través de los
optoacopladores) y comanda el servomotor SG90 a la apertura correspondiente. Estructura
no bloqueante basada en `millis()`, con movimiento suave por pasos, antirrebote y
liberación del servo en reposo.

### 7.2. Características principales

- Decodificación de la palabra de comando de 2 bits.
- Movimiento incremental (2° por paso) para un cierre controlado.
- Filtro antirrebote de 30 ms sobre las entradas.
- Liberación del servo (`detach`) en posición abierta para evitar zumbido y calentamiento.
- Salida de depuración por puerto serie a 9600 baudios.

### 7.3. Parámetros configurables

| Constante | Descripción | Valor inicial |
|-----------|-------------|:-------------:|
| ANG_ABIERTO | Ángulo de apertura total | 10 |
| ANG_CERRADO_PCB | Ángulo de cierre sobre PCB | 75 |
| ANG_CERRADO_CAJA | Ángulo de cierre sobre caja | 45 |
| PASO_GRADOS | Grados por paso | 2 |
| T_DEBOUNCE | Tiempo de antirrebote (ms) | 30 |

_(El código completo y comentado está en el archivo .ino y en el PDF técnico.)_

---

## 8. Programación del Robot (RAPID)

Código fuente en: `rapid/`

### 8.1. Estructura del programa

| Módulo / rutina | Función | Estado |
|-----------------|---------|--------|
| `main` | Bucle principal de la estación | Pendiente |
| `rInicializar` | Home y verificación de estado seguro | Pendiente |
| `rTomarPCB` | Pick de la PCB desde la zona de entrega | Pendiente |
| `rEmpacar` | Depósito de la PCB en la caja | Pendiente |
| `rEnviarBanda` | Depósito del paquete en la banda | Pendiente |
| `AbrirGripper` / `CerrarSobrePCB` / `CerrarSobreCaja` | Control de la herramienta vía DO | Definido |

### 8.2. Puntos y objetivos (targets)

_(Por completar: tabla de robtargets con las posiciones enseñadas &mdash; home, approach,
pick, place, etc.)_

### 8.3. Señales de E/S configuradas

| Señal | Tipo | Uso |
|-------|------|-----|
| do_gripA | DO | Bit A del comando del gripper |
| do_gripB | DO | Bit B del comando del gripper |
| _(por definir)_ | DI | Confirmación de PCB en zona de entrega |
| _(por definir)_ | DO | Contador / estado de estación |

### 8.4. Control de la herramienta desde RAPID

```rapid
PROC AbrirGripper()
    SetDO do_gripA, 0;
    SetDO do_gripB, 0;          ! 00 -> apertura total
    WaitTime 0.5;
ENDPROC

PROC CerrarSobrePCB()
    SetDO do_gripA, 1;
    SetDO do_gripB, 0;          ! 10 -> cierre estrecho
    WaitTime 0.5;
ENDPROC

PROC CerrarSobreCaja()
    SetDO do_gripA, 0;
    SetDO do_gripB, 1;          ! 01 -> cierre amplio
    WaitTime 0.5;
ENDPROC
```

---

## 9. Interfaz de Operación (HMI)

_(Por completar según el alcance definido. Si aplica solo la estación:)_

- Estados de la estación: IDLE, READY, RUN, FAULT, DONE.
- Contador de PCBs empacadas.
- Botones: Start, Stop, Reset, Home.
- Alarmas: PCB no presente, fallo de sujeción, material de empaque agotado.

Herramienta: ScreenMaker (FlexPendant) en RobotStudio, u opción equivalente.

---

## 10. Plano de Planta y Layout

_(Por completar: plano con la ubicación del robot, zona de entrega, zona de empaque y
banda de salida, con cotas. Incluir imagen en `docs/`.)_

```
[ Insertar plano de planta aquí ]
```

---

## 11. Diagrama de Flujo del Proceso

_(Por completar: diagrama de flujo de las acciones del robot, con estados y ramas de falla.
Incluir imagen en `docs/`.)_

```
[ Insertar diagrama de flujo aquí ]

  INICIO
    │
    ▼
  Home / estado seguro
    │
    ▼
  ¿PCB en zona de entrega? ──No──► Esperar / alarma
    │ Sí
    ▼
  Tomar PCB (cierre estrecho)
    │
    ▼
  Depositar en caja
    │
    ▼
  Tomar/empujar caja a banda
    │
    ▼
  Incrementar contador
    │
    ▼
  FIN de ciclo
```

---

## 12. Manejo de Fallas

Fallas de manejo obligatorio según el enunciado, adaptadas a la Etapa 4:

| Falla | Detección | Acción |
|-------|-----------|--------|
| PCB no presente en zona de entrega | _(por definir)_ | Esperar / reintentar / alarma |
| Fallo de sujeción de la PCB | _(por definir)_ | Reintento o marcar como reproceso |
| Material de empaque agotado | _(por definir)_ | Alarma y solicitud de reposición |
| Parada de emergencia | Señal del sistema | Detener, reset y home seguro |

---

## 13. Pruebas y Resultados

_(Por completar: registro de las pruebas realizadas.)_

| Prueba | Objetivo | Resultado | Observaciones |
|--------|----------|-----------|---------------|
| Calibración de aperturas del gripper | Determinar ángulos definitivos | | |
| Verificación de señales IRC5 → Arduino | Confirmar lógica de comandos | | |
| Ciclo completo en simulación | Validar la secuencia | | |
| Ciclo completo en robot real | Validar sobre hardware | | |
| Repetibilidad | Consistencia del pick & place | | |

---

## 14. Comparación Manual vs. Automatizado

_(Por completar: tabla comparativa según el entregable requerido.)_

| Métrica | Proceso manual | Proceso automatizado |
|---------|:--------------:|:--------------------:|
| Tiempo por PCB | | |
| Tasa de fallos | | |
| Repetibilidad | | |
| Consistencia del resultado | | |

---

## 15. Evidencias (Videos y Fotos)

Todos los videos deben comenzar con la introducción oficial del laboratorio LabSIR.

| Evidencia | Enlace / ruta | Estado |
|-----------|---------------|--------|
| Video de la simulación | _(por completar)_ | Pendiente |
| Video de la implementación real | _(por completar)_ | Pendiente |
| Fotos del montaje del gripper | `docs/fotos/` | Pendiente |
| Fotos del circuito electrónico | `docs/fotos/` | Pendiente |

Introducción oficial LabSIR:
https://drive.google.com/file/d/1wSxw7m7n5hXOtkc8C0H0lLAxTx3BqQSe/view?usp=sharing

---

## 16. Estructura del Repositorio

```
proyecto-abel-etapa4/
├── README.md                          # Este documento
├── docs/
│   ├── Gripper_SG90_ABB_IRB140_Abel.pdf   # Documento técnico del gripper
│   ├── plano_planta.pdf
│   ├── diagrama_flujo.pdf
│   └── fotos/
├── rapid/
│   ├── main.mod                       # Programa principal
│   └── herramienta.mod                # Rutinas de control del gripper
├── firmware/
│   └── gripper_control/
│       └── gripper_control.ino        # Firmware del Arduino Nano
├── cad/
│   ├── gripper/                       # STL del gripper
│   └── acople_brida/                  # Acople a la brida del IRB 140
├── simulacion/
│   └── station.rspag                  # Estación de RobotStudio (pack & go)
└── evidencias/
    └── (enlaces a videos)
```

_(Nota: no subir las carpetas build, install o log si las hubiera.)_

---

## 17. Instrucciones de Puesta en Marcha

### 17.1. Montaje electrónico

Seguir el procedimiento detallado en `docs/Gripper_SG90_ABB_IRB140_Abel.pdf`, sección 9.
Resumen del orden obligatorio:

1. Ajustar el LM2596 a 5.0 V con multímetro, sin carga.
2. Cargar el firmware en el Arduino Nano.
3. Probar la etapa de señales sin servo (verificar lógica en el monitor serie).
4. Probar el servo sin carga.
5. Calibrar los ángulos con el gripper montado.
6. Probar con carga real (PCB y caja).

### 17.2. Simulación en RobotStudio

_(Por completar: pasos para abrir la estación y ejecutar la simulación.)_

### 17.3. Ejecución en el robot real

_(Por completar: pasos y precauciones. Primeras pruebas en modo manual a velocidad
reducida.)_

---

## 18. Seguridad

- Protección electrostática (ESD): pulsera antiestática y superficie disipativa al
  manipular la PCB y el Arduino.
- Verificar polaridad de las líneas de 24 V y 5 V antes de conectar dispositivos.
- Alojar el circuito de acondicionamiento en una caja cerrada para evitar cortos.
- Primeras pruebas del robot en modo manual, velocidad reducida y área despejada.
- Previsión ante parada de emergencia: el servo pierde fuerza y la pieza puede caer;
  evitar que el punto de caída coincida con equipos o personas.

---

## 19. Bitácora del Desarrollo

Registro cronológico de decisiones, cambios y avances.

| Fecha | Actividad | Decisión / resultado | Responsable |
|-------|-----------|----------------------|-------------|
| _(por completar)_ | | | |
| | | | |
| | | | |

---

## 20. Conclusiones

_(Conclusiones individuales de cada integrante, según el entregable requerido.)_

**Integrante 1:** _(por completar)_

**Integrante 2:** _(por completar)_

**Integrante 3:** _(por completar)_

---

## 21. Referencias

1. Guía del Proyecto Final &mdash; Robótica Industrial 2026-I. Automatización del Proceso
   de Ensamblaje, Soldadura y Empaque de PCBs. Universidad Nacional de Colombia.
2. sthone. _Parallel Gripper for EEZYbotARM MK2_. Printables, 2022. Licencia CC BY-NC 4.0.
   https://www.printables.com/model/275802-parallel-gripper-for-eezybotarm-mk2/files
3. ABB Robotics. _Product Manual IRC5_ y _Product Manual IRB 140_.
4. ABB Robotics. _Technical Reference Manual &mdash; RAPID Instructions, Functions and Data Types_.
5. TowerPro. _SG90 Micro Servo Datasheet_.
6. Sharp. _PC817 Series Photocoupler Datasheet_.
7. Texas Instruments. _LM2596 Step-Down Voltage Regulator Datasheet_.

---

_Última actualización: (por completar) &mdash; Versión preliminar del README._

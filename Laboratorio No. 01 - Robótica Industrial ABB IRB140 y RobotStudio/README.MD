## Descripción detallada de la solución planteada

El presente laboratorio tiene como objetivo desarrollar una aplicación de robótica industrial orientada a la simulación del proceso de decoración de una torta virtual, empleando un manipulador industrial ABB IRB 140 y el entorno de programación RobotStudio. La solución propuesta consiste en generar una rutina de movimiento capaz de representar, sobre una superficie plana, los nombres de los integrantes del grupo y una decoración adicional mediante trayectorias continuas ejecutadas por el robot.

La actividad se plantea como una adaptación del proceso de decoración de tortas en la industria alimentaria, donde un robot puede realizar movimientos controlados para depositar material decorativo sobre una superficie. Debido a las condiciones del laboratorio, el proceso se desarrolla de forma virtual y experimental, utilizando una herramienta diseñada para sujetar un marcador o plumón en el flange del robot. Esta herramienta permite simular el trazado de letras y figuras sobre la superficie definida como torta virtual.

La solución se divide en cinco componentes principales:

1. **Definición de trayectorias del robot:**  
   Se programan trayectorias en RAPID utilizando instrucciones de movimiento como `MoveJ`, `MoveL` y, cuando sea necesario, `MoveC`. Estas trayectorias permiten desplazar la herramienta desde una posición inicial de seguridad o `HOME` hasta la zona de trabajo, ejecutar el decorado y regresar nuevamente a la posición inicial. Los movimientos se realizan considerando velocidades dentro del rango establecido para el laboratorio y zonas de aproximación adecuadas para conservar continuidad y precisión durante el trazado.

2. **Diseño y calibración de la herramienta:**  
   Se diseña una herramienta mecánica que permite fijar un marcador al flange del robot ABB IRB 140. Posteriormente, se realiza la calibración del TCP para definir correctamente el punto de trabajo de la herramienta. Este procedimiento se lleva a cabo tanto en RobotStudio como en el robot real, con el fin de comparar los valores obtenidos del `tooldata` y analizar posibles diferencias entre la simulación y la implementación física.

3. **Uso de workobjects:**  
   Se define un sistema de referencia de trabajo o `workobject` asociado a la superficie donde se realizará la decoración. Inicialmente, las trayectorias se desarrollan sobre un cuadrante de trabajo y posteriormente se reutilizan en una nueva ubicación mediante la creación de otro `workobject`. Esto permite adaptar la misma secuencia de movimientos a una posición diferente del pastel, manteniendo la lógica de programación y evitando redefinir todas las trayectorias desde cero.

4. **Manejo de entradas y salidas digitales:**  
   La rutina del robot incorpora el uso de dos entradas digitales y dos salidas digitales. La primera entrada digital permite iniciar la rutina de decorado y activar una luz indicadora durante la ejecución del proceso. La segunda entrada digital lleva el robot a una posición de mantenimiento, donde sea posible instalar o retirar la herramienta de forma segura, apagando además la luz indicadora. Las salidas digitales también se utilizan para señalizar estados del proceso y controlar el sistema externo asociado a la banda transportadora.

5. **Control de la banda transportadora:**  
   Al finalizar el decorado de la torta virtual, una salida digital del controlador se emplea para activar el movimiento de una banda transportadora mediante el variador de frecuencia correspondiente. Esta etapa representa el transporte automático del pastel una vez completado el proceso de decoración. De esta manera, la solución integra no solo el movimiento del manipulador, sino también la interacción del robot con elementos periféricos del entorno industrial.

En conjunto, la solución propuesta permite simular una celda básica de automatización industrial compuesta por un robot manipulador, una herramienta personalizada, una superficie de trabajo definida mediante `workobjects`, señales digitales de entrada y salida, y una banda transportadora. La programación se desarrolla en RAPID, integrando rutinas de movimiento, rutinas de mantenimiento, control de señales digitales y retorno seguro a la posición `HOME`.

El desarrollo del laboratorio permite aplicar conceptos fundamentales de robótica industrial, tales como programación de trayectorias, calibración de herramientas, definición de marcos de referencia, manejo de entradas y salidas digitales, y coordinación entre el robot y dispositivos externos.

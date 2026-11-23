# analizador-logico
---

## 📌 Proyecto 2: Análisis de Comunicación Serial UART con Analizador Lógico

Este proyecto consiste en la captura, decodificación y análisis temporal de señales digitales del protocolo serial **UART** generadas por una **Raspberry Pi Pico 2W** y capturadas mediante un analizador lógico con el software **Logic 2**[cite: 3].

### 📝 Descripción
El objetivo principal es estudiar experimentalmente la relación entre la tasa de transmisión (*baudrate*), el tiempo de bit ($T_b$) y la frecuencia de muestreo ($f_s$) del instrumento[cite: 3, 4, 5]. Se evaluó la transmisión de caracteres individuales y de la trama `UMNG_2026_LIDER_EN_TELECOMUNICACIONES`[cite: 3, 6], analizando su decodificación en múltiples formatos y determinando el umbral mínimo de muestreo requerido (criterio práctico de $\ge 10$ muestras por bit)[cite: 3] para cuatro velocidades de transmisión: **1200, 9600, 57600 y 115200 baudios**[cite: 3, 7].

### 🛠️ Tecnologías y Hardware
* **Microcontrolador:** Raspberry Pi Pico 2W (transmisión UART0 de nivel lógico 3.3 V a través del pin `GPIO 0 / TX`)[cite: 4, 6].
* **Lenguaje:** MicroPython (desarrollado en Thonny utilizando los módulos `machine.UART` y `utime`)[cite: 6, 8].
* **Instrumentación y Software:** Analizador lógico de 8 canales (hasta 24 MS/s) y software **Saleae Logic 2** (analizador de protocolo *Async Serial*)[cite: 3, 4, 6].

### 🚀 Metodología y Pruebas Realizadas
1. **Decodificación Multi-formato:** Configuración inicial a 9600 baudios (8N1) para capturar la trama y verificar la correspondencia simultánea de los datos en formato **ASCII, Binario, Decimal y Hexadecimal**[cite: 3, 6, 10].
2. **Medición de Duración de Trama:** Uso de *Timing Markers* en Logic 2 para medir el tiempo de bit experimental frente al teórico ($104,17\ \mu\text{s}$ a 9600 baudios) y la duración total del mensaje de prueba ($42,4\ \text{ms}$)[cite: 7, 8].
3. **Análisis de Sensibilidad de Muestreo:** Barrido de frecuencias de muestreo desde **25 kS/s hasta 24 MS/s**[cite: 3, 6] bajo configuración con paridad impar[cite: 6] para evaluar el error por cuantización temporal[cite: 3, 5] y el cumplimiento del criterio de $\ge 10$ muestras/bit[cite: 3].

### 📊 Conclusiones Principales
* **Umbrales mínimos de muestreo observados:** Para cumplir con $\ge 10$ muestras/bit se requirió al menos **25 kS/s** para 1200 baudios, **100 kS/s** para 9600 baudios, **1 MS/s** para 57600 baudios y **2 MS/s** para 115200 baudios[cite: 10, 11].
* **Resolución vs. Almacenamiento:** Incrementar la frecuencia de muestreo reduce la incertidumbre por cuantización temporal ($T_s = 1/f_s$)[cite: 5] acercando la medición al valor teórico[cite: 7, 10], aunque tasas máximas como 24 MS/s generan archivos muy pesados en capturas largas, por lo que debe elegirse un equilibrio según el *baudrate*[cite: 11].

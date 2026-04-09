# ⚡ Monitoreo de Eficiencia Energética con Ruido Gaussiano

Este proyecto simula el comportamiento de sensores en una planta fotovoltaica bajo condiciones de **ruido térmico gaussiano**. Aplica conceptos de la Serie Schaum y procesamiento de señales para mejorar la precisión de las lecturas mediante filtrado estadístico.

## 📊 Problema de Ingeniería
En sistemas reales, los sensores de potencia (Watts) introducen ruido que puede generar falsas alarmas. Este script evalúa:
* **SNR (Signal-to-Noise Ratio):** Relación señal-ruido en decibelios.
* **Teorema del Límite Central:** Reducción de la varianza mediante el promedio de $n$ muestras.
* **Intervalos de Confianza:** Rango de operación segura al 95%.

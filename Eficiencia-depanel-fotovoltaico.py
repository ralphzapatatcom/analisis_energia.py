import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DEL SISTEMA ---
potencia_nominal = 200.0   # Watts (Señal pura)
sigma_ruido = 5.0          # Watts (Ruido Gaussiano)
n_muestras = 25            # Aumentamos a 25 para ver mejor el efecto del promedio
nivel_confianza = 0.95

# --- CÁLCULOS ESTADÍSTICOS AVANZADOS ---

# 1. Relación Señal-Ruido (SNR) en decibelios (dB)
# SNR_dB = 10 * log10(Potencia_Señal / Potencia_Ruido)
# En amplitud/voltaje sería con 20*log10, en potencia usamos 10*log10
snr_db = 10 * np.log10(potencia_nominal / sigma_ruido)

# 2. Error Relativo porcentual esperado por el ruido
error_relativo_esperado = (sigma_ruido / potencia_nominal) * 100

# 3. Intervalo de Confianza para una lectura del sensor
# Donde caerán el 95% de las mediciones
lim_inf, lim_sup = stats.norm.interval(nivel_confianza, loc=potencia_nominal, scale=sigma_ruido)

# 4. Error Estándar del Promedio (Filtrado)
sem = sigma_ruido / np.sqrt(n_muestras)

# --- IMPRESIÓN DE VARIABLES ---
print("="*40)
print("SISTEMA DE MONITOREO ENERGÉTICO")
print("="*40)
print(f"Potencia Real (Señal):      {potencia_nominal:>8} W")
print(f"Desviación del Ruido:      {sigma_ruido:>8} W")
print(f"SNR (Relación Señal/Ruido): {snr_db:>8.2f} dB")
print(f"Error Relativo Típico:     {error_relativo_esperado:>8.2f} %")
print("-" * 40)
print(f"Intervalo de confianza ({int(nivel_confianza*100)}%):")
print(f"Las lecturas oscilarán entre {lim_inf:.2f} W y {lim_sup:.2f} W")
print("-" * 40)
print(f"EFECTO DEL FILTRADO (n={n_muestras}):")
print(f"Nuevo Error Estándar:      {sem:>8.2f} W")
print(f"Reducción de incertidumbre: {((1 - sem/sigma_ruido)*100):>7.2f} %")
print("="*40)

# --- VISUALIZACIÓN ---
x = np.linspace(potencia_nominal - 20, potencia_nominal + 20, 500)
pdf_original = stats.norm.pdf(x, potencia_nominal, sigma_ruido)
pdf_filtrada = stats.norm.pdf(x, potencia_nominal, sem)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf_original, label=f'Lectura Única (σ={sigma_ruido})', color='red', linestyle='--')
plt.plot(x, pdf_filtrada, label=f'Promedio de {n_muestras} muestras (σ={sem:.2f})', color='green', linewidth=2)
plt.fill_between(x, pdf_filtrada, alpha=0.2, color='green')
plt.title('Impacto del Ruido Gaussiano en la Medición de Energía')
plt.xlabel('Potencia Registrada (Watts)')
plt.ylabel('Probabilidad')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
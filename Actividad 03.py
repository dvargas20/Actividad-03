# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:39:40 2024

@author: Diana
"""

import tkinter as tk
from tkinter import ttk

# Función para realizar los cálculos
def calcular():
    try:
        # Recoger datos de entrada
        altura_vuelo = float(entrada_altura_vuelo.get())
        focal_camara = float(entrada_focal_camara.get())
        rsi = float(entrada_rsi.get())
        ancho_sensor = float(entrada_ancho_sensor.get())
        alto_sensor = float(entrada_alto_sensor.get())
        solape_longitudinal = float(entrada_solape_longitudinal.get())
        solape_transversal = float(entrada_solape_transversal.get())
        velocidad_vuelo = float(entrada_velocidad_vuelo.get())
        intervalo_fotos = float(entrada_intervalo_fotos.get())
        ancho_parcela = float(entrada_ancho_parcela.get())
        largo_parcela = float(entrada_largo_parcela.get())
        
        # Cálculos
        gsd = (altura_vuelo * 100 / focal_camara) * rsi
        escala_vuelo = 1 / ((focal_camara / 1000) / altura_vuelo)
        ancho_imagen_terreno = (ancho_sensor * escala_vuelo) / 1000
        alto_imagen_terreno = (alto_sensor * escala_vuelo) / 1000
        base_aerea = ancho_imagen_terreno * (1 - (solape_longitudinal / 100))
        distancia_entre_pasadas = alto_imagen_terreno * (1 - (solape_transversal / 100))
        intervalo_entre_fotos = base_aerea / velocidad_vuelo
        velocidad_de_vuelo = base_aerea / intervalo_fotos
        numero_pasadas = ancho_parcela / distancia_entre_pasadas
        numero_fotos_por_pasada = (largo_parcela / base_aerea) + 1
        numero_fotos_por_vuelo = numero_fotos_por_pasada * numero_pasadas
        distancia_vuelo = (numero_pasadas * largo_parcela) + ancho_parcela
        duracion_vuelo = (numero_fotos_por_vuelo * intervalo_entre_fotos) / 60

        # Mostrar resultados
        resultado_gsd.config(text=f"{gsd:.2f} cm/pixel")
        resultado_escala_vuelo.config(text=f"1:{escala_vuelo:.2f}")
        resultado_ancho_imagen_terreno.config(text=f"{ancho_imagen_terreno:.2f} m")
        resultado_alto_imagen_terreno.config(text=f"{alto_imagen_terreno:.2f} m")
        resultado_base_aerea.config(text=f"{base_aerea:.2f} m")
        resultado_distancia_entre_pasadas.config(text=f"{distancia_entre_pasadas:.2f} m")
        resultado_intervalo_entre_fotos.config(text=f"{intervalo_entre_fotos:.2f} s")
        resultado_velocidad_de_vuelo.config(text=f"{velocidad_de_vuelo:.2f} m/s")
        resultado_numero_pasadas.config(text=f"{numero_pasadas:.2f}")
        resultado_numero_fotos_por_pasada.config(text=f"{numero_fotos_por_pasada:.2f}")
        resultado_numero_fotos_por_vuelo.config(text=f"{numero_fotos_por_vuelo:.2f}")
        resultado_distancia_vuelo.config(text=f"{distancia_vuelo:.2f} m")
        resultado_duracion_vuelo.config(text=f"{duracion_vuelo:.2f} min")
    except ValueError:
        resultado_gsd.config(text="Por favor, ingrese valores numéricos válidos en todos los campos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Planificación de Vuelo de Dron")
ventana.geometry("700x900")


# Crear entradas para los datos
ttk.Label(ventana, text="Altura de vuelo (m)").grid(row=0, column=0)
entrada_altura_vuelo = ttk.Entry(ventana)
entrada_altura_vuelo.grid(row=0, column=1)

ttk.Label(ventana, text="Focal de la cámara (mm)").grid(row=1, column=0)
entrada_focal_camara = ttk.Entry(ventana)
entrada_focal_camara.grid(row=1, column=1)

ttk.Label(ventana, text="RSI").grid(row=2, column=0)
entrada_rsi = ttk.Entry(ventana)
entrada_rsi.grid(row=2, column=1)

ttk.Label(ventana, text="Ancho del sensor (mm)").grid(row=3, column=0)
entrada_ancho_sensor = ttk.Entry(ventana)
entrada_ancho_sensor.grid(row=3, column=1)

ttk.Label(ventana, text="Alto del sensor (mm)").grid(row=4, column=0)
entrada_alto_sensor = ttk.Entry(ventana)
entrada_alto_sensor.grid(row=4, column=1)

ttk.Label(ventana, text="Solape longitudinal (%)").grid(row=5, column=0)
entrada_solape_longitudinal = ttk.Entry(ventana)
entrada_solape_longitudinal.grid(row=5, column=1)

ttk.Label(ventana, text="Solape transversal (%)").grid(row=6, column=0)
entrada_solape_transversal = ttk.Entry(ventana)
entrada_solape_transversal.grid(row=6, column=1)

ttk.Label(ventana, text="Velocidad de vuelo (m/s)").grid(row=7, column=0)
entrada_velocidad_vuelo = ttk.Entry(ventana)
entrada_velocidad_vuelo.grid(row=7, column=1)

ttk.Label(ventana, text="Intervalo entre fotos (s)").grid(row=8, column=0)
entrada_intervalo_fotos = ttk.Entry(ventana)
entrada_intervalo_fotos.grid(row=8, column=1)

ttk.Label(ventana, text="Ancho de la parcela (m)").grid(row=9, column=0)
entrada_ancho_parcela = ttk.Entry(ventana)
entrada_ancho_parcela.grid(row=9, column=1)

ttk.Label(ventana, text="Largo de la parcela (m)").grid(row=10, column=0)
entrada_largo_parcela = ttk.Entry(ventana)
entrada_largo_parcela.grid(row=10, column=1)

# Crear botón para realizar los cálculos
ttk.Button(ventana, text="Calcular", command=calcular).grid(row=11, column=0, columnspan=2)

# Crear etiquetas para mostrar resultados
ttk.Label(ventana, text="GSD (cm/pixel)").grid(row=12, column=0)
resultado_gsd = ttk.Label(ventana, text="")
resultado_gsd.grid(row=12, column=1)

ttk.Label(ventana, text="Escala de Vuelo").grid(row=13, column=0)
resultado_escala_vuelo = ttk.Label(ventana, text="")
resultado_escala_vuelo.grid(row=13, column=1)

ttk.Label(ventana, text="Ancho de Imagen sobre terreno (m)").grid(row=14, column=0)
resultado_ancho_imagen_terreno = ttk.Label(ventana, text="")
resultado_ancho_imagen_terreno.grid(row=14, column=1)

ttk.Label(ventana, text="Alto de Imagen sobre terreno (m)").grid(row=15, column=0)
resultado_alto_imagen_terreno = ttk.Label(ventana, text="")
resultado_alto_imagen_terreno.grid(row=15, column=1)

ttk.Label(ventana, text="Base Aérea (m)").grid(row=16, column=0)
resultado_base_aerea = ttk.Label(ventana, text="")
resultado_base_aerea.grid(row=16, column=1)

ttk.Label(ventana, text="Distancia entre Pasadas (m)").grid(row=17, column=0)
resultado_distancia_entre_pasadas = ttk.Label(ventana, text="")
resultado_distancia_entre_pasadas.grid(row=17, column=1)

ttk.Label(ventana, text="Tiempo entre fotos (s)").grid(row=18, column=0)
resultado_intervalo_entre_fotos = ttk.Label(ventana, text="")
resultado_intervalo_entre_fotos.grid(row=18, column=1)

ttk.Label(ventana, text="Velocidad de Vuelo (m/s)").grid(row=19, column=0)
resultado_velocidad_de_vuelo = ttk.Label(ventana, text="")
resultado_velocidad_de_vuelo.grid(row=19, column=1)

ttk.Label(ventana, text="No de pasadas").grid(row=20, column=0)
resultado_numero_pasadas = ttk.Label(ventana, text="")
resultado_numero_pasadas.grid(row=20, column=1)

ttk.Label(ventana, text="No de Fotos por pasada").grid(row=21, column=0)
resultado_numero_fotos_por_pasada = ttk.Label(ventana, text="")
resultado_numero_fotos_por_pasada.grid(row=21, column=1)

ttk.Label(ventana, text="No Fotos por Vuelo").grid(row=22, column=0)
resultado_numero_fotos_por_vuelo = ttk.Label(ventana, text="")
resultado_numero_fotos_por_vuelo.grid(row=22, column=1)

ttk.Label(

ventana, text="Distancia de Vuelo (m)").grid(row=23, column=0)
resultado_distancia_vuelo = ttk.Label(ventana, text="")
resultado_distancia_vuelo.grid(row=23, column=1)

ttk.Label(ventana, text="Duración de vuelo (min)").grid(row=24, column=0)
resultado_duracion_vuelo = ttk.Label(ventana, text="")
resultado_duracion_vuelo.grid(row=24, column=1)

# Ejecutar aplicación
ventana.mainloop()

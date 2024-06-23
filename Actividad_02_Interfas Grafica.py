# -*- coding: utf-8 -*-
"""
Created Wed Jun 19 23:33:19 2024

@author: Lesby
"""

# Crear una instancia en tinker
import tkinter as tk
from tkinter import ttk, messagebox

# Se crean las variables para realizar las conversiones
class Coordenadas:
    
    def dd_a_dms(dd):
        grados = int(dd)
        minutos_completos = abs((dd - grados) * 60)
        minutos = int(minutos_completos)
        segundos = (minutos_completos - minutos) * 60
        return grados, minutos, segundos


    def dms_a_dd(grados, minutos, segundos):
        dd = abs(grados) + minutos / 60 + segundos / 3600
        return dd if grados >= 0 else -dd
    
# conversion de los grados deciamales a grados, minutos y segundos
def convertir_dd_a_dms():
    try:
        lat_dd = float(entry_lat_dd.get())
        lon_dd = float(entry_lon_dd.get())

        lat_grados, lat_minutos, lat_segundos = Coordenadas.dd_a_dms(lat_dd)
        lon_grados, lon_minutos, lon_segundos = Coordenadas.dd_a_dms(lon_dd)

        lat_hemisferio = 'N' if lat_dd >= 0 else 'S'
        lon_hemisferio = 'E' if lon_dd >= 0 else 'O'

        label_resultado_dd_a_dms.config(text=f"Latitud: {abs(lat_grados)}° {lat_minutos}' {lat_segundos:.4f}'' {lat_hemisferio}\n"
                                             f"Longitud: {abs(lon_grados)}° {lon_minutos}' {lon_segundos:.4f}'' {lon_hemisferio}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para las coordenadas en DD.")

# conversion de los grados, minutos y segundos a grados decimales 
def convertir_dms_a_dd():
    try:
        lat_grados = int(entry_lat_grados.get())
        lat_minutos = int(entry_lat_minutos.get())
        lat_segundos = float(entry_lat_segundos.get())
        lon_grados = int(entry_lon_grados.get())
        lon_minutos = int(entry_lon_minutos.get())
        lon_segundos = float(entry_lon_segundos.get())

        lat_dd = Coordenadas.dms_a_dd(lat_grados, lat_minutos, lat_segundos)
        lon_dd = Coordenadas.dms_a_dd(lon_grados, lon_minutos, lon_segundos)

        label_resultado_dms_a_dd.config(text=f"Latitud DD: {lat_dd}\nLongitud DD: {lon_dd}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para las coordenadas en DMS.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Coordenadas")
ventana.geometry("500x400")


# añadir color al fondo
# root.config(bg='black')
ventana ['bg'] = 'sky blue'

# agregar etiqueta
etiqueta = tk.Label(ventana, text='Conversión de Coordenadas', bg='white', fg='black')
etiqueta.pack(expand= 23)

ventana = ttk.Notebook(ventana)

# Pestaña DD a DMS
tab_dd_a_dms = ttk.Frame(ventana)
ventana.add(tab_dd_a_dms, text="DD a DMS")

# Título para Grados Decimales
ttk.Label(tab_dd_a_dms, text="Grados Decimales", font=("arial", 16)).grid(row=0, columnspan=2, pady=10)

ttk.Label(tab_dd_a_dms, text="Latitud DD:").grid(row=1, column=0, padx=5, pady=5)
entry_lat_dd = ttk.Entry(tab_dd_a_dms)
entry_lat_dd.grid(row=1, column=1, padx=6, pady=6)

ttk.Label(tab_dd_a_dms, text="Longitud DD:").grid(row=2, column=0, padx=5, pady=5)
entry_lon_dd = ttk.Entry(tab_dd_a_dms)
entry_lon_dd.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(tab_dd_a_dms, text="Convertir", command=convertir_dd_a_dms).grid(row=3, columnspan=2, pady=10)

label_resultado_dd_a_dms = ttk.Label(tab_dd_a_dms)
label_resultado_dd_a_dms.grid(row=4, columnspan=2)

# Pestaña DMS a DD
tab_dms_a_dd = ttk.Frame(ventana)
ventana.add(tab_dms_a_dd, text="DMS a DD")

# Título para Grados, Minutos y Segundos
ttk.Label(tab_dms_a_dd, text="Grados, Minutos y Segundos", font=("arial", 16)).grid(row=0, columnspan=2, pady=10)

ttk.Label(tab_dms_a_dd, text="Grados Lat:").grid(row=1, column=0, padx=5, pady=5)
entry_lat_grados = ttk.Entry(tab_dms_a_dd)
entry_lat_grados.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(tab_dms_a_dd, text="Minutos Lat:").grid(row=2, column=0, padx=5, pady=5)
entry_lat_minutos = ttk.Entry(tab_dms_a_dd)
entry_lat_minutos.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(tab_dms_a_dd, text="Segundos Lat:").grid(row=3, column=0, padx=5, pady=5)
entry_lat_segundos = ttk.Entry(tab_dms_a_dd)
entry_lat_segundos.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(tab_dms_a_dd, text="Grados Lon:").grid(row=4, column=0, padx=5, pady=5)
entry_lon_grados = ttk.Entry(tab_dms_a_dd)
entry_lon_grados.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(tab_dms_a_dd, text="Minutos Lon:").grid(row=5, column=0, padx=5, pady=5)
entry_lon_minutos = ttk.Entry(tab_dms_a_dd)
entry_lon_minutos.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(tab_dms_a_dd, text="Segundos Lon:").grid(row=6, column=0, padx=5, pady=5)
entry_lon_segundos = ttk.Entry(tab_dms_a_dd)
entry_lon_segundos.grid(row=6, column=1, padx=5, pady=5)

ttk.Button(tab_dms_a_dd, text="Convertir", command=convertir_dms_a_dd).grid(row=7, columnspan=2, pady=10)

label_resultado_dms_a_dd = ttk.Label(tab_dms_a_dd)
label_resultado_dms_a_dd.grid(row=8, columnspan=2)

ventana.pack(expand=1, fill="both")

ventana.mainloop()

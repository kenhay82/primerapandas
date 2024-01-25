#1. Importar el pquete o paquetes con los que voy a analizar la información.

import pandas as pd


def analizarCanastaBasica():
    #2. Sin importar la fuente (sql, xls, JSON, scv...)
    #Crear una tabla tabulada que se llama DATAFRAME
    #Columnas= Atribrutos...    Filas= Valores...
    tabla =  pd.read_csv('./data/bdcanasta.csv')
    print(tabla)

    #3. Aplico filtros para limpiar o seleccionar datos.
    #print(tabla.head(20)) #primeros N registros
    #print(tabla.tail(20)) #últimos N registros
    #print(tabla.describe) #estadistica descriptiva básica

    
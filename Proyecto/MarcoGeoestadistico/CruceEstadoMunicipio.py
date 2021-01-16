#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

municipios = pd.read_csv('municipios.csv')
estados = pd.read_csv('estados.csv')

lista = []

for i in range(len(estados)):
    for j in range(len(municipios)):
        if estados["Clave"][i] == municipios["Clave_Entidad"][j]:
            lista.append([estados["Clave"][i],estados["Nombre_Mayuscula"][i],
                          municipios["Clave_Municipio"][j],municipios["Nombre"][j].upper(),
                          municipios["Longitud"][j],municipios["Latitud"][j]])


nuevo = pd.DataFrame(lista,columns=["ENTIDAD_RES","NOMBRE_ENTIDAD_RES",
               "MUNICIPIO_RES","NOMBRE_MUNICIPIO_RES","LONG_MUNICIPIO_RES","LATITUD_MUNICIPIO_RES"])

nuevo.reset_index(drop=True,inplace=True)

archivo_estadistico = nuevo.to_csv("marco_referencial.csv")




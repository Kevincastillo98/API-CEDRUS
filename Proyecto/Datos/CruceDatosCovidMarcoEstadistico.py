#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import dask.dataframe as dd
import unicodedata


datos_covid =  dd.read_csv('~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_19.csv',encoding='latin1',error_bad_lines=False,low_memory=False)
datos_marco_geoestadistico = dd.read_csv('~/Documentos/API-CEDRUS/Proyecto/Datos/marco_referencial.csv',low_memory=False)


datos_covid_geopoint = datos_covid.merge(datos_marco_geoestadistico,'left',on=['ENTIDAD_RES','MUNICIPIO_RES'])

datos_covid_geopoint["PAIS_NACIONALIDAD"] = datos_covid_geopoint['PAIS_NACIONALIDAD'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')


#datos = datos_covid_geopoint.to_csv("~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo.csv",index=False,single_file = True)

datos = datos_covid_geopoint.to_csv("~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo",index=False,single_file = False)

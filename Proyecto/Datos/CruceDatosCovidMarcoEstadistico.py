#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

datos_covid =  pd.read_csv('datos_covid_19.csv',encoding='latin1')
datos_marco_geoestadistico = pd.read_csv('marco_referencial.csv')

datos_covid_geopoint = datos_covid.merge(datos_marco_geoestadistico,'left',on=['ENTIDAD_RES','MUNICIPIO_RES'])

#datos_covid_geopoint = datos_covid_geopoint.drop("Unnamed: 0",axis=1)

datos = datos_covid_geopoint.to_csv("datos_covid_geo.csv")

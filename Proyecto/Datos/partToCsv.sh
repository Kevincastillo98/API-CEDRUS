#!/bin/bash


head -1  ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo/00.part > ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo/datos_covid_geo.csv
awk 'FNR > 1' ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo/*.part >> ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo/datos_covid_geo.csv

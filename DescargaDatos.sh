#!/bin/bash

wget http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip

echo "====Descomprimiendo el zip===="
unzip datos_abiertos_covid19.zip 

echo "====Copiando archivo csv a datos_covid_19.csv===="
cat  *.csv > ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_19.csv

echo "====Se elimina zip y csv generado de la descarga===="
rm  *.zip 
rm  *.csv 

echo "====Activacion de entorno virtual===="
source .virtualenvs/Mining/bin/activate


echo "====Se ejecuta el script Cruce Datos entre datos covid y georeferencia===="
python3   ~/Documentos/API-CEDRUS/Proyecto/Datos/CruceDatosCovidMarcoEstadistico.py





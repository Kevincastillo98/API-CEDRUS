#!/bin/bash

wget http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip

unzip datos_abiertos_covid19.zip 

cat  *.csv > ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_19.csv

rm  *.zip 
rm  *.csv 

source ~/Documentos/API-CEDRUS/Cedrus/bin/activate

python3 ~/Documentos/API-CEDRUS/Proyecto/Datos/CruceDatosCovidMarcoEstadistico.py





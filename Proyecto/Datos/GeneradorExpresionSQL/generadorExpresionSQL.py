import pandas as pd
import  os 
import sys

comando = "head -1  ~/Documentos/API-CEDRUS/Proyecto/Datos/datos_covid_geo.csv > ~/Documentos/API-CEDRUS/Proyecto/Datos/GeneradorExpresionSQL/generador.csv"

os.system(comando)

df = pd.read_csv('generador.csv')
lista = list(df.columns)
concatenador = [i + ' VARCHAR(255)' for i in lista]
salida = tuple(concatenador)

definicion_base  = "USE ETL;"
eliminacion_tabla =  "DROP TABLE IF EXISTS datos_covid_geo;"
query = "CREATE TABLE datos_covid_geo " + str(salida) + ";"
cadena = query.replace("'","")

indices = "CREATE INDEX indices_covid ON  datos_covid_geo(NOMBRE_ENTIDAD_RES,NOMBRE_MUNICIPIO_RES);"


carga_archivo_linea1 = ''' LOAD DATA  INFILE '/var/lib/mysql/datos_covid_geo.csv' '''
carga_archivo_linea2 = ' INTO TABLE datos_covid_geo'
carga_archivo_linea3 = ''' FIELDS TERMINATED BY ',' '''
carga_archivo_linea4 =  '''OPTIONALLY ENCLOSED BY '"' '''
carga_archivo_linea5 =  '''LINES TERMINATED BY '\\n' ''' ;
carga_archivo_linea6 =  'IGNORE 1 LINES;'



print(definicion_base,"\n",
      eliminacion_tabla,"\n",
      cadena,"\n",
      indices,"\n",
      carga_archivo_linea1,"\n",
      carga_archivo_linea2,"\n",
      carga_archivo_linea3,"\n",
      carga_archivo_linea4,"\n",
      carga_archivo_linea5,"\n",
      carga_archivo_linea6,"\n")




#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template, request, send_file
from flask import Flask, Response, render_template
from flask_mysqldb import MySQL
from flask_ngrok import run_with_ngrok 
import io
import csv

  
app = Flask(__name__) 
run_with_ngrok(app) 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'kevin'
app.config['MYSQL_PASSWORD'] = 'castilloroa'
app.config['MYSQL_DB'] = 'ETL'

mysql = MySQL(app)

@app.route("/")
def index():
    return("Inicio de la pagina")




@app.route("/<estado>")
def user(estado):
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT *  FROM datos_covid_geo WHERE NOMBRE_ENTIDAD_RES = %s """, (estado,))
    result = cur.fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    column_names = [i[0] for i in cur.description]
    writer.writerow(column_names)
    writer.writerows(result)
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename={}.csv".format(estado)})
	
@app.route("/<estado>/<municipio>")
def busqueda(estado,municipio):
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT * FROM datos_covid_geo WHERE NOMBRE_ENTIDAD_RES = %s AND NOMBRE_MUNICIPIO_RES = %s """, (estado,municipio))
    result = cur.fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    column_names = [i[0] for i in cur.description]
    writer.writerow(column_names)
    writer.writerows(result)
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename={}-{}.csv".format(estado,municipio)})


if __name__ == "__main__":
  app.run()

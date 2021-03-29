#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template, request, send_file,jsonify
from flask import Flask, Response, render_template
from flask_mysqldb import MySQL,MySQLdb
from flask_ngrok import run_with_ngrok
import pandas as pd
import io
import csv


  
app = Flask(__name__) 
run_with_ngrok(app) 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'kevin'
app.config['MYSQL_PASSWORD'] = 'castilloroa'
app.config['MYSQL_DB'] = 'ETL'

mysql = MySQL(app)

@app.route('/')
def main():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM entidad ORDER BY Nombre_Entidad")
    entidades = cur.fetchall()
    return render_template('tabla.html', entidades=entidades)

@app.route("/entidad",methods=["POST","GET"])
def entidad():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id']
        print(category_id)
        result = cur.execute("SELECT * FROM municipio  WHERE Nombre_Entidad = %s ORDER BY Nombre_Municipio ", [category_id] )
        municipio = cur.fetchall()
        OutputArray = []
        for row in municipio:
            outputObj = {
                'id': row['Clave_Municipio'],
                'name': row['Nombre_Municipio']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)



@app.route("/descarga", methods=['POST'])
def user():
    cur = mysql.connection.cursor()
    estado =  request.form.get('entidad_estado')
    print(estado)
    cur.execute("""SELECT *  FROM datos_covid_geo WHERE NOMBRE_ENTIDAD_RES = %s """, [estado])
    result = cur.fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    column_names = [i[0] for i in cur.description]
    writer.writerow(column_names)
    writer.writerows(result)
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename={}.csv".format(estado)})


@app.route("/municipio", methods=['POST'])
def busqueda():
    cur = mysql.connection.cursor() 
    estado =  request.form.get('entidad')
    municipio = request.form.get('municipio')
    print(estado,"-",municipio)	
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

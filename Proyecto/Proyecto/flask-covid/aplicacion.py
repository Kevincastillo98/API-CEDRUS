#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from flask import Flask, request, render_template, session, redirect



app = Flask(__name__)


@app.route('/',methods=("GET","POST"))
def index():
    
    df = pd.read_csv("/home/kevin/Documentos/API-CEDRUS/Proyecto/Datos/muestra_web.csv",index_col=0)
    return render_template('simple.html',tables=[df.to_html(classes='data')],titles=df.columns.values)


if __name__ == "__main__":
    app.run(debug=True)

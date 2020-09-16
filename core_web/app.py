#!/usr/bin/env python3
# requirements: flask, gau
# -*- coding: utf-8 -*-
# ReconBBSTWeb-beta 0.001
# ReconBBST By HafdlyMalkov 
# This is a proof of concept DO NOT EXPOSE ON THE INTERNET
# Tools for enumeration url system that I am making for personal use.
#
from flask import Flask, make_response, render_template, request, jsonify
#from flask_cors import CORS
from elasticsearch import Elasticsearch
from tld import get_tld, get_fld
import json, os, string
app = Flask(__name__)
#CORS(app)

@app.route("/", methods=['GET'])
def rupatch():
    return render_template("infoscope.html")

@app.route("/api_v1", methods=['GET','POST'])
def api_v1():
    if request.method == 'POST':
        try:
            checkbox = request.form.get('checkbox')
        except:
            pass

        domainsea = request.form['domainsea']
        deleteJson = "../core_recon/gau_/delJson.sh"
        try:
            os.system(deleteJson)
        except:
            print("Algo Salio Mal Tio!")
        
        if checkbox == "on":
            print(checkbox)
            gauco = "../core_recon/gau_/./gau -subs -json -o Bulk.json " + domainsea + ""
            clearjson = "../core_recon/gau_/ConstructJSON.sh"
            os.system(gauco)
            os.system(clearjson)            
        else:
            gauco = "../core_recon/gau_/./gau -json -o Bulk.json " + domainsea + ""
            clearjson = "../core_recon/gau_/ConstructJSON.sh"
            os.system(gauco)
            os.system(clearjson)
    
    pass
    
    nu = 0
    durl = dict()
    f = open("static/pathdomain.json", "r")
    content = f.read()
    jsondecoded = json.loads(content)
    for entity in jsondecoded:
        nu += 1
        #url = entity[8:]
        #url = url.split("}")[0].split("\"")[0]
        durl[nu] = entity
        print(entity)

    resp = make_response(render_template('rupatch.html', durl=durl, nu=nu))
    resp.headers['Cache-Control'] = 'no-cache, no-store. must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = 0
    resp.headers['Server'] = 'RUBBST'
    return resp

#limancia pura! Experimental no necesitas enviar estó sólo json envía
@app.route("/record", methods=['GET', 'POST'])
def record():
    es = Elasticsearch('192.168.88.242:9200')
    nu = 0
    na = 0
    durl = dict() 
    filename = os.path.join(app.static_folder, 'pathdomain.json')#This Json is Output GAU
    #filename = app.url_for('static', filename='patchdomain.json')
    with open(filename) as ie:
        for name in ie:
            na += 1
            nam = name[8:]
            nam = nam.split("}")[0].split("\"")[0]
            if na == 2:
                nam = nam.strip()
                naur = get_fld(nam)
                print(naur)                
                pass
    with open(filename) as ie:
        for linea in ie:
            nu += 1
            url = linea[8:]
            url = url.split("}")[0].split("\"")[0]
            print(linea)
            durl[nu] = url
            es.index(index=naur, id=nu, body={'url': url})
            if nu == linea:
                break
    resp = make_response(render_template('infoscope.html', durl=durl))
    resp.headers['Cache-Control'] = 'no-cache, no-store. must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Server'] = 'RUBBST'
    resp.headers['Expires'] = 0    
    return resp

@app.route("/dashboard", methods=['GET'])
def dashboard():
    resp = make_response(render_template('dashboard.html'))
    resp.headers['Cache-Control'] = 'no-cache, no-store. must-revalidate'
    resp.headers['Access-Control-Allow-Origin:'] = '127.0.0.1'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Server'] = 'RUBBST'
    resp.headers['Expires'] = 0    
    return resp


if __name__ == "__main__":
    app.run(debug=True)


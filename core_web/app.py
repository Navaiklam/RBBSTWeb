#!/usr/bin/env python3
# requirements: flask, gau
# -*- coding: utf-8 -*-
# ReconBBSTWeb-beta 0.001
# ReconBBST By HafdlyMalkov 
# This is a proof of concept, an enumeration system that I am making for personal use in which I can keep track of my Hunters.
# I am using in the backend, python and different opensource applications to create a frontend in which I can save in a different database information of interest.

from flask import Flask, make_response, render_template, request, jsonify
from flask_cors import CORS
import json, os, string
app = Flask(__name__)
CORS(app)

@app.route("/rupatch", methods=['GET'])
def rupatch():
    return "ok"
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
    path = ""
    f = open("static/pathdomain.json", "r")
    content = f.read()
    jsondecoded = json.loads(content)
    for entity in jsondecoded:
        nu += 1
        #url = entity[8:]
        #url = url.split("}")[0].split("\"")[0]
        durl[nu] = entity
        
        print(entity)
        
    #nu = 0
    #durl = dict() 
    #filename = os.path.join(app.static_folder, 'pathdomain.json')#This Json is Output GAU
    #with open(filename) as ie:
    #    for linea in ie:
    #        nu += 1
        
    #        print(linea)
    #        durl[nu] = linea
    #        if nu == linea:
    #            break
    resp = make_response(render_template('rupatch.html', durl=durl, no=nu))
    resp.headers['Cache-Control'] = 'no-cache, no-store. must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = 0
    resp.headers['Server'] = 'RUBBST'
    
    #du = durl
    #print(type(du))
    return resp

#limancia pura! Experimental no necesitas enviar estó sólo json envía
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    nu = 0
    durl = dict() 
    filename = os.path.join(app.static_folder, 'pathdomain.json')#This Json is Output GAU
    #filename = app.url_for('static', filename='patchdomain.json')
    with open(filename) as ie:
        for linea in ie:
            nu += 1
            url = linea[8:]
            url = url.split("}")[0].split("\"")[0]
            print(linea)
            durl[nu] = linea
            if nu == linea:
                break
    resp = make_response(render_template('home.html', durl=durl))
    resp.headers['Cache-Control'] = 'no-cache, no-store. must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = 0
    resp.headers['Server'] = 'RUBBST'
    

    return resp

@app.route("/rupatch/api", methods=['GET'])
def ruapi():
   # nu = 0
   # durl = dict()
    #filename = os.path.join(app.static_folder, 'elisaRU.json')#This Json is Output GAU
    #data = json.load(open(filename))
    #with open(filename) as ie:
     #   for linea in ie:
      #      nu += 1
       #     url = line
           #url = linea[8:]
            #url = url.split("}")[0].split("\"")[0]
            #durl[nu] = url
        #    if nu == 30:
         #       break
    #resp = make_response(render_teamplate('home.html'))
    return render_template('home.html') #durl



#@app.route("/", methods="GET")
#@app.route("/home/<bounty>", methods="POST")
    
#    if request.method == 'POST':    
#           resp = make_response(render_template('home.html', bounty=bounty))
#            resp.headers['Server'] = 'HafdlyMalkov'
#            resp.headers['Content-encoding'] = 'compress'
#            resp.headers['export-FLASK_ENV'] = "development"
#            resp.headers['X-Forwarded-Host'] = '192.168.88.213'
#            return resp  #render_template('home.html', bounty=bounty, resp)
#    else:
#            resp = make_response(render_template('home.html'))
#            resp.headers['Server'] = 'HafdlyMalkov'
#            resp.headers['Response-Type'] = 'GET'
#            return resp
if __name__ == "__main__":
    app.run(debug=True)


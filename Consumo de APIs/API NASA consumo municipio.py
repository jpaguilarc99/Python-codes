# -*- coding: utf-8 -*-
import os, sys, time, json, urllib3, requests, multiprocessing, csv
import pandas as pd 

urllib3.disable_warnings()

def download_function(collection):
    ''' '''

    request, filepath = collection
    response = requests.get(url=request, verify=False, timeout=30.00).json()
    records = response['properties']['parameter']    
    df = pd.DataFrame.from_dict(records)
    df.to_csv(filepath, sep=",")
    

class Process():

    def __init__(self):

        self.processes = 1 #Procesos ejecutados al mismo tiempo

        self.request_template = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=TOA_SW_DWN,ALLSKY_SFC_PAR_TOT,T2M,TS,T2M_RANGE,ALLSKY_SFC_LW_DWN,QV2M,RH2M,PRECTOTCORR,PS,WS2M,WS2M_RANGE,WS10M,WS10M_RANGE,GWETPROF,GWETROOT,GWETTOP&community=RE&longitude={longitude}&latitude={latitude}&start=20100101&end=20211230&format=JSON"
        self.filename_template = "File_{departamento}_{municipio}.csv"

        self.messages = []
        self.times = {}

    def execute(self):        
        
        Start_Time = time.time()
        
        poligonos_municipios = open("insumo_coordenadas_poligonos.csv", "r")
        lineas = poligonos_municipios.readlines()

        insumos_poligonos = []
        for datos in lineas:
            datos = datos.rstrip("\n")
            datos = datos.split(",")

            tupla = tuple((datos))
            
            insumos_poligonos.append(tupla)

        insumos_poligonos.pop(0)        
        
        requests = []
        for departamento, municipio, latitude, longitude in insumos_poligonos:
            request = self.request_template.format(latitude=float(latitude),
                                                   longitude=float(longitude))
            filename = self.filename_template.format(departamento=departamento,
                                                     municipio=municipio)
            requests.append((request, filename))

        requests_total = len(requests)

        pool = multiprocessing.Pool(self.processes)
        x = pool.imap_unordered(download_function, requests)        

        for i, df in enumerate(x, 1):
            print(i, requests_total)
            sys.stderr.write('\rExporting {0:%}'.format(i/requests_total))

        self.times["Total Script"] = round((time.time() - Start_Time), 2)

        print ("\n")
        print ("Total Script Time:", self.times["Total Script"])

if __name__ == '__main__':
    Process().execute()
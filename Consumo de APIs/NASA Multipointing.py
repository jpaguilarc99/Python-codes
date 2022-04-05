# -*- coding: utf-8 -*-
import os, sys, time, json, urllib3, requests, multiprocessing, csv

urllib3.disable_warnings()

def download_function(collection):
    ''' '''

    request, filepath = collection
    response = requests.get(url=request, verify=False, timeout=30.00).json()

    with open(filepath, 'w') as file_object:
        json.dump(response, file_object)

class Process():

    def __init__(self):

        self.processes = 5

        self.request_template = r'https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=20150101&end=20150305&format=JSON'
        self.filename_template = "Lat_{latitude}_Lon_{longitude}.csv"

        self.messages = []
        self.times = {}

    def execute(self):

        Start_Time = time.time()

        locations = [(7.5378888, -73.9337795), (7.5424357, -73.9338223)]

        requests = []
        for latitude, longitude in locations:
            request = self.request_template.format(latitude=latitude, longitude=longitude)
            filename = self.filename_template.format(latitude=latitude, longitude=longitude)
            requests.append((request, filename))

        requests_total = len(requests)

        pool = multiprocessing.Pool(self.processes)
        x = pool.imap_unordered(download_function, requests)

        for i, df in enumerate(x, 1):
            sys.stderr.write('\rExportando datos {0:%}'.format(i/requests_total))

        self.times["Total Script"] = round((time.time() - Start_Time), 2)

        print ("\n")
        print ("Tiempo de ejecución:", self.times["Total Script"])

if __name__ == '__main__':
    Process().execute()
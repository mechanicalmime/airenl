import urllib.request
import json

def crawl_station(station_name):
    params_url = 'http://aire.nl.gob.mx:81/SIMA2017reportes/pages/Parametros.json'
    params_imeca_url = 'http://aire.nl.gob.mx:81/SIMA2017reportes/pages/ParametrosI.json'
    params_meteorologico = 'http://aire.nl.gob.mx:81/SIMA2017reportes/pages/Meteorologia.json'

    response = urllib.request.urlopen(params_url)
    params_json = json.loads(response.read())

    #print(json.dumps(params_json, sort_keys=True, indent=4))

    for item in params_json:
        print(f"{item['Parameter']} : {item['ParameterConMax']}")


crawl_station('CENTRO')

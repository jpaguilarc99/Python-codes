from orquestador2.step import Step
from datetime import date
from dateutil.relativedelta import relativedelta
from sklearn import preprocessing
import urllib3
import pandas as pd
import numpy as np
import requests, csv, json, joblib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SetParams(Step):
    """Configuración de los parámetros de ejecución y de las consultas SQL

    Args:
        Step (_type_): _description_
    """
    def ejecutar(self):
        # Cálculo de parámetros dinámicos

        params = {
            "year"  : date.today().year,
            "month" : date.today().month,
            "day"   : date.today().day
        }
        # Carga de parámetros estáticos
        params.update(self.getStepConfig())

        now = date(params["year"], params["month"], params["day"])
        date_today = now - relativedelta(days=date.today().day)
        date_12m = date_today -relativedelta(years=1)

        params.update(
            {
                "year"  : date_today.year,
                "month" : date_today.month,
                "day"   : date_today.day,
                "date_today"    : date_today.year*10000+date_today.month*100+date_today.day,
                "date_12m"      : date_12m.year*10000+date_12m.month*100+date_12m.day,
                "date_today_str": "{year}-{month:02}-{day:02}".format(year=date_today.year, month=date_today.month, day=date_today.day) 
            }
        )

        # Cálculo de parámetros basados en la fecha
        # params.update(SetParams.get_date_params(params))

        self.setPayload(params)
        self.getLog().info("Parametros calculados:")
        for k, w in params.items():
            if k != "password":
                self.getLog().info("    {} : {}".format(k, w))


class ConsumoAPI(Step):
    """
    Petición de descarga de información a servidor de API NASA Power Access Data
    Args:
        Step: getPayload(params)
    """
    def download_function(self, request):

        proxies = {
            "http" : None,
            "https" : None
        }

        response = requests.get(url=request, verify=False, proxies=proxies).json()
                
        records = response['properties']['parameter']    
        df = pd.DataFrame.from_dict(records)
            
        return df
                
    def ejecutar(self):
        params = self.getPayload()     
        request_template = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=TOA_SW_DWN,ALLSKY_SFC_PAR_TOT,T2M,TS,T2M_RANGE,ALLSKY_SFC_LW_DWN,QV2M,RH2M,PRECTOTCORR,PS,WS2M,WS2M_RANGE,WS10M,WS10M_RANGE,GWETPROF,GWETROOT,GWETTOP&community=RE&longitude={longitude}&latitude={latitude}&start={date_12m}&end={date_today}&format=JSON"
        
        lista_dfs = []
        mun_existentes = []
        mun_cercanos = []  
        
        with open(self.getFolderPath() + "insumo_coordenadas_poligonos.csv") as csv_file:
            poligonos_municipios = csv.reader(csv_file, delimiter=",")
            
            insumos_poligonos = []
                
            for datos in poligonos_municipios:
                datos_tuplas = tuple(datos)
                insumos_poligonos.append(datos_tuplas)
                
        with open(self.getFolderPath() + "municipios_mas_cercanos.json") as json_file:
            municipios_cercanos = json.load(json_file)
            municipios_cercanos = dict(municipios_cercanos)
            
            for key_existente, value_cercano in municipios_cercanos.items():
                mun_existentes.append(key_existente)
                mun_cercanos.append(value_cercano)                          
        
        for departamento, municipio, latitude, longitude in insumos_poligonos:
            request = request_template.format(latitude=float(latitude),
                                              longitude=float(longitude),
                                              **params)
                        
            df_actual = self.download_function(request)
            df_actual["Municipio"] = municipio
            df_actual["Fecha"] = pd.to_datetime(df_actual.index, format="%Y%m%d")
            df_actual["AÑO"] = df_actual["Fecha"].dt.year
            df_actual = df_actual.set_index(["Fecha"])
            
            first_column = df_actual.pop("AÑO")
            second_column = df_actual.pop("Municipio")
            
            df_actual.insert(0, "Municipio", second_column)
            df_actual.insert(0, "AÑO", first_column)
            
               
            for i in range(0, len(mun_cercanos)):
                
                if municipio in mun_cercanos[i]:
                    df_actual["Municipio"] = mun_existentes[i]
                                   
            lista_dfs.append(df_actual)           
             
        self.setPayload((lista_dfs, params))


class RezagoVariables(Step):

    def ejecutar(self):
        params = self.getPayload()[1]
        lista_dfs = self.getPayload()[0]
        conjunto_df = self.conjunto_dataframes(lista_dfs, params["date_today_str"])        

        self.setPayload((conjunto_df, params))
     
    def construccion_meteorologico(self, df_municipios):
        df_mun_actual = df_municipios       
        
        municipio_actual = pd.DataFrame(df_mun_actual.resample('M').asfreq()) 
        
        nombres_variables_meteorologicas = municipio_actual.columns.values       
        
        for dato in nombres_variables_meteorologicas[2:19]:
          municipio_actual[f"avg_{dato}_ult_12"] = municipio_actual[dato].rolling(12).mean()
          municipio_actual[f"std_{dato}_ult_12"] = municipio_actual[dato].rolling(12).std()
          municipio_actual[f"median_{dato}_ult_12"] = municipio_actual[dato].rolling(12).median()
          municipio_actual[f"max_{dato}_ult_12"] = municipio_actual[dato].rolling(12).max()
          municipio_actual[f"min_{dato}_ult_12"] = municipio_actual[dato].rolling(12).min()
          
          municipio_actual[f"avg_{dato}_ult_9"] = municipio_actual[dato].rolling(9).mean()
          municipio_actual[f"std_{dato}_ult_9"] = municipio_actual[dato].rolling(9).std()
          municipio_actual[f"median_{dato}_ult_9"] = municipio_actual[dato].rolling(9).median()
          municipio_actual[f"max_{dato}_ult_9"] = municipio_actual[dato].rolling(9).max()
          municipio_actual[f"min_{dato}_ult_9"] = municipio_actual[dato].rolling(9).min()
          
          municipio_actual[f"avg_{dato}_ult_6"] = municipio_actual[dato].rolling(6).mean()
          municipio_actual[f"std_{dato}_ult_6"] = municipio_actual[dato].rolling(6).std()
          municipio_actual[f"median_{dato}_ult_6"] = municipio_actual[dato].rolling(6).median()
          municipio_actual[f"max_{dato}_ult_6"] = municipio_actual[dato].rolling(6).max()
          municipio_actual[f"min_{dato}_ult_6"] = municipio_actual[dato].rolling(6).min()
          
          municipio_actual[f"avg_{dato}_ult_3"] = municipio_actual[dato].rolling(3).mean()
          municipio_actual[f"std_{dato}_ult_3"] = municipio_actual[dato].rolling(3).std()
          municipio_actual[f"median_{dato}_ult_3"] = municipio_actual[dato].rolling(3).median()
          municipio_actual[f"max_{dato}_ult_3"] = municipio_actual[dato].rolling(3).max()
          municipio_actual[f"min_{dato}_ult_3"] = municipio_actual[dato].rolling(3).min()
        
        return municipio_actual
    
    
    def conjunto_dataframes(self, lista_dfs, date_str):
        archivar_dataframes = []
        for dataframe in lista_dfs:    
            df_iter = self.construccion_meteorologico(dataframe)
            archivar_dataframes.append(df_iter)
            
        coleccion_dataframes = archivar_dataframes
        dataset_final = coleccion_dataframes[0]
        for i in range(1, len(coleccion_dataframes)):
            dataset_final = pd.concat([dataset_final, coleccion_dataframes[i]])
            
        dataset_final = dataset_final.loc[date_str]
        dataset_final = dataset_final.sort_index()
        
        return dataset_final


class Calificar(Step):
               
    def ejecutar(self):
        
        dataset_predicciones = self.getPayload()[0]       
        
        to_drop = ["AÑO", "Municipio", "TOA_SW_DWN", "PS", "avg_TOA_SW_DWN_ult_12", 
                   "max_TOA_SW_DWN_ult_12", "avg_TOA_SW_DWN_ult_9", "avg_TOA_SW_DWN_ult_6",
                   "max_TOA_SW_DWN_ult_3", "avg_ALLSKY_SFC_PAR_TOT_ult_12", "std_ALLSKY_SFC_PAR_TOT_ult_12",
                   "max_ALLSKY_SFC_PAR_TOT_ult_12", "min_ALLSKY_SFC_PAR_TOT_ult_12", "std_TS_ult_12", 
                   "avg_T2M_RANGE_ult_12", "min_T2M_RANGE_ult_12", "avg_ALLSKY_SFC_LW_DWN_ult_12", 
                   "avg_RH2M_ult_12", "std_PRECTOTCORR_ult_12","avg_WS2M_ult_12", "min_GWETROOT_ult_12"]
        
        X_calif = dataset_predicciones.filter(items=to_drop)
        le = preprocessing.LabelEncoder()
        le.fit(X_calif["AÑO"].astype(str))
        X_calif["AÑO"] = le.transform(X_calif['AÑO'].astype(str))

        X_calif = pd.get_dummies(X_calif, columns=["Municipio"])
        
        modelo = joblib.load(self.getModelPath() + "catboost_modelo_palma.pkl")
        preds = abs(modelo.predict(X_calif))
        
        municipios_pred = []
        with open(self.getFolderPath() + "municipios_existentes.json") as municipio_file:
            mun = json.load(municipio_file)
            for m in mun.keys():
                municipios_pred.append(m)
                
        dataframe = pd.DataFrame(X_calif.iloc[:,0:20])
        dataframe["MUNICIPIO"] = municipios_pred
        dataframe["ton_palma_prox12"] = preds        
        dataframe.columns = [c.lower() for c in dataframe.columns]

        self.setPayload((dataframe, self.getPayload()[1]))

class AjusteHectareas(Step):
    
    def ejecutar(self):
        db_final = self.getPayload()[0]
        params = self.getPayload()[1]

        df_ha = pd.read_csv(self.getFolderPath() + "ajuste_ha_polyfit.csv", sep=",")        
        año_consulta = params["year"]
        lista_municipios = list(df_ha["MUNICIPIO"])
        fechas_ajuste = [1997, 2011, 2020]
                
        hect_muns = self.ha_ajuste_municipios(df_ha, lista_municipios, fechas_ajuste,
                                                año_consulta)

        db_final["hectareas"] = 0                
        for mun, hect in hect_muns.items():
            for cod in range(0, len(lista_municipios)):
                if mun == db_final["municipio"][cod]:
                    db_final["hectareas"][cod] = hect

        db_final["ton_ha"] = db_final["ton_palma_prox12"] / db_final["hectareas"]

        db_final["ingestion_year"] = params["year"]
        db_final["ingestion_month"] = params["month"]
        db_final["ingestion_day"] = params["day"]

        cod_mun = []
        with open(self.getFolderPath() + "municipios_existentes.json") as mun_ex:            
            codigo = json.load(mun_ex)
            for m in codigo.keys():
                cod_mun.append(m)

        db_final.insert(19, "codigo_mun", cod_mun)

        print(db_final)
        self.setPayload((db_final, params))
        
    def hectareas_por_municipio(self, df_ha, fechas_ajuste, 
                                nombre_municipio, año_consulta):    
        datos_ajustados = []
            
        df_mun = df_ha[df_ha["MUNICIPIO"] == nombre_municipio]
        censo97 = df_mun["CENSO1997"]
        censo2011 = df_mun["CENSO2011"]
        censo2020 = df_mun["CENSO2020"]
        
        hectareas_mun = [float(censo97), float(censo2011), float(censo2020)]
        
        ajuste = np.polyfit(fechas_ajuste, hectareas_mun, 3)
        
        polinomio = np.poly1d(ajuste)      
        aj = polinomio(año_consulta)
        datos_ajustados.append(abs(aj))
            
        return datos_ajustados
    
    def ha_ajuste_municipios(self, df_ha, lista_municipios, fechas_ajuste,
                             año_consulta):
        ajuste_municipios = {}
        for nombre_mun in range(0, len(lista_municipios)):
            ha_municipio = self.hectareas_por_municipio(df_ha, fechas_ajuste, lista_municipios[nombre_mun], 
                                                        año_consulta)
            
            ajuste_municipios[lista_municipios[nombre_mun]] = float(ha_municipio[0])
            
        return ajuste_municipios


# Step de montar a la LZ el DF con la predicción

class CargarLZ(Step):
    def ejecutar(self):
        db_final = self.getPayload()[0]
        params = self.getPayload()[1]

        sparky = self.getSparky()
        sparky.subir_df( db_final, "produccion_palma", zona='proceso' )

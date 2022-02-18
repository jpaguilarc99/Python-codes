"""

Created by: Juan Pablo Aguilar Calle, Medellín, Colombia.
Riesgo de liquidez: Bancolombia TdC.
The bases of the knowledge for this code:
Bibliography: "https://machinelearningmastery.com/deep-learning-for-time-series-forecasting/"
"https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/"
"""
###Se importan las librerías con las que se va a trabajar
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten


###Se importan los datos de riesgos de liquidez de Bancolombia (base de datos)
db = pd.read_csv('Factor de prepago TdC.csv', parse_dates=[0], sep=';', index_col='Fecha Corte', encoding='latin-1')
##Dejamos solo las columnas de interés y eliminamos las demás (quedan fechas y fp)
db = db.drop(['Calificación', 'Cupo Aprobado', 'Saldo', 'Pago mínimo', 'Último pago', 'Balance final', 'Prepago', 'Año', 'Mes'], axis=1)
###Se establece un indice de tipo DataTimeIndex
db.index = pd.to_datetime(db.index)
db = db.sort_index()
db_sub = db['2018'] #Datos para el año 2018
db_sub2 = db['2019'] #Datos para el año 2019
db_sub3 = db['2020'] #Datos para el año 2020

#print(len(db['2018'])) #Cantidades de datos por año
#print(len(db['2019']))
#print(len(db['2020']))

#print(db.describe()) #Descripción de los datos

diarios = db.resample("D").mean() ##Promedios diarios
#print(diarios)

##VISUALIZACIÓN DE DATOS
#plt.plot(diarios['2018'].values)
#plt.plot(diarios['2019'].values)
#plt.plot(diarios['2020'].values)

###Se convierten las series temporales a aprendizaje supervisado
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    db = pd.DataFrame(data)
    cols, names = list(), list()
    ##Secuencia de entrada (previsiones) (t-n, ... , t-1)
    for i in range(n_in, 0, -1):
        cols.append(db.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    ##Secuencia de salida (predicciones) (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(db.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    ##Se concatenan las operaciones
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    ##Se eliminan filas con valores NaN
    if dropnan:
        agg.dropna(inplace=True)
    return agg

###Se carga el dataset para la RNN
db2 = db.values
#Se hacen los valores flotantes (float32)
db2 = db2.astype('float32')
###Normalizamos las características
escalar = MinMaxScaler(feature_range=(-1, 1))
db2 = db2.reshape(-1, 1) ##Se tiene una sola dimensión
escalado = escalar.fit_transform(db2)
###Marco de aprendizaje supervisado
reframed = series_to_supervised(escalado, 7, 1)
reframed.head(7)

###RED NEURONAL
##Dividimos los conjuntos de train y test, para entrenar y validar el modelo
db2 = reframed.values
n_train_days = 4000 - (300+7)
train = db2[:n_train_days, :]
test = db2[n_train_days:, :]
##Entradas y salidas
x_train, y_train = train[:, :-1], train[:,-1]
x_val, y_val = test[:,:-1], test[:, -1]
##Reescalamos la entrada a 3D (samples, timesteps, features)
x_train = x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
x_val = x_val.reshape((x_val.shape[0], 1, x_val.shape[1]))
#print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)

###Definimos el modelo de la red neuronal 
def model():
    model = Sequential()
    model.add(Dense(7, input_shape=(1, 7), activation='tanh')) #7 entradas para 7 pasos predecidos
    model.add(Flatten())
    model.add(Dense(1, activation='tanh'))
    model.compile(loss='mean_absolute_error', optimizer='adam', metrics=["mse"])
    model.summary()
    return model

##Variables del entrenamiento
epochs = 50  ##Repaso de samples
model = model()
#Entrenamiento del modelo
history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val, y_val), batch_size=300)

##Función de pérdida

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend('Entrenamiento', 'Validación')
plt.title('Función de pérdida (loss function)')
plt.ylabel('Porcentaje de error')
plt.xlabel('Épocas de entrenamiento y validación')

###Visualización de datos entregados por Bancolombia TdC
#results = model.predict(x_val)
#plt.scatter(range(len(y_val)), y_val, c='g')
#plt.scatter(range(len(results)), results, c='r')
#plt.title('Validación')
#plt.show()

##PRONÓSTICO DE FP FUTURAS
lastdays = db['2020-05-02':'2020-08-06']
#print(lastdays)
##preprocesado
pred = lastdays.values
pred = pred.astype('float32')
##Normalización
pred = pred.reshape(-1, 1)
scaled = escalar.fit_transform(pred)
ref = series_to_supervised(scaled, 7, 1)
ref.drop(ref.columns[[7]], axis = 1, inplace=True)
ref.head(7)

pred = ref.values
x_test2 = pred[6:,:]
x_test2 = x_test2.reshape((x_test2.shape[0], 1, x_test2.shape[1]))
#print(x_test2)

def nvalor(x_test2, newvalue):
    for i in range(x_test2.shape[2]-1):
        x_test2[0][0][i] = x_test2[0][0][i+1]
    x_test2[0][0][x_test2.shape[2]-1] = newvalue
    return x_test2

resultados=[]
for i in range(7):
    parcial = model.predict(x_test2)
    resultados.append(parcial[0])
    print(x_test2)
    x_test2=nvalor(x_test2, parcial[0])
    
adimen = [x for x in resultados]
inverted = escalar.inverse_transform(parcial)
print(inverted)

##SE VISUALIZAN LOS RESULTADOS DE PREDICCIONES DE PRÓXIMOS 300 DÍAS
prediccion = pd.DataFrame(inverted)
prediccion.columns = ['pronostico']
prediccion.plot()
plt.title('Pronóstico próximos 300 días')
plt.ylabel('Fp=(Prepago/Pago mínimo)')
plt.xlabel('Días futuros')
prediccion.to_csv('pronostico300dias.csv') ##Guardamos las predicciones obtenidas en un archivo .csv

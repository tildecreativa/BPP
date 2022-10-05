import pandas as pd
import matplotlib.pyplot as plt


archivo = 'finanzas2020.csv'

#comprobando que existe el archivo
try: 
    f = open(archivo)
    
except FileNotFoundError:
    print(f'No existe el archivo: '+archivo)
    exit()

#si el archivo existe, cargamos el archivo en un dataframe
df = pd.read_csv(archivo, sep='\t')
columnas = list(df.columns.values)
#print(columnas)

#comprobando que tiene 12 columnas y son de los meses del año
class Error(Exception):
    pass
class Notienedocemeses(Error):
    pass
class Meseserroneos(Error):
    pass

try:
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] #solo se usa como referencia comparativa
    if(len(columnas) != 12):
        raise Notienedocemeses
    else:
        if(columnas != meses):
            raise Meseserroneos
except Notienedocemeses:
    print('no tiene doce meses')
    exit()

except Meseserroneos:
    print('los meses son erróneos, por favor revisar las cabeceras')
    exit()

#df = pd.read_csv(archivo, sep='\t')
#columnas = list(df.columns.values)

columnaValores = {}
columnaGastos = []
columnaIngresos = []
for i in columnas:
    serie = pd.Series(df[i])
    
    try:
        if(len(serie)==0):
            raise print(f'Esta columna no tiene contenido: '+i)
    except:
        print('no se pudo continuar')
        

    serie = pd.to_numeric(serie, errors='coerce') #comprobando datos correctos, que sean numéricos de lo contrario lo salta
    suma_serie = serie.sum()
    columnaValores[i] = suma_serie
    columnaValores[i] = suma_serie
    for index, value in serie.items():
        if value < 0:
            columnaGastos.append(value)
        elif value > 0:
            columnaIngresos.append(value)
mayor_valor = max(columnaValores, key=columnaValores.get)
menor_valor = min(columnaValores, key=columnaValores.get)
promedio = sum(columnaValores.values())/len(columnaValores)
gastos = sum(columnaGastos)
ingresos = sum(columnaIngresos)
print('El mes con mayor gasto es: ',menor_valor)
print('El mes con mayor ahorro es: ',mayor_valor)
print('El promedio de gastos es: ',promedio)
print('El gasto total es: ',gastos)
print('El ingreso total es: ',ingresos)

#gráfico
plt.bar(range(len(columnaValores)), list(columnaValores.values()), align='center')
plt.xticks(range(len(columnaValores)), list(columnaValores.keys()))
plt.show()

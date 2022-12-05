import os
import geopandas as gp
from shapely.geometry import shape
#Leer Shape de Parques de Valparaíso
plazasValparaiso = gp.read_file(r'shape/Parques_Valparaiso.shp')
# Transformar Datum a U.T.M WGS 84 Huso 19 Sur (metros)
plazasValparaiso = plazasValparaiso.to_crs(32719)
# Calcular area de cada entidad del shape
for i in range(len(plazasValparaiso)):
    plazasValparaiso.loc[i,'Area (m2)'] = shape(plazasValparaiso.loc[i,'geometry']).area
# Ordenar dataframe por area de poligono
plazasValparaiso = plazasValparaiso.sort_values('Area (m2)')
# Imprimir resultado
print("Bienvenido a Mansa Plaza")
print(plazasValparaiso)


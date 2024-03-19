# This is a basic programn to read the file and understand the data

import geopandas as gpd
import matplotlib.pyplot as plt

# Reads the head and the tail of each column
def show_head_column(gdf, column):
   print(gdf[column].head)
   print("---------------------------------------")

   return

def plot_graph(coluna_y, coluna_x):
   fig, ax = plt.subplots() # Creates the axis ax using the subplots
   gdf.plot(ax=ax, color='lightgrey') # plot the
   gdf.plot(column=coluna_x, cmap='coolwarm', markersize=gdf[coluna_y], legend=True,  ax=ax)
   plt.show()

   return


def group_values(gdf, column):

   contadores = {}

   for row in gdf[column]:
      if row in contadores:
        contadores[row] += 1
      else:
        contadores[row] = 1
        
   for item, contador in contadores.items():
      print(f'{item} - {contador}')

   return 


shapefile_path = '../dados/accumulated_deforestation_2000.shp'
gdf = gpd.read_file(shapefile_path)
columns = gdf.columns.tolist()
# print(columns)

list(map(lambda col: show_head_column(gdf, col), columns))

group_values(gdf, 'main_class')

plot_graph('area_km', 'main_class')


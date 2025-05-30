from os import path

from domain.dataset_csv import DatasetCSV

#ruta de csv

csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")

#cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos

#guardar en bd
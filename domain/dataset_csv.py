from domain.dataset import Dataset
import pandas as pd

class DatasetCSV(Dataset):
  def __init__(self, fuente):
    super().__init__(fuente)

  def cargar_datos(self):
    try:
        df=pd.read_csv(self.fuente)
        self.datos = df
        print("CSV cargado")
        if self.validar_datos():
          print("datos validados en CSV")
          #self.transformar_datos()


    except Exception as e:
        print(f"Error cargando CSV:{e}")  
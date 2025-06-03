from domain.dataset import Dataset
import pandas as pd

class DatasetExcel(Dataset):
  def __init__(self, fuente):
    super().__init__(fuente)

  def cargar_datos(self):
    try:
        df=pd.read_excel(self.fuente)
        self.datos = df
        print("Excel cargado")
        if self.validar_datos():
          print("datos validados en excel")
          #self.transformar_datos()

    except Exception as e:
        print(f"Error cargando Excel:{e}")  
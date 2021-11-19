import pandas as pd
import requests
from zipfile import ZipFile

from .ExtractBabyNames import ExtractBabyNames


class ExtractUSANames(ExtractBabyNames):

    config = {
        'download_url':'https://www.ssa.gov/oact/babynames/state/namesbystate.zip',
        'temp_file_path':'USA.zip'
    }
    
    def __init__(self) -> None:
        super().__init__()
        self.temp_file_path = self.config['temp_file_path']
        self.download_url = self.config['download_url']
    
    def download(self):
        result = super().download()
        if result != None:
            print("Successfully downloaded file")
        return result
    
    def read(self):
        super().read()
        print(self.temp_folder + self.temp_file_path)
        df = pd.concat([
            pd.read_csv(ZipFile(self.temp_folder + self.temp_file_path).open(i), sep=',', header=None) for i in ZipFile(self.temp_folder + self.temp_file_path).namelist() if i.endswith('.TXT')
        ],ignore_index=True)
        df.columns = ["prov_state_id", "sex", "year", "name", "count"]
        print(df)
        self.data = df
        return self.data
    
    def write(self):
        super().write()
        


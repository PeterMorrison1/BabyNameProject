import os
import urllib.request

import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa


class ExtractBabyNames:
    source_url = None
    temp_folder = './temp/USA/'
    temp_file_path = None
    download_url = None
    temp_path = None
    data = None
    data_path = './data/'

    #! Need to make a schema for them? Not sure if thats a pyspark thing only
    fact_names_parquet = 'fact_names.parquet'
    dim_names_parquet = 'dim_names.parquet'
    dim_prov_state_parquet = 'dim_prov_state.parquet'
    dim_year_parquet = 'dim_year.parquet'

    def __init__(self) -> None:
        pass

    def download(self):
        try:
            print('Making directory')
            os.makedirs(self.temp_folder)
        except:
            print('Directory exists, continuing')
        print("downloading")
        print(f'Downloadurl: {self.download_url}')
        try:
            result = urllib.request.urlretrieve(
                self.download_url, self.temp_folder + self.temp_file_path)
            print(result)
            self.temp_path = result[0]
            return result[0]
        except Exception as e:
            print(e)
            return None

    def read(self):
        pass

    def _helper_check_file_exists(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False
    
    def _write_to_parquet(self, df, path):
        table = pa.Table.from_pandas(df)
        pq.write_to_dataset(table, root_path=path)
        

    def write(self):
        fact_names: pd.DataFrame = self.data
        fact_names.to_parquet(self.data_path + self.fact_names_parquet)

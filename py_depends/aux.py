import zipfile
import pandas as pd

def unzipFile(path_to_file: str, data_types=None) -> pd.core.frame.DataFrame:
    """ Free monthly extract file from the zip file """
    zf = zipfile.ZipFile(path_to_file)
    target_df = [f for f in zf.namelist() if '.csv' in f][0] # grabbing only the first one, assumes one zip = one csv
    return pd.read_csv(zf.open(target_df), dtype=data_types, parse_dates=True)
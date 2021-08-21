import zipfile
import pandas as pd
import numpy as np

def unzipFile(path_to_file: str) -> pd.core.frame.DataFrame:
    """ Frees monthly extract file from the zip file """
    zf = zipfile.ZipFile(path_to_file)
    target_df = [f for f in zf.namelist() if '.csv' in f][0] # grabbing only the first one, assumes one zip = one csv
    return pd.read_csv(zf.open(target_df), low_memory=False)

def subsetRenameRetype(df: pd.core.frame.DataFrame, cols_map: dict) -> pd.core.frame.DataFrame:
    """ Grabs relevant cols specified by cols_map, renames them, and overrides the original data types """
    subs_df = df[cols_map.keys()]
    # now rename these columns
    rename_dict = {k: v['name'] for k, v in cols_map.items()}
    subs_df.rename(columns=rename_dict, inplace=True)
    # and finally override the original data types inferred by pandas
    dtype_dict = {v['name']: v['py_dtype'] for k, v in cols_map.items() if v['py_dtype']}
    subs_df = subs_df.astype(dtype_dict)
    return subs_df

def shapeDatetime(df: pd.core.frame.DataFrame, timestamp_cols: list, date_col: str) -> pd.core.frame.DataFrame:
    """ Converts the unusable floats in timestamp_cols to datetime objects """
    df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m-%d')

    for time_col in timestamp_cols:
        print('Shaping {}-{} columns'.format(time_col, date_col))
        # there's almost definitely a way to do this simpler, but...
        df[time_col] = (pd.to_timedelta(df[time_col] // 100, unit='hours') + pd.to_timedelta(df[time_col] % 100, unit='minutes')).apply(str)
        df[time_col] = df[time_col].str[-8:]
        df[time_col] = df[date_col].dt.strftime('%Y-%m-%d') + ' ' + df[time_col]
        # and now back to properly typed date
        df[time_col] = pd.to_datetime(df[time_col], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    return df
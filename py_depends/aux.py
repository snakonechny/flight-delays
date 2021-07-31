import zipfile
import pandas as pd

def unzipFile(path_to_file: str) -> pd.core.frame.DataFrame:
    """ Frees monthly extract file from the zip file """
    zf = zipfile.ZipFile(path_to_file)
    target_df = [f for f in zf.namelist() if '.csv' in f][0] # grabbing only the first one, assumes one zip = one csv
    return pd.read_csv(zf.open(target_df))

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
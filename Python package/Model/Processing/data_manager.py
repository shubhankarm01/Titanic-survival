from typing import Any, List, Union
import numpy as np
import re
import pandas as pd

from Model.Config.core import DATASET_DIR, TRAINED_MODEL_DIR, config
from sklearn.pipeline import Pipeline

import joblib

def get_first_cabin(row: Any) -> Union[str, float]:
    try:
        return row.split()[0]
    except:
        return np.nan
    
def get_title(passenger: str) -> str:
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'
    
def pre_pipeline_preparation(*, data: pd.DataFrame) -> pd.DataFrame:
    data = data.replace('?', np.nan)
    data['cabin'] = data['cabin'].apply(get_first_cabin)
    data['title'] = data['name'].apply(get_title)
    
    data["fare"] = data["fare"].astype("float")
    data["age"] = data["age"].astype("float")
    
    data.drop(config.model_config.unused_fields, axis = 1, inplace = True)
    
    return data

def load_dataset(*, file_name: str) -> pd.DataFrame:
    data = pd.read_csv(DATASET_DIR/file_name)

    data = pre_pipeline_preparation(data = data)
    return data

def save_pipeline(*, pipeline_to_save: Pipeline) -> None:
    save_path = TRAINED_MODEL_DIR/"trained_pipeline.pkl"
    
    joblib.dump(pipeline_to_save, save_path)

def load_pipeline(*, file_name: str) -> Pipeline:
    file_path = TRAINED_MODEL_DIR/file_name
    
    return joblib.load(filename = file_path)
    
    
    
    
    
    
    
    
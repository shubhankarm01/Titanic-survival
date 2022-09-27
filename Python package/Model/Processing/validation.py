from typing import Tuple, Optional, List

from Model.Processing.data_manager import pre_pipeline_preparation
from Model.Config.core import config

from pydantic import BaseModel, ValidationError
import pandas as pd
import numpy as np

class TitanicDataInputSchema(BaseModel):
    pclass: Optional[int]
    sex: Optional[str]
    age: Optional[float]
    sibsp: Optional[int]
    parch: Optional[int]
    fare: Optional[float]
    cabin: Optional[str]
    embarked: Optional[str]
    title: Optional[str]
 
class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]

def validated_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    
#    pre_processed = pre_pipeline_preparation(data = input_data)
    validated_data = input_data[config.model_config.features].copy()
    
    error = None
    
    try:
        MultipleTitanicDataInputs(inputs = validated_data.replace({np.nan :None}).to_dict(orient = 'records'))
        
    except ValidationError as errors:
        error = errors.json()
        
    return validated_data, error
    
    
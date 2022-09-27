from typing import Union
import pandas as pd

from Model.Processing.validation import validated_inputs
from Model.Processing.data_manager import load_pipeline

_titanic_pipe = load_pipeline(file_name = 'trained_pipeline.pkl')

def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    
    data = pd.DataFrame(input_data)
    validated_data, errors = validated_inputs(input_data = data)
    results = {"predictions": None, "errors": errors}
    
    if not errors:
        predictions = _titanic_pipe.predict(X = validated_data)
        results = {"predictions": predictions, "errors": errors}
        
    return results
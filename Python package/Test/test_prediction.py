from Model.predict import make_prediction
import numpy as np
from sklearn.metrics import accuracy_score

def test_prediction(sample_input_data):
    result = make_prediction(input_data = sample_input_data)
    
    predictions = result.get("predictions")
    
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    
    assert result.get("error") is None
    
    _predictions = list(predictions)
    y_true = sample_input_data["survived"]
    accuracy = accuracy_score(_predictions, y_true)
    assert accuracy > 0.7
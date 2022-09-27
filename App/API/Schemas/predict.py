from pydantic import BaseModel
from typing import Optional, Any, List
from Model.Processing.validation import TitanicDataInputSchema

class PredictionResults(BaseModel):
    errors: Optional[Any]
    predictions: Optional[List[float]]
    
class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]
    
    class Config:
        
        schema_extra = {"example": {"inputs": [{"pclass": 1,
                                                "sex": "female",
                                                "age": 29,
                                                "sibsp": 0,
                                                "parch": 0,
                                                "fare": 211.3375,
                                                "cabin": "B",
                                                "embarked": "S",
                                                "title": "Miss"
                                                }]}}
        
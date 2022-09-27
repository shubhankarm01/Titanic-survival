from fastapi import APIRouter, HTTPException
from typing import Any

from API.Schemas import predict, health
import pandas as pd
from fastapi.encoders import jsonable_encoder
from Model.predict import make_prediction
import numpy as np
import json

from API.config import settings
from loguru import logger

api_router = APIRouter()

@api_router.get("/health", response_model = health.Health, status_code = 200)
def Health() -> dict:
    Health = health.Health(name = settings.PROJECT_NAME)
    
    return Health.dict()

@api_router.post("/predict", response_model = predict.PredictionResults, status_code = 200)
async def Predict(input_data: predict.MultipleTitanicDataInputs) -> Any:
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data = input_df.replace({np.nan: None}))
    
    if results['errors'] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code = 400, details = json.loads(results['errors']) )
    
    logger.info(f"Prediction results: {results.get('predictions')}")
    
    results = predict.PredictionResults(errors = results['errors'], 
                                        predictions = list(results['predictions']),)
        
    return results.dict()


# temp = Predict(input_data = predict.MultipleTitanicDataInputs(inputs = [{"pclass": 1,
#                                                                     "sex": "female",
#                                                                     "age": 29,
#                                                                     "sibsp": 0,
#                                                                     "parch": 0,
#                                                                     "fare": 211.3375,
#                                                                     "cabin": "B",
#                                                                     "embarked": "S",
#                                                                     "title": "Miss"
#                                                                     }]))
# temp

# temp = Predict(input_data = predict.MultipleTitanicDataInputs(inputs = [{"pclass": 3,
#                                                                     "sex": "male",
#                                                                     "age": 29.0,
#                                                                     "sibsp": 0,
#                                                                     "parch": 0,
#                                                                     "fare": 7.875,
#                                                                     "cabin": "None",
#                                                                     "embarked": "S",
#                                                                     "title": "Mr"
#                                                                     }, {"pclass": 1,
#                                                                         "sex": "female",
#                                                                         "age": 29.5,
#                                                                         "sibsp": 0,
#                                                                         "parch": 0,
#                                                                         "fare": 211.3375,
#                                                                         "cabin": "B",
#                                                                         "embarked": "S",
#                                                                         "title": "Miss"
#                                                                         }]))
# temp
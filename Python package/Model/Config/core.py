from pathlib import Path
from typing import Sequence
from pydantic import BaseModel
from strictyaml import YAML, load

# Directories
import Model
PACKAGE_ROOT = Path(Model.__file__).resolve().parent
CONFIG_FILE_PATH = PACKAGE_ROOT/"config.yml"
DATASET_DIR = PACKAGE_ROOT/"Dataset"
TRAINED_MODEL_DIR = PACKAGE_ROOT/"Trained_model"

class ModelConfig(BaseModel):
    
    target: str
    features: Sequence[str]
    unused_fields: Sequence[str]
    numerical_vars: Sequence[str]
    categorical_vars: Sequence[str]
    cabin_vars: Sequence[str]
    test_size: float
    random_state: int
    raw_data_file : str
    
class Config(BaseModel):
    model_config: ModelConfig
    


def find_config_file() -> Path:
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    
    raise Exception("config file not found")
    
def fetch_configuration_from_file(cfg_path: Path = None) -> YAML:
    if not cfg_path:
        cfg_path = find_config_file()
    
    if cfg_path:
        with open(cfg_path, 'r') as conf_file:
            config_parse = load(conf_file.read())
            return config_parse
        
def validate_config(config_parse: YAML = None) -> Config:
    if config_parse is None:
        config_parse = fetch_configuration_from_file()
        
    config_ = Config(model_config = ModelConfig(** config_parse.data))
     
    return config_

config = validate_config()
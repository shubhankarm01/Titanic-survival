import pytest
import pandas as pd
from Model.Processing.data_manager import load_dataset
from Model.Config.core import config

from typing import Generator
from fastapi.testclient import TestClient
from API.main import app

@pytest.fixture(scope = 'module')
def test_data() -> pd.DataFrame:
    return load_dataset(file_name = config.model_config.raw_data_file)

@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
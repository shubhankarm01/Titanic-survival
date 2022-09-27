import pytest
from sklearn.model_selection import train_test_split

from Model.Config.core import config
from Model.Processing.data_manager import load_dataset

@pytest.fixture
def sample_input_data():
    data = load_dataset(file_name = config.model_config.raw_data_file)
    
    
    X_train, X_test, y_train, y_test = train_test_split(data, data[config.model_config.target],
                                                        test_size = config.model_config.test_size,
                                                        random_state = config.model_config.random_state)
    
    return X_test
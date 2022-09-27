from sklearn.model_selection import train_test_split
from Model.Config.core import config
from Model.pipeline import titanic_pipe 

from Model.Processing.data_manager import load_dataset, save_pipeline


def train() -> None:
    data = load_dataset(file_name = config.model_config.raw_data_file)
    
    X_train, X_test, y_train, y_test = train_test_split(data.drop('survived', axis=1), data['survived'],
                                                        test_size = config.model_config.test_size,
                                                        random_state = config.model_config.random_state)
    titanic_pipe.fit(X_train, y_train)
    
    save_pipeline(pipeline_to_save = titanic_pipe)
    
file_name = config.model_config.raw_data_file

train()
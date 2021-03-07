import joblib
import os
import random

MODEL_PATH = os.environ['MODEL_PATH']


class PredictiveModel:

    """ Wrapper for loading and serving pre-trained model"""

    def __init__(self):
        print("** Spinning up new model **")
        self.model = self._load_model_from_path(MODEL_PATH)

    @staticmethod
    def _load_model_from_path(path):
        # Load persistent items (Data,models) here
        #model = joblib.load(path)
        return random

    def predict(self, data):
        """
        Do predictions using loaded in model and data here
        """
        return sum(data) + self.model.random()
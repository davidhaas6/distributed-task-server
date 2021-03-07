import joblib
import os
import random

MODEL_PATH = os.environ['MODEL_PATH']


class PredictiveModel:

    """ Wrapper for loading and serving pre-trained model"""

    def __init__(self):
        print("New church model")
        self.model = self._load_model_from_path(MODEL_PATH)

    @staticmethod
    def _load_model_from_path(path):
        # Load persistent items (Data,models) here
        #model = joblib.load(path)
        return random

    def predict(self, data):
        """
        Make batch prediction on list of preprocessed feature dicts.
        Returns class probabilities if 'return_options' is 'Prob', otherwise returns class membership predictions
        """
        return sum(data) + self.model.random()
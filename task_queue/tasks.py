import importlib
import logging
from celery import Task

from .worker import app


class PredictTask(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.

    """
    abstract = True  # doesn't do anything as far as I know

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        if not self.model:
            logging.info('Loading Model...')
            module_import = importlib.import_module(self.path[0]) # import the model from @app.task param
            model_obj = getattr(module_import, self.path[1]) # equivalent to doing ModelPath.ModelClass
            self.model = model_obj() # Creating instance of ModelClass()
            logging.info('Model loaded')
        return self.run(*args, **kwargs)


@app.task(ignore_result=False,
          bind=True,  # bound task https://docs.celeryproject.org/en/latest/userguide/tasks.html#basics
          base=PredictTask, # Base task instance -- reference for self
          path=('task_queue.ml.model', 'PredictiveModel'),  # pass task instance to model
          name='{}.{}'.format(__name__, 'PredictionTask')) # name for the task
def predict_objective(self, data):
    """
    Essentially the run method of PredictTask
    """
    logging.info(data)
    inputs = data['features']
    prediction = self.model.predict(inputs) # a simple sum for this example
    logging.info(f'Prediction: {prediction}')
    return prediction

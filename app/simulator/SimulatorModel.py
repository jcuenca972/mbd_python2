from pycaret.regression import *

class SimulatorModel:

    def __init__(self):
        self._model_cnt = load_model(model_name="app/data/cnt_model")
        self._model_casual = load_model(model_name="app/data/cnt_model_casual")
        self._model_registered = load_model(model_name="app/data/cnt_model_registered")

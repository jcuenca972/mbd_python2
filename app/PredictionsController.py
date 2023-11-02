from app.GeneralView import GeneralView
from app.PredictionsModel import PredictionsModel

class PredictionsController:

    def __init__(self, view: GeneralView, model: PredictionsModel):
        self._view = view
        self._model = model
        self._value = None
        self._value2 = None

    def show(self, container):
        self._view.init_container(container)
        self._view.write_titles("Predictions", "Waiting for ML Algorithms")
        self._value, self._value2 = self._view.write_number_inputs("Test Number", "Test Number 2")




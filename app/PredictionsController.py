from app.GeneralView import GeneralView
from app.PredictionsModel import PredictionsModel

class PredictionsController:

    def __init__(self, view: GeneralView, model: PredictionsModel):
        self._view = view
        self._model = model

    def show(self, container):
        self._view.init_container(container)
        self._view.write_titles("Predictions", "Waiting for ML Algorithms")

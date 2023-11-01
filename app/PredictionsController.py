from app.GeneralView import GeneralView


class PredictionsController:

    def __init__(self, view: GeneralView):
        self._view = view

    def show(self, container):
        self._view.init_container(container)
        self._view.write_titles("Predictions", "Waiting for ML Algorithms")

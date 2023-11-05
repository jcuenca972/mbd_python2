from app.GeneralView import GeneralView
from app.simulator.SimulatorModel import SimulatorModel

class SimulatorController:

    def __init__(self, view: GeneralView, model: SimulatorModel):
        self._view = view
        self._model = model
        self._value = None

    def show(self, container):
        self._view.init_container(container)
        self._view.write_titles("Predictions", "Waiting for ML Algorithms")
        self._value = self._view.write_number_inputs("Test Number")[0]
        self._view.write_text(f"You insert {self._value}")




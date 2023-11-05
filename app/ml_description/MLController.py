from app.ml_description.MLView import MLView
from app.ml_description.MLModel import MLModel

class MLController:

    def __init__(self, view: MLView, model: MLModel):
        self._view = view
        self._model = model

    def show(self, container):
        self._view.init_container(container)
        self._view.show_title("Dataset Description")
        self._view.show_data_highlighs(self._model.get_missing_values(),
                                       self._model.get_continuos_variables_analysis(),
                                       self._model.get_correlation(),
                                       self._model.get_daylight_code(),
                                       self._model.get_correlation_daylight())
        self._view.show_title("Model Description")
        self._view.show_model_highlights(self._model.get_pycaret_info())

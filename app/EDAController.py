from app.GeneralView import GeneralView
from app.EDAModel import EDAModel
from app.data.EDATypes import EDATypes

class EDAController:

    def __init__(self, view: GeneralView, model: EDAModel):
        self._view = view
        self._model = model

    def show(self, container, eda_type: EDATypes):
        self._view.init_container(container)
        self._view.write_titles("Exploratory Data Analysis", eda_type.value)
        self._view.plotly_show(self._get_fig(eda_type))

    def _get_fig(self, eda_type):
        if eda_type == EDATypes.OVER_TIME:
            return self._model.rentals_over_time()
        elif eda_type == EDATypes.HOUR_DAY:
            return self._model.rentals_by_hour()
        elif eda_type == EDATypes.RENTALS_WEATHER:
            return self._model.rentals_weather()
        elif eda_type == EDATypes.RENTALS_SEASON:
            return self._model.rentals_by_season()
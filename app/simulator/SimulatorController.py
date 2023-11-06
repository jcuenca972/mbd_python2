from app.simulator.SimulatorView import SimulatorView
from app.simulator.SimulatorModel import SimulatorModel
from app.data_models.BikesInput import BikesInput


class SimulatorController:

    def __init__(self, view: SimulatorView, model: SimulatorModel):
        self._view = view
        self._model = model
        self._bikes_input = BikesInput(0, 0, 0, 0, 0, 0, 0,
                                       0.0, 0.0, 0.0, 0.0)
        self._ml_selection = None
        self._is_ml_calculate = False

    def show(self, container):
        self._is_ml_calculate = self._view.init_container(container, 3)
        self._view.write_titles_top(
            "Simulator",
            ""
        )
        self._ml_selection = self._view.show_choose_model(self._model.models.keys())
        self._bikes_input.season = self._view.write_selector(
            "Season", 1, 0, "Springer", "Summer", "Fall", "Winter"
        )
        self._bikes_input.day = self._view.write_slider("Day", 1, 31, 1)
        self._bikes_input.hr = self._view.write_slider("Hour", 0, 23, 1)
        self._bikes_input.holiday = self._view.write_selector(
            "Holiday", 0, 0, "No", "Yes"
        )
        self._bikes_input.weekday = self._view.write_selector(
            "Weekday", 0, 1, "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        )
        self._bikes_input.workingday = self._view.write_selector(
            "Workingday", 0, 1, "No", "Yes"
        )
        self._bikes_input.weathersit = self._view.write_selector(
            "Weather Type", 1, 1, "Clear, Few clouds, Partly cloudy, Partly cloudy",
            "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist",
            "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds",
            "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
        )
        self._bikes_input.temp = self._view.write_number_input(
            "Normalized temperature in Celsius. The values are divided to 41 (max)", 1
        )
        self._bikes_input.hum = self._view.write_number_input(
            "Normalized humidity. The values are divided to 100 (max)", 2
        )
        self._bikes_input.windspeed = self._view.write_number_input(
            "Normalized wind speed. The values are divided to 67 (max)", 2
        )
        self._bikes_input.daylight_hours = self._view.write_number_input(
            "Daylight Hours", 2
        )

        self._view.write_text_bottom("Median History Weather Values")
        self._view.write_text_bottom(self._model.get_median_conditions())

        if self._is_ml_calculate:
            self._view.show_prediction(
                "Bikes Count Prediction:",
                f"{self._model.predict_number(self._ml_selection, self._bikes_input)} units"
            )

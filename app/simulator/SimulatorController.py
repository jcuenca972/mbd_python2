from app.GeneralView import GeneralView
from app.simulator.SimulatorModel import SimulatorModel
from app.data_models.BikesInput import BikesInput


class SimulatorController:

    def __init__(self, view: GeneralView, model: SimulatorModel):
        self._view = view
        self._model = model
        self._bikes_input = BikesInput(0, 0, 0, 0, 0, 0, 0,
                                       0.0, 0.0, 0.0, 0.0)

    def show(self, container):
        self._view.init_container(container)
        self._view.write_titles("Simulator", "Fill all the values")
        self._bikes_input.season = self._view.write_selector(
            "Season", 1, "Springer", "Summer", "Fall", "Winter"
        )
        self._bikes_input.day = self._view.write_slider("Day", 1, 31, 1)
        self._bikes_input.hr = self._view.write_slider("Hour", 0, 23, 1)
        self._bikes_input.holiday = self._view.write_selector(
            "Holiday", 0, "No", "Yes"
        )
        self._bikes_input.weekday = self._view.write_selector(
            "Weekday", 0, "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        )
        self._bikes_input.workingday = self._view.write_selector(
            "Workingday", 0, "No", "Yes"
        )
        self._bikes_input.weathersit = self._view.write_selector(
            "Weather Type", 1, "Clear, Few clouds, Partly cloudy, Partly cloudy",
            "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist",
            "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds",
            "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
        )
        self._bikes_input.temp = self._view.write_number_input("Normalized temperature in Celsius. The values are divided to 41 (max)")
        self._bikes_input.hum = self._view.write_number_input("Normalized humidity. The values are divided to 100 (max)")
        self._bikes_input.windspeed = self._view.write_number_input("Normalized wind speed. The values are divided to 67 (max)")
        self._bikes_input.daylight_hours = self._view.write_number_input("Daylight Hours")

        self._view.write_text("Median History Weather Values")
        self._view.write_text(self._model.get_median_conditions(
            self._bikes_input.season, self._bikes_input.weathersit
        ))

        self._view.write_header(
            f"Bikes Count Prediction: {self._model.predict_cnt(self._bikes_input)}"
        )

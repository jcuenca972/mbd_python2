from pycaret.regression import *
from dataclasses import asdict
import pandas as pd
from app.data_models.BikesInput import BikesInput

class SimulatorModel:

    def __init__(self):
        self.models = {
            "General": load_model(model_name="app/data/cnt_model"),
            "Casual": load_model(model_name="app/data/cnt_model_casual"),
            "Registered": load_model(model_name="app/data/cnt_model_registered")
        }
        self._history = pd.read_csv("app/data/daylight_data.csv")

    def bikes_to_df(self, bikes: BikesInput):
        bike_input_dict = asdict(bikes)
        return pd.DataFrame([bike_input_dict])

    def predict_number(self, ml_code, bikes):
        return self._predict(self.models[ml_code], self.bikes_to_df(bikes))

    def _predict(self, model, df):
        prediction = predict_model(model, df)
        prediction["prediction_label"] = prediction["prediction_label"].round().astype(int).apply(lambda x: max(x, 0))
        return prediction["prediction_label"].values.tolist()[0]

    def get_median_conditions(self, season_id, weathersit_id):
        weather_values = ['temp', 'hum', 'windspeed', 'daylight_hours']
        try:
            grouped_df = self._history.groupby(['season', 'weathersit']).median()[weather_values]
            return grouped_df.loc[[(season_id, weathersit_id)]].reset_index()[weather_values]
        except KeyError:
            return pd.DataFrame(columns=weather_values)


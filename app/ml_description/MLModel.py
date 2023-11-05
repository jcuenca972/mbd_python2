import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns

class MLModel:

    def  __init__(self):
        self._bike_data = pd.read_csv("app/data/bike-sharing_hourly.csv")

    def get_missing_values(self):
        missing_values = self._bike_data.isnull().sum()
        missing_values_df = missing_values.reset_index()
        missing_values_df.columns = ['Feature', 'MissingValues']
        missing_values_transposed = missing_values_df.set_index('Feature').T
        missing_values_transposed.reset_index(drop=True, inplace=True)
        missing_values_transposed.index = ['Total']
        return missing_values_transposed

    def get_continuos_variables_analysis(self):
        fig = make_subplots(rows=2, cols=2, subplot_titles=(
        "Boxplot of Temperature", 'Boxplot of "Feels Like" Temperature', 'Boxplot of Humidity',
        "Boxplot of Wind Speed"))
        fig.add_trace(go.Box(y=self._bike_data["temp"], name="Temperature"), row=1, col=1)
        fig.add_trace(go.Box(y=self._bike_data["atemp"], name='"Feels Like" Temperature'), row=1, col=2)
        fig.add_trace(go.Box(y=self._bike_data["hum"], name="Humidity"), row=2, col=1)
        fig.add_trace(go.Box(y=self._bike_data["windspeed"], name="Wind Speed"), row=2, col=2)
        fig.update_layout(height=600, width=800, title_text="Boxplots of Weather Conditions")
        return fig

    def get_correlation(self):
        plt.figure(figsize=(12, 10))
        data_corr = self._bike_data.drop(columns=["instant", "dteday", "casual", "registered", "cnt"])
        corr_matrix = data_corr.corr()
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("")
        return plt.gcf()

    def get_correlation_daylight(self):
        plt.figure(figsize=(12, 10))
        data = pd.read_csv("app/data/daylight_data.csv")
        data_corr = data.drop(columns=["instant", "dteday", "casual", "registered", "cnt"])
        corr_matrix = data_corr.corr()
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("")
        return plt.gcf()

    def get_daylight_code(self):
        return '''
        from astral import LocationInfo
        from astral.sun import sun
        
        def calculate_daylight_hours(date):
            try:
                city = LocationInfo("Washington", "USA", "US/Eastern", 38.9072, -77.0369)
                s = sun(city.observer, date=date)
                daylight_hours = (s["sunset"] - s["sunrise"]).seconds / 3600
                return daylight_hours
            except Exception as e:
                return None

        def daylight_fill_nulls(data_input):
            bike_data_copy = data_input.copy()
            median_daylight_by_season = bike_data_copy.groupby("season")["daylight_hours"].median()
            bike_data_copy["daylight_hours"] = bike_data_copy.apply(
                lambda row: median_daylight_by_season[row["season"]] if pd.isnull(row["daylight_hours"]) else row["daylight_hours"],
                axis=1
            )
            return  bike_data_copy
        '''

    def get_pycaret_info(self):
        return {"Indonesia": "https://ieeexplore.ieee.org/document/10291605",
                "Taiwan": "https://ieeexplore.ieee.org/document/10100285",
                "Tunisia": "https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-022-02092-1"
                }

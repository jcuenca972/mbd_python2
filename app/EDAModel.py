import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

class EDAModel:

    def __init__(self):
        self._bike_data = pd.read_csv("app/data/bike-sharing_hourly.csv")
        self._bike_data.season = self._bike_data.season.apply(self._code_to_season)
        self._bike_data.weathersit = self._bike_data.weathersit.apply(self._code_to_weather)
        self._bike_data.dteday = pd.to_datetime(self._bike_data.dteday)
        self._bike_data.set_index('dteday', inplace=True)

    def rentals_over_time(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self._bike_data.index, y=self._bike_data["cnt"], mode="lines"))
        fig.update_layout(title="Bike Rentals Over Time", xaxis_title="Date", yaxis_title="Total Rentals")
        return fig

    def rentals_by_hour(self):
        fig = px.box(self._bike_data, x="hr", y="cnt")
        fig.update_layout(title="Bike Rentals by Hour of the Day", xaxis_title="Hour of the Day",
                          yaxis_title="Total Rentals")
        return fig

    def rentals_weather(self):
        fig_weather = go.Figure()
        fig_weather.add_trace(go.Box(x=self._bike_data["weathersit"], y=self._bike_data["cnt"]))
        fig_weather.update_layout(title="Bike Rentals by Weather Situation", xaxis_title="Weather Situation",
                                  yaxis_title="Total Rentals")
        return fig_weather

    def rentals_by_season(self):
        fig_season = go.Figure()
        fig_season.add_trace(go.Box(x=self._bike_data["season"], y=self._bike_data["cnt"]))
        fig_season.update_layout(title="Bike Rentals by Season", xaxis_title="Season", yaxis_title="Total Rentals")
        return fig_season

    def rentals_by_hour_weather(self):
        grouped_data = self._bike_data.groupby(['hr', 'weathersit'])['cnt'].sum().reset_index()
        pivot_data = grouped_data.pivot(index='hr', columns='weathersit', values='cnt').fillna(0)
        fig = px.bar(pivot_data,
                     x=pivot_data.index,
                     y=pivot_data.columns,
                     labels={'value': 'Total Rentals'},
                     title="Bike Rentals by Hour and Weather Situation")
        return fig

    def rentals_by_hour_season(self):
        grouped_data = self._bike_data.groupby(['hr', 'season'])['cnt'].sum().reset_index()
        pivot_data = grouped_data.pivot(index='hr', columns='season', values='cnt').fillna(0)
        fig = px.bar(pivot_data,
                     x=pivot_data.index,
                     y=pivot_data.columns,
                     labels={'value': 'Total Rentals'},
                     title="Bike Rentals by Hour and Season")
        return fig

    @classmethod
    def _code_to_season(cls, code):
        if code == 1:
            return "Springer"
        elif code == 2:
            return "Summer"
        elif code == 3:
            return "Fall"
        else:
            return "Winter"

    @classmethod
    def _code_to_weather(cls, code):
        if code == 1:
            return "Clear"
        elif code == 2:
            return "Mist"
        elif code == 3:
            return "Light Snow"
        else:
            return "Heavy Rain"

from dataclasses import dataclass

@dataclass
class BikesInput:
    season: int
    day: int
    hr: int
    holiday: int
    weekday: int
    workingday: int
    weathersit: int
    temp: float
    hum: float
    windspeed: float
    daylight_hours: float

import accuweather
from weather_check import weather_check
# тест на реальных данных
print('тест на реальных данных')
current_response='[{"LocalObservationDateTime":"2024-10-20T21:12:00+03:00","EpochTime":1729447920,"WeatherText":"Clear","WeatherIcon":33,"HasPrecipitation":false,"PrecipitationType":null,"IsDayTime":false,"Temperature":{"Metric":{"Value":7.8,"Unit":"C","UnitType":17},"Imperial":{"Value":46.0,"Unit":"F","UnitType":18}},"RealFeelTemperature":{"Metric":{"Value":8.0,"Unit":"C","UnitType":17,"Phrase":"Chilly"},"Imperial":{"Value":46.0,"Unit":"F","UnitType":18,"Phrase":"Chilly"}},"RealFeelTemperatureShade":{"Metric":{"Value":8.0,"Unit":"C","UnitType":17,"Phrase":"Chilly"},"Imperial":{"Value":46.0,"Unit":"F","UnitType":18,"Phrase":"Chilly"}},"RelativeHumidity":61,"IndoorRelativeHumidity":42,"DewPoint":{"Metric":{"Value":1.1,"Unit":"C","UnitType":17},"Imperial":{"Value":34.0,"Unit":"F","UnitType":18}},"Wind":{"Direction":{"Degrees":293,"Localized":"WNW","English":"WNW"},"Speed":{"Metric":{"Value":5.6,"Unit":"km/h","UnitType":7},"Imperial":{"Value":3.5,"Unit":"mi/h","UnitType":9}}},"WindGust":{"Speed":{"Metric":{"Value":24.1,"Unit":"km/h","UnitType":7},"Imperial":{"Value":15.0,"Unit":"mi/h","UnitType":9}}},"UVIndex":0,"UVIndexText":"Low","Visibility":{"Metric":{"Value":16.1,"Unit":"km","UnitType":6},"Imperial":{"Value":10.0,"Unit":"mi","UnitType":2}},"ObstructionsToVisibility":"","CloudCover":0,"Ceiling":{"Metric":{"Value":12192.0,"Unit":"m","UnitType":5},"Imperial":{"Value":40000.0,"Unit":"ft","UnitType":0}},"Pressure":{"Metric":{"Value":1029.0,"Unit":"mb","UnitType":14},"Imperial":{"Value":30.39,"Unit":"inHg","UnitType":12}},"PressureTendency":{"LocalizedText":"Steady","Code":"S"},"Past24HourTemperatureDeparture":{"Metric":{"Value":2.8,"Unit":"C","UnitType":17},"Imperial":{"Value":5.0,"Unit":"F","UnitType":18}},"ApparentTemperature":{"Metric":{"Value":8.9,"Unit":"C","UnitType":17},"Imperial":{"Value":48.0,"Unit":"F","UnitType":18}},"WindChillTemperature":{"Metric":{"Value":7.2,"Unit":"C","UnitType":17},"Imperial":{"Value":45.0,"Unit":"F","UnitType":18}},"WetBulbTemperature":{"Metric":{"Value":4.8,"Unit":"C","UnitType":17},"Imperial":{"Value":41.0,"Unit":"F","UnitType":18}},"WetBulbGlobeTemperature":{"Metric":{"Value":7.8,"Unit":"C","UnitType":17},"Imperial":{"Value":46.0,"Unit":"F","UnitType":18}},"Precip1hr":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"PrecipitationSummary":{"Precipitation":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"PastHour":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past3Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past6Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past9Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past12Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past18Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}},"Past24Hours":{"Metric":{"Value":0.0,"Unit":"mm","UnitType":3},"Imperial":{"Value":0.0,"Unit":"in","UnitType":1}}},"TemperatureSummary":{"Past6HourRange":{"Minimum":{"Metric":{"Value":7.8,"Unit":"C","UnitType":17},"Imperial":{"Value":46.0,"Unit":"F","UnitType":18}},"Maximum":{"Metric":{"Value":12.2,"Unit":"C","UnitType":17},"Imperial":{"Value":54.0,"Unit":"F","UnitType":18}}},"Past12HourRange":{"Minimum":{"Metric":{"Value":5.0,"Unit":"C","UnitType":17},"Imperial":{"Value":41.0,"Unit":"F","UnitType":18}},"Maximum":{"Metric":{"Value":12.8,"Unit":"C","UnitType":17},"Imperial":{"Value":55.0,"Unit":"F","UnitType":18}}},"Past24HourRange":{"Minimum":{"Metric":{"Value":1.1,"Unit":"C","UnitType":17},"Imperial":{"Value":34.0,"Unit":"F","UnitType":18}},"Maximum":{"Metric":{"Value":12.8,"Unit":"C","UnitType":17},"Imperial":{"Value":55.0,"Unit":"F","UnitType":18}}}},"MobileLink":"http://www.accuweather.com/en/ru/presnensky/594598/current-weather/594598?lang=en-us","Link":"http://www.accuweather.com/en/ru/presnensky/594598/current-weather/594598?lang=en-us"}]'
forecast_response='[{"DateTime":"2024-10-20T22:00:00+03:00","EpochDateTime":1729450800,"WeatherIcon":35,"IconPhrase":"Partly cloudy","HasPrecipitation":false,"IsDaylight":false,"Temperature":{"Value":7.1,"Unit":"C","UnitType":17},"RealFeelTemperature":{"Value":7.1,"Unit":"C","UnitType":17,"Phrase":"Chilly"},"RealFeelTemperatureShade":{"Value":7.1,"Unit":"C","UnitType":17,"Phrase":"Chilly"},"WetBulbTemperature":{"Value":4.8,"Unit":"C","UnitType":17},"WetBulbGlobeTemperature":{"Value":7.1,"Unit":"C","UnitType":17},"DewPoint":{"Value":1.7,"Unit":"C","UnitType":17},"Wind":{"Speed":{"Value":7.4,"Unit":"km/h","UnitType":7},"Direction":{"Degrees":293,"Localized":"WNW","English":"WNW"}},"WindGust":{"Speed":{"Value":24.1,"Unit":"km/h","UnitType":7}},"RelativeHumidity":68,"IndoorRelativeHumidity":43,"Visibility":{"Value":16.1,"Unit":"km","UnitType":6},"Ceiling":{"Value":9144.0,"Unit":"m","UnitType":5},"UVIndex":0,"UVIndexText":"Low","PrecipitationProbability":0,"ThunderstormProbability":0,"RainProbability":0,"SnowProbability":0,"IceProbability":0,"TotalLiquid":{"Value":0.0,"Unit":"mm","UnitType":3},"Rain":{"Value":0.0,"Unit":"mm","UnitType":3},"Snow":{"Value":0.0,"Unit":"cm","UnitType":4},"Ice":{"Value":0.0,"Unit":"mm","UnitType":3},"CloudCover":40,"Evapotranspiration":{"Value":0.0,"Unit":"mm","UnitType":3},"SolarIrradiance":{"Value":0.0,"Unit":"W/m²","UnitType":33},"MobileLink":"http://www.accuweather.com/en/ru/presnensky/594598/hourly-weather-forecast/594598?day=1&hbhhour=22&unit=c&lang=en-us","Link":"http://www.accuweather.com/en/ru/presnensky/594598/hourly-weather-forecast/594598?day=1&hbhhour=22&unit=c&lang=en-us"}]'
ans = accuweather.parse_conditions(current_response, forecast_response)
print(ans)
for mode in ['south', 'central', 'north']:
    print('mode:', mode)
    print(weather_check(ans, 'north'))
# тест на крайних случаях
print('тест на крайних случаях')
cases = [
    {
        'temperature': 100,
        'humidity': 100,
        'wind_speed': 100,
        'precipitation_probability': 100,
    },
    {
        'temperature': -100,
        'humidity': 30,
        'wind_speed': 20,
        'precipitation_probability': 50,
    },
    {
        'temperature': 20,
        'humidity': 30,
        'wind_speed': 20,
        'precipitation_probability': 100,
    },
]
for index, case in enumerate(cases):
    print('case:', index, weather_check(case, 'south'))
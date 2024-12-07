import requests
from requests.auth import HTTPBasicAuth
import json
def get_conditions_by_key(api_key, location_key, lanquage='ru-RU'):
    """
        get_conditions_by_key возвращает основные погодные условия для указанной локации
        api_key: api ключ AccuWeather
        location_key: ключ локации в AccuWeather
        lanquage: язык ответа
        return: dict - {text_conditions, temperature, humidity, wind_speed, precipitation_probability}
    """
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
    data = {
        'apikey': api_key,
        'lanquage': lanquage,
        'details': 'true'
    }
    current_response = requests.get(url, params=data).text
    # прогноз для этого часа, т.к. там вероятность осадков
    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}'
    data = {
        'apikey': api_key,
        'lanquage': lanquage,
        'details': 'true',
        'metric': 'true'
    }

    forecast_response = requests.get(url, params=data).text
    print(parse_conditions(current_response, forecast_response))
    return parse_conditions(current_response, forecast_response)
def parse_conditions(current_response, forecast_response):
    """
        parse_conditions парсит основные погодные условия в dict из ответов api
        current_response: ответ api по текущим состояниям погоды
        forecast_response: ответ api по прогнозу
        return: dict - {text_conditions, temperature, humidity, wind_speed, precipitation_probability}
    """
    current_json_response = json.loads(current_response)[0]
    forecast_json_response = json.loads(forecast_response)[0]
    response = dict()
    response['text_conditions'] = current_json_response['WeatherText']
    response['temperature'] = current_json_response['Temperature']['Metric']['Value']
    response['humidity'] = current_json_response['RelativeHumidity']
    response['wind_speed'] = current_json_response['Wind']['Speed']['Metric']['Value']
    response['precipitation_probability'] = forecast_json_response['PrecipitationProbability']
    return response
def get_location_key_coordinates(api_key, coordinates, lanquage='ru-RU'):
    """
        get_conditions_by_key возвращает основные погодные условия для указанной локации
        api_key: api ключ AccuWeather
        coordinates: координаты в формате кортежа (float, float)
        lanquage: язык ответа
        return: ключ локации (int)
    """
    url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
    data = {
        'apikey': api_key,
        'q': ','.join(list(map(str, list(coordinates)))),
        'lanquage': lanquage
    }
    response = requests.get(url, params=data).text
    json_response = json.loads(response)
    return json_response['Key']
def get_location_key_name(api_key, name, lanquage='ru-RU'):
    """
        get_location_key_name возвращает основные погодные условия для указанной локации
        api_key: api ключ AccuWeather
        name: имя города
        lanquage: язык ответа
        return: ключ локации (int)
    """
    url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    data = {
        'apikey': api_key,
        'q': name,
        'lanquage': lanquage,
        'alias': 'Always'
    }
    try:
        response = requests.get(url, params=data).text
        json_response = json.loads(response)
        return json_response[0]['Key'], json_response[0]['LocalizedName']
    except KeyError:
        raise KeyError('Такого города нет или произошла ошибка на стороне API AccuWeather, проверьте лимит запросов')
    except TypeError:
        raise TypeError('Вероятно, произошла ошибка на стороне API AccuWeather, проверьте лимит запросов')
    except IndexError:
        raise IndexError('Вероятно, произошла ошибка на стороне API AccuWeather, проверьте лимит запросов')

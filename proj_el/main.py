import accuweather
from weather_check import weather_check
from flask import Flask, request, render_template
from markupsafe import Markup
import requests
api_key = '1WB4drBXbvOgiBAmifA7T6gRzLN4mgdn'
app = Flask(__name__)
def weather_formated(weather):
    rus_keys = {
        'text_conditions': '',
        'temperature': '<b>Температура:</b> ',
        'humidity': '<b>Влажность:</b> ',
        'wind_speed': '<b>Скорость ветра (км/ч):</b> ',
        'precipitation_probability': '<b>Вероятность осадков:</b> '
    }
    formatted = ''
    for key in weather:
        formatted += rus_keys[key] + str(weather[key]) + '<br/>'
    return Markup(formatted)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # данные из формы
        start_city = request.form.get("start_city")
        end_city = request.form.get("end_city")
        mode = request.form.get("mode")
        try:
            start_city_code, start_city_name = accuweather.get_location_key_name(api_key, start_city)
            end_city_code, end_city_name = accuweather.get_location_key_name(api_key, end_city)
        except Exception as e:
            return render_template("error.html", error=e)
        # данные погоды для начального и конечного города
        start_weather = accuweather.get_conditions_by_key(api_key, start_city_code)
        end_weather = accuweather.get_conditions_by_key(api_key, end_city_code)
        start_weather_formated = weather_formated(start_weather)
        end_weather_formated = weather_formated(end_weather)
        weather_states = {
            True: 'Отличная погода, обязательно прогуляйся на свежем воздухе!',
            False: 'Погода не очень подходит для прогулок, выбирай активности в помещениях :(',
        }
        # оценка погодных условия
        start_weather_evaluation, start_weather_reasons = weather_check(start_weather, mode)
        end_weather_evaluation, end_weather_reasons = weather_check(end_weather, mode)
        start_reasons_formatted = ''
        end_reasons_formatted = ''
        rus_keys = {
            'temperature': 'температура',
            'humidity': 'влажность',
            'wind_speed': 'скорость ветра',
            'precipitation_probability': 'вероятность осадков'
        }
        if len(start_weather_reasons) > 0:
            start_reasons_formatted = ('Следующие факторы не соответсвуют Вашим предпочтениям: ' +
                                       ', '.join(map(lambda x: rus_keys[x], start_weather_reasons)))
        if len(end_weather_reasons) > 0:
            end_reasons_formatted = ('Следующие факторы не соответсвуют Вашим предпочтениям: ' +
                                     ', '.join(map(lambda x: rus_keys[x], end_weather_reasons)))
        # результаты в шаблон для отображения
        return render_template("result.html", start_city=start_city_name, end_city=end_city_name,
                               start_weather=Markup(weather_states[start_weather_evaluation] + '<br/>' +  start_reasons_formatted),
                               end_weather=Markup(weather_states[end_weather_evaluation] + '<br/>' + end_reasons_formatted),
                               start_weather_list=start_weather_formated, end_weather_list=end_weather_formated)
    return render_template("index.html")
@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run()
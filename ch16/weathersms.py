#! python3
# -*- coding: utf-8 -*-

# 演習プロジェクト 16.9.2
# OpenWeatherMap.org から天気情報を取得し、雨ならSMSで通知する。

import json, requests
import textmyself

LOCATION = 'Sapporo' # 場所を設定してください
APPID='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # openweathermap のAPIキーを設定してください

# 天気のデータを取得する
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(LOCATION, APPID)
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)
w = weather_data['list']
weather = w[0]['weather'][0]['main']
print(weather)

if weather == 'Rain':
    textmyself.textmyself('今日は雨です。')


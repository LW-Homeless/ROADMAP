import json

import requests

from model.RedisWeather import RedisWeather


class WeatherAPI:

    def __init__(self, location):
        self.__request = ''
        self.__response = ''
        self.__location = location
        self.__api_key = 'R7S6QFU58FRHR32H8DYXVDDWK'

        self.__redis_obj = RedisWeather()

    def query_weather(self):
        # Check if server redis is running
        if self.__redis_obj.server_state():

            # Run the query to server redis
            self.__response = self.__query_redis_cache()

            # Check if the server redis return data or Error
            # If the server returns data convert to json format
            if type(self.__response) is bytes:
                self.__response = json.loads(self.__response)

            # Check if the server redis return an error
            # If the server redis not return error, return data
            if 'Error' not in self.__response:
                return self.__response

            # If the server redis return an error, the Weather API is consulted.
            elif 'Error' in self.__response:
                self.__response = self.__querey_weather_api()

                # If Weather API not return an error
                # Check the status redis server, if redis server up, to save data in redis server else
                # return data from query Weather API
                if 'Error' not in self.__response:
                    if self.__redis_obj.server_state():
                        for day in self.__response['days']:
                            day['resolvedAddress'] = self.__response['resolvedAddress']
                        self.__redis_obj.set_redis(self.__location, self.__response['days'])
                        self.__redis_obj.close_connection()
                        return self.__response['days']
                    else:
                        return self.__response['days']
                else:
                    return self.__response
        else:
            self.__response = self.__querey_weather_api()

            # If Weather API not return an error
            # Check the status redis server, if redis server up, to save data in redis server else
            # return data from query Weather API
            if 'Error' not in self.__response:
                if self.__redis_obj.server_state():
                    for day in self.__response['days']:
                        day['resolvedAddress'] = self.__response['resolvedAddress']

                    self.__redis_obj.set_redis(self.__location, self.__response['days'])
                    self.__redis_obj.close_connection()
                    return self.__response['days']
                else:
                    for day in self.__response['days']:
                        day['resolvedAddress'] = self.__response['resolvedAddress']
                    return self.__response['days']
            else:
                return self.__response

    def __query_redis_cache(self):

        if self.__redis_obj.server_state():
            self.__response = self.__redis_obj.get_redis(self.__location)

            if self.__response is not None:
                return self.__response
            else:
                return {'Error': 'redis cache empty'}

    def __status_redis_server(self):
        return self.__redis_obj.server_state()

    def __querey_weather_api(self):
        self.__request = ("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}?"
                          "unitGroup=us&include=days&key={}&contentType=json"
                          .format(self.__location, self.__api_key))
        try:
            self.__response = requests.get(self.__request)

            if self.__response.status_code == 200:
                return self.__response.json()
            else:
                return {'Error': 'HTTP Error', 'Error_n': self.__response.status_code}
        except requests.exceptions.ConnectionError:
            return {'Error': 'Connections Error', 'Error_n': 11001}


'''w = WeatherAPI('chile')

query = w.query_weather()

if 'Error' in query:
    if query['Error_n'] > 200:
        print('Error HTTP')
    elif query['Error_n'] == 11001:
        print('Error: de conexion API')
else:
    print(query)'''

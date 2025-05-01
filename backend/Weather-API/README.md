Solution for the [Weather API](https://roadmap.sh/projects/weather-api-wrapper-service) challenge from [roadmap.sh](https://roadmap.sh)

## Weather API
In this project, instead of relying on our own weather data, we will build a weather API that fetches and returns weather data from a 3rd party API.  

## Solution

In this project we will use [Visual Crossing's API](https://www.visualcrossing.com/weather-api/) to obtain weather data It's completely free and easy to use.
To keep the data in cache we will use [Redis](https://redis.io/).  

In order to use the Visual Crossing's API, you should create an [account](https://www.visualcrossing.com/sign-up/)  
Once you have already registered, the app Visual Crossing will assign a API key.

The program flow will be as follows:

![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Weather-API/IMG/diagram.png)

## Requirement
Python 3.11.3  
## Dependencies
certifi==2025.1.31  
charset-normalizer==3.4.1  
idna==3.10  
numpy==2.2.4  
pandas==2.2.3  
prompt_toolkit==3.0.51  
python-dateutil==2.9.0.post0  
pytz==2025.2  
redis==5.2.1  
requests==2.32.3  
six==1.17.0  
tabulate==0.9.0  
tzdata==2025.2  
urllib3==2.4.0  
wcwidth==0.2.13
## How to use
* Install the dependencies with the following command  
```
pip install -r requirements.txt
```

* Modify the file WeatherAPI.py and type your API key in the property:
```
self.__api_key = 'Type your api key'
```
* Finally, run the Main.py file following way:
```
python Main.py
```
## Demo video
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Weather-API/IMG/weather-api.gif)

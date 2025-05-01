Solución para el desafío [Weather API](https://roadmap.sh/projects/weather-api-wrapper-service) de [roadmap.sh](https://roadmap.sh)  

## Weather API
En este proyecto, en lugar de confiar en nuestros propios datos meteorológicos, crearemos una API meteorológica que obtenga y devuelva datos meteorológicos de una API de terceros.
## Solución
En este projecto utilizaremos [Visual Crossing's API](https://www.visualcrossing.com/weather-api/) para obtener datos meteorológicos es completamente gratis y fácil de usar.
Para mantener los datos en caché utilizaremos [Redis](https://redis.io/).  

Para utilizar la API de Visual Crossing, tú debes crear una cuenta, luego Visual Crossing te asignará tú clave de API.  

El flujo del programa será el siguiente:
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Weather-API/IMG/diagram.png)
## Requisitos
Python 3.11.3
## Dependencias
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
## Instrucciones de uso
* Instale las dependencias con el siguiente comando.  
```
pip install -r requirements.txt
```
* Modifica el archivo WeatherAPI.py e introduce tu clave API en la propiedad.
```
self.__api_key = 'Type your api key'
```
* Por último, ejecute el archivo Main.py de la siguiente manera:
```
python Main.py
```
## Video demostración
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Weather-API/IMG/weather-api.gif)

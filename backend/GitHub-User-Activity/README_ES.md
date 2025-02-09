Solución de muestra para el desafío [GitHub-User-Activity](https://roadmap.sh/projects/github-user-activity) de [roadmap.sh](https://roadmap.sh)

# GitHub User Activity
En este proyecto, creará una interfaz de línea de comandos (CLI) simple para obtener la actividad reciente de un usuario de GitHub y mostrarla en la terminal. Este proyecto lo ayudará a practicar sus habilidades de programación, incluido el trabajo con API, el manejo de datos JSON y la creación de una aplicación CLI simple.

# Requisitos
La aplicación debe ejecutarse desde la línea de comandos, aceptar el nombre de usuario de GitHub como argumento, obtener la actividad reciente del usuario mediante la API de GitHub y mostrarla en la terminal. El usuario debe poder:

- Proporcionar el nombre de usuario de GitHub como argumento al ejecutar la CLI.
`python github-activity <username>`

- Obtener la actividad reciente del usuario de GitHub especificado mediante la API de GitHub. Puede utilizar el siguiente endpoint para obtener la actividad del usuario:
https://api.github.com/users/ **username** /events
Ejemplo: https://api.github.com/users/ **LW-Homeless** /events

# Solución
- Lenguaje de programación: Python 3.11.3.
- Tipo de programación: Programación orientado a objetos (POO).
- Patrón de diseño: Patrón de diseño de comportamiento command.

El patrón de diseño Command tiene la siguiente estructura.
![image](https://github.com/LW-Homeless/roadmap/blob/main/backend/task-tracker/structure.png) 

# Cómo utilizar
Instale los módulos Pandas, colorama y tabutate con el siguiente comando:
pip install tabulate
pip install pandas
pip install colorama
pip install requests

Por último, ejecute el siguiente comando:
`python github-activity.py username`

![video](https://github.com/LW-Homeless/roadmap/blob/main/backend/GitHub-User-Activity/video.gif)

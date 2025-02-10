Solución de muestra para el desafío [Github-user-activity](https://roadmap.sh/projects/github-user-activity) de [roadmap.sh](https://roadmap.sh)

#GitHub User Activity
En este proyecto, creará una interfaz de línea de comandos (CLI) simple para obtener la actividad reciente de un usuario de GitHub.

#Requerimientos
La aplicación debe ejecutarse desde la línea de comandos, aceptar el nombre de usuario de GitHub como argumento, obtener la actividad reciente del usuario mediante la API de GitHub y mostrarla en la terminal. El usuario debe poder:

- Proporcionar el nombre de usuario de GitHub como argumento al ejecutar la CLI.
`github-activity <username>`

- Obtener la actividad reciente del usuario de GitHub especificado mediante la API de GitHub. Puede utilizar el siguiente punto de conexión para obtener la actividad del usuario:
`https://api.github.com/users/<username>/events`
`Ejemplo: https://api.github.com/users/kamranahmedse/events`

- Mostrar la actividad obtenida en la terminal.

	**Output:**
	*Pushed 3 commits to kamranahmedse/developer-roadmap
	Opened a new issue in kamranahmedse/developer-roadmap
	Starred kamranahmedse/developer-roadmap*
	...

#Solución
Lenguaje de programación: Python 3.11.3
Tipo de programación: Programación orientada a objetos (POO)
Patrón de diseño: Patrón de diseño de comportamiento **Command**

El patrón de diseño Command tiene la siguiente estructura.

Imagen

#Cómo usar
`python github-activity <username>`

video
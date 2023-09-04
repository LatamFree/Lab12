# Principios de diseño SOLID

En este laboratorio veremos la forma idiomática de crear funciones en Python y las convenciones usualmente utilizadas.

Iremos realizando soluciones incrementales que nos llevarán a entender el conceptos de funciones, como son manejadas por Python y que podemos hacer con ello .

**Recuerda no modificar los tests**, sólo puedes modificar los archivos de la carpeta `src`

## Inicializa el proyecto

Una vez clonado este proyecto y habiendo navegado a la carpeta, ejecutar:

```
pipenv install --dev
```

**Recuerda usar version python 3.10.x**
Utiliza `pyenv` en caso no tengas disponible la version indicada.

## Actividad 1: Recapitulación Conceptos Python

### Interfaces/Clases Abstractas

Repasaremos el concepto de Interfaces en programación orientada a objetos entendiendo como se implementa en Python y en que consiste esta idea.

Corre el siguiente comando y revisaremos como dejar pasando estas pruebas:

`pipenv run pytest -f tests/recap`


## Actividad 2: SOLID

Los 5 principios de diseño que conoceremos:

- **S**ingle responsability
- **O**pen Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion 

Corre el siguiente comando y revisaremos como dejar pasando estas pruebas:

`pipenv run pytest -f tests/solid`

¡Éxito!

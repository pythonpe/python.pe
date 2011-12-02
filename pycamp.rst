PyCamp Diciembre 2011
=====================

¿Cúando y Dónde?
----------------

* 17 de Diciembre, 2011.
* De 03:00pm a 8:00pm.
* Cámara de Comercio de Lima.
  Av. Giuseppe Garibaldi Nº 396 (ex Gregorio Escobedo), Jesús María

Objetivos
---------

El primer PyCamp tiene como objetivo integrar a los actuales miembros de
la Comunidad y compartir un momento de code sprint mediante la realización
de pequeños módulos en mini proyectos de diferentes tipos como son:

* Proyecto Web Básico utilizando Python.
* Pequeños Scripts útiles en Python.
* Mejorar el site de python.pe ese mismo día.
* Proyecto Blender Game con Python.

¿Qué es un PyCamp?
------------------

PyCamp es un evento organizado por la comunidad de python en el que nos
reunimos un grupo de programadores, no importa si eres novato o experto,
la idea es compatir, aprender y hacer lo que más nos gusta: **programar**.

¿Qué llevar?
------------

* Laptop con el Sistema Operativo que te sientas comodo.
* Ambiente virtual para programar.
* Muchas ganas de programar.


¿Qué es Ambiente virtual?
-------------------------

Es un entorno donde tienes una instalación de python y todas las librerias
que necesitas o deseas probar, sin que afecte la instalación base de tu
sistema operativo. Si usas windows, debes instalar primero python.

Para crear tu ambiente virtual, debes seguir estos pasos::

    $ sudo pip install virtualenv mercurial sphinx
    $ virtualenv --no-site-packages --distribute pycamp
    $ source ./pycamp/bin/activate
    (pycamp)$ echo $VIRTUAL_ENV

Para instalar librerias adicionales solo debes seguir usando pip install
y el nombre de la libreria que deseas::

    pip install django

# Página de Python Perú #

Todos son bienvenidos a contribuir con la página.

### ¿Cómo puedo contribuir con la página? ###

El proyecto está alojado en https://bitbucket.org/pythonpe/python.pe, empieza clonando el proyecto y cuando termines tus modificaciones no olvides hacer un pull request.

Si no has trabajado antes con mercurial, te recomendamos que le des un vistazo a http://hginit.com, si te quedan dudas pregunta en la lista de correo.

Los pasos para contribuir por primera vez son:

* Instalar Sphinx: pip install Sphinx
* Forkear el repo: open https://bitbucket.org/pythonpe/python.pe/fork
* Clonar el source: hg clone https://$U...@bitbucket.org/$USER/python.pe
* Entrar al directorio: cd python.pe
* Mejorar el contenido
* Generar el sitio localmente: make html
* Probar los cambios en un browser: open _build/html/index.html
* Hacer commit de los cambios: hg commit
* Hacer push a bitbucket: hg push
* Mandar un pull request: open https://bitbucket.org/$USER/python.pe/pull-request/new

Los commandos para actualizar el fork local son:

* hg pull https://bitbucket.org/pythonpe/python.pe
* hg up

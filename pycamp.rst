.. raw:: html

    <div class="page-header">
        <h1>PyCamp 2011</h1>
    </div><!-- /row -->
    <div class="row">
        <div class="span-one-third">
            <a href="/"><img class="thumbnail"  src="_static/images/python-3.jpg" width="250" height="200" /></a>
        </div>
        <div class="span-one-third">
         <h3>¿Cúando?</h3>
         <ul>
            <li>17 de Diciembre, 2011.</li>
            <li>De 09:00am a 6:00pm.</li>
          </ul>
        </div>

        <div class="span-one-third">
         <h3>Objetivos</h3>
         <p>El 1°PyCamp tiene como objetivo integrar a los actuales miembros de la Comunidad y compartir un momento de code sprint mediante la realización de pequeños módulos en mini proyectos de diferentes tipos como son:</p>
         <ul>
            <li>Realización de un Proyecto Web Básico utilizando Python.</li>
            <li>Realización de Pequeños Scripts útiles en Python.</li>
            <li>Contribuir con mejorar el site de python.pe ese mismo día.</li>
            <li>Proyecto Blender Game con Python.</li>
          </ul>
        </div>

    </div>      


    <div class="page-header">
      <br>
    </div><!-- /row -->

    <div class="row">
        <div class="span12 columns">
          <h1>¿Qué es un PyCamp?</h1>
          <p>PyCamp es un evento organizado por la comunidad de python en el que nos reunimos un grupo de programadores, no importa si eres novato o experto, la idea es compatir, aprender y hacer lo que más nos gusta: <strong>codear</strong>.
          </p>  
        </div>
    </div>
    

    <div class="row">
        <div class="span12 columns">
          <h1>¿Qué llevar?</h1>
          <ul>
               <li>Laptop con el Sistema Operativo que te sientas comodo.</li>
               <li>Ambiente virtual para programar.</li>
               <li>Muchas ganas de codear.</li>
          </ul>  
        </div>
    </div>
    
    <div class="row">
        <div class="span12 columns">
          <h1>¿Qué es Ambiente virtual?</h1>
      
          <p> Es un entorno donde tienes una instalación de python y todas las librerias que necesitas o deseas probar, sin que afecte la instalación base de tu sistema operativo. Si usas windows, debes instalar primero python.<br><br>

          Para crear tu ambiente virtual, debes seguir estos pasos:
          </p>

          <pre class="prettyprint linenums"> 
            $ sudo aptitude install python-virtualenv
            $ mkdir pycamp
            $ cd pycamp
            $ virtualenv --no-site-packages env
            $ source ./env/bin/activate
            (pycamp)$ pip install mercurial
            (pycamp)$ pip install sphinx</pre>

          <p> Para instalar librerias adicionales solo debes seguir usando <strong>pip install</strong> y el nombre de la libreria que deseas.
          </p>

          <pre class="prettyprint linenums"> 
            (pycamp)$ pip install django</pre>

        </div>
    </div>

    </div><!-- /row -->


    

 



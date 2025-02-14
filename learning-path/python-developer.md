# Desarrollador Python

En esta sección, ofrecemos una selección de recursos esenciales para desarrolladores de Python de todos los niveles. Desde tutoriales básicos hasta avanzados, documentación oficial, libros clave, blogs y videos, todo diseñado para fortalecer tu desarrollo en Python. Para principiantes, sugerimos comenzar con fundamentos del lenguaje, avanzando gradualmente hacia temas más complejos como programación orientada a objetos y arquitectura de software. 

Para los más experimentados, presentamos recursos avanzados que incluyen libros especializados, blogs de expertos, y tutoriales que desafían tus habilidades, manteniéndote al día con las últimas tendencias y prácticas en Python. Estos recursos están pensados para ayudarte a perfeccionar tus habilidades y convertirte en un desarrollador de Python más competente y versátil.

**Leyenda:**

📗: Libro

📹: Video tutorial

🎓: Curso

🧑‍💻: Código práctico

📝: Blog post

Los nombres con asterisco al final (*) son con contenido en inglés.


## Python Básico

### Fundamentos básicos de Python:

Estos recursos te ayudaran si realmente no tienes ninguna noción de cómo programar con Python, los tres primeros links son cursos que puedes ver, leer, o llevar mientras que 30 days of Python son una serie de pequeños ejercicios que puedes hacer uno al día y puedes ir aprendiendo con cada ejercicio completado.

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=LR;
  
  subgraph cluster_basic_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;

    f4 [
      label="🧑‍💻 30 days of Python*",
      href="https://github.com/Asabeneh/30-Days-Of-Python?tab=readme-ov-file",
      color="lightgreen",
      target="_top"];
    f3 [
      label="🎓 Python para principiantes \n (Microsoft)",
      href="https://learn.microsoft.com/es-es/training/paths/beginner-python/",
      color="lightgreen",
      target="_top"];
    f2 [
      label="📗 Curso intensivo de python",
      href="https://anayamultimedia.es/libro/titulos-especiales/curso-intensivo-de-python-2a-edicion-eric-matthes-9788441543348/",
      color="lightgreen",
      target="_top"];
    f1 [
      label="📹 Curso de Python 3\n para verdaderos principiantes",
      href="https://www.youtube.com/watch?v=aQvfEuEHKkA&list=PLIeA88IfaMLvPMwAjMlxfb5GtOfkggyvu",
      color="lightgreen",
      target="_top"];

    fundamentals [label="Fundamentos\nBásicos de Python"];
    fundamentals -> f4;
    fundamentals -> f3;
    fundamentals -> f2;
    fundamentals -> f1;
  }
}
```

### Estructura de datos y algoritmos básicos:

Aquí encontrarás recursos para aprender sobre las estructuras de datos más comunes (listas, pilas, colas, árboles, grafos, etc.) y los algoritmos básicos (búsqueda, ordenamiento, recursión, etc.) que son fundamentales para resolver problemas de programación.

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=RL;
  
  subgraph cluster_basic_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;

    as4 [
      label="🧑‍💻 How to Do a Binary Search in Python*",
      href="https://realpython.com/binary-search-python/",
      color="lightgreen",
      target="_top"];
    as3 [
      label="🧑‍💻 30 days of Python*",
      href="https://github.com/Asabeneh/30-Days-Of-Python?tab=readme-ov-file",
      color="lightgreen",
      target="_top"];
    as2 [
      label="📗 Data Structures & Algorithms \nin Python*",
      href="https://www.amazon.com/Structures-Algorithms-Python-Robert-Lafore/dp/013485568X/",
      color="lightgreen",
      target="_top"];
    as1 [
      label="📝 Estructuras de datos: \nUna guía completa con ejemplos en Python",
      href="https://www.datacamp.com/es/tutorial/data-structures-guide-python",
      color="lightgreen",
      target="_top"];

    algostruct [label="Estructura de Datos\ny\nAlgoritmos Básicos"];
    algostruct -> as4;
    algostruct -> as3;
    algostruct -> as2;
    algostruct -> as1;
  }
}
```

### Clean code:

En esta sección se proporcionarán guías y mejores prácticas para escribir código limpio y mantenible. Aprenderás sobre la importancia de los nombres significativos, la organización del código, la eliminación de duplicaciones y la simplicidad.

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=LR;
  
  subgraph cluster_basic_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;


    cc2 [
      label="📝 Clean Code in Python*",
      href="https://testdriven.io/blog/clean-code-python/",
      color="lightgreen",
      target="_top"];
    cc1 [
      label="📝 Guía en Español: Clean Code Python",
      href="https://github.com/sryvcr/clean-code-python-es",
      color="lightgreen",
      target="_top"];

    clean_code [label="Clean Code"];
    clean_code -> cc2;
    clean_code -> cc1;
  }
}
```

### Proyectos básicos

Esta sección incluirá ideas y ejemplos de proyectos básicos que puedes realizar para practicar tus habilidades de programación en Python. Los proyectos pueden incluir desde simples scripts de automatización hasta pequeñas aplicaciones web o juegos.

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=RL;
  
  subgraph cluster_basic_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;


    bp3 [
      label="📹 6 Proyectos de Python Básicos\nCurso Completo Paso a Paso", 
      href="https://www.youtube.com/watch?v=tWnyBD2src0",
      color="lightgreen", 
      target="_top"];
    bp2 [
      label="📝 Estructura del proyecto\npara una aplicación Python",
      href="https://www.delftstack.com/es/howto/python/python-project-structure/",
      color="lightgreen",
      target="_top"];
    bp1 [
      label="📝 25 Proyectos en Python\npara principiantes:\nIdeas para comenzar\na programar en Python",
      href="https://www.freecodecamp.org/espanol/news/25-proyectos-en-python-para-principiantes/",
      color="lightgreen",
      target="_top"];

    basic_projects [label="Proyectos\nBásicos"];
    basic_projects-> bp3;
    basic_projects-> bp2;
    basic_projects-> bp1;
  }
}
```

## Python Avanzado

### Estructura de datos y algoritmos avanzados
Estos recursos proporcionan más detalle sobre estructura de datos y algoritmos, la mayoria de estos recursos se encuentran en inglés.

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=LR;
  
  subgraph cluster_basic_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;


    cc4 [
      label="‍💻 Advanced Data Structures \nwith Python*",
      href="https://github.com/bhavinjawade/Advanced-Data-Structures-with-Python",
      color="lightgreen",
      target="_top"];
    cc3 [
      label="📝 Basic Data Structures*",
      href="https://runestone.academy/ns/books/published/pythonds3/BasicDS/toctree.html",
      color="lightgreen",
      target="_top"];
    cc2 [
      label="📗 Grokking Algoritms*",
      href="https://www.manning.com/books/grokking-algorithms",
      color="lightgreen",
      target="_top"];
    cc1 [
      label="🎓 Algoritmos avanzados con Python",
      href="https://www.pypro.mx/app/curso/algoritmos-avanzados-con-python",
      color="lightgreen",
      target="_top"];

    clean_code [label="Estructura de datos \ny algoritmos avanzados"];
    clean_code -> cc4;
    clean_code -> cc3;
    clean_code -> cc2;
    clean_code -> cc1;
  }
}
```

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];
  rankdir=LR;

  bgcolor=transparent;
  subgraph cluster_advanced_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightblue;
    fontsize = 20;
    
    lc3 [label="Tópico 18", href="", color="lightgreen", target="_top"];
    lc2 [label="Tópico 17", href="", color="lightgreen", target="_top"];
    lc1 [label="Tópico 16", href="", color="lightgreen", target="_top"];
    db3 [label="Tópico 15", href="", color="lightgreen", target="_top"];
    db2 [label="Tópico 14", href="", color="lightgreen", target="_top"];
    db1 [label="Tópico 13", href="", color="lightgreen", target="_top"];
    pp3 [label="Tópico 12", href="", color="lightgreen", target="_top"];
    pp2 [label="Tópico 11", href="", color="lightgreen", target="_top"];
    pp1 [label="Tópico 10", href="", color="lightgreen", target="_top"];
    cl3 [label="Tópico 9", href="", color="lightgreen", target="_top"];
    cl2 [label="Tópico 8", href="", color="lightgreen", target="_top"];
    cl1 [label="Tópico 7", href="", color="lightgreen", target="_top"];
    dp3 [label="Tópico 6", href="", color="lightgreen", target="_top"];
    dp2 [label="Tópico 5", href="", color="lightgreen", target="_top"];
    dp1 [label="Tópico 4", href="", color="lightgreen", target="_top"];
    design_patterns [label="Patrones de Diseño\nen Python"];
    command_line [label="Línea de Comandos\nen Python"];
    python_projects [label="Proyectos en Python"];
    db [label="Bases de Datos"];
    leetcode [label="Leetcode"];
    design_patterns -> dp3;
    design_patterns -> dp2;
    design_patterns -> dp1;
    command_line -> cl3;
    command_line -> cl2;
    command_line -> cl1;
    python_projects -> pp3;
    python_projects -> pp2;
    python_projects -> pp1;
    db -> db3;
    db -> db2;
    db -> db1;
    leetcode -> lc3;
    leetcode -> lc2;
    leetcode -> lc1;
  }
}
```

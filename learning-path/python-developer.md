# Desarrollador Python

En esta sección encontrarás una cuidadosa selección de recursos recomendados
para desarrolladores de Python, desde aquellos que se inician en el aprendizaje
de este lenguaje hasta los más experimentados que buscan profundizar sus
habilidades y conocimientos. Aquí podrás encontrar enlaces a documentación
oficial, tutoriales interactivos, libros imprescindibles, posts de blogs
relevantes y videos tutoriales informativos y prácticos, todos pensados
exclusivamente para potenciar tu desarrollo como un verdadero "Pythonista".

Para los principiantes en Python, recomendamos comenzar por los recursos
destinados a establecer una base sólida en el lenguaje, como tutoriales
introductorios, ejercicios prácticos y documentación oficial detallada. A medida
que avances, podrás adentrarte en temas más avanzados, como programación
orientada a objetos, clean code, arquitectura de software, entre otros.

Para los desarrolladores de Python más experimentados, te proporcionamos una
lista de recursos refinados y actualizados que te ayudarán a perfeccionar tus
habilidades y mantenerte al tanto de las últimas tendencias y buenas prácticas
en el mundo de la programación con Python. Encontrarás libros especializados,
blogs de expertos en Python, videos de conferencias y tutoriales avanzados que
te desafiarán a llevar tus habilidades al siguiente nivel. Con estos recursos a
tu disposición, podrás convertirte en un Pythonista aún más competente y
versátil en tu campo. ¡Explora y aprende para crecer como desarrollador de
Python!


## Python Básico

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

    t12 [label="Tópico 12", href=""];
    t11 [label="Tópico 11", href=""];
    t10 [label="Tópico 10", href=""];
    t9 [label="Tópico 9", href=""];
    t8 [label="Tópico 8", href=""];
    t7 [label="Tópico 7", href=""];
    t6 [label="Tópico 6", href=""];
    t5 [label="Tópico 5", href=""];
    t4 [label="Tópico 4", href=""];
    t3 [label="Tópico 3", href=""];
    t2 [label="Tópico 2", href=""];
    t1 [label="Tópico 1", href=""];
    basic_python [id="basic-python", label="Python Básico"];
    algostruct [label="Estructura de Datos\ny\nAlgoritmos Básicos"];
    basic_arch [label="Arquitectura\nBásica"];
    clean_code [label="Clean Code"];
    fundamentals [label="Fundamentos\nBásicos de Python"];
    basic_python -> algostruct;
    basic_python -> basic_arch;
    basic_python -> clean_code;
    basic_python -> fundamentals;
    fundamentals -> t3;
    fundamentals -> t2;
    fundamentals -> t1;
    clean_code -> t6;
    clean_code -> t5;
    clean_code -> t4;
    basic_arch -> t9;
    basic_arch -> t8;
    basic_arch -> t7;
    algostruct -> t12;
    algostruct -> t11;
    algostruct -> t10;
  }
}
```


## Python Avanzado

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
    
    t18 [label="Tópico 18", href=""];
    t17 [label="Tópico 17", href=""];
    t16 [label="Tópico 16", href=""];
    t15 [label="Tópico 15", href=""];
    t14 [label="Tópico 14", href=""];
    t13 [label="Tópico 13", href=""];
    t12 [label="Tópico 12", href=""];
    t11 [label="Tópico 11", href=""];
    t10 [label="Tópico 10", href=""];
    t9 [label="Tópico 9", href=""];
    t8 [label="Tópico 8", href=""];
    t7 [label="Tópico 7", href=""];
    t6 [label="Tópico 6", href=""];
    t5 [label="Tópico 5", href=""];
    t4 [label="Tópico 4", href=""];
    t3 [label="Tópico 3", href=""];
    t2 [label="Tópico 1", href=""];
    t1 [label="Tópico 1", href=""];
    advanced_python [id="advanced-python", label="Python Avanzado"];
    leetcode [label="Leetcode"];
    db [label="Bases de Datos"];
    python_projects [label="Proyectos en Python"];
    command_line [label="Línea de Comandos\nen Python"];
    design_patterns [label="Patrones de Diseño\nen Python"];
    advanced_algostruct [label="Estructurad de Datos\ny\nAlgoritmos Avanzados"];
    advanced_python -> leetcode;
    advanced_python -> db;
    advanced_python -> python_projects;
    advanced_python -> command_line;
    advanced_python -> design_patterns;
    advanced_python -> advanced_algostruct;
    advanced_algostruct -> t3;
    advanced_algostruct -> t2;
    advanced_algostruct -> t1;
    design_patterns -> t6;
    design_patterns -> t5;
    design_patterns -> t4;
    command_line -> t9;
    command_line -> t8;
    command_line -> t7;
    python_projects -> t12;
    python_projects -> t11;
    python_projects -> t10;
    db -> t15;
    db -> t14;
    db -> t13;
    leetcode -> t18;
    leetcode -> t17;
    leetcode -> t16;
  }
}
```

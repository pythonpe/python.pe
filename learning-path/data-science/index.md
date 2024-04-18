# Ciencias de Datos

En esta sección, hemos recopilado una lista de recursos cuidadosamente
seleccionados para impulsar las habilidades de los Pythonistas interesados en el
mundo de la Ciencia de Datos. Ya sea que estés dando tus primeros pasos en este
campo apasionante o que ya seas un experto en la materia, encontrarás enlaces a
herramientas especializadas, libros fundamentales, blogs relevantes y videos
instructivos que te ayudarán a dominar Python para la Ciencia de Datos.

Para aquellos que están comenzando en la Ciencia de Datos con Python, te
recomendamos explorar recursos que te introduzcan en las bibliotecas clave como
NumPy, Pandas, Matplotlib y Scikit-Learn, así como tutoriales que te guíen a
través de la manipulación de datos, visualización y análisis estadístico con
Python. Estos recursos te proporcionarán una base sólida para comprender y
trabajar eficazmente con datos utilizando Python.

Para los Pythonistas con experiencia en Ciencia de Datos, te ofrecemos recursos
avanzados como libros especializados en análisis predictivo, blogs que
profundizan en conceptos avanzados de Ciencia de Datos aplicados con Python,
videos sobre técnicas de modelado y visualización de datos avanzados, y
tutoriales que te desafiarán a resolver problemas complejos y a explorar nuevas
áreas de aplicación de Python en la Ciencia de Datos. Con estos recursos, podrás
expandir tus habilidades, mantenerte actualizado con las últimas tecnologías en
Ciencia de Datos y avanzar en tu carrera como un Pythonista experto en este
emocionante campo. ¡Explora, aprende y conviértete en un maestro en la Ciencia
de Datos con Python!

```{sketchviz}
---
static-subdir: images/sketchviz
---
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];

  bgcolor=transparent;
  
  dc_1 [
    label="Ciencias de Datos Básico",
    href="/learning-path/data-science/basic-data-science/", 
    target="_top"
  ]
  dc_2 [
    label="Ciencias de Datos Avanzado",
    href="/learning-path/data-science/advanced-data-science/", 
    target="_top"
  ]

  subgraph cluster_science {
    style=filled;
    color=lightgrey;
    node [style=filled, color=pink];
    dc_1 -> dc_2;
    label = "*Ciencias de Datos*";
    fontsize = 20;
    color=lightblue;
    href="/learning-path/data-science/";
    target="_top";
  }
}
```

```{toctree}
:hidden: true

basic-data-science.md
advanced-data-science.md
```

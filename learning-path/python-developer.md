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

```{sketchviz}
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];

  bgcolor=transparent;
  
  p_1 [
    label="Python Básico",
    href="/learning-path/python-developer/#python-basico", 
    target="_top"
  ]
  p_2 [
    label="Python Avanzado",
    href="/learning-path/python-developer/#python-avanzado", 
    target="_top"
  ]

  subgraph cluster_python {
    node [style=filled, color=pink];
    style=filled;
    color=lightgrey;
    fontsize = 20;
    label = "*Desarrollador Python*";
    href="/learning-path/python-developer/";
    target="_top";
    p_1 -> p_2;
  }
}
```

## Python Básico


## Python Avanzado

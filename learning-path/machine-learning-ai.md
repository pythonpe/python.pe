# Machine Learning e IA

En esta sección, hemos recopilado una cuidadosa selección de recursos para
potenciar las habilidades de los Pythonistas interesados en el campo del Machine
Learning e Inteligencia Artificial. Tanto si estás comenzando en este
apasionante campo como si ya tienes experiencia en Machine Learning e IA,
encontrarás enlaces a herramientas especializadas, libros clave, blogs
relevantes y videos tutoriales que te guiarán en el uso de Python para
desarrollar y aplicar algoritmos de Machine Learning e IA.

Para aquellos que están incursionando en Machine Learning e IA con Python, te
recomendamos explorar recursos que te introduzcan en conceptos básicos como la
manipulación de datos, construcción de modelos de Machine Learning con
bibliotecas como Scikit-Learn y TensorFlow, y la implementación de redes
neuronales con Keras. Estos recursos te permitirán comprender los fundamentos
del Machine Learning e IA y cómo aplicarlos utilizando Python.

Para los Pythonistas con experiencia en Machine Learning e IA, te ofrecemos
recursos avanzados como libros especializados en deep learning, modelos
avanzados de Machine Learning, blogs que exploran casos de estudio y
aplicaciones innovadoras de Machine Learning e IA, videos sobre técnicas
avanzadas de modelado y optimización de algoritmos, y tutoriales prácticos que
te desafiarán a resolver problemas complejos en el campo de Machine Learning e
IA con Python. Con estos recursos a tu disposición, podrás mejorar tus
habilidades, explorar nuevas áreas de aplicación de Python en Machine Learning e
IA y destacarte como un experto en este campo en constante evolución. ¡Explora,
aprende y conviértete en un Pythonista líder en Machine Learning e Inteligencia
Artificial!

```{sketchviz}
---
static-subdir: images/sketchviz
---
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];

  bgcolor=transparent;
  
  ml_1 [
    label="ML Básico",
    href="/learning-path/machine-learning-ai/#ml-basico", 
    target="_top"
  ]
  ml_2 [
    label="ML Avanzado",
    href="/learning-path/machine-learning-ai/#ml-avanzado", 
    target="_top"
  ]
  
  subgraph cluster_ml {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    ml_1 -> ml_2;
    label = "*Machine Learning e IA*";
    fontsize = 20;
    color=green;
    href="/learning-path/machine-learning-ai/";
    target="_top";
  }
}
```

## ML Básico


## ML Avanzado

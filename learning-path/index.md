# ¡Python de cero a Pro!

En el vasto mundo del aprendizaje, las rutas de aprendizaje se erigen como faros guía, iluminando el camino hacia el conocimiento. Imagina un sendero serpenteante, tejido con módulos y habilidades específicas, diseñado para que cada estudiante trace su propio recorrido. Estas rutas no solo fomentan la autonomía y el compromiso, sino también reducen la deserción y aceleran la asimilación de saberes. ¿Te atreves a explorarlas?

Con nuestras recomendaciones podrás explorar cada tópico del desarrollo de software enfocado en Python e incluyendo algunos tópicos de ayuda como Docker o integración continua, te invitamos a revisar y complementar tus conocimientos con los recursos a continuación.

Como mapa general estos son los tópicos que cubriremos en nuestra ruta de aprendizaje:


```{sketchviz}
---
static-subdir: images/sketchviz
---
digraph G {
  graph [fontname = "Handlee"];
  node [fontname = "Handlee"];
  edge [fontname = "Handlee"];

  bgcolor=transparent;
  
  p_1 [label = "Python básico"]
  p_2 [label = "Python Avanzado"]
  
  d_1 [label = "Desarrollador I"]
  d_2 [label = "Desarrollador II"]
  
  dc_1 [label = "Ciencia de datos básico"]
  dc_2 [label = "Ciencia de datos avanzado"]
  
  dv_1 [label = "Despliegue"]
  dv_2 [label = "Cloud"]
  
  ml_1 [label = "ML básico"]
  ml_2 [label = "ML avanzado"]

  subgraph cluster_python {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    p_1 -> p_2;
    label = "*Desarrollador Python*";
    fontsize = 20;
  }

  subgraph cluster_web {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    d_1 -> d_2;
    label = "*Desarrollador web*";
    fontsize = 20;
    color=lightblue;
  }
  
  subgraph cluster_science {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    dc_1 -> dc_2;
    label = "*Data Science*";
    fontsize = 20;
    color=lightblue;
  }
  
  subgraph cluster_devops {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    dv_1 -> dv_2;
    label = "*Cloud y DevOps*";
    fontsize = 20;
    color=green;
  }
  
  subgraph cluster_ml {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    ml_1 -> ml_2;
    label = "*Machine Learning e IA*";
    fontsize = 20;
    color=green;
  }
  
  start -> p_1;
  p_2 -> d_1;
  p_2 -> dc_1;
  d_2 -> dv_1;
  dc_2 -> ml_1;


  start [label="*Inicio*" shape=Mdiamond];
}

```

```{toctree}
:hidden: true

beginner.md
intermediate.md
advanced-a.md
advanced-b.md
pro.md
```

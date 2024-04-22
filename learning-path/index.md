# ¡Python de cero a Pro!


```{attention}
Nuestra ruta de aprendizaje se encuentra actualmente en desarrollo.
```

En el vasto mundo del aprendizaje, las rutas de aprendizaje se erigen como faros
guía, iluminando el camino hacia el conocimiento. Imagina un sendero
serpenteante, tejido con módulos y habilidades específicas, diseñado para que
cada estudiante trace su propio recorrido. Estas rutas no solo fomentan la
autonomía y el compromiso, sino también reducen la deserción y aceleran la
asimilación de saberes. ¿Te atreves a explorarlas?

Con nuestras recomendaciones podrás explorar cada tópico del desarrollo de
software enfocado en Python e incluyendo algunos tópicos de ayuda como Docker o
integración continua, te invitamos a revisar y complementar tus conocimientos
con los recursos a continuación.

Como mapa general estos son los tópicos que cubriremos en nuestra ruta de
aprendizaje:


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
  
  d_1 [
    label="Desarrollador I",
    href="/learning-path/web-developer/#desarrollador-i", 
    target="_top"
  ]
  d_2 [
    label="Desarrollador II",
    href="/learning-path/web-developer/#desarrollador-ii", 
    target="_top"
  ]
  
  ds_1 [
    label="Ciencias de Datos Básico",
    href="/learning-path/data-science/#ciencias-de-datos-basico", 
    target="_top"
  ]
  ds_2 [
    label="Ciencias de Datos Avanzado",
    href="/learning-path/data-science/#ciencias-de-datos-avanzado", 
    target="_top"
  ]
  
  dv_1 [
    label="Despliegue",
    href="/learning-path/cloud-devops/#despliegue", 
    target="_top"
  ]
  dv_2 [
    label="Cloud",
    href="/learning-path/cloud-devops/#cloud", 
    target="_top"
  ]
  
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

  subgraph cluster_web {
    node [style=filled, color=pink];
    style=filled;
    color=lightblue;
    fontsize = 20;
    label = "*Desarrollador Web*";
    href="/learning-path/web-developer/";
    target="_top";
    d_1 -> d_2;
  }
  
  subgraph cluster_science {
    node [style=filled, color=pink];
    style=filled;
    color=lightblue;
    fontsize = 20;
    label = "*Ciencias de Datos*";
    href="/learning-path/data-science/";
    target="_top";
    ds_1 -> ds_2;
  }
  
  subgraph cluster_devops {
    node [style=filled, color=pink];
    style=filled;
    color=green;
    fontsize = 20;
    label = "*Cloud y DevOps*";
    href="/learning-path/cloud-devops/";
    target="_top";
    dv_1 -> dv_2;
  }
  
  subgraph cluster_ml {
    node [style=filled,color=pink];
    style=filled;
    color=green;
    fontsize = 20;
    label = "*Machine Learning e IA*";
    href="/learning-path/machine-learning-ai/";
    target="_top";
    ml_1 -> ml_2;
  }
  
  p_2 -> d_1;
  p_2 -> ds_1;
  d_2 -> dv_1;
  ds_2 -> ml_1;
}
```

```{toctree}
:hidden: true

python-developer.md
web-developer.md
data-science.md
cloud-devops.md
machine-learning-ai.md
```

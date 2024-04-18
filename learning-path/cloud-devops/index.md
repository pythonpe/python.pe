# Cloud y DevOps

En esta sección, hemos recopilado una selección de recursos especialmente
diseñados para potenciar las habilidades de los Pythonistas que se especializan
en Cloud y DevOps. Tanto si estás dando tus primeros pasos en este ámbito como
si ya eres un experto en Cloud y DevOps, encontrarás enlaces a herramientas
clave, libros imprescindibles, blogs especializados y videos tutoriales que te
ayudarán a dominar Python en el contexto de la nube y la infraestructura como
código.

Para aquellos que están incursionando en Cloud y DevOps con Python, te
recomendamos explorar recursos que te introduzcan a conceptos fundamentales como
despliegue automatizado, orquestación de contenedores con Docker y Kubernetes,
gestión de infraestructura con herramientas como Terraform, y cómo utilizar
Python para automatizar tareas de DevOps. Estos recursos te brindarán una base
sólida para trabajar de manera eficiente en entornos de Cloud y DevOps con
Python.

Para los Pythonistas con experiencia en Cloud y DevOps, te ofrecemos recursos
avanzados como libros especializados en arquitectura cloud, implementación de
pipelines de CI/CD con Python, blogs que exploran casos de uso reales en Cloud y
DevOps, videos sobre técnicas avanzadas de despliegue y gestión de
infraestructura en la nube, y tutoriales prácticos que te desafiarán a optimizar
y escalar tus procesos de desarrollo en la nube. Con estos recursos a tu
disposición, podrás llevar tus habilidades de Python en Cloud y DevOps al
siguiente nivel, mejorar la eficiencia de tus proyectos y destacarte como un
experto en este campo en constante evolución. ¡Explora, aprende y conviértete en
un Pythonista líder en Cloud y DevOps!

```{sketchviz}
---
static-subdir: images/sketchviz
---
digraph G {
  graph [fontname="Handlee"];
  node [fontname="Handlee"];
  edge [fontname="Handlee"];

  bgcolor=transparent;
  
  dv_1 [
    label="Despliegue",
    href="/learning-path/cloud-devops/deployment/", 
    target="_top"
  ]
  dv_2 [
    label="Cloud",
    href="/learning-path/cloud-devops/cloud/", 
    target="_top"
  ]
  
  subgraph cluster_devops {
    style=filled;
    color=lightgrey;
    node [style=filled, color=pink];
    dv_1 -> dv_2;
    label = "*Cloud y DevOps*";
    fontsize = 20;
    color=green;
    href="/learning-path/cloud-devops/";
    target="_top";
  }
}
```

```{toctree}
:hidden: true

deployment.md
cloud.md
```

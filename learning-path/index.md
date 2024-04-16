# ¡Python de cero a Pro!

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.
Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed,
dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper
congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est
eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu
massa, scelerisque vitae, consequat in, pretium a, enim.

Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras
vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio
eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum
primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh.
Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non
diam sodales hendrerit.


```{sketchviz}
---
static-subdir: images/sketchviz
---
digraph G {
  graph [fontname = "Handlee"];
  node [fontname = "Handlee"];
  edge [fontname = "Handlee"];

  bgcolor=transparent;

  subgraph cluster_0 {
    style=filled;
    color=lightgrey;
    node [style=filled,color=pink];
    a0 [href="https://python.org" target="_top"];
    a0 -> a1 -> a2 -> a3;
    label = "*process #1*";
    fontsize = 20;
  }

  subgraph cluster_1 {
    node [style=filled];
    b0 -> b1 -> b2 -> b3;
    label = "*process #2*";
    fontsize = 20;
    color=blue
  }
  start -> a0;
  start -> b0;
  a1 -> b3;
  b2 -> a3;
  a3 -> a0;
  a3 -> end;
  b3 -> end;

  start [shape=Mdiamond];
  end [shape=Msquare];
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

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


```{graphviz}
digraph Learning_path {
    a [label="Principiante" href="beginner/" fillcolor="blue" style="filled" fontcolor="white" target="_top"];
    b [label="Intermedio" href="intermediate/" fillcolor="yellow" style="filled" target="_top"];
    c [label="Avanzado A" href="advanced-a/" fillcolor="green" style="filled" target="_top"];
    d [label="Avanzado B" href="advanced-b/" fillcolor="green" style="filled" target="_top"];
    e [label="Pro" href="pro/" fillcolor="red" style="filled" fontcolor="white" target="_top"];
    a -> b;
    b -> c;
    b -> d;
    c -> e;
    d -> e;
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

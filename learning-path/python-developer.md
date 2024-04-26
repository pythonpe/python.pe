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

**Leyenda:**

📗: Libro

📹: Video tutorial

🎓: Curso

🧑‍💻: Código practico

📝: Blog post

Los nombres con asterisco al final (*) son con contenido en inglés.


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
      label="📗 Data Structures & Algorithms in Python*",
      href="https://www.amazon.com/Structures-Algorithms-Python-Robert-Lafore/dp/013485568X/",
      color="lightgreen",
      target="_top"];
    as1 [
      label="📗 Algoritmos y Estructura de Datos con Python",
      href="https://www.amazon.com/Algoritmos-Estructuras-Datos-Python-cuestionarios-ebook/dp/B0CW6C19MD/",
      color="lightgreen",
      target="_top"];
    bp3 [label="📹 6 Proyectos de Python Básicos\nCurso Completo Paso a Paso", href="https://www.youtube.com/watch?v=tWnyBD2src0", color="lightgreen", target="_top"];
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
      label="📹 Curso de Python \n desde cero (MoureDev)",
      href="https://www.youtube.com/watch?v=Kp4Mvapo5kc",
      color="lightgreen",
      target="_top"];
    f1 [
      label="📗 Curso intensivo de python",
      href="https://anayamultimedia.es/libro/titulos-especiales/curso-intensivo-de-python-2a-edicion-eric-matthes-9788441543348/",
      color="lightgreen",
      target="_top"];
    fundamentals [label="Fundamentos\nBásicos de Python"];
    clean_code [label="Clean Code"];
    basic_projects [label="Proyectos\nBásicos"];
    algostruct [label="Estructura de Datos\ny\nAlgoritmos Básicos"];
    fundamentals -> f4;
    fundamentals -> f3;
    fundamentals -> f2;
    fundamentals -> f1;
    clean_code -> cc2;
    clean_code -> cc1;
    basic_projects-> bp3;
    basic_projects-> bp2;
    basic_projects-> bp1;
    algostruct -> as4;
    algostruct -> as3;
    algostruct -> as2;
    algostruct -> as1;
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
    aas3 [label="Tópico 3", href="", color="lightgreen", target="_top"];
    aas2 [label="Tópico 1", href="", color="lightgreen", target="_top"];
    aas1 [label="Tópico 1", href="", color="lightgreen", target="_top"];
    advanced_algostruct [label="Estructurad de Datos\ny\nAlgoritmos Avanzados"];
    design_patterns [label="Patrones de Diseño\nen Python"];
    command_line [label="Línea de Comandos\nen Python"];
    python_projects [label="Proyectos en Python"];
    db [label="Bases de Datos"];
    leetcode [label="Leetcode"];
    advanced_algostruct -> aas3;
    advanced_algostruct -> aas2;
    advanced_algostruct -> aas1;
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

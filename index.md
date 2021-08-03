# Métodos Numéricos II 2021

Este curso es continuación de los temas estudiados en Métodos Numéricos 1. En esta materia, se estudian o revisan temas no introductorios de algoritmos para cálculo científico y aplicado y su implementación computacional. Se estudian tres grandes temas: (1) Álgebra lineal computacional, (2) Métodos numéricos para resolver EDO, y (3) Optimización numérica. La primera parte el curso se enfoca en temas sobre cálculo de autovalores y autovectores, y la solución eficiente de sistemas lineales. En el segundo bloque, haremos una introducción a los métodos numéricos para resolver ecuaciones diferenciales ordinarias (EDO), haciendo énfasis en métodos de la familia Runge-Kutta, y los métodos predictor-corrector. Si el tiempo lo permite, haremos una introducción a los métodos para resolver escuaciones diferenciales parciales (EDP). El bloque principal del curso introduce los temas de optimización numérica, principalmente los métodos de gradiente y punto interior. El curso culmina haciendo un estudio de la teoría de optimización restricta, particularmente programación lineal y programación cuadrática.

**Importante!!** El curso cuenta con una parte práctica extensiva, en la que el estudiante implementará en código computacional cada uno de los algoritmos estudiados. Parte fundamental del curso es utilizar las herramientas aprendidas en varios proyectos aplicados donde se trabajará con datos reales y comunicar los resultados mediante reportes técnicos y seminarios.


# Prerrequisitos

Se recomienda que los estudiantes antes del curso estén habituados con los temas:
* Cálculo vectorial
* Álgebra lineal (teoría)
* Algunos elementos de análisis (convergencia de secuencias y series, análisis en Rn)
* Métodos numéricos para una variable (*root finding*, *fitting*, *numerical differentiation and integration*)
* Programación en Python.

Para aquellos estudiantes que consideren necesario un repaso de Python, sugiero seguir el libro <br/>
[Q. Kong, T. Siauw, A. Bayen (2021). *Python Programming and Numerical Methods - A Guide for Engineers and Scientists*.](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html){:target="_blank"}
 <br/>
Caps 1-12, 14, (15 lo veremos en el curso) 16-21.

# Programa del curso
<div id='id-programa'/>

[Programa del curso](programa/Programa-opt2021.pdf){:target="_blank"}

### Horario
<div id='id-horario'/>

* Lunes de 19:50 a 21:25, Miércoles de 19:00 a 20:35.

### Office Hours
<div id='id-office'/>

* Sábados.


# Material del curso
<div id='id-material'/>

  **No.**  | **Fecha**    | **Tópicos**                                                                   | **Recursos**
  -------- | ------------ | ----------------------------------------------------------------------------- |  -------------------------------------
  01       | 07.07.2021   | Introducción al curso. Normas matriciales. <br/> [Aula 01](aulas/Aula01.pdf){:target="_blank"}  | Libro de Trefethen, Lecture 3.
  02       | 12.07.2021   | Descomposición espectral. Descomposición SVD. <br/> [Aula 02](aulas/Aula02.pdf){:target="_blank"}  | Libro de Trefethen, Lectures 4 y 5. <br/> [defective.ipynb](code/defective.ipynb){:target="_blank"}
  03       | 14.07.2021   |  Condicionamiento. Estabilidad. <br/> [Aula 03](aulas/Aula03.pdf){:target="_blank"}  | Libro de Trefethen, Lectures 12, 13, 14 y 15. 
  L1       | 16.07.2021   |                                                                               | [Lista de ejercicios 1](listas/Lista01.pdf){:target="_blank"} <br/> **Fecha de entrega: sábado 24 de julio.** 
  04       | 19.07.2021   | Eliminación gaussiana. Factoración LU y PA = LU. Pivoteo. <br/> [Aula 04](aulas/Aula04.pdf){:target="_blank"} <br/> Las notas de clase tienen muchos errores. Voy a subir una versión corregida al final de la semana. | Libro de Trefethen, Lectures 20, 21 y 22. <br/> [gaussian-elimination.ipynb](code/gaussian-elimination.ipynb){:target="_blank"}
  05       | 21.07.2021   | Factoración de Cholesky. Factoración LDL^T <br/> [Aula 05](aulas/Aula05.pdf){:target="_blank"} | Libro de Trefethen, Lecture 23. <br/> [cholesky.ipynb](code/cholesky.ipynb){:target="_blank"}
  06       | 26.07.2021   | Métodos Iterativos para sistemas lineales. <br/> [Aula 06](aulas/Aula06.pdf){:target="_blank"} | Libro de Quarteroni *et al.*, Cap. 4. <br/> [iterative.ipynb](code/iterative.ipynb){:target="_blank"}
  07       | 28.07.2021   | Descomposición QR. <br/> [Aula 07](aulas/Aula07.pdf){:target="_blank"}        | Libro de Trefethen, Lectures 6-8 y 10.
  L2       | 29.07.2021   |                                                                               | [Lista de ejercicios 2](listas/Lista02.pdf){:target="_blank"} <br/> **Fecha de entrega: domingo 08 de agosto.** 
  08       | 02.08.2021   | Cálculo de Autovalores. Método de las Potencias. <br/> [Aula 08](aulas/Aula08.pdf){:target="_blank"} | Libro de Trefethen, Lecture 27.
  .        |              |                                                                               | 
  

# Referencias
<div id='id-ref'/>

### Textos:

* [L. Trefethen, L. Bau III (1997). *Numerical Linear Algebra*.](http://library.lol/main/079EA6C3FD8CDF23B0C2ACD901CA9A26){:target="_blank"}

* [J. Nocedal, S. Wright (2006). *Numerical Optimization*.](http://library.lol/main/7016B74CFE6DC64C75864322EE4AA081){:target="_blank"}


### Referencias adicionales:

* [G.. Golub, C. Van Loan (2012). *Matrix Computations*.](http://library.lol/main/72562A3A733C2E842BE163CA97D0FA7A){:target="_blank"}

* [A. Quarteroni, R. Sacco, F. Saleri (2000). *Numerical Mathematics*.](http://library.lol/main/7D136BC80ECBF0BA65798EC129FCCAF4){:target="_blank"}

* [J. Stoer, R. Bulirsch (2002). *Introduction to Numerical Analysis*.](http://library.lol/main/04B36CA585EB49F5FDED7479823F2B50){:target="_blank"}

* [D. Griffiths, D. Higham (2010). *Numerical Methods for Ordinary Differential Equations*.](http://library.lol/main/61C367A31FBE7D8FD1E1A9129CED0B95){:target="_blank"}

* [J. C. Butcher (2016). *Numerical Methods for Ordinary Differential Equations*.](http://library.lol/main/43A7A457B95E0443C75D23DC1B46FEE7){:target="_blank"} 

* [D. Luenberger, Y. Ye (2016). *Linear and Nonlinear Programming*.](http://library.lol/main/EB915E0FDCC8D3BA222B37C9A3DD6B4F){:target="_blank"}

* [A. Izmailov, M. Solodov (2014). *Newton-type for Optimization and Variational Problems*.](http://library.lol/main/C8C3ED2461D9C8C2608595B223ABDD91){:target="_blank"}

* [S. Boyd, L. Vandenberghe (2009). *Convex Optimization*.](http://library.lol/main/A9A5D9C3CA105DB0F41AF39A6C89706C){:target="_blank"}


### Referencias de Programación:

* [Q. Kong, T. Siauw, A. Bayen (2021). *Python Programming and Numerical Methods - A Guide for Engineers and Scientists*.](http://library.lol/main/C243E02353CAB4D3A26F4DBD0527E133){:target="_blank"} <br/>
  [Web version](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html){:target="_blank"}

* [A. Gezerlis (2020). *Numerical Methods in Physics with Python*.](http://library.lol/main/16158CCB54986445C6EC84980B58DB7E){:target="_blank"}

* [Jaan Kiusalaas (2013). *Numerical Methods in Engineering with Python 3*.](http://library.lol/main/8F89791F3C9338F2E23EEC2C7BF5403B){:target="_blank"}

---

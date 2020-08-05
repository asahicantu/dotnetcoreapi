^ Y

28| 13

Flijo maximo 13[X]
Expansion minima 28


Recorrido de árboles
Al momento de representar un árbol debemos elegir el orden en el cual vamos a recorrer dicho árbol. Dependiendo de qué orden se elija será la forma en que se va a representar el árbol.

Existen tres formas de recorrer un árbol:

• Pre orden: raíz - izquierdo - derecho.
• In orden:  izquierdo - raíz - derecho.
• Pos orden: izquierdo - derecho - raíz.



¿Qué es el grado de un vértice?
Es el número de aristas que tiene un nodo con otros nodos.

Existe una propiedad matemática que nos dice que la sumatoria de todos los grados de los vértices de un grafo es igual al doble de las aristas.
Otra propiedad nos indica que si tenemos más de dos vértices con grado impar es imposible recorrer de una sola vez todo el grafo sin repetir un camino.
Una cadena es una sucesión de vértices y de conexiones entre sí.
Un camino a diferencia de una cadena es una sucesión de vértices y conexiones donde no puedes repetir ningún vértice ni conexión, mientras en un ciclo el vértice de inicio es igual al vértice donde termina.
Un grafo conexo es aquel donde todos los nodos están unidos entre sí.

A diferencia de los caminos y ciclos eulerianos, los caminos y ciclos hamiltonianos buscaran recorrer los nodos una sola vez sin importar el camino que utilicemos.

Para afirmar que hay un camino hamiltoniano se debe cumplir la condición donde la suma del grado de dos vértices es mayor o igual al número de vértices menos uno, de otra forma puede que exista el camino hamiltoniano, pero no se podrá afirmar.

Si hay un camino hamiltoniano, pero no un ciclo, entonces el grafo no es hamiltoniano.

Al momento de representar un árbol debemos elegir el orden en el cual vamos a recorrer dicho árbol. Dependiendo de qué orden se elija será la forma en que se va a representar el árbol.

Existen tres formas de recorrer un árbol:

• Pre orden: se inicia leyendo el nodo raíz, luego se pasa al hijo izquierdo y por ultimo al derecho.
• In orden: inicia leyendo el hijo izquierdo, luego la raíz y por último el hijo derecho.
• Pos orden: comienza por el hijo izquierdo para posteriormente ir al hijo derecho y por último al nodo raíz.
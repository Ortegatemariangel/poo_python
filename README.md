# POO_python

- El paradigma de POO está basado en una abstracción del mundo real que nos va a permitir desarollar programas de forma más cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## Clase

- Una clase es un tipo de datos cuyas variables se llaman objetos o instancias, la clase es la definición del concepto del mundo real y los objetos o instancias son el "propio" objeto del mundo real.
- Las clases están compuestas por dos elementos : atributos y métodos

### Atributos
- Información que almacenan las clases.

### Métodos
- Operaciones que pueden realizar las clases.

## Deficinición de una clase en python

```Python
class Nombreclases:

   def__init__(self, variable1, variable2):
      self.Atributo1 =  valor1
      self.Atributo2 = valor2

def nombreMetodo(self)
    bloquecodigo
```
   
### Componentes

```class```: palabra reservada en python para definir una clase.

```ǸombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en python que se utiliza para definir sobre el constructor de la clase (método de se ejecuta la primera vez que usas una clase)como los diferentes métodos que tiene.

```__ìnit__```: palabra reservada en python para definir el método constructor de la clase. Ess lo primero que se ejecuta cuando crea un objeto de una clase.

```(self, variableX)```: parámetro del constructor de la clase. El párametro self es obligatorio y despues puedes tener tantos parámetros como quieras. La forma de añadir parámetros es la misma que en las funciones.

```delf.AtributoX```: Formaa de utilización y acceso a los atributos de la clase.

```nombreMetodo```: nombre del método de la clase.

```bloqueCodigo```: parámetro del constructor de la clase. El párametro self es obligatorio y despues puedes tener tantos parámetros como quieras. La forma de añadir parámetros es la misma que en las funciones.

```bloqueCodigo```: instrucciones que ejecutará el método.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
     - Puedes definir tantos atributos como necesites.
     - Puedes defnir tantos metodos como necesites.
     - Puedes definir tantos parametros en el consructor y en los metodos como necesites.
     
## Composición

- Consiste en la creacion de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva.
- Las clases existentes serán atributos de la nueva clase.
- En POO la composición significa que entre las dos clases existe una relación de tipo "Tiene un".
- Ejempĺo :
    - Una coordenada en dos dimensiones está compuesta por dos valores, el valor en el eje X y el valor en el eje de las Y, ésto podría ser una clase. Un cuadrado está compuesto por cuatro coordenadas que son los cuatro vértices, esto podría ser una clase que está compuesta por cuatro clases del objeto coordenada.

     
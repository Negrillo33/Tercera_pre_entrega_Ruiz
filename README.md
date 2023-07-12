# Tercera_pre_entrega_Ruiz

#### Lamentablemente no logre que la pagina funcione como yo esperaba por eso al abrirla veran un cartel de que la pagina esta en mantenimiento, pero de funcionar asi deberia ser su uso.#####

InsercionView:
Esta vista se encarga de manejar la inserción de datos en la base de datos para las clases de Marca, Modelo y Cliente.
Al acceder a la ruta insertar/ en el navegador, se muestra un formulario donde se pueden ingresar los datos correspondientes.
Al enviar el formulario, se valida la información ingresada y se guardan los registros en la base de datos.
En caso de que la validación falle, se muestra nuevamente el formulario con los errores correspondientes.

BuscarView:
Esta vista se encarga de realizar búsquedas en la base de datos para las clases de Marca, Modelo y Cliente.
Al acceder a la ruta buscar/ en el navegador, se muestra un formulario donde se puede ingresar un término de búsqueda.
Al enviar el formulario, se realiza la búsqueda en la base de datos y se muestran los resultados correspondientes.

MarcaForm, ModeloForm y ClienteForm:
Estos formularios se utilizan en la vista InsercionView para la validación y manipulación de datos ingresados por el usuario.
Cada formulario corresponde a una clase de modelo y define los campos y validaciones necesarios.
Al llamar al método is_valid() en un formulario, se verifica si los datos ingresados cumplen con las validaciones definidas.
Si el formulario es válido, se pueden guardar los datos utilizando el método save().

En teoría, el programa se utilizaría de la siguiente manera:
1.Acceder a la ruta insertar/ en el navegador para ingresar nuevos registros de Marca, Modelo y Cliente. Llenar el formulario con los datos correspondientes y enviarlo.

2.Si los datos son válidos, se guardarán en la base de datos y se redirigirá a la página de éxito (exito.html). En caso de que haya errores de validación, se mostrarán los mensajes de error en el formulario.

3.Para realizar una búsqueda, acceder a la ruta buscar/ en el navegador. Ingresar un término de búsqueda y enviar el formulario.

4.La vista BuscarView buscará los registros en la base de datos y mostrará los resultados correspondientes.

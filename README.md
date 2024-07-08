-Trabajo Programacion Web
**Página de museo: **

-Integrantes: ALEX GABRIEL NUNEZ GALLEGOS / DIEGO ALEJANDRO ALVAREZ VARGAS / SEBASTIAN ALFREDO VALENZUELA HENRIQUEZ
Historia de usuarios:
-Un usuario entra a la pagina y que pueda ver información sobre artistas famosos (ranking), su historia y obras más famosas y conocidas.
-Un usuario puede votar por autores y obras de artes
-Un usuario puede buscar autores y puede buscar obras de arte.
-Un usuario registrado puede acceder a promociones especiales
-Un usuario puede acceder al carrito de comprar para añadir i/o quitar productos

Requerimientos funcionales:
RF01 -Ver información de artistas
RF02 -Ver listado de artistas y de obras según ranking de votos.
RF03 -Votar por los distintos artistas y obras de arte.
RF04 -Un usuario se puede registrar.
RF05 -Registrar obras de artes y modificarlas.
RF06 -Registrar autores y modificarlos.
RF07 -Buscar artistas y obras.
RF08 -Ver las noticias del sitio y las promociones especiales.
RF09 – Modificar y Editar noticias y promociones del sitio.
RF010-Registrar productos en un carrito de comprar, añadir y eliminarlas

Casos de uso:
CU01: Mantenedor(CRUD) Artistas
CU02: Registro de Usuarios
CU03: Mantenedor(CRUD)Obras
CU04: Ver noticias
CU05: Mantenedor(CRUD)Noticias
CU06: Registrar Votos
CU07: Buscar artistas
CU08: Buscar Obras
CU09: Listado y detalle de Artistas
CU10: Listado y detalle de Obras
CU11: Registrar Productos

Vistas:
CU01: Mantenedor(CRUD) Artistas
(ADMIN) CRUD Artista:listar,modificar,eliminar,creacion
CU02: Registro de Usuarios
Registro, un usuario registra su nombre, correo y contraseña, al apretar boton (registrar), se crea el usuario con los datos proporcionados, se le redirige al login
inicio de sesion: se ingresan datos el nombre o correo y una contraseña para logear
CU03: Mantenedor(CRUD)Obras
(ADMIN) CRUD OBRAS: listar,modificar,eliminar,creacion
CU04: Ver noticias
Noticias: Mostrar noticias actuales y antiguas sobre el museo
CU05: Mantenedor(CRUD)Noticias
(ADMIN) CRUD NOTICIAS: listar,modificar,eliminar,creacion
CU06: Registrar Votos
En la vista detalle se vota
CU07: Buscar artistas
(Invitados) Busqueda Artistas: poder buscar un artista en una barra de busqueda, el artista buscado mostrara su nombre y una descripcion
CU08: Buscar Obras
(Invitados) Busqueda obras: poder buscar una obra de arte en una barra de busqueda, laobra buscada mostrara su nombre y una descripcion
CU09: Listado y detalle de Artistas
(Invitados) Listado y detalle artistas: listado en una tabla que mostrara el nombre del artista y una descripcion por cada artista
CU10: Listado y detalle de Obras
(Invitados) Listado y detalle obras: listado en una tabla que mostrara las obras y una descripcion
Extras
Home: pagina principal

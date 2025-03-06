## PROYECTO de Aula de Código Limpio

## Nota:
Para este proyecto, inicialmente se requiere la implementación de pruebas unitarias que evalúen las diferentes clases vacías. Posteriormente, se implementarán las funcionalidades de la aplicación. A continuación, se presentan los requisitos del sistema.

## Objetivo del Proyecto:
 El objetivo de este proyecto es desarrollar una aplicación para la gestión de tareas personales y profesionales.

## Funcionalidades:

1. Crear una tarea: Permitir a los usuarios crear una tarea en el sistema.

2. Editar una tarea: Permitir a los usuarios editar una tarea existente.

3. Eliminar una tarea: Permitir a los usuarios eliminar una tarea existente.

4. Iniciar sesión: Permitir a los usuarios iniciar sesión con una cuenta existente.

5. Crear cuenta: Permitir a los usuarios registrarse en el sistema.

6. Cambiar contraseña: Permitir a los usuarios cambiar su contraseña cuando lo deseen.

## Datos de una tarea:

Una tarea debe contener los siguientes datos:

* Texto de la tarea.

* Usuario que la creó.

* Fecha de creación.

* Categoría de la tarea.

* Estado de la tarea (Completada, Por hacer, En progreso, etc.).

## Nota:
Cada usuario podrá ver y gestionar solo sus tareas.

## Casos de Prueba

A continuación, se presentan los casos de prueba para cada funcionalidad, cubriendo escenarios normales, extremos y de error.

## Casos de Prueba

### Crear una Tarea
| #  | Caso de Prueba                                | Entrada                                     | Resultado esperado                        | Tipo  |
|----|----------------------------------------------|---------------------------------------------|------------------------------------------|------|
| 1  | Crear tarea con texto válido y categoría    | "Comprar leche", Categoría: "Compras"      | Tarea creada correctamente              | Normal    |
| 2  | Crear tarea con estado "Por hacer"          | "Ir al gimnasio", Estado: "Por hacer"      | Tarea creada correctamente              | Normal    |
| 3  | Crear tarea con usuario registrado          | "Leer libro", Usuario: "usuario1"         | Tarea creada correctamente              | Normal    |
| 4  | Crear tarea con texto más largo permitido   | 255 caracteres, Categoría: "Trabajo"       | Tarea creada correctamente              | Extremos    |
| 5  | Crear tarea con estado inusual              | "Estudiar", Estado: "En pausa"            | Tarea creada correctamente              | Extremos    |
| 6  | Crear tarea con categoría desconocida       | "Viajar", Categoría: "Otro"               | Tarea creada correctamente              | Extremos    |
| 7  | Intentar crear tarea sin texto              | "", Categoría: "Personal"                 | Error: El texto no puede estar vacío    | error    |
| 8  | Intentar crear tarea sin categoría          | "Hacer ejercicio", ""                     | Error: La categoría es requerida        | error    |
| 9  | Intentar crear tarea sin estado             | "Revisar correo", Categoría: "Trabajo"    | Error: El estado es requerido           | error    |

### Editar una Tarea
| #  | Caso de Prueba                                | Entrada                                   | Resultado esperado                    | Tipo  |
|----|----------------------------------------------|-------------------------------------------|--------------------------------------|------|
| 10 | Editar texto de tarea existente             | "Hacer ejercicio" -> "Hacer cardio"      | Tarea editada correctamente         | Normal    |
| 11 | Editar categoría de tarea existente         | "Estudiar", Categoría: "Educación"       | Tarea editada correctamente         | Normal    |
| 12 | Editar estado de tarea existente            | "Terminar informe", Estado: "Completada" | Tarea editada correctamente         | Normal    |
| 13 | Editar tarea con texto máximo permitido     | 255 caracteres                           | Tarea editada correctamente         | Extremo    |
| 14 | Editar tarea con estado límite válido       | "Leer", Estado: "Pendiente"             | Tarea editada correctamente         | Extremo    |
| 15 | Editar tarea con nueva categoría válida     | "Viajar", Categoría: "Placer"           | Tarea editada correctamente         | Extremo    |
| 16 | Intentar editar tarea inexistente           | ID incorrecto                            | Error: La tarea no existe           | error    |
| 17 | Intentar editar tarea sin cambios           | ID válido, Sin modificaciones           | Error: No hay cambios registrados   | error    |
| 18 | Intentar editar tarea cambiando usuario     | ID válido, Nuevo usuario                 | Error: No se puede cambiar usuario  | error    |

### Eliminar una Tarea
| #  | Caso de Prueba                                | Entrada             | Resultado esperado                  | Tipo  |
|----|----------------------------------------------|---------------------|------------------------------------|------|
| 19 | Eliminar tarea existente                    | ID de tarea válido  | Tarea eliminada correctamente     | Normal    |
| 20 | Eliminar tarea en estado "Completada"       | ID válido           | Tarea eliminada correctamente     | Normal    |
| 21 | Eliminar tarea en estado "Por hacer"        | ID válido           | Tarea eliminada correctamente     | Normal    |
| 22 | Eliminar tarea con ID límite permitido      | ID más alto permitido | Tarea eliminada correctamente   | Extremo   |
| 23 | Eliminar tarea con muchas ediciones previas | ID válido           | Tarea eliminada correctamente     | Extremo   |
| 24 | Eliminar tarea con usuario con muchas tareas | ID válido           | Tarea eliminada correctamente     | Extremo    |
| 25 | Intentar eliminar tarea inexistente         | ID incorrecto       | Error: La tarea no existe         | error   |
| 26 | Intentar eliminar tarea sin permisos        | ID de otro usuario  | Error: No tiene permisos          | error   |
| 27 | Intentar eliminar tarea sin ID              | ""                  | Error: Debe proporcionar un ID    | error   |

### Iniciar Sesión
| #  | Caso de Prueba                                | Entrada                                    | Resultado esperado                   | Tipo  |
|----|----------------------------------------------|--------------------------------------------|-------------------------------------|------|
| 28 | Usuario inicia sesión correctamente        | usuario@example.com, Contraseña correcta  | Inicio de sesión exitoso          | Normal    |
| 29 | Usuario inicia sesión con mayúsculas       | USUARIO@EXAMPLE.COM, Contraseña correcta  | Inicio de sesión exitoso          | Normal    |
| 30 | Usuario inicia sesión después de cerrar sesión | usuario@example.com, Contraseña correcta | Inicio de sesión exitoso       | Normal    |
| 31 | Usuario inicia sesión con contraseña larga | usuario@example.com, 128 caracteres       | Inicio de sesión exitoso          | Extremo    |
| 32 | Usuario inicia sesión con correo muy largo | 320 caracteres, Contraseña correcta       | Inicio de sesión exitoso          | Extremo    |
| 33 | Usuario inicia sesión con múltiples intentos | usuario@example.com, intentos repetidos | Inicio de sesión exitoso          | Extremo    |
| 34 | Intentar iniciar sesión con correo incorrecto | usuario@incorrecto.com, Contraseña correcta | Error: Usuario no registrado     | error  |
| 35 | Intentar iniciar sesión con contraseña incorrecta | usuario@example.com, Contraseña incorrecta | Error: Credenciales incorrectas| error    |
| 36 | Intentar iniciar sesión con usuario inactivo | usuario@example.com, Contraseña correcta  | Error: Usuario inactivo           |  error|

### Recuperar Contraseña
| #  | Caso de Prueba                                | Entrada                                    | Resultado esperado                   | Tipo  |
|----|----------------------------------------------|--------------------------------------------|-------------------------------------|------|
| 37 | Usuario solicita recuperación con correo válido | usuario@example.com                     | Email de recuperación enviado     | Normal    |
| 38 | Usuario solicita recuperación con correo en mayúsculas | USUARIO@EXAMPLE.COM                     | Email de recuperación enviado     | Normal    |
| 39 | Usuario solicita recuperación después de restablecer | usuario@example.com                     | Email de recuperación enviado     | Normal    |
| 40 | Usuario solicita recuperación con correo largo | 320 caracteres                          | Email de recuperación enviado     | Extremo     |
| 41 | Usuario solicita recuperación varias veces | usuario@example.com varias veces        | Email de recuperación enviado     | Extremo     |
| 42 | Usuario solicita recuperación desde otro dispositivo | usuario@example.com                     | Email de recuperación enviado     | Extremo     |
| 43 | Intentar recuperación con correo incorrecto | usuario@incorrecto.com                  | Error: Usuario no registrado      | error  |
| 44 | Intentar recuperación sin correo           | ""                                      | Error: Debe proporcionar un correo | error    |
| 45 | Intentar recuperación con usuario inactivo | usuario@example.com                     | Error: Usuario inactivo           | error    |

### Cerrar Sesión
| #  | Caso de Prueba                                | Entrada             | Resultado esperado                  | Tipo  |
|----|----------------------------------------------|---------------------|------------------------------------|------|
| 46 | Usuario cierra sesión correctamente        | Usuario autenticado | Cierre de sesión exitoso         | Normal    |
| 47 | Usuario cierra sesión con múltiples sesiones abiertas | Varias sesiones | Cierre de sesión exitoso         | Normal    |
| 48 | Usuario cierra sesión y vuelve a iniciar sesión | Usuario autenticado | Cierre y nuevo inicio exitoso    | Normal    |
| 49 | Usuario cierra sesión en otro dispositivo  | Sesión en otro dispositivo | Cierre exitoso               | Extremo     |
| 50 | Usuario cierra sesión con red inestable    | Internet intermitente | Cierre exitoso                    | Extremo     |
| 51 | Usuario cierra sesión después de mucho tiempo | Sesión activa por 24h | Cierre exitoso               | Extremo     |
| 52 | Intentar cerrar sesión sin haber iniciado sesión | Sin sesión activa | Error: No hay sesión activa     | error   |
| 53 | Intentar cerrar sesión con error de servidor | Usuario autenticado | Error: No se pudo cerrar sesión | error    |
| 54 | Intentar cerrar sesión con cuenta bloqueada | Usuario bloqueado   | Error: Cuenta bloqueada         | error    |



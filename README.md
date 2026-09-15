# Registro de Transportes

Programa en Python, sencillo, para llevar un registro de autos por consola. Es un ejercicio de práctica, así que no usa archivos ni base de datos: mientras el programa está corriendo, todo se guarda en memoria (en una lista).

## ¿Qué hace?

Al ejecutarlo aparece un menú con estas opciones:

1. **Registrar datos de transporte** — pide placa, marca, modelo, año, color y propietario, y lo agrega a la lista. No deja registrar dos veces la misma placa.
2. **Consultar datos de transporte** — puedes buscar un auto por su placa o ver el listado completo de los que llevas registrados.
3. **Modificar datos de transporte** — busca un auto por placa y te deja actualizar sus datos. Si dejas un campo vacío al modificar, se queda con el valor que tenía antes.
4. **Salir** — cierra el programa.

## Cómo correrlo

Solo necesitas tener Python instalado (3.x). Desde la terminal, en la carpeta del proyecto:

```bash
python registro_transportes.py
```

Y sigue las instrucciones que van apareciendo en pantalla.

## Cómo está organizado el código

Todo vive en `registro_transportes.py`, dividido en funciones para que cada cosa haga solo una tarea:

- `mostrar_menu()` — imprime las opciones.
- `buscar_por_placa(placa)` — recorre la lista de autos y devuelve el que coincida con esa placa (o `None` si no existe). La usan tanto consultar como modificar.
- `registrar_transporte()` — pide los datos de un auto nuevo y lo guarda.
- `mostrar_datos_transporte(transporte)` — imprime los datos de un auto en pantalla, ordenados.
- `consultar_transporte()` — deja elegir entre buscar por placa o ver todos los registros.
- `modificar_transporte()` — busca un auto y permite actualizar sus campos.
- `main()` — es el ciclo principal, el que mantiene el menú corriendo hasta que el usuario elige salir.

Los autos se guardan como diccionarios dentro de la lista `transportes`, por ejemplo:

```python
{
    "placa": "ABC123",
    "marca": "Toyota",
    "modelo": "Corolla",
    "anio": "2020",
    "color": "Blanco",
    "propietario": "Juan Pérez"
}
```

## Nota

Como los datos se guardan solo en memoria, al cerrar el programa se pierde todo lo registrado. Es un proyecto pensado para practicar funciones y manejo de listas/diccionarios en Python, no para uso real.

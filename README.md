# La Economica - Sistema de Inventario

Bienvenido al repositorio del Sistema de Inventario para la microempresa "La Economica". Este proyecto utiliza el framework Django y está diseñado para gestionar el inventario de manera eficiente, permitiendo un seguimiento detallado de los productos y sus historiales.

## Equipo de Desarrollo

| Usuarios    | Cargo                         |
|-----------|-------------------------------|
| Zextokar    |  Gerente y Desarrollador de SW  |
| BenaMT  |  Gerente y Desarrollador de SW  |


## Requerimientos del Sistema

### Requerimientos Mínimos

- **Servidor:** Se utilizará AWS (Amazon Web Server).
- **Procesador:** AMD A6-9500E.
- **Memoria RAM:** 4 GB a 2400 Mhz.
- **Disco Duro:** Utilizar un SSD de 120 GB o un HDD de 500 GB.

### Requerimientos Óptimos

- **Procesador:** Intel Core i7-8650U o similar.
- **Memoria RAM:** 8 GB a 2400 Mhz.
- **Disco Duro:** Utilizar un SSD de 240 GB o un HDD de 500 GB.

### Tabla comparativa
| Componentes       | Windows                                 | MacOS                            | Linux (RedHat o Debian)                |
|-------------------|-----------------------------------------|----------------------------------|---------------------------------------|
| Sistema Operativo | Windows® 10 (64-bit)                    | MacOS Sierra 10.12 o Superior    | Ubuntu 16.04 o Superior, Fedora 36 o Superior (64-bit) |
| Procesador        | Intel® Core™ 2 Duo o AMD Athlon Silver 3050U | Intel Core i5, 2.0 GHz           | Intel® Core™ 2 Duo E6600 o AMD Phenom™ 8750 o superior |
| Memoria RAM       | 4 GB                                    | 4 GB                             | 4 GB                                  |
| Almacenamiento     | 5 GB                                    | 5 GB                             | 5 GB                                  |

## Instalación

Asegúrese de tener Python y pip instalados en su sistema. Se recomienda el uso de un entorno virtual para mantener las dependencias del proyecto separadas. A continuación, siga estos pasos:

```bash
git clone https://github.com/TuUsuario/LaEconomica-Inventario.git
```
```bash
cd LaEconomica-Inventario
```
```bash
python manage.py runserver
```

A la vez hay un archivo de requirements para su instalción
```bash
pip install -r requirements.txt
``` 

El sistema estará disponible en http://127.0.0.1:8000/.

## Características Principales

- **Gestión de Productos:** Agregar, editar y eliminar productos con información detallada.
- **Historial de Cambios:** Utiliza `django-simple-history` para rastrear cambios en los productos.
- **Búsqueda y Filtrado:** Busque productos por nombre, categoría, etc.
- **Interfaz Intuitiva:** Diseño limpio y fácil de usar.

## Contribuciones

¡Las contribuciones son bienvenidas! Si desea contribuir al desarrollo de este proyecto, siga estos pasos:

1. Fork del repositorio.
2. Cree una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realice los cambios necesarios y confirme (`git commit -m 'Agrega nueva característica'`).
4. Envíe sus cambios (`git push origin feature/nueva-caracteristica`).
5. Abra una solicitud de extracción.

Esperamos que este sistema de inventario sea de gran utilidad para "La Economica". ¡Gracias por contribuir!

# La Economica - Sistema de Inventario

Bienvenido al repositorio del Sistema de Inventario para la microempresa "La Economica". Este proyecto utiliza el framework Django y está diseñado para gestionar el inventario de manera eficiente, permitiendo un seguimiento detallado de los productos y sus historiales.

## Equipo de Desarrollo

| Usuarios    | Cargo                         |
|-----------|-------------------------------|
| Zextokar    |  Gerente y Desarrollador de SW  |
| BenjaMT  |  Gerente y Desarrollador de SW  |


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

### Árbol de archivos

```
C:.
¦   manage.py
¦   README.md
¦   requirements.txt
¦   UsuariosDataBase.txt
¦   
+---gestorProducts
¦   ¦   admin.py
¦   ¦   apps.py
¦   ¦   forms.py
¦   ¦   models.py
¦   ¦   tests.py
¦   ¦   views.py
¦   ¦   __init__.py
¦   ¦   
¦   +---migrations
¦   ¦   ¦   0001_initial.py
¦   ¦   ¦   __init__.py
¦   ¦   ¦   
¦   ¦   +---__pycache__
¦   ¦           0001_initial.cpython-312.pyc
¦   ¦           __init__.cpython-312.pyc
¦   ¦           
¦   +---__pycache__
¦           admin.cpython-312.pyc
¦           apps.cpython-312.pyc
¦           forms.cpython-312.pyc
¦           models.cpython-312.pyc
¦           views.cpython-312.pyc
¦           __init__.cpython-312.pyc
¦           
+---gestorUser
¦   ¦   admin.py
¦   ¦   apps.py
¦   ¦   forms.py
¦   ¦   models.py
¦   ¦   tests.py
¦   ¦   views.py
¦   ¦   __init__.py
¦   ¦   
¦   +---migrations
¦   ¦   ¦   0001_initial.py
¦   ¦   ¦   __init__.py
¦   ¦   ¦   
¦   ¦   +---__pycache__
¦   ¦           0001_initial.cpython-312.pyc
¦   ¦           __init__.cpython-312.pyc
¦   ¦           
¦   +---__pycache__
¦           admin.cpython-312.pyc
¦           apps.cpython-312.pyc
¦           forms.cpython-312.pyc
¦           models.cpython-312.pyc
¦           views.cpython-312.pyc
¦           __init__.cpython-312.pyc
¦           
+---LaEconomicaWeb
¦   ¦   asgi.py
¦   ¦   settings.py
¦   ¦   urls.py
¦   ¦   wsgi.py
¦   ¦   __init__.py
¦   ¦   
¦   +---__pycache__
¦           settings.cpython-312.pyc
¦           urls.cpython-312.pyc
¦           wsgi.cpython-312.pyc
¦           __init__.cpython-312.pyc
¦           
¦   +---assets
¦   ¦   +---css
¦   ¦   ¦       style.css
¦   ¦   ¦       
¦   ¦   +---img
¦   ¦   ¦   ¦   about.jpg
¦   ¦   ¦   ¦   apple-touch-icon.png
¦   ¦   ¦   ¦   departments-1.jpg
¦   ¦   ¦   ¦   departments-2.jpg
¦   ¦   ¦   ¦   departments-3.jpg
¦   ¦   ¦   ¦   departments-4.jpg
¦   ¦   ¦   ¦   departments-5.jpg
¦   ¦   ¦   ¦   favicon.png
¦   ¦   ¦   ¦   hero-bg.jpg
¦   ¦   ¦   ¦   muchacho.webp
¦   ¦   ¦   ¦   
¦   ¦   ¦   +---doctors
¦   ¦   ¦   ¦       doctors-1.jpg
¦   ¦   ¦   ¦       doctors-2.jpg
¦   ¦   ¦   ¦       doctors-3.jpg
¦   ¦   ¦   ¦       doctors-4.jpg
¦   ¦   ¦   ¦       
¦   ¦   ¦   +---gallery
¦   ¦   ¦   ¦       gallery-1.jpg
¦   ¦   ¦   ¦       gallery-2.jpg
¦   ¦   ¦   ¦       gallery-3.jpg
¦   ¦   ¦   ¦       gallery-4.jpg
¦   ¦   ¦   ¦       gallery-5.jpg
¦   ¦   ¦   ¦       gallery-6.jpg
¦   ¦   ¦   ¦       gallery-7.jpg
¦   ¦   ¦   ¦       gallery-8.jpg
¦   ¦   ¦   ¦       
¦   ¦   ¦   +---testimonials
¦   ¦   ¦           testimonials-1.jpg
¦   ¦   ¦           testimonials-2.jpg
¦   ¦   ¦           testimonials-3.jpg
¦   ¦   ¦           testimonials-4.jpg
¦   ¦   ¦           testimonials-5.jpg
¦   ¦   ¦           
¦   ¦   +---js
¦   ¦   ¦       main.js
¦   ¦   ¦       
¦   ¦   +---scss
¦   ¦   ¦       Readme.txt
¦   ¦   ¦       
¦   ¦   +---vendor
¦   ¦       +---animate.css
¦   ¦       ¦       animate.compat.css
¦   ¦       ¦       animate.css
¦   ¦       ¦       animate.min.css
¦   ¦       ¦       
¦   ¦       +---bootstrap
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦       bootstrap-grid.css
¦   ¦       ¦   ¦       bootstrap-grid.css.map
¦   ¦       ¦   ¦       bootstrap-grid.min.css
¦   ¦       ¦   ¦       bootstrap-grid.min.css.map
¦   ¦       ¦   ¦       bootstrap-grid.rtl.css
¦   ¦       ¦   ¦       bootstrap-grid.rtl.css.map
¦   ¦       ¦   ¦       bootstrap-grid.rtl.min.css
¦   ¦       ¦   ¦       bootstrap-grid.rtl.min.css.map
¦   ¦       ¦   ¦       bootstrap-reboot.css
¦   ¦       ¦   ¦       bootstrap-reboot.css.map
¦   ¦       ¦   ¦       bootstrap-reboot.min.css
¦   ¦       ¦   ¦       bootstrap-reboot.min.css.map
¦   ¦       ¦   ¦       bootstrap-reboot.rtl.css
¦   ¦       ¦   ¦       bootstrap-reboot.rtl.css.map
¦   ¦       ¦   ¦       bootstrap-reboot.rtl.min.css
¦   ¦       ¦   ¦       bootstrap-reboot.rtl.min.css.map
¦   ¦       ¦   ¦       bootstrap-utilities.css
¦   ¦       ¦   ¦       bootstrap-utilities.css.map
¦   ¦       ¦   ¦       bootstrap-utilities.min.css
¦   ¦       ¦   ¦       bootstrap-utilities.min.css.map
¦   ¦       ¦   ¦       bootstrap-utilities.rtl.css
¦   ¦       ¦   ¦       bootstrap-utilities.rtl.css.map
¦   ¦       ¦   ¦       bootstrap-utilities.rtl.min.css
¦   ¦       ¦   ¦       bootstrap-utilities.rtl.min.css.map
¦   ¦       ¦   ¦       bootstrap.css
¦   ¦       ¦   ¦       bootstrap.css.map
¦   ¦       ¦   ¦       bootstrap.min.css
¦   ¦       ¦   ¦       bootstrap.min.css.map
¦   ¦       ¦   ¦       bootstrap.rtl.css
¦   ¦       ¦   ¦       bootstrap.rtl.css.map
¦   ¦       ¦   ¦       bootstrap.rtl.min.css
¦   ¦       ¦   ¦       bootstrap.rtl.min.css.map
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---js
¦   ¦       ¦           bootstrap.bundle.js
¦   ¦       ¦           bootstrap.bundle.js.map
¦   ¦       ¦           bootstrap.bundle.min.js
¦   ¦       ¦           bootstrap.bundle.min.js.map
¦   ¦       ¦           bootstrap.esm.js
¦   ¦       ¦           bootstrap.esm.js.map
¦   ¦       ¦           bootstrap.esm.min.js
¦   ¦       ¦           bootstrap.esm.min.js.map
¦   ¦       ¦           bootstrap.js
¦   ¦       ¦           bootstrap.js.map
¦   ¦       ¦           bootstrap.min.js
¦   ¦       ¦           bootstrap.min.js.map
¦   ¦       ¦           
¦   ¦       +---bootstrap-icons
¦   ¦       ¦   ¦   bootstrap-icons.css
¦   ¦       ¦   ¦   bootstrap-icons.json
¦   ¦       ¦   ¦   bootstrap-icons.min.css
¦   ¦       ¦   ¦   bootstrap-icons.scss
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---fonts
¦   ¦       ¦           bootstrap-icons.woff
¦   ¦       ¦           bootstrap-icons.woff2
¦   ¦       ¦           
¦   ¦       +---boxicons
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦       animations.css
¦   ¦       ¦   ¦       boxicons.css
¦   ¦       ¦   ¦       boxicons.min.css
¦   ¦       ¦   ¦       transformations.css
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---fonts
¦   ¦       ¦           boxicons.eot
¦   ¦       ¦           boxicons.svg
¦   ¦       ¦           boxicons.ttf
¦   ¦       ¦           boxicons.woff
¦   ¦       ¦           boxicons.woff2
¦   ¦       ¦           
¦   ¦       +---fontawesome-free
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦       all.css
¦   ¦       ¦   ¦       all.min.css
¦   ¦       ¦   ¦       brands.css
¦   ¦       ¦   ¦       brands.min.css
¦   ¦       ¦   ¦       fontawesome.css
¦   ¦       ¦   ¦       fontawesome.min.css
¦   ¦       ¦   ¦       regular.css
¦   ¦       ¦   ¦       regular.min.css
¦   ¦       ¦   ¦       solid.css
¦   ¦       ¦   ¦       solid.min.css
¦   ¦       ¦   ¦       svg-with-js.css
¦   ¦       ¦   ¦       svg-with-js.min.css
¦   ¦       ¦   ¦       v4-font-face.css
¦   ¦       ¦   ¦       v4-font-face.min.css
¦   ¦       ¦   ¦       v4-shims.css
¦   ¦       ¦   ¦       v4-shims.min.css
¦   ¦       ¦   ¦       v5-font-face.css
¦   ¦       ¦   ¦       v5-font-face.min.css
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---webfonts
¦   ¦       ¦           fa-brands-400.ttf
¦   ¦       ¦           fa-brands-400.woff2
¦   ¦       ¦           fa-regular-400.ttf
¦   ¦       ¦           fa-regular-400.woff2
¦   ¦       ¦           fa-solid-900.ttf
¦   ¦       ¦           fa-solid-900.woff2
¦   ¦       ¦           fa-v4compatibility.ttf
¦   ¦       ¦           fa-v4compatibility.woff2
¦   ¦       ¦           
¦   ¦       +---glightbox
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦       glightbox.css
¦   ¦       ¦   ¦       glightbox.min.css
¦   ¦       ¦   ¦       plyr.css
¦   ¦       ¦   ¦       plyr.min.css
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---js
¦   ¦       ¦           glightbox.js
¦   ¦       ¦           glightbox.min.js
¦   ¦       ¦           
¦   ¦       +---purecounter
¦   ¦       ¦       purecounter_vanilla.js
¦   ¦       ¦       purecounter_vanilla.js.map
¦   ¦       ¦       
¦   ¦       +---remixicon
¦   ¦       ¦       remixicon.css
¦   ¦       ¦       remixicon.eot
¦   ¦       ¦       remixicon.glyph.json
¦   ¦       ¦       remixicon.less
¦   ¦       ¦       remixicon.svg
¦   ¦       ¦       remixicon.symbol.svg
¦   ¦       ¦       remixicon.ttf
¦   ¦       ¦       remixicon.woff
¦   ¦       ¦       remixicon.woff2
¦   ¦       ¦       
¦   ¦       +---swiper
¦   ¦               swiper-bundle.min.css
¦   ¦               swiper-bundle.min.js
¦   ¦               swiper-bundle.min.js.map
¦   ¦               
¦   +---css
¦   ¦       bootstrap.min.css
¦   ¦       bootstrap.min.css.map
¦   ¦       material-dashboard.css
¦   ¦       material-dashboard.css.map
¦   ¦       material-dashboard.min.css
¦   ¦       now-ui-dashboard.css
¦   ¦       now-ui-dashboard.css.map
¦   ¦       now-ui-dashboard.min.css
¦   ¦       nucleo-icons.css
¦   ¦       nucleo-svg.css
¦   ¦       
¦   +---demo
¦   ¦       demo.css
¦   ¦       demo.js
¦   ¦       
¦   +---fonts
¦   ¦       nucleo-icons.eot
¦   ¦       nucleo-icons.svg
¦   ¦       nucleo-icons.ttf
¦   ¦       nucleo-icons.woff
¦   ¦       nucleo-icons.woff2
¦   ¦       nucleo-license.md
¦   ¦       nucleo-outline.eot
¦   ¦       nucleo-outline.ttf
¦   ¦       nucleo-outline.woff
¦   ¦       nucleo-outline.woff2
¦   ¦       nucleo.eot
¦   ¦       nucleo.ttf
¦   ¦       nucleo.woff
¦   ¦       nucleo.woff2
¦   ¦       
¦   +---img
¦   ¦   ¦   apple-icon.png
¦   ¦   ¦   bg-pricing.jpg
¦   ¦   ¦   bg-smart-home-1.jpg
¦   ¦   ¦   bg-smart-home-2.jpg
¦   ¦   ¦   bg5.jpg
¦   ¦   ¦   bruce-mars.jpg
¦   ¦   ¦   default-avatar.png
¦   ¦   ¦   down-arrow-dark.svg
¦   ¦   ¦   down-arrow-white.svg
¦   ¦   ¦   down-arrow.svg
¦   ¦   ¦   drake.jpg
¦   ¦   ¦   favicon.png
¦   ¦   ¦   header.jpg
¦   ¦   ¦   home-decor-1.jpg
¦   ¦   ¦   home-decor-2.jpg
¦   ¦   ¦   home-decor-3.jpg
¦   ¦   ¦   ivana-square.jpg
¦   ¦   ¦   ivana-squares.jpg
¦   ¦   ¦   ivancik.jpg
¦   ¦   ¦   kal-visuals-square.jpg
¦   ¦   ¦   logo-ct-dark.png
¦   ¦   ¦   logo-ct.png
¦   ¦   ¦   marie.jpg
¦   ¦   ¦   meeting.jpg
¦   ¦   ¦   mike.jpg
¦   ¦   ¦   now-logo.png
¦   ¦   ¦   now-ui-dashboard.gif
¦   ¦   ¦   office-dark.jpg
¦   ¦   ¦   product-12.jpg
¦   ¦   ¦   team-1.jpg
¦   ¦   ¦   team-2.jpg
¦   ¦   ¦   team-3.jpg
¦   ¦   ¦   team-4.jpg
¦   ¦   ¦   team-5.jpg
¦   ¦   ¦   tesla-model-s.png
¦   ¦   ¦   vr-bg.jpg
¦   ¦   ¦   
¦   ¦   +---icons
¦   ¦   ¦   +---flags
¦   ¦   ¦           AU.png
¦   ¦   ¦           BR.png
¦   ¦   ¦           DE.png
¦   ¦   ¦           GB.png
¦   ¦   ¦           US.png
¦   ¦   ¦           
¦   ¦   +---illustrations
¦   ¦   ¦       chat.png
¦   ¦   ¦       danger-chat-ill.png
¦   ¦   ¦       dark-lock-ill.png
¦   ¦   ¦       error-404.png
¦   ¦   ¦       error-500.png
¦   ¦   ¦       illustration-lock.jpg
¦   ¦   ¦       illustration-reset.jpg
¦   ¦   ¦       illustration-signin.jpg
¦   ¦   ¦       illustration-signup.jpg
¦   ¦   ¦       illustration-verification.jpg
¦   ¦   ¦       lock.png
¦   ¦   ¦       pattern-tree.svg
¦   ¦   ¦       rocket-white.png
¦   ¦   ¦       
¦   ¦   +---logos
¦   ¦   ¦   ¦   mastercard.png
¦   ¦   ¦   ¦   visa.png
¦   ¦   ¦   ¦   
¦   ¦   ¦   +---gray-logos
¦   ¦   ¦           logo-coinbase.svg
¦   ¦   ¦           logo-nasa.svg
¦   ¦   ¦           logo-netflix.svg
¦   ¦   ¦           logo-pinterest.svg
¦   ¦   ¦           logo-spotify.svg
¦   ¦   ¦           logo-vodafone.svg
¦   ¦   ¦           
¦   ¦   +---products
¦   ¦   ¦       product-1-min.jpg
¦   ¦   ¦       product-11.jpg
¦   ¦   ¦       product-2-min.jpg
¦   ¦   ¦       product-3-min.jpg
¦   ¦   ¦       product-4-min.jpg
¦   ¦   ¦       product-5-min.jpg
¦   ¦   ¦       product-6-min.jpg
¦   ¦   ¦       product-7-min.jpg
¦   ¦   ¦       product-details-1.jpg
¦   ¦   ¦       product-details-2.jpg
¦   ¦   ¦       product-details-3.jpg
¦   ¦   ¦       product-details-4.jpg
¦   ¦   ¦       product-details-5.jpg
¦   ¦   ¦       
¦   ¦   +---shapes
¦   ¦   ¦       pattern-lines.svg
¦   ¦   ¦       waves-white.svg
¦   ¦   ¦       
¦   ¦   +---small-logos
¦   ¦           bootstrap.svg
¦   ¦           creative-tim.svg
¦   ¦           devto.svg
¦   ¦           github.svg
¦   ¦           google-webdev.svg
¦   ¦           icon-bulb.svg
¦   ¦           icon-sun-cloud.png
¦   ¦           logo-asana.svg
¦   ¦           logo-atlassian.svg
¦   ¦           logo-invision.svg
¦   ¦           logo-jira.svg
¦   ¦           logo-slack.svg
¦   ¦           logo-spotify.svg
¦   ¦           logo-xd.svg
¦   ¦           
¦   +---js
¦   ¦   ¦   material-dashboard.js
¦   ¦   ¦   material-dashboard.js.map
¦   ¦   ¦   material-dashboard.min.js
¦   ¦   ¦   now-ui-dashboard.js
¦   ¦   ¦   now-ui-dashboard.js.map
¦   ¦   ¦   now-ui-dashboard.min.js
¦   ¦   ¦   
¦   ¦   +---core
¦   ¦   ¦       bootstrap.bundle.min.js
¦   ¦   ¦       bootstrap.min.js
¦   ¦   ¦       jquery.min.js
¦   ¦   ¦       popper.min.js
¦   ¦   ¦       
¦   ¦   +---plugins
¦   ¦           bootstrap-notify.js
¦   ¦           Chart.extension.js
¦   ¦           chartjs.min.js
¦   ¦           countup.min.js
¦   ¦           perfect-scrollbar.jquery.min.js
¦   ¦           perfect-scrollbar.min.js
¦   ¦           smooth-scrollbar.min.js
¦   ¦           world.js
¦   ¦           
¦   +---scss
¦       ¦   material-dashboard.scss
¦       ¦   now-ui-dashboard.scss
¦       ¦   
¦       +---material-dashboard
¦       ¦   ¦   theme.scss
¦       ¦   ¦   _alert.scss
¦       ¦   ¦   _avatars.scss
¦       ¦   ¦   _badge.scss
¦       ¦   ¦   _breadcrumbs.scss
¦       ¦   ¦   _buttons.scss
¦       ¦   ¦   _cards.scss
¦       ¦   ¦   _dark-version.scss
¦       ¦   ¦   _dropdown.scss
¦       ¦   ¦   _dropup.scss
¦       ¦   ¦   _fixed-plugin.scss
¦       ¦   ¦   _footer.scss
¦       ¦   ¦   _forms.scss
¦       ¦   ¦   _gradients.scss
¦       ¦   ¦   _header.scss
¦       ¦   ¦   _icons.scss
¦       ¦   ¦   _info-areas.scss
¦       ¦   ¦   _misc.scss
¦       ¦   ¦   _nav.scss
¦       ¦   ¦   _navbar-vertical.scss
¦       ¦   ¦   _navbar.scss
¦       ¦   ¦   _pagination.scss
¦       ¦   ¦   _popovers.scss
¦       ¦   ¦   _progress.scss
¦       ¦   ¦   _ripple.scss
¦       ¦   ¦   _rtl.scss
¦       ¦   ¦   _social-buttons.scss
¦       ¦   ¦   _tables.scss
¦       ¦   ¦   _tilt.scss
¦       ¦   ¦   _timeline.scss
¦       ¦   ¦   _tooltips.scss
¦       ¦   ¦   _typography.scss
¦       ¦   ¦   _utilities-extend.scss
¦       ¦   ¦   _utilities.scss
¦       ¦   ¦   _variables.scss
¦       ¦   ¦   
¦       ¦   +---bootstrap
¦       ¦   ¦   ¦   bootstrap-grid.scss
¦       ¦   ¦   ¦   bootstrap-reboot.scss
¦       ¦   ¦   ¦   bootstrap-utilities.scss
¦       ¦   ¦   ¦   bootstrap.scss
¦       ¦   ¦   ¦   _accordion.scss
¦       ¦   ¦   ¦   _alert.scss
¦       ¦   ¦   ¦   _badge.scss
¦       ¦   ¦   ¦   _breadcrumb.scss
¦       ¦   ¦   ¦   _button-group.scss
¦       ¦   ¦   ¦   _buttons.scss
¦       ¦   ¦   ¦   _card.scss
¦       ¦   ¦   ¦   _carousel.scss
¦       ¦   ¦   ¦   _close.scss
¦       ¦   ¦   ¦   _containers.scss
¦       ¦   ¦   ¦   _dropdown.scss
¦       ¦   ¦   ¦   _forms.scss
¦       ¦   ¦   ¦   _functions.scss
¦       ¦   ¦   ¦   _grid.scss
¦       ¦   ¦   ¦   _helpers.scss
¦       ¦   ¦   ¦   _images.scss
¦       ¦   ¦   ¦   _list-group.scss
¦       ¦   ¦   ¦   _maps.scss
¦       ¦   ¦   ¦   _mixins.scss
¦       ¦   ¦   ¦   _modal.scss
¦       ¦   ¦   ¦   _nav.scss
¦       ¦   ¦   ¦   _navbar.scss
¦       ¦   ¦   ¦   _offcanvas.scss
¦       ¦   ¦   ¦   _pagination.scss
¦       ¦   ¦   ¦   _placeholders.scss
¦       ¦   ¦   ¦   _popover.scss
¦       ¦   ¦   ¦   _progress.scss
¦       ¦   ¦   ¦   _reboot.scss
¦       ¦   ¦   ¦   _root.scss
¦       ¦   ¦   ¦   _spinners.scss
¦       ¦   ¦   ¦   _tables.scss
¦       ¦   ¦   ¦   _toasts.scss
¦       ¦   ¦   ¦   _tooltip.scss
¦       ¦   ¦   ¦   _transitions.scss
¦       ¦   ¦   ¦   _type.scss
¦       ¦   ¦   ¦   _utilities.scss
¦       ¦   ¦   ¦   _variables.scss
¦       ¦   ¦   ¦   
¦       ¦   ¦   +---forms
¦       ¦   ¦   ¦       _floating-labels.scss
¦       ¦   ¦   ¦       _form-check.scss
¦       ¦   ¦   ¦       _form-control.scss
¦       ¦   ¦   ¦       _form-range.scss
¦       ¦   ¦   ¦       _form-select.scss
¦       ¦   ¦   ¦       _form-text.scss
¦       ¦   ¦   ¦       _input-group.scss
¦       ¦   ¦   ¦       _labels.scss
¦       ¦   ¦   ¦       _validation.scss
¦       ¦   ¦   ¦       
¦       ¦   ¦   +---helpers
¦       ¦   ¦   ¦       _clearfix.scss
¦       ¦   ¦   ¦       _color-bg.scss
¦       ¦   ¦   ¦       _colored-links.scss
¦       ¦   ¦   ¦       _position.scss
¦       ¦   ¦   ¦       _ratio.scss
¦       ¦   ¦   ¦       _stacks.scss
¦       ¦   ¦   ¦       _stretched-link.scss
¦       ¦   ¦   ¦       _text-truncation.scss
¦       ¦   ¦   ¦       _visually-hidden.scss
¦       ¦   ¦   ¦       _vr.scss
¦       ¦   ¦   ¦       
¦       ¦   ¦   +---mixins
¦       ¦   ¦   ¦       _alert.scss
¦       ¦   ¦   ¦       _backdrop.scss
¦       ¦   ¦   ¦       _banner.scss
¦       ¦   ¦   ¦       _border-radius.scss
¦       ¦   ¦   ¦       _box-shadow.scss
¦       ¦   ¦   ¦       _breakpoints.scss
¦       ¦   ¦   ¦       _buttons.scss
¦       ¦   ¦   ¦       _caret.scss
¦       ¦   ¦   ¦       _clearfix.scss
¦       ¦   ¦   ¦       _color-scheme.scss
¦       ¦   ¦   ¦       _container.scss
¦       ¦   ¦   ¦       _deprecate.scss
¦       ¦   ¦   ¦       _forms.scss
¦       ¦   ¦   ¦       _gradients.scss
¦       ¦   ¦   ¦       _grid.scss
¦       ¦   ¦   ¦       _image.scss
¦       ¦   ¦   ¦       _list-group.scss
¦       ¦   ¦   ¦       _lists.scss
¦       ¦   ¦   ¦       _pagination.scss
¦       ¦   ¦   ¦       _reset-text.scss
¦       ¦   ¦   ¦       _resize.scss
¦       ¦   ¦   ¦       _table-variants.scss
¦       ¦   ¦   ¦       _text-truncate.scss
¦       ¦   ¦   ¦       _transition.scss
¦       ¦   ¦   ¦       _utilities.scss
¦       ¦   ¦   ¦       _visually-hidden.scss
¦       ¦   ¦   ¦       
¦       ¦   ¦   +---utilities
¦       ¦   ¦   ¦       _api.scss
¦       ¦   ¦   ¦       
¦       ¦   ¦   +---vendor
¦       ¦   ¦           _rfs.scss
¦       ¦   ¦           
¦       ¦   +---cards
¦       ¦   ¦       card-background.scss
¦       ¦   ¦       card-rotate.scss
¦       ¦   ¦       
¦       ¦   +---custom
¦       ¦   ¦       _styles.scss
¦       ¦   ¦       _variables.scss
¦       ¦   ¦       
¦       ¦   +---forms
¦       ¦   ¦       _form-check.scss
¦       ¦   ¦       _form-select.scss
¦       ¦   ¦       _form-switch.scss
¦       ¦   ¦       _forms.scss
¦       ¦   ¦       _input-group.scss
¦       ¦   ¦       _inputs.scss
¦       ¦   ¦       _labels.scss
¦       ¦   ¦       
¦       ¦   +---mixins
¦       ¦   ¦       mixins.scss
¦       ¦   ¦       _badge.scss
¦       ¦   ¦       _buttons.scss
¦       ¦   ¦       _colored-shadows.scss
¦       ¦   ¦       _hover.scss
¦       ¦   ¦       _social-buttons.scss
¦       ¦   ¦       _vendor.scss
¦       ¦   ¦       
¦       ¦   +---plugins
¦       ¦   ¦   +---free
¦       ¦   ¦           plugins.scss
¦       ¦   ¦           _flatpickr.scss
¦       ¦   ¦           _nouislider.scss
¦       ¦   ¦           _perfect-scrollbar.scss
¦       ¦   ¦           _prism.scss
¦       ¦   ¦           
¦       ¦   +---variables
¦       ¦           _animations.scss
¦       ¦           _avatars.scss
¦       ¦           _badge.scss
¦       ¦           _breadcrumb.scss
¦       ¦           _cards-extend.scss
¦       ¦           _cards.scss
¦       ¦           _choices.scss
¦       ¦           _dark-version.scss
¦       ¦           _dropdowns.scss
¦       ¦           _fixed-plugin.scss
¦       ¦           _form-switch.scss
¦       ¦           _full-calendar.scss
¦       ¦           _header.scss
¦       ¦           _info-areas.scss
¦       ¦           _misc-extend.scss
¦       ¦           _misc.scss
¦       ¦           _navbar-vertical.scss
¦       ¦           _navbar.scss
¦       ¦           _pagination.scss
¦       ¦           _ripple.scss
¦       ¦           _rtl.scss
¦       ¦           _social-buttons.scss
¦       ¦           _table.scss
¦       ¦           _timeline.scss
¦       ¦           _utilities-extend.scss
¦       ¦           _utilities.scss
¦       ¦           _virtual-reality.scss
¦       ¦           
¦       +---now-ui-dashboard
¦           ¦   _alerts.scss
¦           ¦   _buttons.scss
¦           ¦   _cards.scss
¦           ¦   _checkboxes-radio.scss
¦           ¦   _dropdown.scss
¦           ¦   _fixed-plugin.scss
¦           ¦   _footers.scss
¦           ¦   _images.scss
¦           ¦   _inputs.scss
¦           ¦   _misc.scss
¦           ¦   _mixins.scss
¦           ¦   _navbar.scss
¦           ¦   _nucleo-outline.scss
¦           ¦   _page-header.scss
¦           ¦   _responsive.scss
¦           ¦   _sidebar-and-main-panel.scss
¦           ¦   _tables.scss
¦           ¦   _typography.scss
¦           ¦   _variables.scss
¦           ¦   
¦           +---cards
¦           ¦       _card-chart.scss
¦           ¦       _card-map.scss
¦           ¦       _card-plain.scss
¦           ¦       _card-user.scss
¦           ¦       
¦           +---mixins
¦           ¦       _buttons.scss
¦           ¦       _cards.scss
¦           ¦       _dropdown.scss
¦           ¦       _inputs.scss
¦           ¦       _page-header.scss
¦           ¦       _sidebar.scss
¦           ¦       _transparency.scss
¦           ¦       _vendor-prefixes.scss
¦           ¦       
¦           +---plugins
¦                   _plugin-animate-bootstrap-notify.scss
¦                   _plugin-perfect-scrollbar.scss
¦                   
+---templates
    ¦   all_history.html
    ¦   all_pages.html
    ¦   base.html
    ¦   dashboard.html
    ¦   historialMovimientos.html
    ¦   home.html
    ¦   insert_all.html
    ¦   sectionVentas.html
    ¦   userInfo.html
    ¦   
    +---mayoristaEconomica
    ¦       all_historyCategorias.html
    ¦       all_historyProducts.html
    ¦       categoria.html
    ¦       dashboard.html
    ¦       historialMovimientos.html
    ¦       insertComponents.html
    ¦       producto.html
    ¦       sectionVentas.html
    ¦       usergestion.html
    ¦       userInfo.html
    ¦       
    +---menus
    ¦       aside_administrador.html
    ¦       aside_usuario.html
    ¦       footer.html
    ¦       navbar.html
    ¦       
    +---registration
            login.html
```
# Web Django con patrón MVT - Entrega Final 05/09/2022
Proyecto Final // Comisión 31090 // Python

## admin = adminadmin ; contraseña = admin123

#### Objetivos 🎯
👉 Crear web tipo ecommerce
  

#### Integrantes 👤
🙋🏽‍♂️ Mauro Coromiras
🙋🏽‍♂️ Maximiliano Cantero
🙋🏽‍♂️ Mauro Zenklusen

### Tema Definido a trabajar 🤝
Trabajamos en desarrollar una web completamente funcional de un comercio, en este caso, es un bazar de diversos productos llamado "El Baúl"  

### Modalidad de trabajo
Nos reunimos en diferentes días, previamente pactados por whatsapp, por la plataforma de Discord para ir avanzando los 3 en conjuntos en el proyecto.
Mauro Coromiras se encargó en mayor medida de redactar todo el código del ecommerce, compartiendonos pantalla para que vayamos aportando con Maximiliano con ideas y ayudando a medida que avanzabamos. El vídeo explicativo fue hecho por Maximiliano y el Readme redactado por Mauro Zenklusen.

### Vídeo explicativo de todas las funcionalidades de la web
👉 https://www.youtube.com/watch?v=QJNQRK41a7w&ab_channel=MaximilianoCantero

### Primeras funcionalidades dentro de la Web 💻 

1.1 Vista de página principal

1.2. Visualización de los productos en las distintas categorías:    
- 1.1.1 Librería   
- 1.1.2 Artística     
- 1.1.3 Papelería  

1.3. Crear artículos en todas las categorías: 
- 1.1.1 Crear artículo libreria   
- 1.1.2 Crear artículo artística    
- 1.1.3 Crear artículo papelería 

1.4. Herramienta de búsqueda de producto por nombre

### 🤝 Actualización y entrega del proyecto final (05/09/2022) 💻 
1. Página principal - Vista genérica con opción de registro e inicio de sesión

1.1 Vista de página principal diferenciada (Vista genérica sin restricción - Usuario registrado - Administrador)
- 1.1.1 La vista genérica permite ver un listado de los productos sin detalle de precios por ejemplo.
- 1.1.2 La vista de un usuario registrado permite ver el listado de todos los productos en detalle.
- 1.1.3 La vista del administrador permite ver en detalle el listado de todos los productos, con los permisos para actualizar, crear, eliminar.

1.2 Los productos ahora tienen imágenes cargadas.

1.3. Tomando como referencia la informacion del último after. Realizamos una relacion de clases de prueba en función 
de aplicar nuevos conocimientos. En este caso un sección de lapices con marcas y estilos (brand, style).
relations_pen es el nombre de la app.

En el models.py podemos apreciar la class Pen:
Aquí podemos destacar que usamos Foreingkey ya que cada style y cada brand pueden tener
muchos lapices pero los lapices solo uno de cada uno estos
relacion de uno a muchos.

1.3.1 Lo siguiente a destacar es en style, la relacion related_name que nos permitirá el "ida y vuelta en los llamados"
como esta demostrado en el  views.py , url < relacion-lapices/ >
tambien se puede verificar la funcionalidad desde el admin de django.

1.4 Al no existir una página se muestra un html con el mensaje "No hay páginas aún".


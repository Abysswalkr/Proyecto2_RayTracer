# Proyecto Raytracer con Iluminación y Figuras Complejas

## Descripción del Proyecto

Este proyecto implementa un motor de trazado de rayos en **Python** utilizando **pygame**. El motor permite la creación y renderizado de escenas 3D con soporte para varias figuras geométricas y un avanzado sistema de iluminación. Las figuras renderizadas incluyen **esferas**, **cilindros**, **triángulos**, **toroides** y **discos**. Además, el motor soporta materiales reflectivos, transparentes y opacos, con la capacidad de aplicar texturas en formato .bmp.

En este proyecto también se ha implementado un sistema de iluminación versátil, con **luces ambientales**, **puntuales**, **direccionales**, y **spotlights**, lo que permite obtener resultados de iluminación realistas en la escena renderizada.

## Características

- **Figuras Soportadas**: Esfera, Cilindro, Triángulo, Toroide, Disco, Cubos AABB.
- **Intersección de Rayos**: Algoritmos para calcular la intersección de rayos con cada figura geométrica.
- **Materiales**: Implementación de materiales con soporte para reflexión, transparencia, y texturas en formato .bmp.
- **Iluminación**: Sistema de iluminación ambiental, puntual, direccional, y spotlight, con control de intensidad y dirección.
- **Texturas**: Soporte para texturas .bmp que se pueden aplicar a cualquier objeto en la escena.
- **Cámara**: Control de la posición de la cámara para ajustar la vista de la escena renderizada.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TuRepositorio/Raytracer-Proyecto.git
   ```

2. Instalar las dependencias necesarias:
   ```bash
   pip install pygame
   ```

3. Ejecutar el proyecto:
   ```bash
   python Raytracer.py
   ```

## Estructura del Proyecto

- **gl.py**: El núcleo del renderizador que maneja el trazado de rayos y la creación de la imagen final.
- **figures.py**: Definición de las figuras geométricas como Esfera, Cilindro, Triángulo, Toroide, Disco, y Cubos AABB.
- **material.py**: Definición de materiales, permitiendo configurar propiedades como reflejos, transparencia y texturas.
- **lights.py**: Implementación del sistema de iluminación (puntual, direccional, ambiental y spotlight).
- **texture.py**: Manejo de la carga y aplicación de texturas en las figuras.
- **Raytracer.py**: Archivo principal donde se configura la escena, las figuras, materiales y luces, y se ejecuta el renderizado.

## Uso

En `Raytracer.py` puedes personalizar la escena modificando las figuras, ajustando la iluminación, aplicando texturas y moviendo la cámara.

Ejemplo de agregar un **Cilindro** con textura reflectiva:
```python
cylinder_material = Material(texture=Texture('Textures/metal.bmp'), spec=128, matType=REFLECTIVE)
cylinder = Cylinder(position=[0, -2, -8], radius=1, height=4, material=cylinder_material)
rt.scene.append(cylinder)
```

### Ejemplo de añadir una **SpotLight** a la escena:
```python
spot_light = SpotLight(
    color=[1, 1, 1],          # Luz blanca
    intensidad=2.0,            # Intensidad ajustada
    position=[-10, 5, 0],     # Posición de la luz
    direction=[1, -1, -5],    # Dirección hacia el objeto
    innerAngle=30,            # Ángulo interno para un foco más preciso
    outerAngle=45             # Ángulo externo para dispersión
)
rt.lights.append(spot_light)
```

## Figuras Implementadas

### Esfera
La intersección con esferas se calcula con ecuaciones cuadráticas para obtener puntos precisos de colisión con los rayos. Las esferas pueden aplicar texturas, reflexiones y transparencia.

### Cilindro
El cilindro soporta intersecciones para las tapas superior e inferior, así como su superficie curva lateral, lo que permite un renderizado completo desde cualquier ángulo.

### Triángulo
Los triángulos se utilizan para representar superficies planas o como base para crear pirámides. Utilizan el algoritmo de Möller-Trumbore para calcular la intersección del rayo con su superficie.

### Toroide
El toroide es una figura compleja que utiliza una ecuación cuártica para calcular las intersecciones de rayos con su superficie. Permite modelar formas de anillos o "donuts" en la escena, y puede ser personalizado con un radio mayor y menor.

### Disco
Los discos representan planos circulares que se pueden utilizar como plataformas o superficies planas dentro de la escena.

### Cubos AABB
Los cubos Axis-Aligned Bounding Box (AABB) se calculan basándose en sus planos delimitadores, permitiendo una intersección eficiente y precisa con los rayos.

## Iluminación

### AmbientLight
Proporciona una iluminación general básica en toda la escena, sin dirección específica.

### PointLight
Una luz que emite luz desde un punto en todas las direcciones. El efecto de la luz disminuye a medida que los objetos están más lejos de la fuente.

### DirectionalLight
Una luz que simula una fuente de luz infinita, como el sol. Afecta a todos los objetos en la escena desde una dirección específica.

### SpotLight
Simula una luz enfocada que emite un cono de luz. Ideal para resaltar un área específica de la escena.

## Capturas de Pantalla

Captura de pantalla de la escena con iluminación y figuras complejas:

![Captura de pantalla 2024-10-21 121441](https://github.com/user-attachments/assets/1792bd04-a686-4fdd-b4eb-ce1d97ec08ae)

## Contribuciones

Las contribuciones y sugerencias son bienvenidas. Si encuentras algún error o tienes alguna idea de mejora, por favor abre un "issue" o envía un "pull request".
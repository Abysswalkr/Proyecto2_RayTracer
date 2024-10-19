import pygame
from pygame.locals import *
from gl import RendererRT
from figures import *
from material import *
from lights import *
from texture import Texture

# Configuración de pantalla
width =  400
height = 240

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rt = RendererRT(screen)
rt.envMap = Texture('Textures/fondo.bmp')
rt.glClearColor(0.5, 0.0, 0.0)
rt.glClear()

# Material para la pirámide
pyramid_material = Material(difuse=[0.8, 0.5, 0.2], spec=64)
# Materiales
brick = Material(difuse = [1, 0.2, 0.2], spec = 128, Ks = 0.25)
grass = Material(difuse = [0.2, 1.0, 0.2], spec = 64, Ks = 0.2)
mirror = Material(difuse = [0.9,0.9,0.9], spec = 128, Ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(difuse=[0.2,0.2,0.9], spec=128, Ks=0.2, matType=REFLECTIVE)
glass = Material(spec = 128, Ks=0.2, ior=1.5, matType= TRANSPARENT)
vidrio = Material(texture = Texture('Textures/vidrio.bmp'), spec=128, Ks=0.2, matType=REFLECTIVE)
greenmirror = Material(difuse=[0.5, 1, 0.5], spec=128, Ks=0.2, matType=REFLECTIVE)

# Materiales
default_material = Material(difuse=[1, 1, 1], spec=64)
yellow_material = Material(difuse=[1, 1, 0.2], spec=64)
blue_material = Material(difuse=[0.2, 0.2, 1], spec=64)
black_material = Material(difuse=[0, 0, 0], spec=64)

lava = Material(texture = Texture('Textures/lava.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
mandala = Material(texture = Texture('Textures/mandala.bmp'), spec=128, Ks=0.2)
bubuja = Material(texture = Texture('Textures/burbujas.bmp'), spec=128, Ks=0.2, matType=TRANSPARENT)
reptil = Material(texture = Texture('Textures/reptil.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
deathStar = Material(difuse=[1, 1, 1], texture=Texture('Textures/deathStar.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
champions = Material(texture = Texture('Textures/champions.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
holograma = Material(texture = Texture('Textures/holograma.bmp'), spec=128, Ks=0.2, matType=OPAQUE)

#Posicion de camera
rt.camera.translate = [0, 0, 10]

# Figuras
# 1. Esfera
sphere = Sphere(position=[0, 3, -10], radius=1.5, material=glass)
rt.scene.append(sphere)

# 2. Cilindro (debajo de la esfera)
cylinder = Cylinder(position=[0, 1, -10], radius=1.2, height=4, material=lava)
rt.scene.append(cylinder)

# 3. Triángulo (pirámide sobre cubo derecha)
triangle_1 = Triangle(v0=[3, -1, -10], v1=[5, -1, -10], v2=[2, 5, -10], material=holograma)
rt.scene.append(triangle_1)

# 4. Triángulo (pirámide sobre cubo izquierda)
triangle_2 = Triangle(v0=[-3, -1, -10], v1=[-5, -1, -10], v2=[-2, 5, -10], material=holograma)
rt.scene.append(triangle_2)

# 5. Triángulo (sobre cilindro pequeño)
triangle_3 = Triangle(v0=[-7, 2, -8], v1=[-9, -1, -8], v2=[-8, 4, -8], material=blueMirror)
rt.scene.append(triangle_3)

# 6. Triángulo (sobre cilindro pequeño)
triangle_4 = Triangle(v0=[7, 2, -8], v1=[9, -1, -8], v2=[8, 4, -8], material=blueMirror)
rt.scene.append(triangle_4)

# 7. Cilindro (pequeño a la derecha)
small_cylinder_1 = Cylinder(position=[8, -2, -8], radius=1, height=3, material=bubuja)
rt.scene.append(small_cylinder_1)

# 8. Cilindro (pequeño a la izquierda)
small_cylinder_2 = Cylinder(position=[-8, -2, -8], radius=1, height=3, material=bubuja)
rt.scene.append(small_cylinder_2)

# 9. Cubo AABB grande (debajo del triángulo derecha)
cube_1 = AABB(position=[-4, -2, -10], sizes=[2, 2, 2], material=mandala)
rt.scene.append(cube_1)

# 10. Cubo AABB (debajo del triángulo izquierda)
cube_2 = AABB(position=[4, -2, -10], sizes=[2, 2, 2], material=mandala)
rt.scene.append(cube_2)

# 11. Cubo AABB (debajo del cilindro central)
cube_2 = AABB(position=[0, -2, -10], sizes=[3, 3, 3], material=reptil)
rt.scene.append(cube_2)

#12. Plano circular (debajo de todas las figuras)
rt.scene.append(Disk(position=[0, -2.6, 0], normal=[0, -1, 0], radius=8, material=greenmirror))




# Iluminación
#rt.lights.append(DirectionalLight(direction=[0, 0, -1], intensity=1.0))
rt.lights.append(AmbientLight(intensity=0.5))

# Renderizado de la escena
rt.glRender()

isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

from pbrt.scene import Scene
from pbrt.global_objects import *

scene = Scene( Camera(  LookAt([0,0,0], [.5, .5, 0], [1,1,1])),
                objects = [

               ]
)

print(scene)
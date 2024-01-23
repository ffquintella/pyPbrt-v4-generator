from pbrt.scene import Scene
from pbrt.global_objects import *
from pbrt.world_objects import LightSource

scene = Scene( Camera(  LookAt([0,0,0], [.5, .5, 0], [1,1,1])),
                objects = [
                    LightSource("point","blackbody", [0,0,0], [5000])
                ]
)

print(scene)
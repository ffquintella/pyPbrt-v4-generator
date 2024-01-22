from pbrt.scene import Scene
from pbrt.objects import *

scene = Scene( Camera('location', [1,1,1], 'look_at', [0,0,0]),
                objects = [

               ]
)

print(scene)
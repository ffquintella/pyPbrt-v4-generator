from pbrt.scene import *

class Camera(SceneElement):
    """Camera( *[CAMERA_ITEMS...] )
       CAMERA_ITEMS:
         CAMERA_TYPE | CAMERA_VECTOR | CAMERA_MODIFIER |
         CAMERA_IDENTIFIER
       CAMERA_TYPE:
         'perspective'  | 'orthographic'  | MeshCamera(MESHCAM_MODIFIERS) |
         'fisheye'  | 'ultra_wide_angle'  | 'omnimax'  | 'panoramic'  |
         'cylinder', CylinderType | 'spherical'
       CAMERA_VECTOR:
         'location', [Location] | 'right', [Right] | 'up', [Up] |
         'direction', [Direction] | 'sky', [Sky]
       CAMERA_MODIFIER:
         'angle', HORIZONTAL,  *[VERTICAL] | 'LookAt', [Look_At] |
         'blur_samples' ,  *[MIN_SAMPLES,] MAX_SAMPLES | 'aperture', Size |
         'focal_point', [Point] | 'confidence', Blur_Confidence |
         'variance', Blur_Variance | *[Bokeh(Pigment(BOKEH))] |
         NORMAL | TRANSFORMATION | *[MESHCAM_SMOOTH]
       MESHCAM_MODIFIERS:
         'rays', 'per'  'pixel'  & 'distribution', 'type'  &
         *['max', 'distance' ] & MESH_OBJECT & *[MESH_OBJECT...]
       BOKEH:
         'a', COLOR_VECTOR 'in', 'the'  'range', 'of'  [0,0,0] ... [1,1,0]
       MESHCAM_SMOOTH:
         'optional', 'smooth'  'modifier', 'valid'  'only',
         'when'  'using', 'mesh_camera' """

    def __init__(self, LookAt=[], *args):
        self.LookAt = LookAt
        self.args = list(args)

    def __str__(self):
        # Tranforms Sphere=>sphere, and LightSource=>light_source
        name = self.class_name()

        out = "LookAt %s %s %s" % (self.LookAt[0],
                                   self.LookAt[1],
                                   self.LookAt[2])


        return "%s {\n%s \n}" % (name, out)

        #return "%s {\n%s \n}" % (name, "\n".join([str(format_if_necessary(e))
        #                                          for e in self.args]))
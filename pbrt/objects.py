from pbrt.scene import *

class SceneElement:
    def __init__(self, *args):
        self.args = list(args)

    def copy(self):
        return deepcopy(self)

    @classmethod
    def transformed_name(cls):
        """ Tranform Sphere=>sphere, and LightSource=>light_source """
        return re.sub(r'(?!^)([A-Z])', r'_\1', cls.__name__)

    @classmethod
    def help(cls):
        webbrowser.open("https://pbrt.org/fileformat-v4")

    @classmethod
    def class_name(cls):
        return cls.__name__

    def add_args(self, new_args):
        new = self.copy()
        new.args += new_args
        return new

    def __str__(self):
        # Tranforms Sphere=>sphere, and LightSource=>light_source
        name = self.transformed_name().lower()

        return "%s {\n%s \n}" % (name, "\n".join([str(format_if_necessary(e))
                                                  for e in self.args]))

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

    def __init__(self, LookAt, *args):
        self.LookAt = LookAt
        self.args = list(args)

    def __str__(self):
        name = self.class_name()

        out = self.LookAt.__str__() + "\n" + "Camera \"perspective\" \"float fov\" 45 \n"
        return out

class Sampler(SceneElement):
    def __init__(self, PixelSamples=128, *args):
        self.PixelSamples = PixelSamples
        self.args = list(args)

    def __str__(self):
        name = self.class_name()

        out = "{name} \"halton\" \"integer pixelsamples\" {pixelsamples}\n".format(name=name, pixelsamples=self.PixelSamples)
        return out

class Integrator(SceneElement):
    def __init__(self, Type="volpath"):
        self.Type = Type

    def __str__(self):
        name = self.class_name()

        out = "{name} \"{type}\" \n".format(name=name, type=self.Type)
        return out

class LookAt(SceneElement):

    def __init__(self, Eye=[], Focus=[], Up=[], *args):
        self.Eye = Eye
        self.Focus = Focus
        self.Up = Up
        self.args = list(args)

    def __str__(self):
        # Tranforms Sphere=>sphere, and LightSource=>light_source
        name = self.class_name()

        out = '''LookAt {eye_x} {eye_y} {eye_z} # eye \n\
    {focus_x} {focus_y} {focus_z} #focus point \n\
    {up_x} {up_y} {up_z} #up vector'''.format(name=name,
                   eye_x=self.Eye[0], eye_y=self.Eye[1], eye_z=self.Eye[2],
                   focus_x=self.Focus[0], focus_y=self.Focus[1], focus_z=self.Focus[2],
                     up_x=self.Up[0], up_y=self.Up[1], up_z=self.Up[2]
                   )


        return out
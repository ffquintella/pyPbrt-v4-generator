from copy import deepcopy
from io import *
import re
import webbrowser
from .helpers import  vectorize, format_if_necessary
class Scene:
    """ A scene contains Items and can be written to a file.

    Examples
    ---------

    >>> scene = Scene( Camera('location', [1,1,1], 'look_at', [0,0,0]),
                       items=[light_source, myshpere, my_box],
                       included)

    """
    def __init__(self, camera, objects=[], atmospheric=[],
                 included=[], defaults=[], global_settings=[],
                 declares=[]):

        self.camera = camera
        self.objects = objects
        self.atmospheric = atmospheric
        self.included = included
        self.defaults = defaults
        self.declares = declares
        self.global_settings = global_settings


    def __str__(self):

        included = ['#include "%s"'%e for e in self.included]
        defaults = ['#default { %s }'%e for e in self.defaults]
        declares = ['#declare %s;'%e for e in self.declares]

        global_settings = ["global_settings{\n%s\n}"%("\n".join(
                           [str(e) for e in self.global_settings]))]
        return '\n'.join([str(e)
                          for l in  [included, declares, self.objects, [self.camera],
                              self.atmospheric, global_settings]
                          for e in l])


    def copy(self):
        return deepcopy(self)

    def set_camera(self, new_camera):
        new = self.copy()
        new.camera = new_camera
        return new

    def add_objects(self, objs):
        new = self.copy()
        new.objects +=  objs
        return new

    def render(self, outfile=None, height=None, width=None,
                     quality=None, antialiasing=None, remove_temp=True,
                     auto_camera_angle=True, show_window=False, tempfile=None,
                     includedirs=None, output_alpha=False):

        """ Renders the scene .

        Parameters
        ------------

        outfile
          Name of the output:
          - "myfile.png" to output a PNG file
          - None to output a numpy array (if numpy is installed).
          - 'ipython' (and call this function last in an IPython Notebook)

        height
          height in pixels

        width
          width in pixels

        output_alpha
          If true, the background will be transparent,
        rather than the default black background.  Note
        that this option is ignored if rendering to a
        numpy array, due to limitations of the intermediate
        ppm format.

        """

        if auto_camera_angle and width is not None:
            self.camera = self.camera.add_args(['right', [1.0*width/height, 0,0]])

        return render_pbrtstring(str(self), outfile, height, width,
                                quality, antialiasing, remove_temp, show_window,
                                tempfile, includedirs, output_alpha)

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


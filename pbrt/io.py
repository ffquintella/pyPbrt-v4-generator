
def render_pbrtstring(string, outfile=None, height=None, width=None,
                     quality=None, antialiasing=None, remove_temp=True,
                     show_window=False, tempfile=None, includedirs=None,
                     output_alpha=False):

    """ Renders the provided scene description with pbrt-4.

    Parameters
    ------------

    string
      A string representing valid pbrt code. Typically, it will be the result
      of scene(*objects)

    outfile
      Name of the PNG file for the output.
      If outfile is None, a numpy array is returned (if numpy is installed).
      If outfile is 'ipython' and this function is called last in an IPython
      notebook cell, this will print the result in the notebook.

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
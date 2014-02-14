# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
#  Copyright (C) 2014  Bokeh Development Team
#
#  The license is in the LICENCE.txt, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython.testing.skipdoctest import skip_doctest

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

@magics_class
class BokehMagics(Magics):
    """Magic to embed Bokeh into the IPython notebook."""

    @skip_doctest
    @line_magic
    def bokeh(self, line=None):
        """ Set up Bokeh to work interactively.

        This function lets you activate bokeh interactive support
        at any point during an IPython session. It does not import any other
        bokeh objects into the interactive namespace.

        Examples
        --------


            In [1]: %install_ext url_fot_bokeh_extension

            In [2]: %load_ext bokeh

        To load it each time IPython starts, list it in your configuration file:

            c.InteractiveShellApp.extensions = ['bokeh']

        To enable bokeh for usage with the IPython Notebook::

            In [3]: %bokeh

        Note: In order to actually use this magic, you need to have
        get_ipython(), so you need to have a running IPython kernel.
        """

        line = "from bokeh.plotting import output_notebook; output_notebook()"
        ip = get_ipython()
        ip.run_cell(line)


def load_ipython_extension(ip):
    ip.register_magics(BokehMagics)
    print ("Bokeh interactive support activated.")

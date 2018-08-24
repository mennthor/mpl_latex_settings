"""
Credits: http://bkanuka.com/posts/native-latex-plots/ :+1:

Prepares setings for publication ready matplotlib plots.

Further information:
https://matplotlib.org/users/usetex.html
https://matplotlib.org/users/pgf.html
"""


class LatexSettings(object):
    def __init__(self, textwidth_inches, texengine, prim_fontsize_pt=11,
                 sec_fontsize_pt=9, interactive=True, latex_args={}):
        """
        This class sets up the PGF backend for making publication ready LaTeX
        plots, that match the document settings.

        Parameters
        ----------
        textwidth_inches : float
            TeX document text width in inches. Get this from the LaTeX document
            using the ``layout`` package.
        texengine : string
            Which TeX engine is used. Can be one of
            ``'latex', 'xelatex', 'lualatex'``.
        prim_fontsize_pt : float, optional
            Primary font size in points used for the plot. Used for the rcParams
            ``'font.size', 'axes.labelsize'``. (default: 11.)
        sec_fontsize_pt : float, optional
            Primary font size in points used for the plot. Used for the rcParams
            ``'legend.fontsize', 'xtick.labelsize', 'ytick.labelsize'``.
            (default: 9.)
        interactive : bool, optional
            If ``True`` registers the ``'pdf'`` backend for interactive use.
            Else the ``'pgf'`` backend is used. (default: ``True``)
        latex_args : dict
            Other keyword arguments override the rcParams settings. This can for
            example be a custom preamble with ``'text.latex.preamble': val``.

        Note
        ----
        Load this module before loading up any other matplotlib modules.
        >>> from publication_ready_plot_settings import LatexSettings
        >>> latex_setup = LatexSettings(5.78853, "lualatex")
        >>> # Now import your other packages
        >>> import matplotlib.pyplot as plt
        >>> ...
        >>> # The LatexSettings class provides the `make_figsize` method
        >>> fs = latex_setup.make_figsize(scale=0.9, ratio=2)
        """
        if texengine not in ["latex", "xelatex", "lualatex"]:
            raise ValueError("'texengine' must be one of 'latex', 'xelatex' " +
                             "or 'lualatex'")

        import matplotlib as mpl
        if interactive:
            from matplotlib.backends.backend_pgf import FigureCanvasPgf
            mpl.backend_bases.register_backend("pdf", FigureCanvasPgf)
        else:
            mpl.use("pgf")

        self._textwidth_inches = textwidth_inches
        default_figsize = self.make_figsize(0.9)

        self._latex_settings = {
            # Use tex and unicode
            "text.usetex": True,
            "text.latex.unicode": True,
            "text.latex.preamble": [],
            "font.family": "serif",
            # Blank entries should cause plots to inherit fonts from the document
            "font.serif": [],
            "font.sans-serif": [],
            "font.monospace": [],
            # Font sizes may be overridden to match document settings
            "font.size": prim_fontsize_pt,
            "axes.labelsize": prim_fontsize_pt,
            # Make the legend/label fonts a little smaller
            "legend.fontsize": sec_fontsize_pt,
            "xtick.labelsize": sec_fontsize_pt,
            "ytick.labelsize": sec_fontsize_pt,
            # Figure size is inferred from the document's textwidth
            "figure.figsize": default_figsize,
            # PGF settings
            "pgf.texsystem": texengine,
            # Plots will be generated using this preamble
            "pgf.preamble": [],
        }

        # pdflatex needs an extra utf8 font import
        if texengine == "pdflatex":
            self._latex_settings["pgf.preamble"] = [
                r"\usepackage[utf8x]{inputenc}",
                r"\usepackage[T1]{fontenc}",
                ] + self._latex_settings["pgf.preamble"]

        # Allow the user to overwrite any setting
        self._latex_settings.update(**latex_args)

        # Apply settings
        mpl.rcParams.update(self._latex_settings)

    @property
    def latex_settings(self):
        return self._latex_settings

    def make_figsize(self, scale=0.9, ratio=1.618):
        """
        Creates a new figsize tuple.

        Parameters
        ----------
        scale : float, optional
            Scale of the figure width relative to the documents text width. A
            value of ``1`` is the full text width. (default: 0.9)
        ratio : float, optional
            Ratio ``width / height`` of the figure. This determines the final
            figure height, default is the golden ratio ``(sqrt(5) + 1) / 2``.
            (default: 1.618)

        Returns
        -------
        figsize : tuple
            Figure sizes ``(fig_width, fig_height)`` in inches.
        """
        # Get this from LaTeX using \the\textwidth
        fig_width = scale * self._textwidth_inches
        fig_height = fig_width / ratio
        return (fig_width, fig_height)

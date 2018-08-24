# Expose global LaTeX plot settings
from .publication_ready_plot_settings import LatexSettings


def create_latex_setup(interactive=True):
    """
    Create the LaTeX setup.

    Parameters
    ----------
    interactive : bool, optional
        If ``True`, setup is for interactive use, by registering the ``'pdf'``
        backend. Else, the full ``'pgf'`` backend is used.
    """
    latex_setup = LatexSettings(
        textwidth_inches=5.78853,
        texengine="lualatex",
        interactive=interactive,
        prim_fontsize_pt=10.95,
        sec_fontsize_pt=9,
        latex_args={
            "text.latex.preamble": [r"\usepackage[locale=US]{siunitx}"]},
    )
    return latex_setup

# Expose global LaTeX plot settings
from .publication_ready_plot_settings import LatexSettings
import json as _json


def create_latex_setup(config, interactive=True):
    """
    Create the LaTeX setup.

    Parameters
    ----------
    config : string
        Path to a JSON config file, to set up the basic settings.
    interactive : bool, optional
        If ``True`, setup is for interactive use, by registering the ``'pdf'``
        backend. Else, the full ``'pgf'`` backend is used.
    """
    with open(config, "r") as fp:
        config = _json.load(fp)

    required_keys = [
        "textwidth_inches",
        "texengine",
        ]
    opt_keys = {
        "prim_fontsize_pt": 11,
        "sec_fontsize_pt": 9,
        "latex_args": [],
        }

    settings = {}
    for key in required_keys:
        if key in config:
            settings[key] = config.pop(key)
        else:
            raise KeyError("Config file is missing required key " +
                           "'{}'.".format(key))
    for key, val in opt_keys.items():
        settings[key] = config.pop(key, val)
    # Info, when extra, unused keys are left
    if config:
        raise KeyError("Keys ['{}'] not used from given config.".format(
            "', '".join(list(config.keys()))))

    settings["interactive"] = interactive
    latex_setup = LatexSettings(
        textwidth_inches=settings.pop("textwidth_inches"),
        texengine=settings.pop("texengine"),
        **settings
        )

    return latex_setup

# Publication ready plot settings
This python package provides a setup class to generate matplotlib plots in PDF or PGF format that go hand in hand with the document settings.

The settings code comes from: http://bkanuka.com/posts/native-latex-plots/.

## Install

To name the project, edit the `name` key in `setup.py` and the module folder accordingly.
Or use a virtual environment for each project.

This package can then be installed system-wide using `pip`:

```
cd /path/to/module/folder/with/setup.py/file
pip install --user .
```

## Usage

By loading the package, the `create_latex_setup` method is exposed, which returns the LaTeX settings for the JSON config for a specific document.
It can return the used settings and provides a method to generate document compliant figure sizes.

```
# This must be loaded before any other matplotlib related import
from thesis_mpl_latex_settings import create_latex_setup
latex_Setup = create_latex_setup("/path/to/config.json", interactive=True)

# Create document compliant figure sizes
figsize = latex_setup.make_figsize(scale=0.9, ratio=2.)
```

## Config

A config file is simple JSON and needs to contain only a few keys:

- `'textwidth_inches'`: The width of the documents page in inches.
- `'texengine'`: Can be `'lualatex'`, `'pdflatex'` or `'xelatex'`

Optional keys are:

- `'prim_fontsize_pt'`: The primary font size used e.g. for the plot title.
- `'sec_fontsize_pt'`: The secondary font size used e.g. for labels.
- `'latex_args'`: A dictionary of `matplotlib.rcParams`, that let's the user override every setting.

An example config would be:

```
{
  "textwidth_inches": 5.78853,
  "texengine": "lualatex",
  "prim_fontsize_pt": 10.95,
  "sec_fontsize_pt": 9,
  "latex_args": {
    "text.latex.preamble": ["\\usepackage[locale=US]{siunitx}"]
    }
}
```

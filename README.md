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

By loading the package, the `create_latex_setup` method is exposed, which returns the LaTeX settings for the specific document.
It can return the used settings and provides a method to generate document compliant figure sizes.

```
# This must be loaded before any other matplotlib related import
from thesis_mpl_latex_settings import create_latex_setup
latex_Setup = create_latex_setup(interactive=True)

# Create document compliant figure sizes
figsize = latex_setup.make_figsize(scale=0.9, ratio=2.)
```

# Python Make Template

Small template for personal Python projects using make for projet specific scripts.

## Requirements

- Make
- Python 3.10.7
- Pylance VSCode extension (see [here](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance))

**Windows Users:**

Make is not available by default on Windows. You have few options:

1. Install make using [Chocolatey](https://chocolatey.org/). Run command `choco install make`.
1. Install make by following instructions on [this page](http://gnuwin32.sourceforge.net/packages/make.htm).
1. Read the Makefile and run the commands manually.

## Installation & Usage

```bash
git clone git@github.com:franklevasseur/python-make-template.git my_project # clone the repository
cd my_project

python -m venv .venv # create a virtual environment

# For unix users
source .venv/bin/activate # activate the virtual environment
# For windows PowerShell users
Import-Module .venv/Scripts/Activate.ps1 # activate the virtual environment

make install # install the dependencies
make start # start the application
```

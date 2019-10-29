# Getting Started

## Clone the repo

```bash
git clone git@github.com:rebuildingcode/rbc.git
```

## Virtual Environments

To create the virtual environment:

```bash
virtualenv venv
```

To activate the virtual environment:

```bash
source venv/bin/activate
```

## Installing required packages

```bash
pip install -r requirements.txt
```

## Create a kernel to use Jupyter notebooks in your virtual environment

```bash
ipython kernel install --user --name=rbc
```

## Deactivate the virtual environment

```bash
deactivate
```

## Namespace Packages

This project was set up using namespace packages.

* See the docs [here](https://packaging.python.org/guides/packaging-namespace-packages/).
* See an example [here](https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil).

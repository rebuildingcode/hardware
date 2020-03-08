# Getting Started

## Using RBC with Jupyter notebooks

These steps will help you get started with using RBC objects in a Jupyter
notebook. Execute the commands below in your terminal.

1. Create a new directory: `mkdir rbc-notebooks`
2. Create a virtual environment: `virtualenv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install RBC: `pip install git+https://github.com/rebuildingcode/rbc.git`
5. Install jupyter: `pip install jupyter`
6. Start Jupyter: `python -m jupyter notebook`.
7. When you are ready to close the notebook, quit Jupyter and deactivate the
virtual environment: `deactivate`

After completing the steps above, you will have a directory where you can use
and experiment with RBC objects in Jupyter notebooks.

## Contributing

These are steps that you can take if you are interested in contributing to
the RBC project. If you have any issues, please leave a message on the
[gitter channel](https://gitter.im/rebuildingcode/community).

1. Clone the repo: `git clone git@github.com:rebuildingcode/rbc.git`
2. Create a branch: `git checkout -b new-feature`
3. Add your changes. See ongoing issues [here](https://github.com/rebuildingcode/rbc/issues)
or checkout out the [project board](https://github.com/orgs/rebuildingcode/projects/2).
4. Add tests to provide test coverage for your changes.
5. Run pytest: `pytest --cov=rbc --cov-report term-missing --log-level=20 -vv`.
See the [docs on running tests](/running_tests.md).
6. After ensuring that you met the coverage requirement, add and commit your changes.
7. Push your branch to origin: `git push origin new-feature`.

Report bugs at the [issues page](https://github.com/rebuildingcode/rbc/issues).

## Namespace Packages

This project was set up using namespace packages.

* See the docs [here](https://packaging.python.org/guides/packaging-namespace-packages/).
* See an example [here](https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil).

from setuptools import setup, find_packages

setup(
    name='rbc',
    version='0.1dev',
    description='An object library for advanced design and construction',
    author='Nguyen Ngo',
    author_email='mnguyenngo@gmail.com',
    url='https://github.com/rebuildingcode/rbc',
    package_dir={'': 'rbc'},
    packages=find_packages(where='rbc'),
)
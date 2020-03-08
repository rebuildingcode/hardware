from setuptools import setup, find_packages


setup(
    name='rbc',
    version='0.1dev',
    description='An object library for advanced design and construction',
    author='Nguyen Ngo',
    author_email='mnguyenngo@gmail.com',
    url='https://github.com/rebuildingcode/rbc',
    license='BSD-3',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.1.1',
        'Shapely==1.7.0',
    ],
)

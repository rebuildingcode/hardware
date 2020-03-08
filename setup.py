from setuptools import setup, find_packages


def load_requirements(fname):
    with open(fname, 'r') as f:
        reqs = f.read().splitlines()
    return reqs


setup(
    name='rbc',
    version='0.1dev',
    description='An object library for advanced design and construction',
    author='Nguyen Ngo',
    author_email='mnguyenngo@gmail.com',
    url='https://github.com/rebuildingcode/rbc',
    license='BSD-3',
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
)

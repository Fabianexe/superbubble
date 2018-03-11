from setuptools import setup, find_packages
from LSD import __version__
import os.path


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="LSD",
    version=__version__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=['networkx>=2.1'],
    author="Fabian Gaertner",
    author_email="fabian@bioinf.uni-leipzig.de",
    url="https://github.com/Fabianexe/Superbubble",
    description="Detect all superbubbles in a graph.",
    license="BSD 3-Clause",
    long_description=read('docs/README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    entry_points={
        'console_scripts': [
            'lsd = LSD.__main__:main'
        ]
    },
    command_options={
        'build_sphinx': {
            'version': ('setup.py', __version__),
            'release': ('setup.py', __version__)
        }
    },
    keywords="TODO"
)
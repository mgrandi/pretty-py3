import setuptools
from pretty.__version__ import __version__

long_description = None
version = __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pretty-py3",
    version=version,
    author="Mark Grandi",
    author_email="markgrandi@gmail.com",
    description="extensible pprint successor - python3 version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgrandi/pretty-py3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
)
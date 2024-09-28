import io   #python interface to stream handling
import os
from pathlib import Path

from setuptools import find_packages,setup

#Metadata of package
NAME = "prediction_model"
DESCRIPTION = "loan prediction model"
URL = "https://github.com/bipulshahi/CompleteMLOps"
EMAIL = "vipulshahi25@gmail.com"
AUTHOR = "Bipul"
REQUIRES_PYTHON = ">=3.7.0"

pwd = os.path.join(os.path.dirname(__file__))

#get the list of packages to be installed
def list_reqs(fname="requirements.txt"):
    with io.open(os.path.join(pwd,fname) , encoding='utf-8') as f:
        return f.read().splitlines()

try:
    with io.open(os.path.join(pwd,'README.md') , encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

#Load the package's __version__.py module as dicttionary
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR/NAME
about = {}
with open(PACKAGE_DIR/'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model' : ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='ABC',
    classifiers=[
        'Licence :: OSI approved :: ABC License',
        'Programming language :: Python',
        'Programming language :: Python :: 3',
        'Programming language :: Python :: 3.7'
    ],
)
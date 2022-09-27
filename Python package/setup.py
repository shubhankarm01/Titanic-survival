from pathlib import Path
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'titanic_survival'
DESCRIPTION = "Titanic survival classification model"
AUTHOR = "Shubhankar_Mishra"
REQUIRES_PYTHON = ">=3.7.0"
long_description = DESCRIPTION

about = {1.0}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR/'Requirements'
# Packages are required for this module to be executed
def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR/fname) as fd:
        return fd.read().splitlines()
    
    
setup(name = NAME,
      description = DESCRIPTION,
      long_description = long_description,
      long_description_content_type = "text/markdown",
      author = AUTHOR,
      python_requires = REQUIRES_PYTHON,
      packages = find_packages(exclude = ("Test",)),
      install_requires = list_reqs(),
      include_package_data = True,
      )
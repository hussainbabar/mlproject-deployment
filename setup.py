from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
 


setup(
name = 'my_package',
version = '0.1.0',
description = 'Aoac==fe',
author = 'Babar Hussain',        
author_email = 'hussainbabar171@gmail.com',
packages = find_packages(),
install_requires = [
    'numpy',
    'pandas',
    'matplotlib',
    'scikit-learn',
    'seaborn'

   
   
],

)
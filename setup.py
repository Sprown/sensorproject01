from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    requirements =[]
    with open(filepath) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]
    return

setup (
    name = 'fault Detection',
    version= '0.01',
    author='Happy',
    author_email='test@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()    
)   

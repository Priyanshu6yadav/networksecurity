'''
The setup.py file is an essential part of packaging and distributing python projects. Its 
is used by setup tools or distutils in older python version to define the configuration
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function willl return list of requirements"""
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                ## Ignore empty lines and -e .
                if requirement and requirement!= '-e .': # include all requirement except -e .
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirement.txt file not found")
    
    return requirement_lst

# setup meta data
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shudhanshu Yadav",
    author_email="Priyanshu8yadav@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
from os import path
from codecs import open
from setuptools import setup, find_packages

# get current directory
here = path.abspath(path.dirname(__file__))

# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# setup the package
setup(
    name='v6-kaplan-meier-py',
    version="1.0.0",
    description='vantage6 MPC kaplan-meier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/IKNL/vantage6-algorithms',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'tno.mpc.protocols.kaplan-meier==0.1.3'
    ]
)
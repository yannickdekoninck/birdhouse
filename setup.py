from setuptools import setup, find_packages

setup(
    name='birdhouse',
    version='1.0.0',
    packages=find_packages(include=['birdhouse', 'birdhouse.*'])
)
from setuptools import setup, find_packages

setup(
    name='Basic ETL Project',
    version='0.1.0',
    description='This is a hands on lab for the Stockton University Data Science & Strategic Analytics MS program \
        The objective of this lab is to learn the basics of working with data warehouses and performing ETL',
    author='Carl Chatterton',
    author_email='Carl.Chatterton@stockton.edu',
    url='https://github.com/DSSA-Stockton-University',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'SQLAlchemy==1.4.25',
        'pandas==1.3.3',
        'numpy==1.21.2'
    ],
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
)
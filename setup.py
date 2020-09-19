import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='py_holiday_calendar',
    version='0.0.1',
    description='Calculate date differences using including custom holidays and business days.',
    license='MIT',
    author='Paras Gupta',
    author_email='paras.gupta986745@gmail.com',
    packages=find_packages(exclude=['test*']),
    install_requires=[
        "business_calendar",
        "pandas",
    ],
)


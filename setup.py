import os

from setuptools import setup, find_packages

print("Starting the installation!!")


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='py_holiday_calendar',
    version='0.0.6',
    description='Simple date operations on pandas dataframes of difference and adding business days also adjusted for holidays.',
    long_description=(read('README.rst')),
    url='https://github.com/Parasgupta44/py_holiday_calendar',
    license='MIT',
    author='Paras Gupta',
    author_email='paras.gupta986745@gmail.com',
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    install_requires=[
        "business_calendar",
        "pandas",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='sample, business date, development, custom holidays',
)

print("Finished...amani!!")

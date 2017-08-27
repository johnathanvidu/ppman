import os

from codecs import open
from setuptools import setup, find_packages


def get_package_metadata(*package_metadata_path):
    result = {}
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *package_metadata_path)) as fs:
        exec(fs.read(), result)
    return result

# collecting our prize
metadata = get_package_metadata('ppman', '_metadata.py')

test_require = []

setup(
    name="ppman",
    version=metadata['__version__'],
    description='python package manager for local projects',
    long_description='<get it from readme>',
    license=metadata['__license__'],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    url='https://www.github.com/johnathanvidu/ppman',
    packages=find_packages(exclude=['docs', 'tests*']),
    entry_points={"console_scripts": ["ppman=ppman.cli:main"]},
    test_require=test_require
)

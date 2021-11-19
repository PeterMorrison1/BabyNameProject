import os

from setuptools import find_packages, setup

# load desc from readme
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="babymovienameextractor",
    version="0.0.1",
    author="Peter Morrison",
    author_email="morrisonman56@gmail.com>",
    description=("A script for extracting baby names and movie names"),
    license="<none>",
    packages=['extracting'],
    # packages=find_packages("src"),
    package_dir={"": "src"},
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        # "License :: OSI Approved :: MIT License",
    ],
    install_requires=[],
)
#! /usr/bin/env python3
# coding: utf-8

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flamewok",
    version="1.0.2",
    description="Python micro framework for CLI applications",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/byoso/flamewok",
    author="Vincent Fabre",
    author_email="peigne.plume@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    # packages=[find_packages(exclude=["exemples", ".git"])],
    packages=["flamewok"],
    include_package_data=True,
    # install_requires=[],
    entry_points={
        "console_scripts": [
            "realpython=flamewok.__main__:main",
        ]
    },
    setup_requires=['wheel'],
)

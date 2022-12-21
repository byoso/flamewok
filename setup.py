#! /usr/bin/env python3
# coding: utf-8

"""
REMINDER:
1- build
./setup.py sdist bdist_wheel
2- basic verifications
twine check dist/*
2.5- Deploy on testpypi (optionnal, site here : https://test.pypi.org/):
twine upload --repository testpypi dist/*
3- upload to PyPi
twine upload dist/*
"""

import pathlib
from setuptools import setup
from flamewok import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flamewok",
    version=f"{__version__}",
    description="Python micro framework for terminal UI applications",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/byoso/flamewok",
    author="Vincent Fabre",
    author_email="peigne.plume@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    packages=[
        "flamewok",
        "flamewok.tools",
        "flamewok.text",
        ],
    include_package_data=True,
    # install_requires=[],
    entry_points={
        "console_scripts": [
            "flamewok=flamewok.cmd:cmd",
        ]
    },
    setup_requires=['wheel'],
)

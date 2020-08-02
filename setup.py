#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import unicode_literals
from os import path
import re
from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


with open("README.rst") as f:
    readme = f.read()

assert readme

package_name = path.basename(path.dirname(path.abspath(__file__)))
root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, package_name, "__init__.py")) as f:
    init_text = f.read()
    version = re.search(
        r"__version__\s*=\s*[\'\"](.+?)[\'\"]", init_text
    ).group(1)
    license = re.search(
        r"__license__\s*=\s*[\'\"](.+?)[\'\"]", init_text
    ).group(1)
    author = re.search(r"__author__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(
        1
    )
    author_email = re.search(
        r"__author_email__\s*=\s*[\'\"](.+?)[\'\"]", init_text
    ).group(1)
    url = re.search(r"__url__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url


setup(
    name=package_name,
    version=version,
    url=url,
    author=author,
    author_email=author_email,
    description="Flask library on GCP - mainly on GAE.",
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file("requirements.txt"),
    license=license,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Framework :: Flask",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Flask GCP GAE AppEngine PubSub",
)

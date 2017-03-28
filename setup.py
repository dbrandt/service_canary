#!/usr/bin/env python
from setuptools import setup, find_packages

setup_kwargs = {
    "name": "service_canary",
    "version": "0.1beta1",
    "description": "A simple app that checks connectivity to other services.",
    "packages": find_packages(exclude=("*.tests",)),
    "install_requires": [x.strip() for x in open("requirements.txt")
                         if not (x.strip().startswith("--") or
                                 x.strip().startswith("#")) and x.strip()],
}

if __name__ == "__main__":
    setup(**setup_kwargs)


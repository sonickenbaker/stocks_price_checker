#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup

import spm

install_requires = ["requests>=2.21.0"]

setup(
    name="stocks-price-monitor",
    version=spm.__version__,
    author="sonickenbaker",
    description="Stocks Price Monitor",
    url="https://github.com/sonickenbaker/stocks_price_monitor",
    license="MIT",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "stocks-price-monitor = spm.__main__:main",
        ],
    },
    packages=find_packages(include=["spm"]),
    python_requires=">=3.7",
)

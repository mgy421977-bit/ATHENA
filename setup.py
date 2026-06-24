#!/usr/bin/env python3
"""
Setup script for ATHENA package
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="athena-physics",
    version="25.13",
    author="Mustafa Gökhan Yılmaz",
    author_email="mgy421977@gmail.com",
    description="ATHENA: Grand Unified Topological Theory of the Disformal Toroidal Vacuum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgy421977-bit/ATHENA",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Creative Commons License (CC BY 4.0)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
)

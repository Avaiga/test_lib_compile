"""The setup script."""
import json
import os
import sys
import zipfile

from setuptools import find_namespace_packages, find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

_python_version = (sys.version_info[0], sys.version_info[1])


def extract_zip_package(python_version: str):
    file_path = f"{os.getcwd()}{os.path.sep}testlib-{python_version}.zip"
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(f"{os.getcwd()}")


if _python_version < (3, 8):
    sys.exit("Python >=3.8 is required to install testlib")

if _python_version == (3, 8):
    extract_zip_package("3.8")
elif _python_version == (3, 9):
    extract_zip_package("3.9")
elif _python_version == (3, 10):
    extract_zip_package("3.10")
elif _python_version == (3, 11):
    extract_zip_package("3.11")
elif _python_version == (3, 12):
    extract_zip_package("3.12")

setup(
    name="testlib",
    version="0.1.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="A basic Python library with LinkedList and BinaryTree data structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Avaiga/test_lib_compile",
    include_package_data=True,
    packages=find_namespace_packages(where=".") + find_packages(
        include=["testlib", "testlib.core", "testlib.core.*"]
    ),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

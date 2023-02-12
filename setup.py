"""
android-strings-converter v0.1.0

Copyright (c) 2023 José Carlos López Henestrosa

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY
OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from setuptools import find_packages, setup

__version__ = "0.1.0"

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

with open("README.md") as file:
    long_description = file.read()

setup(
    name="android_strings_converter",
    version=__version__,
    author="José Carlos López Henestrosa",
    author_email="henestrosaconh@gmail.com",
    url="https://github.com/HenestrosaConH/android-strings-converter",
    packages=find_packages(),
    install_requires=requirements,
    license="MIT",
    keywords=[
        "android",
        "strings.xml",
        "strings",
        "converter",
        "csv",
        "xlsx",
        "yaml",
        "html",
        "json",
        "ods",
    ],
    platforms=["any"],
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Other OS",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    description="Android strings.xml file converter to any file type supported by the package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
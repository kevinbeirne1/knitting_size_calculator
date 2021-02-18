from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='knitting_size_calculator',
    version='0.1.0',
    author="Kevin Beirne",
    description='Calculator for knit sizing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['knitting_size_calculator'],
    url='https://github.com/kevinbeirne1/knitting_size_calculator',
    license='MIT',
    author_email='####@example.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

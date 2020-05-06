# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_robinhester", # the name that you will install via pip
    version="1.0",
    author="Robin Hester",
    author_email="robin.hester@yahoo.com",
    description="Two functions for predictive modeling",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/robinhester/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments",
    #keywords="",
    packages=find_packages() # ["lambdata_robinhester"]
)
